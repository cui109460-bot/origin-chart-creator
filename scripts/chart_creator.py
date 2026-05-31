# -*- coding: utf-8 -*-
"""
图表创建脚本
封装OriginPro图表库的功能，供技能使用
"""

import sys
import os
import pandas as pd
import numpy as np

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import origin_graph_library as ogl


class ChartCreator:
    """图表创建器类"""
    
    def __init__(self):
        self.current_chart = None
        self.chart_history = []
    
    def create_line_chart(self, x_data, y_data, title="Line Chart", 
                         xlabel="X", ylabel="Y", save_path=None):
        """创建折线图"""
        self.current_chart = ogl.line_chart(x_data, y_data, title, xlabel, ylabel, save_path)
        self.chart_history.append(('line', self.current_chart))
        return self.current_chart
    
    def create_scatter_chart(self, x_data, y_data, title="Scatter Plot",
                           xlabel="X", ylabel="Y", save_path=None):
        """创建散点图"""
        self.current_chart = ogl.scatter_chart(x_data, y_data, title, xlabel, ylabel, save_path)
        self.chart_history.append(('scatter', self.current_chart))
        return self.current_chart
    
    def create_column_chart(self, categories, values, title="Column Chart",
                          xlabel="Category", ylabel="Value", save_path=None):
        """创建柱状图"""
        self.current_chart = ogl.column_chart(categories, values, title, xlabel, ylabel, save_path)
        self.chart_history.append(('column', self.current_chart))
        return self.current_chart
    
    def create_bar_chart(self, categories, values, title="Bar Chart",
                        xlabel="Value", ylabel="Category", save_path=None):
        """创建条形图"""
        self.current_chart = ogl.bar_chart(categories, values, title, xlabel, ylabel, save_path)
        self.chart_history.append(('bar', self.current_chart))
        return self.current_chart
    
    def create_pie_chart(self, labels, values, title="Pie Chart", save_path=None):
        """创建饼图"""
        self.current_chart = ogl.pie_chart(labels, values, title, save_path)
        self.chart_history.append(('pie', self.current_chart))
        return self.current_chart
    
    def create_area_chart(self, x_data, y_data, title="Area Chart",
                         xlabel="X", ylabel="Y", save_path=None):
        """创建面积图"""
        self.current_chart = ogl.area_chart(x_data, y_data, title, xlabel, ylabel, save_path)
        self.chart_history.append(('area', self.current_chart))
        return self.current_chart
    
    def create_histogram(self, data, title="Histogram", xlabel="Value", 
                        ylabel="Frequency", save_path=None):
        """创建直方图"""
        self.current_chart = ogl.histogram_chart(data, title, xlabel, ylabel, save_path)
        self.chart_history.append(('histogram', self.current_chart))
        return self.current_chart
    
    def create_box_chart(self, data_list, labels, title="Box Plot",
                        xlabel="Group", ylabel="Value", save_path=None):
        """创建箱线图"""
        self.current_chart = ogl.box_chart(data_list, labels, title, xlabel, ylabel, save_path)
        self.chart_history.append(('box', self.current_chart))
        return self.current_chart
    
    def create_heatmap(self, data, title="Heatmap", save_path=None):
        """创建热力图"""
        self.current_chart = ogl.heatmap_chart(data, title, save_path)
        self.chart_history.append(('heatmap', self.current_chart))
        return self.current_chart
    
    def create_multi_line_chart(self, x_data, y_data_list, labels, title="Multi-Line Chart",
                               xlabel="X", ylabel="Y", save_path=None):
        """创建多线图"""
        self.current_chart = ogl.multi_line_chart(x_data, y_data_list, labels, title, xlabel, ylabel, save_path)
        self.chart_history.append(('multi_line', self.current_chart))
        return self.current_chart
    
    def create_error_bar_chart(self, x_data, y_data, y_error, title="Error Bar Chart",
                              xlabel="X", ylabel="Y", save_path=None):
        """创建误差棒图"""
        self.current_chart = ogl.error_bar_chart(x_data, y_data, y_error, title, xlabel, ylabel, save_path)
        self.chart_history.append(('error_bar', self.current_chart))
        return self.current_chart
    
    def create_grouped_column_chart(self, categories, data_dict, title="Grouped Column Chart",
                                   xlabel="Category", ylabel="Value", save_path=None):
        """创建分组柱状图"""
        self.current_chart = ogl.grouped_column_chart(categories, data_dict, title, xlabel, ylabel, save_path)
        self.chart_history.append(('grouped_column', self.current_chart))
        return self.current_chart
    
    def create_stacked_column_chart(self, categories, data_dict, title="Stacked Column Chart",
                                   xlabel="Category", ylabel="Value", save_path=None):
        """创建堆叠柱状图"""
        self.current_chart = ogl.stacked_column_chart(categories, data_dict, title, xlabel, ylabel, save_path)
        self.chart_history.append(('stacked_column', self.current_chart))
        return self.current_chart
    
    def create_violin_chart(self, data_list, labels, title="Violin Chart",
                           xlabel="Group", ylabel="Value", save_path=None):
        """创建小提琴图"""
        self.current_chart = ogl.violin_chart(data_list, labels, title, xlabel, ylabel, save_path)
        self.chart_history.append(('violin', self.current_chart))
        return self.current_chart
    
    def create_radar_chart(self, categories, data_dict, title="Radar Chart", save_path=None):
        """创建雷达图"""
        self.current_chart = ogl.radar_chart(categories, data_dict, title, save_path)
        self.chart_history.append(('radar', self.current_chart))
        return self.current_chart
    
    def create_bubble_chart(self, x_data, y_data, size_data, title="Bubble Chart",
                           xlabel="X", ylabel="Y", save_path=None):
        """创建气泡图"""
        self.current_chart = ogl.bubble_chart(x_data, y_data, size_data, title=title, 
                                             xlabel=xlabel, ylabel=ylabel, save_path=save_path)
        self.chart_history.append(('bubble', self.current_chart))
        return self.current_chart
    
    def create_forest_chart(self, studies, effect_sizes, ci_lower, ci_upper, 
                           weights=None, title="Forest Plot", save_path=None):
        """创建森林图"""
        self.current_chart = ogl.forest_chart(studies, effect_sizes, ci_lower, ci_upper, 
                                            weights, title, save_path=save_path)
        self.chart_history.append(('forest', self.current_chart))
        return self.current_chart
    
    def create_survival_chart(self, time_data, event_data, groups=None, 
                             title="Kaplan-Meier Curve", save_path=None):
        """创建生存曲线"""
        self.current_chart = ogl.survival_chart(time_data, event_data, groups, title, save_path=save_path)
        self.chart_history.append(('survival', self.current_chart))
        return self.current_chart
    
    def create_bland_altman_chart(self, method1, method2, title="Bland-Altman Plot", save_path=None):
        """创建Bland-Altman图"""
        self.current_chart = ogl.bland_altman_chart(method1, method2, title, save_path=save_path)
        self.chart_history.append(('bland_altman', self.current_chart))
        return self.current_chart
    
    def create_scatter_matrix(self, data_dict, title="Scatter Matrix", save_path=None):
        """创建散点矩阵"""
        self.current_chart = ogl.scatter_matrix(data_dict, title, save_path)
        self.chart_history.append(('scatter_matrix', self.current_chart))
        return self.current_chart
    
    def customize_chart(self, x_title=None, y_title=None, x_min=None, x_max=None, 
                       y_min=None, y_max=None, color=None, line_width=None):
        """
        自定义图表样式
        
        参数:
            x_title: X轴标题
            y_title: Y轴标题
            x_min: X轴最小值
            x_max: X轴最大值
            y_min: Y轴最小值
            y_max: Y轴最大值
            color: 颜色
            line_width: 线宽
        """
        if self.current_chart is None:
            raise ValueError("请先创建图表")
        
        # 设置坐标轴
        if any([x_title, y_title, x_min, x_max, y_min, y_max]):
            ogl.set_axis_properties(self.current_chart, x_title=x_title, y_title=y_title,
                                   x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
        
        # 设置颜色
        if color:
            ogl.set_plot_color(self.current_chart, color=color)
        
        # 设置线宽
        if line_width:
            ogl.set_plot_style(self.current_chart, line_width=line_width)
        
        return self.current_chart
    
    def add_legend(self):
        """添加图例"""
        if self.current_chart is None:
            raise ValueError("请先创建图表")
        
        ogl.add_legend(self.current_chart)
        return self.current_chart
    
    def save_chart(self, filepath, dpi=300):
        """
        保存图表
        
        参数:
            filepath: 保存路径
            dpi: 分辨率
        """
        if self.current_chart is None:
            raise ValueError("请先创建图表")
        
        self.current_chart.save_fig(filepath, dpi=dpi)
        return filepath
    
    def export_all(self, output_dir, format='png', dpi=300):
        """
        导出所有图表
        
        参数:
            output_dir: 输出目录
            format: 文件格式
            dpi: 分辨率
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for i, (chart_type, chart) in enumerate(self.chart_history):
            filepath = os.path.join(output_dir, f"chart_{i+1}_{chart_type}.{format}")
            chart.save_fig(filepath, dpi=dpi)
            print(f"导出: {filepath}")
        
        return len(self.chart_history)
    
    def get_chart_info(self):
        """获取当前图表信息"""
        if self.current_chart is None:
            return None
        
        return {
            'type': self.chart_history[-1][0] if self.chart_history else None,
            'total_charts': len(self.chart_history)
        }


def recommend_chart_type(data_info):
    """
    根据数据特征推荐图表类型
    
    参数:
        data_info: 数据信息字典
    
    返回:
        list: 推荐的图表类型列表
    """
    recommendations = []
    
    columns = data_info.get('columns', [])
    dtypes = data_info.get('dtypes', {})
    
    # 统计数据类型
    numeric_cols = [col for col, dtype in dtypes.items() if 'float' in dtype or 'int' in dtype]
    categorical_cols = [col for col, dtype in dtypes.items() if 'object' in dtype or 'category' in dtype]
    
    # 推荐图表类型
    if len(numeric_cols) >= 2:
        recommendations.append(('scatter_chart', '散点图 - 展示两个变量的相关性'))
        recommendations.append(('scatter_matrix', '散点矩阵 - 展示多个变量的相关性'))
    
    if len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
        recommendations.append(('column_chart', '柱状图 - 分类数据比较'))
        recommendations.append(('grouped_column_chart', '分组柱状图 - 多系列分类比较'))
        recommendations.append(('box_chart', '箱线图 - 展示数据分布'))
        recommendations.append(('violin_chart', '小提琴图 - 展示数据分布密度'))
    
    if len(numeric_cols) >= 1:
        recommendations.append(('histogram', '直方图 - 展示数据分布'))
        recommendations.append(('line_chart', '折线图 - 展示趋势变化'))
    
    if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
        recommendations.append(('pie_chart', '饼图 - 展示比例关系'))
        recommendations.append(('stacked_column_chart', '堆叠柱状图 - 展示组成成分'))
    
    # 如果没有明确推荐，提供默认建议
    if not recommendations:
        recommendations.append(('line_chart', '折线图 - 通用图表'))
        recommendations.append(('column_chart', '柱状图 - 通用图表'))
    
    return recommendations


if __name__ == '__main__':
    # 测试图表创建器
    print("图表创建器测试")
    print("=" * 50)
    
    creator = ChartCreator()
    
    # 测试创建折线图
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]
    
    chart = creator.create_line_chart(x, y, title="测试折线图", xlabel="X", ylabel="Y")
    print(f"创建图表: {creator.get_chart_info()}")
    
    # 测试自定义
    creator.customize_chart(x_title="自定义X轴", y_title="自定义Y轴", color='red')
    print("自定义样式完成")
    
    print("\n测试完成！")
