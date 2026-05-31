---
name: origin-chart-creator
description: |
  创建出版质量的OriginPro图表，支持25种论文常见图表类型，提供Nature/Science级别样式。
  当用户需要创建图表、可视化数据、生成论文图表、画图时使用。
  支持：折线图、柱状图、散点图、箱线图、热力图、误差棒图、分组柱状图、堆叠柱状图、
  小提琴图、雷达图、气泡图、森林图、生存曲线、Bland-Altman图、散点矩阵等。
  自动处理数据导入、清洗、转换，并智能推荐图表类型。
---

# OriginPro 图表创建技能

创建出版质量的科学图表，支持25种论文常见图表类型。

## 功能概述

1. 数据导入和处理（CSV/Excel）
2. 智能图表类型推荐（根据数据特征）
3. 图表创建和样式定制
4. 导出为出版质量格式（PNG/SVG/PDF/TIFF）

## 用户引导

当用户请求模糊（如"根据数据生成图表"）时，读取 `references/guidance.md` 获取完整的引导流程。

## 支持的图表类型

### 基础（15种）
| 类型 | 函数 | 用途 |
|------|------|------|
| 折线图 | `line_chart` | 趋势变化 |
| 柱状图 | `column_chart` | 分类比较 |
| 条形图 | `bar_chart` | 水平比较 |
| 散点图 | `scatter_chart` | 相关性 |
| 饼图 | `pie_chart` | 比例 |
| 面积图 | `area_chart` | 累积变化 |
| 直方图 | `histogram_chart` | 分布 |
| 箱线图 | `box_chart` | 异常值检测 |
| 热力图 | `heatmap_chart` | 矩阵数据 |
| 等高线图 | `contour_chart` | 3D→2D |
| 3D表面图 | `surface_chart` | 3D可视化 |
| 多线图 | `multi_line_chart` | 多系列 |
| 双Y轴图 | `dual_axis_chart` | 不同量纲 |
| 线性拟合 | `linear_fit` | 回归 |
| 非线性拟合 | `nonlinear_fit` | 曲线拟合 |

### 扩展（10种）
| 类型 | 函数 | 用途 |
|------|------|------|
| 误差棒图 | `error_bar_chart` | Mean±SD/SE |
| 分组柱状图 | `grouped_column_chart` | 多系列并列 |
| 堆叠柱状图 | `stacked_column_chart` | 组成成分 |
| 气泡图 | `bubble_chart` | 三变量 |
| 小提琴图 | `violin_chart` | 分布密度 |
| 雷达图 | `radar_chart` | 多维比较 |
| 森林图 | `forest_chart` | Meta分析 |
| 生存曲线 | `survival_chart` | Kaplan-Meier |
| Bland-Altman图 | `bland_altman_chart` | 方法一致性 |
| 散点矩阵 | `scatter_matrix` | 多变量相关 |

## 快速示例

```python
import origin_graph_library as ogl

# 折线图
ogl.line_chart([1,2,3,4,5], [10,20,30,40,50], title="Demo", xlabel="X", ylabel="Y")

# 误差棒图
ogl.error_bar_chart(x, y, y_error, title="Mean±SD")

# 分组柱状图
ogl.grouped_column_chart(['A','B','C'], {'Control':[25,30,35], 'Treatment':[40,45,50]})
```

## 数据处理

```python
from data_processing import load_csv, DataPipeline, handle_missing_values

df = load_csv('data.csv')
pipeline = DataPipeline()
pipeline.add_step(handle_missing_values, strategy='mean')
clean = pipeline.execute(df)
```

## 样式指南

详见 `references/style_guide.md`：
- 颜色：低饱和度（NMI pastel）
- 字体：Arial 7-10pt
- 分辨率：600 DPI
- 格式：SVG/PDF/TIFF（可编辑文本）

## 文件结构

```
origin-chart-creator/
├── SKILL.md                  # 本文件
├── scripts/
│   ├── chart_creator.py      # 图表创建
│   ├── data_processor.py     # 数据处理
│   └── style_templates.py    # 样式模板
├── references/
│   ├── guidance.md           # 用户引导流程
│   ├── chart_types.md        # 图表类型详解
│   ├── style_guide.md        # 样式指南
│   └── examples.md           # 示例代码
└── assets/
    ├── color_palettes.json   # 颜色方案
    └── sample_data/          # 测试数据
```

## 依赖项

- Python 3.8+
- pandas, numpy
- originpro（OriginPro Python接口）

## 常见问题

**Q: 如何选择图表类型？** A: 系统会根据数据特征自动推荐。

**Q: 如何达到Nature级别？** A: 使用专业配色 + 简洁布局 + 600 DPI + 可编辑文本。

**Q: 如何批量处理？** A: 使用 `export_all_graphs()` 或循环处理多个数据集。

## 相关技能

- `nature-figure` - Nature级别图表设计
- `chart-generator` - matplotlib图表生成
