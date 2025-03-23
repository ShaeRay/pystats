# django-dockerfile
FROM python:3.9
 
# 设置工作目录
WORKDIR /app
 
# 复制项目文件到容器中的工作目录
COPY . /app
 
# 安装项目依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirements.txt
 
# 暴露容器的 8000 端口
EXPOSE 8000
 
# 启动 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
