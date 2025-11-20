#!/usr/bin/env python3
"""
验证设备不匹配修复
"""

import re
from pathlib import Path

def verify_fix():
    """检查tensor.to(device)是否已添加"""
    
    trainer_file = Path("/home/lujunxi57/trl/src/trainer/dapo_trainer.py")
    content = trainer_file.read_text()
    
    print("=" * 80)
    print("验证设备不匹配修复")
    print("=" * 80)
    
    # 检查1: 确认有.to(device)调用
    if '.to(device) for s in my_samples' in content:
        print("✅ 已添加 .to(device) 移动tensor到正确设备")
    else:
        print("❌ 缺少 .to(device) 调用")
        return False
    
    # 检查2: 确认3个tensor都移动了
    patterns = [
        r's\["rewards_per_func"\]\.to\(device\)',
        r's\["total_reward"\]\.to\(device\)',
        r's\["filter_score"\]\.to\(device\)',
    ]
    
    found_count = 0
    for pattern in patterns:
        if re.search(pattern, content):
            found_count += 1
    
    if found_count == 3:
        print(f"✅ 所有3个tensor都添加了 .to(device)")
    else:
        print(f"⚠️  只找到 {found_count}/3 个tensor的 .to(device)")
        return False
    
    # 检查3: 确认有注释说明
    if "Move all tensors to current rank's device" in content or \
       "Samples may come from different ranks" in content:
        print("✅ 添加了清晰的注释说明")
    else:
        print("⚠️  缺少注释说明")
    
    # 检查4: 确认torch.stack位置
    if 'torch.stack([s["rewards_per_func"].to(device)' in content:
        print("✅ torch.stack 调用正确")
    else:
        print("⚠️  torch.stack 调用可能不正确")
        return False
    
    print("\n" + "=" * 80)
    print("✅ 所有修复点验证通过！")
    print("=" * 80)
    print("\n修复内容:")
    print("在torch.stack之前，将所有tensor移动到当前rank的设备:")
    print("  rewards_per_func = torch.stack([s['rewards_per_func'].to(device) for s in my_samples])")
    print("  total_rewards = torch.stack([s['total_reward'].to(device) for s in my_samples])")
    print("  filter_scores = torch.stack([s['filter_score'].to(device) for s in my_samples])")
    print("\n为什么需要这个修复？")
    print("- 跨rank数据共享后，样本可能来自不同的GPU")
    print("- rank2切片[32:48]可能包含rank2(cuda:2)和rank3(cuda:3)的样本")
    print("- torch.stack要求所有tensor在同一设备上")
    print("- .to(device)将tensor移动到当前rank的设备")
    print("\n预期效果:")
    print("1. 不再出现 'Expected all tensors to be on the same device' 错误")
    print("2. 所有rank能够成功从全局池切片和使用样本")
    print("3. 训练顺利进行")
    print("\n下一步:")
    print("1. 重新运行训练: bash baseline.sh")
    print("2. 观察是否不再出现设备错误")
    print("3. 检查训练是否继续到step 2, 3, ...")
    
    return True

if __name__ == "__main__":
    import sys
    success = verify_fix()
    sys.exit(0 if success else 1)

