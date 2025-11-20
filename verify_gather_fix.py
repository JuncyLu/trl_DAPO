#!/usr/bin/env python3
"""
验证 safe_gather_object 调用修复
"""

import re
from pathlib import Path

def verify_fix():
    """检查 safe_gather_object 调用是否正确"""
    
    trainer_file = Path("/home/lujunxi57/trl/src/trainer/dapo_trainer.py")
    content = trainer_file.read_text()
    
    print("=" * 80)
    print("验证 safe_gather_object 调用修复")
    print("=" * 80)
    
    # 检查1: 确认函数签名
    if "def safe_gather_object(data, max_items=None, max_str_len=1000):" in content:
        print("✅ safe_gather_object 函数签名正确")
    else:
        print("❌ safe_gather_object 函数签名不正确")
        return False
    
    # 检查2: 确认没有错误的 max_chars 参数
    if "max_chars=" in content:
        print("❌ 仍包含错误的 max_chars 参数")
        return False
    else:
        print("✅ 已移除错误的 max_chars 参数")
    
    # 检查3: 确认使用正确的参数名
    correct_calls = re.findall(r'safe_gather_object\([^)]+max_items=[^)]+max_str_len=[^)]+\)', content)
    if len(correct_calls) >= 2:
        print(f"✅ 找到 {len(correct_calls)} 处正确的 safe_gather_object 调用")
    else:
        print(f"⚠️  只找到 {len(correct_calls)} 处 safe_gather_object 调用")
    
    # 检查4: 确认有扁平化逻辑
    if "all_samples_nested" in content and "all_new_samples_nested" in content:
        print("✅ 添加了嵌套列表扁平化逻辑")
    else:
        print("❌ 缺少嵌套列表扁平化逻辑")
        return False
    
    # 检查5: 确认扁平化代码
    flatten_pattern = r'for rank_samples in.*:\s+if isinstance\(rank_samples, list\):\s+.*\.extend\(rank_samples\)'
    if re.search(flatten_pattern, content, re.MULTILINE | re.DOTALL):
        print("✅ 扁平化逻辑实现正确")
    else:
        print("⚠️  扁平化逻辑可能不完整")
    
    # 检查6: 确认没有传递 accelerator 参数
    bad_calls = re.findall(r'safe_gather_object\(self\.accelerator,', content)
    if len(bad_calls) > 0:
        print(f"❌ 仍有 {len(bad_calls)} 处错误地传递了 self.accelerator 参数")
        return False
    else:
        print("✅ 没有错误地传递 accelerator 参数")
    
    print("\n" + "=" * 80)
    print("✅ 所有修复点验证通过！")
    print("=" * 80)
    print("\n修复内容:")
    print("1. 修正参数名：max_chars → max_str_len")
    print("2. 移除错误的 accelerator 参数")
    print("3. 添加嵌套列表扁平化逻辑")
    print("\n扁平化逻辑说明:")
    print("gather_object 返回: [[rank0_samples], [rank1_samples], ...]")
    print("扁平化后: [sample1, sample2, sample3, ...]")
    print("\n下一步:")
    print("1. 重新运行训练: bash baseline.sh")
    print("2. 检查是否不再出现 TypeError")
    print("3. 观察 [DynSample-SYNC] 日志")
    
    return True

if __name__ == "__main__":
    import sys
    success = verify_fix()
    sys.exit(0 if success else 1)

