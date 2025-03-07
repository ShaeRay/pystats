from rest_framework import viewsets, parsers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView  # type: ignore
import pandas as pd
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .stats import get_stats, ttest, anova, calculate_correlation


# 上传文件
class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def create(self, request, *args, **kwargs):
        # print("Request data:", request.data)
        file_obj = request.data.get('file')

        if not file_obj:
            return Response({'error': 'No file was provided'}, status=status.HTTP_400_BAD_REQUEST)

        allowed_extensions = ['csv', 'xls', 'xlsx']
        if not file_obj.name.split('.')[-1].lower() in allowed_extensions:
            return Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

        # 检查文件是否已存在
        existing_file = UploadedFile.objects.filter(file=file_obj.name).first()
        if existing_file:
            serializer = UploadedFileSerializer(existing_file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        try:
            if file_obj.name.endswith('.csv'):
                data = pd.read_csv(file_obj).reset_index(drop=True)
            else:
                print("Reading Excel file:", file_obj.name)
                data = pd.read_excel(file_obj).reset_index(drop=True)

            # 检查数据类型是否存在问题
            for col in data.columns:
                if data[col].dtype == object:
                    try:
                        data[col] = data[col].astype('float64')
                    except (ValueError, TypeError):
                        pass

            data = data.dropna(axis=1, how='all')
            data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

            uploaded_file = UploadedFile(
                file=None, data=data.to_json(orient='records'))
            uploaded_file.save()
            uploaded_file.file.save(file_obj.name, file_obj)

            serializer = UploadedFileSerializer(uploaded_file)
            # 返回json数组
            return Response(serializer.data['data'], status=status.HTTP_201_CREATED)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


# 用于处理描述统计数据计算请求,仅限post
class StatsView(APIView):
    def post(self, request, *args, **kwargs):
        req_data = request.data

        # 检查请求数据是否存在
        if not req_data:
            return Response({"error": "Request data is empty or not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        column = req_data.get('column')
        data = req_data.get('data')

        # 检查column键是否存在
        if not column:
            return Response({"error": "Column is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查data键是否存在
        if not data:
            return Response({"error": "Data is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查data是否为列表
        if not isinstance(data, list):
            return Response({"error": "Data should be a list"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查列表中的项目是否为字典
        if not all(isinstance(item, dict) for item in data):
            return Response({"error": "All items in data should be dictionaries"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 获取具有有效数值类型的数据列
            values = [item.get(column) for item in data if isinstance(
                item.get(column), (int, float))]

            if not values:
                return Response({"error": "Column not found in data or contains no valid numeric data"}, status=status.HTTP_404_NOT_FOUND)

            stats_data = get_stats(values)
            return Response(stats_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        return Response({"error": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# 相关系数
class CorrelationView(APIView):
    def post(self, request):
        try:
            data = request.data

            if not data:
                return Response({"error": "没有提供数据。"}, status=status.HTTP_400_BAD_REQUEST)

            column1_name = data.get('column1')
            column2_name = data.get('column2')

            if column1_name is None or column2_name is None:
                return Response({"error": "缺少必要的数据列名称。"}, status=status.HTTP_400_BAD_REQUEST)

            origin_data = pd.DataFrame.from_dict(data.get('data'))

            corr_coefficient = calculate_correlation(
                origin_data, column1_name, column2_name)

            return Response({"correlation": corr_coefficient})

        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "服务器内部错误: {}".format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# t检验
class TTestView(APIView):
    def post(self, request, *args, **kwargs):
        req_data = request.data

        if not req_data:
            return Response({"error": "Request data is empty or not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        column1 = req_data.get('column1')
        column2 = req_data.get('column2')
        data = req_data.get('data')
        alpha = req_data.get('alpha', 0.05)

        if not column1 or not column2 or not data:
            return Response({"error": "column1, column2, and data are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data1 = [item.get(column1) for item in data if isinstance(
                item.get(column1), (int, float))]
            data2 = [item.get(column2) for item in data if isinstance(
                item.get(column2), (int, float))]

            result = ttest(data1, data2, alpha)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 单因素方差分析
class AnovaView(APIView):
    def post(self, request, *args, **kwargs):
        req_data = request.data

        if not req_data:
            return Response({"error": "Request data is empty or not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        column1 = req_data.get('column1')
        column2 = req_data.get('column2')
        data = req_data.get('data')
        alpha = req_data.get('alpha', 0.05)

        if not column1 or not column2 or not data:
            return Response({"error": "column1, column2, and data are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group1 = [d[column1] for d in data]
            group2 = [d[column2] for d in data]

            result = anova(group1, group2, alpha)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
