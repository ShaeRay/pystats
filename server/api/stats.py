import numpy as np
from scipy import stats
from scipy.stats import pearsonr, f_oneway


# 描述统计
def get_stats(values):
    values = np.array(values)
    mean = np.mean(values)
    median = np.median(values)
    std_dev = np.std(values)
    variance = np.var(values)
    minimum = np.min(values)
    maximum = np.max(values)
    range_val = np.ptp(values)
    quartiles = np.percentile(values, [25, 50, 75])
    # 使用Shapiro-Wilk测试，返回值包括统计量和p-value
    shapiro_stat, shapiro_p_value = stats.shapiro(values)
    is_normal = shapiro_p_value > 0.05  # 如果p-value大于0.05，则数据接近正态分布

    return {
        "mean": mean.item(),  # 平均值
        "median": median.item(),  # 中位数
        "std_dev": std_dev.item(),  # 标准差
        "variance": variance.item(),  # 方差
        "min": minimum.item(),  # 最小值
        "max": maximum.item(),  # 最大值
        "range": range_val.item(),  # 全距
        "quartiles": quartiles.tolist(),  # 四分位数 (25%, 50%, 75%)
        "is_normal": is_normal,  # 正态性检测结果
    }


# 相关系数
def calculate_correlation(origin_data, column1_name, column2_name):
    if column1_name not in origin_data.columns or column2_name not in origin_data.columns:
        raise ValueError("指定的列名在数据中不存在。")

    corr_coefficient, _ = pearsonr(
        origin_data[column1_name], origin_data[column2_name])

    return corr_coefficient  # 相关系数


# t检验
def ttest(data1, data2, alpha=0.05):
    t_stat, p_val = stats.ttest_ind(data1, data2)

    result = {
        "t_statistic": t_stat,  # t值
        "p_value": p_val  # p值
    }

    return result


# 方差分析
def anova(column1, column2, alpha=0.05):
    f_value, p_value = f_oneway(column1, column2)

    result = {
        "f_statistic": f_value,  # f值
        "p_value": p_value,  # p值
        "conclusion": "Reject null hypothesis" if p_value < alpha else "Fail to reject null hypothesis"
    }

    return result
