# 图表类型详解

本文档详细介绍OriginPro支持的25种图表类型，包括使用场景、参数说明和示例代码。

## 基础图表类型

### 1. 折线图 (Line Chart)

**用途**: 展示数据随时间或其他连续变量的变化趋势

**适用场景**:
- 时间序列数据
- 实验结果趋势
- 连续变量关系

**函数签名**:
```python
line_chart(x_data, y_data, title="Line Chart", xlabel="X", ylabel="Y", save_path=None)
```

**参数说明**:
- `x_data`: X轴数据列表
- `y_data`: Y轴数据列表
- `title`: 图表标题
- `xlabel`: X轴标签
- `ylabel`: Y轴标签
- `save_path`: 保存路径（可选）

**示例**:
```python
import origin_graph_library as ogl

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

ogl.line_chart(x, y, title="实验结果", xlabel="时间", ylabel="浓度")
```

---

### 2. 散点图 (Scatter Plot)

**用途**: 展示两个变量之间的相关性

**适用场景**:
- 相关性分析
- 离群值检测
- 数据分布可视化

**函数签名**:
```python
scatter_chart(x_data, y_data, title="Scatter Plot", xlabel="X", ylabel="Y", save_path=None)
```

**示例**:
```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

ogl.scatter_chart(x, y, title="相关性分析", xlabel="X变量", ylabel="Y变量")
```

---

### 3. 柱状图 (Column Chart)

**用途**: 比较不同类别的数值大小

**适用场景**:
- 分类数据比较
- 组间差异分析
- 频率统计

**函数签名**:
```python
column_chart(categories, values, title="Column Chart", xlabel="Category", ylabel="Value", save_path=None)
```

**示例**:
```python
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

ogl.column_chart(categories, values, title="组间比较", xlabel="组别", ylabel="测量值")
```

---

### 4. 条形图 (Bar Chart)

**用途**: 水平展示分类数据比较

**适用场景**:
- 长标签分类
- 排名展示
- 水平比较

**函数签名**:
```python
bar_chart(categories, values, title="Bar Chart", xlabel="Value", ylabel="Category", save_path=None)
```

---

### 5. 饼图 (Pie Chart)

**用途**: 展示各部分占整体的比例

**适用场景**:
- 比例展示
- 组成成分
- 百分比分布

**函数签名**:
```python
pie_chart(labels, values, title="Pie Chart", save_path=None)
```

**示例**:
```python
labels = ['A', 'B', 'C', 'D']
values = [30, 25, 20, 25]

ogl.pie_chart(labels, values, title="组成比例")
```

---

### 6. 面积图 (Area Chart)

**用途**: 展示数据的累积变化

**适用场景**:
- 累积效应
- 堆叠趋势
- 面积比较

**函数签名**:
```python
area_chart(x_data, y_data, title="Area Chart", xlabel="X", ylabel="Y", save_path=None)
```

---

### 7. 直方图 (Histogram)

**用途**: 展示数据的频率分布

**适用场景**:
- 数据分布分析
- 正态性检验
- 频率统计

**函数签名**:
```python
histogram_chart(data, title="Histogram", xlabel="Value", ylabel="Frequency", save_path=None)
```

**示例**:
```python
import numpy as np

data = np.random.normal(100, 15, 1000)
ogl.histogram_chart(data, title="数据分布", xlabel="值", ylabel="频率")
```

---

### 8. 箱线图 (Box Plot)

**用途**: 展示数据的分布和异常值

**适用场景**:
- 描述性统计
- 组间分布比较
- 异常值检测

**函数签名**:
```python
box_chart(data_list, labels, title="Box Plot", xlabel="Group", ylabel="Value", save_path=None)
```

**示例**:
```python
data_list = [
    np.random.normal(50, 10, 100),
    np.random.normal(60, 15, 100),
    np.random.normal(55, 12, 100)
]
labels = ['Control', 'Treatment1', 'Treatment2']

ogl.box_chart(data_list, labels, title="组间分布比较", xlabel="组别", ylabel="测量值")
```

---

### 9. 热力图 (Heatmap)

**用途**: 展示矩阵数据

**适用场景**:
- 相关矩阵
- 基因表达
- 热力分布

**函数签名**:
```python
heatmap_chart(data, title="Heatmap", save_path=None)
```

---

### 10. 等高线图 (Contour Plot)

**用途**: 将三维数据用二维等高线展示

**适用场景**:
- 地形图
- 响应面
- 等值线图

**函数签名**:
```python
contour_chart(x_data, y_data, z_data, title="Contour Plot", save_path=None)
```

---

### 11. 3D表面图 (Surface Plot)

**用途**: 展示三维数据

**适用场景**:
- 响应面分析
- 曲面拟合
- 三维可视化

**函数签名**:
```python
surface_chart(x_data, y_data, z_data, title="Surface Plot", save_path=None)
```

---

### 12. 多线图 (Multi-Line Chart)

**用途**: 比较多个系列的趋势

**适用场景**:
- 多组实验结果
- 多指标趋势
- 系列比较

**函数签名**:
```python
multi_line_chart(x_data, y_data_list, labels, title="Multi-Line Chart", 
                xlabel="X", ylabel="Y", save_path=None)
```

**示例**:
```python
x = [1, 2, 3, 4, 5]
y_data_list = [
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [20, 30, 40, 50, 60]
]
labels = ['Series A', 'Series B', 'Series C']

ogl.multi_line_chart(x, y_data_list, labels, title="多系列比较")
```

---

### 13. 双Y轴图 (Dual Axis Chart)

**用途**: 展示不同量纲的数据

**适用场景**:
- 多指标趋势
- 不同单位比较
- 双变量分析

**函数签名**:
```python
dual_axis_chart(x_data, y1_data, y2_data, title="Dual Axis Chart",
               xlabel="X", ylabel1="Y1", ylabel2="Y2", save_path=None)
```

---

### 14. 线性拟合 (Linear Fit)

**用途**: 进行线性回归分析

**适用场景**:
- 相关性分析
- 预测模型
- 趋势线

**函数签名**:
```python
linear_fit(x_data, y_data, title="Linear Fit", save_path=None)
```

---

### 15. 非线性拟合 (Nonlinear Fit)

**用途**: 进行非线性回归分析

**适用场景**:
- 剂量反应曲线
- 生长曲线
- 非线性关系

**函数签名**:
```python
nonlinear_fit(x_data, y_data, function='gauss', title="Nonlinear Fit", save_path=None)
```

---

## 扩展图表类型

### 16. 误差棒图 (Error Bar Chart)

**用途**: 展示数据的不确定性（标准差、标准误、置信区间）

**适用场景**:
- Mean±SD/SE展示
- 实验误差表示
- 置信区间可视化

**函数签名**:
```python
error_bar_chart(x_data, y_data, y_error, title="Error Bar Chart",
               xlabel="X", ylabel="Y", save_path=None)
```

**示例**:
```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
y_error = [1.5, 2.0, 1.8, 2.5, 3.0]

ogl.error_bar_chart(x, y, y_error, title="实验结果（Mean±SD）", 
                   xlabel="时间", ylabel="浓度")
```

---

### 17. 分组柱状图 (Grouped Column Chart)

**用途**: 多系列并列比较

**适用场景**:
- 多组比较
- 多指标分析
- 并列展示

**函数签名**:
```python
grouped_column_chart(categories, data_dict, title="Grouped Column Chart",
                    xlabel="Category", ylabel="Value", save_path=None)
```

**示例**:
```python
categories = ['Group A', 'Group B', 'Group C']
data_dict = {
    'Control': [25, 30, 35],
    'Treatment': [40, 45, 50]
}

ogl.grouped_column_chart(categories, data_dict, title="组间比较")
```

---

### 18. 堆叠柱状图 (Stacked Column Chart)

**用途**: 展示组成成分

**适用场景**:
- 比例比较
- 组成分析
- 累积效果

**函数签名**:
```python
stacked_column_chart(categories, data_dict, title="Stacked Column Chart",
                    xlabel="Category", ylabel="Value", save_path=None)
```

---

### 19. 气泡图 (Bubble Chart)

**用途**: 展示三个变量的关系

**适用场景**:
- 三变量分析
- 多维数据
- 气泡大小表示第三维

**函数签名**:
```python
bubble_chart(x_data, y_data, size_data, title="Bubble Chart",
            xlabel="X", ylabel="Y", save_path=None)
```

**示例**:
```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
size = [100, 200, 300, 400, 500]

ogl.bubble_chart(x, y, size, title="三变量关系", xlabel="X", ylabel="Y")
```

---

### 20. 小提琴图 (Violin Chart)

**用途**: 展示数据分布密度

**适用场景**:
- 分布比较
- 密度估计
- 多组分布

**函数签名**:
```python
violin_chart(data_list, labels, title="Violin Chart",
            xlabel="Group", ylabel="Value", save_path=None)
```

**示例**:
```python
data_list = [
    np.random.normal(50, 10, 100),
    np.random.normal(60, 15, 100)
]
labels = ['Control', 'Treatment']

ogl.violin_chart(data_list, labels, title="分布比较")
```

---

### 21. 雷达图 (Radar Chart)

**用途**: 多维数据比较

**适用场景**:
- 能力评估
- 多指标对比
- 综合评价

**函数签名**:
```python
radar_chart(categories, data_dict, title="Radar Chart", save_path=None)
```

**示例**:
```python
categories = ['Speed', 'Strength', 'Endurance', 'Flexibility', 'Agility']
data_dict = {
    'Athlete1': [85, 90, 75, 80, 95],
    'Athlete2': [90, 85, 80, 75, 85]
}

ogl.radar_chart(categories, data_dict, title="运动员能力评估")
```

---

### 22. 森林图 (Forest Plot)

**用途**: 展示Meta分析结果

**适用场景**:
- 系统综述
- 效应量汇总
- 置信区间展示

**函数签名**:
```python
forest_chart(studies, effect_sizes, ci_lower, ci_upper, weights=None,
            title="Forest Plot", xlabel="Effect Size", save_path=None)
```

**示例**:
```python
studies = ['Study1', 'Study2', 'Study3', 'Study4', 'Study5']
effect_sizes = [0.5, 0.3, 0.8, 0.6, 0.4]
ci_lower = [0.2, 0.1, 0.5, 0.3, 0.2]
ci_upper = [0.8, 0.5, 1.1, 0.9, 0.6]
weights = [20, 15, 25, 18, 12]

ogl.forest_chart(studies, effect_sizes, ci_lower, ci_upper, weights,
                title="Meta分析结果")
```

---

### 23. 生存曲线 (Kaplan-Meier)

**用途**: 生存分析

**适用场景**:
- 临床研究
- 生存率分析
- 风险比较

**函数签名**:
```python
survival_chart(time_data, event_data, groups=None, title="Kaplan-Meier Curve",
              xlabel="Time", ylabel="Survival Probability", save_path=None)
```

**示例**:
```python
time_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
event_data = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
groups = ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']

ogl.survival_chart(time_data, event_data, groups, title="生存曲线")
```

---

### 24. Bland-Altman图

**用途**: 方法一致性分析

**适用场景**:
- 方法学比较
- 一致性评估
- 偏差分析

**函数签名**:
```python
bland_altman_chart(method1, method2, title="Bland-Altman Plot",
                  xlabel="Mean of Two Methods", ylabel="Difference", save_path=None)
```

**示例**:
```python
method1 = [100, 105, 110, 95, 102]
method2 = [102, 103, 112, 97, 100]

ogl.bland_altman_chart(method1, method2, title="方法一致性分析")
```

---

### 25. 散点矩阵 (Scatter Matrix)

**用途**: 多变量相关性分析

**适用场景**:
- 探索性数据分析
- 多变量关系
- 相关性矩阵

**函数签名**:
```python
scatter_matrix(data_dict, title="Scatter Matrix", save_path=None)
```

**示例**:
```python
data_dict = {
    'Var1': np.random.randn(100),
    'Var2': np.random.randn(100),
    'Var3': np.random.randn(100)
}

ogl.scatter_matrix(data_dict, title="多变量相关性")
```

---

## 图表选择指南

### 根据数据类型选择

| 数据类型 | 推荐图表 |
|---------|---------|
| 时间序列 | 折线图、面积图 |
| 分类比较 | 柱状图、条形图、分组柱状图 |
| 相关性 | 散点图、散点矩阵 |
| 分布 | 直方图、箱线图、小提琴图 |
| 比例 | 饼图、堆叠柱状图 |
| 多维 | 雷达图、气泡图 |
| 统计 | 误差棒图、森林图、生存曲线 |

### 根据展示目的选择

| 展示目的 | 推荐图表 |
|---------|---------|
| 趋势变化 | 折线图 |
| 大小比较 | 柱状图、条形图 |
| 关系分析 | 散点图 |
| 分布形状 | 箱线图、小提琴图 |
| 组成成分 | 饼图、堆叠柱状图 |
| 不确定性 | 误差棒图 |
| 综合评估 | 雷达图 |
