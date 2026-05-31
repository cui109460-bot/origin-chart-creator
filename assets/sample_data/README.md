# Sample Data

用于测试 origin-chart-creator 技能的示例数据集。

## 文件说明

| 文件 | 数据类型 | 适用图表 |
|------|---------|---------|
| `time_series.csv` | 时间序列 | 折线图、面积图、多线图 |
| `group_comparison.csv` | 分组比较 | 柱状图、箱线图、误差棒图 |
| `multivariate.csv` | 多变量相关 | 散点图、散点矩阵、热力图 |

## 使用示例

```python
from scripts.data_processor import DataProcessor

processor = DataProcessor()
processor.load_data('assets/sample_data/time_series.csv')
print(processor.get_data_info())
```
