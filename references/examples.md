# 示例代码

本文档提供各种图表类型的完整示例代码，可直接运行。

## 示例1：临床试验折线图

### 场景
展示不同治疗组随时间变化的疗效指标。

### 数据
- 时间点：0, 1, 2, 4, 8, 12周
- 治疗组：对照组、低剂量组、高剂量组
- 指标：生物标志物浓度

### 代码
```python
import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_processing import DataPipeline, handle_missing_values
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)
n_patients = 30
time_points = [0, 1, 2, 4, 8, 12]

clinical_data = []
for patient in range(n_patients):
    treatment = np.random.choice(['Control', 'Low Dose', 'High Dose'])
    for time in time_points:
        if treatment == 'Control':
            value = 50 + time * 0.5 + np.random.randn() * 5
        elif treatment == 'Low Dose':
            value = 50 + time * 2 + np.random.randn() * 6
        else:
            value = 50 + time * 4 + np.random.randn() * 7
        
        clinical_data.append({
            'patient_id': patient,
            'time_weeks': time,
            'treatment': treatment,
            'biomarker': value
        })

df = pd.DataFrame(clinical_data)

# 计算每组的均值和标准误
grouped = df.groupby(['time_weeks', 'treatment'])['biomarker'].agg(['mean', 'sem']).reset_index()

# 创建图表
for treatment in grouped['treatment'].unique():
    data = grouped[grouped['treatment'] == treatment]
    ogl.error_bar_chart(
        data['time_weeks'].tolist(),
        data['mean'].tolist(),
        data['sem'].tolist(),
        title=f"Clinical Trial Results - {treatment}",
        xlabel="Time (weeks)",
        ylabel="Biomarker Concentration"
    )
```

---

## 示例2：分组柱状图比较

### 场景
比较不同组别在多个指标上的表现。

### 数据
- 组别：A、B、C
- 指标：指标1、指标2、指标3

### 代码
```python
import origin_graph_library as ogl

# 准备数据
categories = ['Group A', 'Group B', 'Group C']
data_dict = {
    'Indicator 1': [25, 30, 35],
    'Indicator 2': [40, 45, 50],
    'Indicator 3': [35, 40, 45]
}

# 创建分组柱状图
chart = ogl.grouped_column_chart(
    categories, data_dict,
    title="Multi-Indicator Comparison",
    xlabel="Group",
    ylabel="Score"
)

# 自定义样式
ogl.set_axis_properties(chart, x_title="Experimental Group", y_title="Score (0-100)")
ogl.add_legend(chart)
```

---

## 示例3：相关性散点图

### 场景
分析两个变量之间的相关性。

### 数据
- 变量X：身高
- 变量Y：体重

### 代码
```python
import numpy as np
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)
n = 100

height = np.random.normal(170, 10, n)  # 身高（cm）
weight = 0.5 * height + np.random.randn(n) * 5 + 20  # 体重（kg）

# 创建散点图
chart = ogl.scatter_chart(
    height.tolist(),
    weight.tolist(),
    title="Height vs Weight Correlation",
    xlabel="Height (cm)",
    ylabel="Weight (kg)"
)

# 添加线性拟合
ogl.linear_fit(height.tolist(), weight.tolist(), title="Linear Regression")
```

---

## 示例4：箱线图分布比较

### 场景
比较不同组别的数据分布。

### 数据
- 组别：对照组、处理组1、处理组2
- 测量值：连续变量

### 代码
```python
import numpy as np
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)

data_list = [
    np.random.normal(50, 10, 100).tolist(),  # 对照组
    np.random.normal(60, 15, 100).tolist(),  # 处理组1
    np.random.normal(55, 12, 100).tolist()   # 处理组2
]
labels = ['Control', 'Treatment 1', 'Treatment 2']

# 创建箱线图
chart = ogl.box_chart(
    data_list, labels,
    title="Distribution Comparison",
    xlabel="Group",
    ylabel="Measurement Value"
)
```

---

## 示例5：热力图相关矩阵

### 场景
展示多个变量之间的相关性。

### 数据
- 变量：5个连续变量
- 相关系数矩阵

### 代码
```python
import numpy as np
import pandas as pd
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)
n = 100

# 创建相关数据
x1 = np.random.randn(n)
x2 = x1 * 0.8 + np.random.randn(n) * 0.2
x3 = x1 * 0.5 + np.random.randn(n) * 0.5
x4 = np.random.randn(n)
x5 = x3 * 0.6 + np.random.randn(n) * 0.4

data = pd.DataFrame({
    'Variable 1': x1,
    'Variable 2': x2,
    'Variable 3': x3,
    'Variable 4': x4,
    'Variable 5': x5
})

# 计算相关矩阵
corr_matrix = data.corr()

# 创建热力图
chart = ogl.heatmap_chart(
    corr_matrix.values.tolist(),
    title="Correlation Matrix"
)
```

---

## 示例6：堆叠柱状图组成分析

### 场景
展示不同类别的组成成分。

### 数据
- 类别：产品A、B、C
- 成分：成分1、2、3

### 代码
```python
import origin_graph_library as ogl

# 准备数据
categories = ['Product A', 'Product B', 'Product C']
data_dict = {
    'Component 1': [30, 25, 35],
    'Component 2': [20, 30, 25],
    'Component 3': [10, 15, 20]
}

# 创建堆叠柱状图
chart = ogl.stacked_column_chart(
    categories, data_dict,
    title="Product Composition Analysis",
    xlabel="Product",
    ylabel="Quantity"
)
```

---

## 示例7：雷达图多维比较

### 场景
比较多个对象在多个维度上的表现。

### 数据
- 对象：运动员1、运动员2
- 维度：速度、力量、耐力、灵活性、敏捷性

### 代码
```python
import origin_graph_library as ogl

# 准备数据
categories = ['Speed', 'Strength', 'Endurance', 'Flexibility', 'Agility']
data_dict = {
    'Athlete 1': [85, 90, 75, 80, 95],
    'Athlete 2': [90, 85, 80, 75, 85]
}

# 创建雷达图
chart = ogl.radar_chart(
    categories, data_dict,
    title="Athlete Performance Comparison"
)
```

---

## 示例8：森林图Meta分析

### 场景
展示多个研究的效应量和置信区间。

### 数据
- 研究：5个独立研究
- 效应量：标准化均数差
- 置信区间：95% CI

### 代码
```python
import origin_graph_library as ogl

# 准备数据
studies = ['Study 1', 'Study 2', 'Study 3', 'Study 4', 'Study 5']
effect_sizes = [0.5, 0.3, 0.8, 0.6, 0.4]
ci_lower = [0.2, 0.1, 0.5, 0.3, 0.2]
ci_upper = [0.8, 0.5, 1.1, 0.9, 0.6]
weights = [20, 15, 25, 18, 12]

# 创建森林图
chart = ogl.forest_chart(
    studies, effect_sizes, ci_lower, ci_upper, weights,
    title="Meta-Analysis Results",
    xlabel="Standardized Mean Difference"
)
```

---

## 示例9：生存曲线

### 场景
展示不同治疗组的生存率。

### 数据
- 时间：月
- 事件：死亡/删失
- 组别：治疗组、对照组

### 代码
```python
import numpy as np
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)
n = 200

time_data = np.random.exponential(24, n).tolist()
event_data = np.random.choice([0, 1], n, p=[0.3, 0.7]).tolist()
groups = np.random.choice(['Treatment', 'Control'], n).tolist()

# 创建生存曲线
chart = ogl.survival_chart(
    time_data, event_data, groups,
    title="Kaplan-Meier Survival Curve",
    xlabel="Time (months)",
    ylabel="Survival Probability"
)
```

---

## 示例10：Bland-Altman一致性分析

### 场景
比较两种测量方法的一致性。

### 数据
- 方法1：标准方法
- 方法2：新方法

### 代码
```python
import numpy as np
import origin_graph_library as ogl

# 生成模拟数据
np.random.seed(42)
n = 50

method1 = np.random.normal(100, 10, n).tolist()
method2 = [m + np.random.randn() * 3 for m in method1]

# 创建Bland-Altman图
chart = ogl.bland_altman_chart(
    method1, method2,
    title="Bland-Altman Agreement Analysis",
    xlabel="Mean of Two Methods",
    ylabel="Difference"
)
```

---

## 批量处理示例

### 场景
批量处理多个数据文件并生成图表。

### 代码
```python
import os
import pandas as pd
import origin_graph_library as ogl
from data_processing import load_csv, DataPipeline, handle_missing_values

# 文件列表
file_list = ['data1.csv', 'data2.csv', 'data3.csv']

# 输出目录
output_dir = 'output_charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 批量处理
for i, filepath in enumerate(file_list):
    # 加载数据
    df = load_csv(filepath)
    
    # 数据处理
    pipeline = DataPipeline()
    pipeline.add_step(handle_missing_values, strategy='mean')
    clean_data = pipeline.execute(df)
    
    # 创建图表
    chart = ogl.line_chart(
        clean_data['x'].tolist(),
        clean_data['y'].tolist(),
        title=f"Chart {i+1}",
        xlabel="X",
        ylabel="Y"
    )
    
    # 保存图表
    output_path = os.path.join(output_dir, f"chart_{i+1}.png")
    chart.save_fig(output_path, dpi=300)
    print(f"Saved: {output_path}")
```

---

## 完整工作流示例

### 场景
从数据导入到图表导出的完整流程。

### 代码
```python
import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_processing import (
    load_csv, DataPipeline, handle_missing_values,
    filter_data, aggregate_data, export_for_origin
)
import origin_graph_library as ogl

# 步骤1：加载数据
print("Step 1: Loading data...")
df = load_csv('experiment_data.csv')

# 步骤2：数据清洗
print("Step 2: Cleaning data...")
pipeline = DataPipeline()
pipeline.add_step(handle_missing_values, strategy='mean')
clean_data = pipeline.execute(df)

# 步骤3：数据筛选
print("Step 3: Filtering data...")
filtered_data = filter_data(clean_data, conditions={'age': {'gte': 18}})

# 步骤4：数据聚合
print("Step 4: Aggregating data...")
agg_data = aggregate_data(
    filtered_data,
    group_by='treatment',
    agg_funcs={'outcome': ['mean', 'std']}
)

# 步骤5：准备OriginPro数据
print("Step 5: Preparing OriginPro data...")
origin_data = export_for_origin(
    filtered_data,
    x_column='time',
    y_columns=['outcome']
)

# 步骤6：创建图表
print("Step 6: Creating chart...")
chart = ogl.error_bar_chart(
    origin_data['x_data'],
    [np.mean(y) for y in origin_data['y_data']],
    [np.std(y) for y in origin_data['y_data']],
    title="Treatment Outcome Over Time",
    xlabel="Time (days)",
    ylabel="Outcome Score"
)

# 步骤7：自定义样式
print("Step 7: Customizing style...")
ogl.set_axis_properties(chart, x_title="Time (days)", y_title="Outcome Score")
ogl.add_legend(chart)

# 步骤8：导出图表
print("Step 8: Exporting chart...")
output_path = 'final_chart.png'
chart.save_fig(output_path, dpi=600)
print(f"Chart saved to: {output_path}")

print("Complete workflow finished!")
```
