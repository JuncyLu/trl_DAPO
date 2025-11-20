#!/usr/bin/env python3
"""验证代码清理结果"""

import re

def check_file(filepath, checks):
    """检查文件是否符合预期"""
    print(f"\n检查文件: {filepath}")
    print("=" * 60)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = []
    for check_name, pattern, expected_behavior in checks:
        matches = re.findall(pattern, content, re.MULTILINE)
        count = len(matches)
        
        if expected_behavior == "should_exist":
            status = "✅" if count > 0 else "❌"
            print(f"{status} {check_name}: 找到 {count} 处")
        elif expected_behavior == "should_not_exist":
            status = "✅" if count == 0 else "❌"
            print(f"{status} {check_name}: 找到 {count} 处 (期望0)")
        elif isinstance(expected_behavior, int):
            status = "✅" if count == expected_behavior else "❌"
            print(f"{status} {check_name}: 找到 {count} 处 (期望{expected_behavior})")
        
        results.append(status == "✅")
    
    return all(results)

# 检查trainer文件
trainer_checks = [
    ("三位小数格式 (std)", r'f"{s:.3f}"', "should_exist"),
    ("group详细得分输出", r'group\{gi\}:', "should_exist"),
    ("Initial batch输出", r'\[DynSample\] Initial:', "should_exist"),
    ("Resample batch输出", r'\[DynSample\] Resample', "should_exist"),
]

# 检查logging文件
logging_checks = [
    ("_debug_log函数", r'def _debug_log', "should_not_exist"),
    ("_debug_log调用", r'_debug_log\(', "should_not_exist"),
    ("三位小数格式 (rewards)", r':.3f', "should_exist"),
    ("emit_rollout_logs函数", r'def emit_rollout_logs', "should_exist"),
    ("perform_realtime_rollout_logging函数", r'def perform_realtime_rollout_logging', "should_exist"),
]

print("=" * 60)
print("代码清理验证")
print("=" * 60)

trainer_ok = check_file("src/trainer/dapo_trainer.py", trainer_checks)
logging_ok = check_file("src/utils/dapo_logging.py", logging_checks)

print("\n" + "=" * 60)
print("总结")
print("=" * 60)
print(f"✅ trainer文件: {'通过' if trainer_ok else '未通过'}")
print(f"✅ logging文件: {'通过' if logging_ok else '未通过'}")

if trainer_ok and logging_ok:
    print("\n🎉 所有检查通过！代码清理完成。")
else:
    print("\n⚠️  部分检查未通过，请检查上述输出。")

# 显示文件大小变化
import os
trainer_size = os.path.getsize("src/trainer/dapo_trainer.py") / 1024
logging_size = os.path.getsize("src/utils/dapo_logging.py") / 1024

print("\n" + "=" * 60)
print("文件大小")
print("=" * 60)
print(f"trainer: {trainer_size:.1f} KB")
print(f"logging: {logging_size:.1f} KB")

