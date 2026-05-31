# origin-chart-creator

An OpenCode skill for creating publication-quality OriginPro charts with **25 chart types**.

## Features

- 25 chart types (line, scatter, bar, box, heatmap, error bar, grouped bar, stacked bar, violin, radar, bubble, forest, survival, Bland-Altman, scatter matrix, and more)
- Smart chart type recommendation based on data characteristics
- Nature/Science journal styling
- Data processing pipeline (CSV/Excel import, cleaning, transformation)
- User guidance workflow with chart comparison

## Installation

```bash
# Install via skillkit
npx skillkit install <your-repo>/origin-chart-creator

# Or clone directly
git clone https://github.com/cui109460-bot/origin-chart-creator.git skills/origin-chart-creator
```

## Supported Chart Types

### Basic (15)
| Chart | Function | Use Case |
|-------|----------|----------|
| Line | `line_chart` | Trend over time |
| Column | `column_chart` | Category comparison |
| Bar | `bar_chart` | Horizontal comparison |
| Scatter | `scatter_chart` | Correlation |
| Pie | `pie_chart` | Proportion |
| Area | `area_chart` | Cumulative change |
| Histogram | `histogram_chart` | Distribution |
| Box | `box_chart` | Outlier detection |
| Heatmap | `heatmap_chart` | Matrix data |
| Contour | `contour_chart` | 3D-to-2D projection |
| 3D Surface | `surface_chart` | 3D visualization |
| Multi-Line | `multi_line_chart` | Multi-series trends |
| Dual Axis | `dual_axis_chart` | Different scales |
| Linear Fit | `linear_fit` | Regression |
| Nonlinear Fit | `nonlinear_fit` | Curve fitting |

### Extended (10)
| Chart | Function | Use Case |
|-------|----------|----------|
| Error Bar | `error_bar_chart` | Mean±SD/SE |
| Grouped Bar | `grouped_column_chart` | Multi-series comparison |
| Stacked Bar | `stacked_column_chart` | Composition |
| Violin | `violin_chart` | Distribution density |
| Radar | `radar_chart` | Multi-dimensional |
| Bubble | `bubble_chart` | 3 variables |
| Forest | `forest_chart` | Meta-analysis |
| Survival | `survival_chart` | Kaplan-Meier |
| Bland-Altman | `bland_altman_chart` | Method agreement |
| Scatter Matrix | `scatter_matrix` | Multi-variable correlation |

## Usage

```python
import origin_graph_library as ogl

# Line chart
ogl.line_chart([1,2,3,4,5], [10,20,30,40,50], title="Demo", xlabel="X", ylabel="Y")

# Error bar chart
ogl.error_bar_chart(x, y, y_error, title="Mean±SD")

# Grouped bar chart
ogl.grouped_column_chart(categories, {'Control': [...], 'Treatment': [...]})
```

## License

MIT
