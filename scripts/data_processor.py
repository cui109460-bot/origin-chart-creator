# -*- coding: utf-8 -*-
"""
数据处理脚本
封装数据处理模块的功能，供技能使用
"""

import sys
import os
import pandas as pd
import numpy as np

# 添加项目根目录到Python路径
# 脚本位于 skills/origin-chart-creator/scripts/，需要向上3级到达项目根目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
SKILLS_DIR = os.path.dirname(SKILL_DIR)
PROJECT_ROOT = os.path.dirname(SKILLS_DIR)

sys.path.insert(0, PROJECT_ROOT)

from data_processing import (
    load_csv,
    load_excel,
    load_multiple_files,
    handle_missing_values,
    convert_data_types,
    remove_duplicates,
    detect_outliers,
    filter_data,
    sort_data,
    aggregate_data,
    descriptive_stats,
    correlation_analysis,
    DataPipeline,
    export_csv,
    export_for_origin
)


class DataProcessor:
    """数据处理器类"""
    
    def __init__(self):
        self.data = None
        self.pipeline = DataPipeline()
    
    def load_data(self, filepath, **kwargs):
        """
        加载数据文件
        
        参数:
            filepath: 文件路径（CSV或Excel）
            **kwargs: 传递给加载函数的参数
        """
        if filepath.endswith('.csv'):
            self.data = load_csv(filepath, **kwargs)
        elif filepath.endswith(('.xlsx', '.xls')):
            self.data = load_excel(filepath, **kwargs)
        else:
            raise ValueError(f"不支持的文件格式: {filepath}")
        
        return self.data
    
    def clean_data(self, missing_strategy='mean', remove_dup=True, detect_outlier=True):
        """
        清洗数据
        
        参数:
            missing_strategy: 缺失值处理策略
            remove_dup: 是否删除重复值
            detect_outlier: 是否检测异常值
        """
        if self.data is None:
            raise ValueError("请先加载数据")
        
        # 处理缺失值
        self.data = handle_missing_values(self.data, strategy=missing_strategy)
        
        # 删除重复值
        if remove_dup:
            self.data = remove_duplicates(self.data)
        
        # 检测异常值
        if detect_outlier:
            self.data, outliers = detect_outliers(self.data)
            if len(outliers) > 0:
                print(f"检测到 {len(outliers)} 个异常值")
        
        return self.data
    
    def transform_data(self, filter_conditions=None, sort_by=None, group_by=None, agg_funcs=None):
        """
        转换数据
        
        参数:
            filter_conditions: 筛选条件
            sort_by: 排序列
            group_by: 分组列
            agg_funcs: 聚合函数
        """
        if self.data is None:
            raise ValueError("请先加载数据")
        
        # 筛选数据
        if filter_conditions:
            self.data = filter_data(self.data, conditions=filter_conditions)
        
        # 排序数据
        if sort_by:
            self.data = sort_data(self.data, by=sort_by)
        
        # 聚合数据
        if group_by and agg_funcs:
            self.data = aggregate_data(self.data, group_by=group_by, agg_funcs=agg_funcs)
        
        return self.data
    
    def analyze_data(self, columns=None):
        """
        分析数据
        
        参数:
            columns: 要分析的列名列表
        """
        if self.data is None:
            raise ValueError("请先加载数据")
        
        stats = descriptive_stats(self.data, columns=columns)
        corr = correlation_analysis(self.data, columns=columns)
        
        return {
            'descriptive_stats': stats,
            'correlation': corr
        }
    
    def prepare_for_origin(self, x_column, y_columns):
        """
        为OriginPro准备数据
        
        参数:
            x_column: X轴列名
            y_columns: Y轴列名或列名列表
        """
        if self.data is None:
            raise ValueError("请先加载数据")
        
        return export_for_origin(self.data, x_column=x_column, y_columns=y_columns)
    
    def get_data_info(self):
        """获取数据基本信息"""
        if self.data is None:
            return None
        
        return {
            'shape': self.data.shape,
            'columns': list(self.data.columns),
            'dtypes': {col: str(dtype) for col, dtype in self.data.dtypes.items()},
            'missing_values': self.data.isnull().sum().to_dict(),
            'missing_percentage': (self.data.isnull().sum() / len(self.data) * 100).round(2).to_dict(),
        }


def quick_process(filepath, x_column, y_columns, clean=True):
    """
    快速处理数据并准备OriginPro格式
    
    参数:
        filepath: 数据文件路径
        x_column: X轴列名
        y_columns: Y轴列名列表
        clean: 是否清洗数据
    
    返回:
        dict: OriginPro兼容的数据格式
    """
    processor = DataProcessor()
    processor.load_data(filepath)
    
    if clean:
        processor.clean_data()
    
    return processor.prepare_for_origin(x_column, y_columns)


def batch_process(file_list, x_column, y_columns, output_dir=None):
    """
    批量处理多个数据文件
    
    参数:
        file_list: 文件路径列表
        x_column: X轴列名
        y_columns: Y轴列名列表
        output_dir: 输出目录（可选）
    
    返回:
        dict: {文件名: OriginPro数据格式}
    """
    results = {}
    
    for filepath in file_list:
        filename = os.path.basename(filepath)
        try:
            data = quick_process(filepath, x_column, y_columns)
            results[filename] = data
            
            if output_dir:
                # 保存处理后的数据
                output_path = os.path.join(output_dir, f"processed_{filename}")
                processor = DataProcessor()
                processor.load_data(filepath)
                processor.clean_data()
                export_csv(processor.data, output_path)
                
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")
            results[filename] = None
    
    return results


if __name__ == '__main__':
    # 测试数据处理器
    print("数据处理器测试")
    print("=" * 50)
    
    # 创建测试数据
    test_data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 30, 40, 50],
        'category': ['A', 'B', 'A', 'B', 'A']
    })
    
    # 保存测试数据
    test_file = 'test_data.csv'
    test_data.to_csv(test_file, index=False)
    
    # 测试处理器
    processor = DataProcessor()
    processor.load_data(test_file)
    
    print(f"数据形状: {processor.data.shape}")
    print(f"列名: {list(processor.data.columns)}")
    
    # 测试数据准备
    origin_data = processor.prepare_for_origin('x', ['y'])
    print(f"OriginPro数据: {origin_data}")
    
    # 清理
    os.remove(test_file)
    
    print("\n测试完成！")
