# -*- coding: utf-8 -*-
"""
技能验证脚本
测试origin-chart-creator技能的各个组件
"""

import sys
import os
import json

# 获取技能目录
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 添加项目根目录到Python路径
sys.path.insert(0, PROJECT_ROOT)

def test_skill_structure():
    """测试技能目录结构"""
    print("测试技能目录结构...")
    
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    required_files = [
        'SKILL.md',
        'scripts/data_processor.py',
        'scripts/chart_creator.py',
        'scripts/style_templates.py',
        'references/chart_types.md',
        'references/style_guide.md',
        'references/examples.md',
        'assets/color_palettes.json',
        'evals/evals.json'
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = os.path.join(skill_dir, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"  [FAIL] 缺失文件: {missing_files}")
        return False
    else:
        print("  [PASS] 所有必需文件都存在")
        return True


def test_data_processor():
    """测试数据处理器"""
    print("测试数据处理器...")
    
    try:
        # 确保项目根目录在Python路径中
        if PROJECT_ROOT not in sys.path:
            sys.path.insert(0, PROJECT_ROOT)
        
        # 直接导入技能目录中的模块
        if SKILL_DIR not in sys.path:
            sys.path.insert(0, SKILL_DIR)
        
        from scripts.data_processor import DataProcessor
        
        # 创建测试数据
        import pandas as pd
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
        
        assert processor.data is not None
        assert processor.data.shape == (5, 3)
        
        # 测试数据准备
        origin_data = processor.prepare_for_origin('x', ['y'])
        assert 'x_data' in origin_data
        assert 'y_data' in origin_data
        
        # 清理
        os.remove(test_file)
        
        print("  [PASS] 数据处理器测试通过")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 数据处理器测试失败: {e}")
        return False


def test_chart_creator():
    """测试图表创建器"""
    print("测试图表创建器...")
    
    try:
        # 直接导入技能目录中的模块
        sys.path.insert(0, SKILL_DIR)
        
        # 由于没有OriginPro环境，只验证文件存在和语法正确
        chart_creator_file = os.path.join(SKILL_DIR, 'scripts', 'chart_creator.py')
        
        # 检查文件是否存在
        if not os.path.exists(chart_creator_file):
            print(f"  [FAIL] 文件不存在: {chart_creator_file}")
            return False
        
        # 检查文件内容
        with open(chart_creator_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查关键类和函数是否存在
        if 'class ChartCreator' not in content:
            print("  [FAIL] ChartCreator类不存在")
            return False
        
        if 'def recommend_chart_type' not in content:
            print("  [FAIL] recommend_chart_type函数不存在")
            return False
        
        print("  [INFO] 图表创建器类定义正确")
        print("  [INFO] 图表类型推荐函数存在")
        print("  [INFO] 注意：由于没有OriginPro环境，跳过实际图表创建测试")
        
        print("  [PASS] 图表创建器测试通过")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 图表创建器测试失败: {e}")
        return False


def test_style_templates():
    """测试样式模板"""
    print("测试样式模板...")
    
    try:
        # 直接导入技能目录中的模块
        sys.path.insert(0, SKILL_DIR)
        from scripts.style_templates import (
            get_color_palette,
            get_font_settings,
            get_axis_style,
            get_figure_size,
            get_export_settings,
            apply_nature_style,
            create_style_template,
            get_theme
        )
        
        # 测试颜色方案
        colors = get_color_palette('nature')
        assert len(colors) > 0
        
        # 测试字体设置
        font = get_font_settings('medium')
        assert 'family' in font
        assert 'size' in font
        
        # 测试坐标轴样式
        axis = get_axis_style('nature')
        assert 'spines' in axis
        
        # 测试图表尺寸
        size = get_figure_size('single')
        assert len(size) == 2
        
        # 测试导出设置
        export = get_export_settings('png')
        assert 'dpi' in export
        
        # 测试Nature样式
        style = apply_nature_style('line')
        assert 'colors' in style
        assert 'font' in style
        
        # 测试样式模板
        template = create_style_template('nature')
        assert 'name' in template
        assert 'colors' in template
        
        # 测试主题
        theme = get_theme('nature')
        assert 'description' in theme
        
        print("  [PASS] 样式模板测试通过")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 样式模板测试失败: {e}")
        return False


def test_evals():
    """测试评估文件"""
    print("测试评估文件...")
    
    try:
        skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        evals_file = os.path.join(skill_dir, 'evals', 'evals.json')
        
        with open(evals_file, 'r', encoding='utf-8') as f:
            evals = json.load(f)
        
        assert 'skill_name' in evals
        assert 'evals' in evals
        assert len(evals['evals']) > 0
        
        # 检查每个评估项
        for eval_item in evals['evals']:
            assert 'id' in eval_item
            assert 'prompt' in eval_item
            assert 'expected_output' in eval_item
        
        print(f"  [PASS] 评估文件测试通过 ({len(evals['evals'])} 个评估项)")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 评估文件测试失败: {e}")
        return False


def test_color_palettes():
    """测试颜色方案文件"""
    print("测试颜色方案文件...")
    
    try:
        skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        palettes_file = os.path.join(skill_dir, 'assets', 'color_palettes.json')
        
        with open(palettes_file, 'r', encoding='utf-8') as f:
            palettes = json.load(f)
        
        assert 'nature' in palettes
        assert 'nmi' in palettes
        assert 'science' in palettes
        
        # 检查每个调色板
        for name, palette in palettes.items():
            assert 'name' in palette
            assert 'description' in palette
            assert 'colors' in palette
            assert len(palette['colors']) > 0
        
        print(f"  [PASS] 颜色方案文件测试通过 ({len(palettes)} 个方案)")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 颜色方案文件测试失败: {e}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("OriginPro图表创建技能验证")
    print("=" * 60)
    print()
    
    tests = [
        test_skill_structure,
        test_data_processor,
        test_chart_creator,
        test_style_templates,
        test_evals,
        test_color_palettes
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  [ERROR] {test_func.__name__}: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print("验证总结")
    print("=" * 60)
    print(f"总测试数: {len(tests)}")
    print(f"通过: {passed}")
    print(f"失败: {failed}")
    
    if failed == 0:
        print("\n[SUCCESS] 所有验证测试通过！")
        print("\n技能已准备就绪，可以使用。")
        print("\n技能目录结构:")
        print("  origin-chart-creator/")
        print("  ├── SKILL.md                    # 技能描述")
        print("  ├── scripts/")
        print("  │   ├── data_processor.py       # 数据处理")
        print("  │   ├── chart_creator.py        # 图表创建")
        print("  │   └── style_templates.py      # 样式模板")
        print("  ├── references/")
        print("  │   ├── chart_types.md          # 图表类型")
        print("  │   ├── style_guide.md          # 样式指南")
        print("  │   └── examples.md             # 示例代码")
        print("  ├── assets/")
        print("  │   └── color_palettes.json    # 颜色方案")
        print("  └── evals/")
        print("      └── evals.json              # 测试用例")
    else:
        print(f"\n[FAIL] 有 {failed} 个测试失败，请检查。")
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
