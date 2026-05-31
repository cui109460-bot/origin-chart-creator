# -*- coding: utf-8 -*-
"""
样式模板
提供Nature级别图表样式
"""

# Nature级别颜色方案
NATURE_COLORS = {
    'primary': ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B'],
    'secondary': ['#4CAF50', '#FF9800', '#9C27B0', '#00BCD4', '#795548'],
    'pastel': ['#B5D8EB', '#E8B4CB', '#FFD4A3', '#F5B7B1', '#D5C4A1'],
    'monochrome': ['#2C3E50', '#34495E', '#7F8C8D', '#95A5A6', '#BDC3C7'],
    'nmi': ['#5B8DB8', '#8FBCDA', '#B5D8EB', '#D4E6F1', '#E8F4F8']
}

# 字体设置
FONT_SETTINGS = {
    'family': 'Arial',
    'size': {
        'small': 7,
        'medium': 9,
        'large': 12,
        'title': 14
    },
    'weight': {
        'normal': 'normal',
        'bold': 'bold'
    }
}

# 坐标轴样式
AXIS_STYLES = {
    'nature': {
        'spines': {'top': False, 'right': False},
        'linewidth': 0.8,
        'tick_direction': 'out',
        'tick_length': 4
    },
    'modern': {
        'spines': {'top': False, 'right': False},
        'linewidth': 1.0,
        'tick_direction': 'out',
        'tick_length': 6
    },
    'minimal': {
        'spines': {'top': False, 'right': False, 'bottom': False, 'left': False},
        'linewidth': 0,
        'tick_direction': 'none',
        'tick_length': 0
    }
}

# 图表尺寸（毫米）
FIGURE_SIZES = {
    'single': (89, 70),      # 单栏图
    '1.5column': (140, 100), # 1.5栏图
    'double': (183, 120),    # 双栏图
    'full_page': (183, 240), # 整页图
    'square': (100, 100),    # 正方形图
    'wide': (183, 80),       # 宽图
    'tall': (89, 150)        # 高图
}

# 导出设置
EXPORT_SETTINGS = {
    'png': {'dpi': 600, 'bbox_inches': 'tight'},
    'svg': {'fonttype': 'none', 'bbox_inches': 'tight'},
    'pdf': {'fonttype': 42, 'bbox_inches': 'tight'},
    'tiff': {'dpi': 600, 'compression': 'lzw'}
}


def get_color_palette(palette_name='primary', n_colors=None):
    """
    获取颜色方案
    
    参数:
        palette_name: 方案名称 ('primary', 'secondary', 'pastel', 'monochrome', 'nmi')
        n_colors: 需要的颜色数量
    
    返回:
        list: 颜色列表
    """
    palette = NATURE_COLORS.get(palette_name, NATURE_COLORS['primary'])
    
    if n_colors is None:
        return palette
    
    # 如果需要的颜色数量超过方案中的数量，循环使用
    if n_colors > len(palette):
        return [palette[i % len(palette)] for i in range(n_colors)]
    
    return palette[:n_colors]


def get_font_settings(size='medium', weight='normal'):
    """
    获取字体设置
    
    参数:
        size: 字体大小 ('small', 'medium', 'large', 'title')
        weight: 字体粗细 ('normal', 'bold')
    
    返回:
        dict: 字体设置字典
    """
    return {
        'family': FONT_SETTINGS['family'],
        'size': FONT_SETTINGS['size'].get(size, FONT_SETTINGS['size']['medium']),
        'weight': FONT_SETTINGS['weight'].get(weight, FONT_SETTINGS['weight']['normal'])
    }


def get_axis_style(style_name='nature'):
    """
    获取坐标轴样式
    
    参数:
        style_name: 样式名称 ('nature', 'modern', 'minimal')
    
    返回:
        dict: 坐标轴样式字典
    """
    return AXIS_STYLES.get(style_name, AXIS_STYLES['nature'])


def get_figure_size(size_name='single'):
    """
    获取图表尺寸
    
    参数:
        size_name: 尺寸名称 ('single', '1.5column', 'double', 'full_page', 'square', 'wide', 'tall')
    
    返回:
        tuple: (宽度, 高度) 毫米
    """
    return FIGURE_SIZES.get(size_name, FIGURE_SIZES['single'])


def get_export_settings(format='png'):
    """
    获取导出设置
    
    参数:
        format: 文件格式 ('png', 'svg', 'pdf', 'tiff')
    
    返回:
        dict: 导出设置字典
    """
    return EXPORT_SETTINGS.get(format, EXPORT_SETTINGS['png'])


def apply_nature_style(chart_type='line'):
    """
    应用Nature样式到图表
    
    参数:
        chart_type: 图表类型
    
    返回:
        dict: 样式设置字典
    """
    style = {
        'colors': get_color_palette('nmi'),
        'font': get_font_settings('medium'),
        'axis': get_axis_style('nature'),
        'figure_size': get_figure_size('single')
    }
    
    # 根据图表类型调整样式
    if chart_type in ['scatter', 'line']:
        style['marker_size'] = 6
        style['line_width'] = 1.5
    elif chart_type in ['column', 'bar']:
        style['bar_width'] = 0.8
        style['edge_color'] = 'white'
    elif chart_type in ['heatmap']:
        style['colormap'] = 'YlOrRd'
        style['annot'] = True
    
    return style


def create_style_template(style_name='nature'):
    """
    创建样式模板
    
    参数:
        style_name: 样式名称
    
    返回:
        dict: 完整的样式模板
    """
    template = {
        'name': style_name,
        'colors': get_color_palette('nmi'),
        'font': {
            'family': FONT_SETTINGS['family'],
            'sizes': FONT_SETTINGS['size'],
            'weights': FONT_SETTINGS['weight']
        },
        'axis': get_axis_style('nature'),
        'figure_sizes': FIGURE_SIZES,
        'export': EXPORT_SETTINGS
    }
    
    return template


# 预定义的样式主题
THEMES = {
    'nature': {
        'description': 'Nature期刊样式',
        'colors': NATURE_COLORS['nmi'],
        'axis_style': 'nature',
        'font_size': 'medium'
    },
    'science': {
        'description': 'Science期刊样式',
        'colors': NATURE_COLORS['primary'],
        'axis_style': 'modern',
        'font_size': 'medium'
    },
    'cell': {
        'description': 'Cell期刊样式',
        'colors': NATURE_COLORS['secondary'],
        'axis_style': 'modern',
        'font_size': 'medium'
    },
    'minimal': {
        'description': '极简样式',
        'colors': NATURE_COLORS['monochrome'],
        'axis_style': 'minimal',
        'font_size': 'small'
    }
}


def get_theme(theme_name='nature'):
    """
    获取主题样式
    
    参数:
        theme_name: 主题名称 ('nature', 'science', 'cell', 'minimal')
    
    返回:
        dict: 主题设置
    """
    return THEMES.get(theme_name, THEMES['nature'])


if __name__ == '__main__':
    # 测试样式模板
    print("样式模板测试")
    print("=" * 50)
    
    # 测试颜色方案
    print("颜色方案:")
    for name, colors in NATURE_COLORS.items():
        print(f"  {name}: {colors}")
    
    # 测试字体设置
    print("\n字体设置:")
    print(f"  small: {get_font_settings('small')}")
    print(f"  medium: {get_font_settings('medium')}")
    print(f"  large: {get_font_settings('large')}")
    
    # 测试图表尺寸
    print("\n图表尺寸:")
    for name, size in FIGURE_SIZES.items():
        print(f"  {name}: {size} mm")
    
    # 测试主题
    print("\n主题:")
    for name, theme in THEMES.items():
        print(f"  {name}: {theme['description']}")
    
    print("\n测试完成！")
