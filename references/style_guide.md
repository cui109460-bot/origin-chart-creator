# Nature级别图表样式指南

本文档提供创建出版质量图表的详细指南，遵循Nature、Science等顶级期刊的样式标准。

## 核心原则

### 1. 简洁清晰
- 避免冗余元素
- 使用清晰的标签
- 保持适当的留白

### 2. 专业配色
- 使用低饱和度颜色
- 避免过于鲜艳的颜色
- 确保颜色对比度足够

### 3. 可读性
- 使用合适的字体大小
- 确保文本清晰可读
- 避免重叠和遮挡

### 4. 可编辑性
- 使用矢量格式（SVG、PDF）
- 保持文本可编辑
- 避免栅格化文本

## 颜色方案

### 推荐配色

#### Nature风格（低饱和度）
```python
nature_colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B']
```

#### NMI风格（柔和色调）
```python
nmi_colors = ['#5B8DB8', '#8FBCDA', '#B5D8EB', '#D4E6F1', '#E8F4F8']
```

#### 单色方案
```python
monochrome = ['#2C3E50', '#34495E', '#7F8C8D', '#95A5A6', '#BDC3C7']
```

### 颜色使用规则

1. **数量限制**: 每个图表使用3-5种颜色
2. **对比度**: 确保颜色之间有足够的对比度
3. **一致性**: 同一系列使用相同颜色
4. **色盲友好**: 避免仅依赖颜色区分

## 字体规范

### 推荐字体

- **主要字体**: Arial、Helvetica
- **备选字体**: DejaVu Sans、Liberation Sans
- **避免使用**: Times New Roman（除非期刊要求）

### 字体大小

| 元素 | 大小（pt） |
|------|-----------|
| 轴标签 | 7-9 |
| 刻度标签 | 6-7 |
| 图例 | 7-8 |
| 标题 | 10-12 |
| 注释 | 6-7 |

### 字体设置代码

```python
import matplotlib as mpl

mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 7,
    'axes.titlesize': 10,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7
})
```

## 坐标轴样式

### 基本设置

```python
mpl.rcParams.update({
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 4,
    'ytick.major.size': 4,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8
})
```

### 坐标轴标签

- 使用描述性标签
- 包含单位（如适用）
- 避免缩写（除非必要）

**示例**:
```python
# 好的标签
plt.xlabel('Time (minutes)')
plt.ylabel('Concentration (μM)')

# 不好的标签
plt.xlabel('t')
plt.ylabel('C')
```

## 图表尺寸

### 推荐尺寸（毫米）

| 类型 | 宽度 | 高度 | 用途 |
|------|------|------|------|
| 单栏图 | 89 | 70 | 期刊单栏 |
| 1.5栏图 | 140 | 100 | 期刊1.5栏 |
| 双栏图 | 183 | 120 | 期刊双栏 |
| 整页图 | 183 | 240 | 整页展示 |
| 正方形图 | 100 | 100 | 特殊用途 |

### 尺寸转换代码

```python
def mm_to_inches(mm):
    return mm / 25.4

# 创建图表
fig, ax = plt.subplots(figsize=(mm_to_inches(183), mm_to_inches(120)))
```

## 导出设置

### 推荐格式

| 格式 | 用途 | 设置 |
|------|------|------|
| SVG | 矢量图，可编辑 | `fonttype='none'` |
| PDF | 矢量图，出版用 | `fonttype=42` |
| TIFF | 位图，高分辨率 | `dpi=600, compression='lzw'` |
| PNG | 位图，预览用 | `dpi=300` |

### 导出代码

```python
# SVG导出
fig.savefig('figure.svg', bbox_inches='tight')

# PDF导出
fig.savefig('figure.pdf', bbox_inches='tight')

# TIFF导出
fig.savefig('figure.tiff', dpi=600, bbox_inches='tight', compression='lzw')
```

## 图例位置

### 推荐位置

- **最佳位置**: 图表内部空白区域
- **避免位置**: 遮挡数据点
- **备选位置**: 图表外部（右侧或下方）

### 图例样式

```python
legend = ax.legend(
    loc='best',  # 自动选择最佳位置
    frameon=False,  # 无边框
    fontsize=7,
    ncol=1,  # 列数
    handlelength=2,  # 图例线长度
    handletextpad=0.5,  # 文本间距
    columnspacing=1  # 列间距
)
```

## 网格线

### 使用建议

- **使用**: 当需要精确读取数值时
- **不使用**: 当图表已经足够清晰时
- **样式**: 浅灰色、细线、虚线

### 网格线代码

```python
ax.grid(True, linestyle='--', alpha=0.3, color='gray', linewidth=0.5)
ax.set_axisbelow(True)  # 网格线在数据下方
```

## 特殊图表类型

### 箱线图

```python
boxprops = dict(linestyle='-', linewidth=0.8, color='black')
medianprops = dict(linestyle='-', linewidth=1.5, color='red')
whiskerprops = dict(linestyle='-', linewidth=0.8, color='black')
capprops = dict(linestyle='-', linewidth=0.8, color='black')

ax.boxplot(data, boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops)
```

### 误差棒图

```python
ax.errorbar(x, y, yerr=error, fmt='o', markersize=4, capsize=3, 
            capthick=0.8, elinewidth=0.8, color='black')
```

### 热力图

```python
im = ax.imshow(data, cmap='YlOrRd', aspect='auto')
cbar = plt.colorbar(im, ax=ax)
cbar.ax.tick_params(labelsize=7)
```

## 常见错误

### 避免的问题

1. **颜色过于鲜艳**: 使用低饱和度颜色
2. **字体太小**: 确保打印后清晰可读
3. **图表太复杂**: 保持简洁
4. **缺少单位**: 在标签中包含单位
5. **图例遮挡**: 将图例放在合适位置
6. **分辨率太低**: 使用600 DPI
7. **文本不可编辑**: 使用矢量格式

## 检查清单

在提交图表前，检查以下项目：

- [ ] 颜色方案合适
- [ ] 字体大小足够
- [ ] 坐标轴标签清晰
- [ ] 图例位置合适
- [ ] 分辨率足够（600 DPI）
- [ ] 格式正确（SVG/PDF/TIFF）
- [ ] 文本可编辑
- [ ] 无冗余元素
- [ ] 尺寸符合要求

## 参考资源

- [Nature Methods Style Guidelines](https://www.nature.com/nmeth/collect/)
- [Science Magazine Art Guidelines](https://www.science.org/content/page/instructions-preparing-initial-manuscript)
- [Cell Press Figure Guidelines](https://www.cell.com/figure-guidelines)
