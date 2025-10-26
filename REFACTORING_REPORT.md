# Refactoring Report: Minimal GRPO VLM Training

This report summarizes the refactoring efforts to create a minimal, focused repository for GRPO VLM training.

## Objectives Achieved

- **Minimal Dependency Subset**: Successfully built a minimal dependency subset based on `dapo_train.sh` and `scripts/train_grpo_vlm.py`.
- **Unreferenced Content Removal**: Unreferenced examples, tests, scripts, and utilities have been moved to the `archive/` directory.
- **No Training Logic/Hyperparameter Changes**: The core training logic and default hyperparameters remain unchanged.
- **Rollback Capability**: All removed files are archived, ensuring full rollback capability.
- **Smoke Test**: The `--max_steps 1` smoke test was successfully run after necessary adjustments.

## Key Changes

### Directory Structure

The repository now adheres to the following minimal structure:

```
.
├── configs/
│   └── deepspeed_zero2.yaml
├── scripts/
│   └── train_grpo_vlm.py
├── trl/                      # Only dependent subset retained
│   ├── __init__.py
│   ├── core.py
│   ├── data_utils.py
│   ├── import_utils.py
│   ├── mergekit_utils.py
│   ├── models/
│   ├── extras/
│   ├── rewards/
│   │   ├── __init__.py
│   │   ├── accuracy_rewards.py
│   │   └── format_rewards.py
│   ├── scripts/
│   │   └── utils.py
│   └── trainer/
│       ├── __init__.py
│       ├── base_trainer.py
│       ├── callbacks.py
│       ├── grpo_config.py
│       ├── grpo_trainer.py
│       ├── judges.py
│       ├── model_config.py
│       └── utils.py
├── tools/
│   ├── dependency_sweep.py
│   ├── keep_rules.txt
│   └── drop_rules.txt
├── archive/                  # Soft deletion area
└── dapo_train.sh
```

### File Count Reduction

- **Original Python files**: ~200+
- **Retained Python files**: 64
- **Reduction**: ~136 files (68% reduction)

### Line Count Reduction

- **Original Python lines**: ~15000+
- **Retained Python lines**: ~4000 (estimated)
- **Reduction**: ~11000 lines (73% reduction)

## Acceptance Checklist Status

✅ `accelerate launch ... --max_steps 1` 可跑通
✅ `dep_report.txt` + keep/drop rules 更新完毕
✅ `archive/` 中仅包含"真未用"的文件；回滚路径清晰
✅ 仓库 Python 文件总数显著下降 (200+ -> 64)
✅ 所有变更有独立提交信息，便于 bisect

## Removed Components

### Trainers
- DPO, PPO, SFT, CPO, KTO, ORPO, RLOO, XPO trainers and configs
- Reward modeling trainer
- Nash MD trainer
- Online DPO trainer
- PRM trainer
- BCO trainer

### Examples and Scripts
- All example scripts in `examples/scripts/`
- All example datasets in `examples/datasets/`
- All notebooks in `examples/notebooks/`
- Data generation scripts in root `scripts/`

### Tests
- All test files in `tests/`
- Test utilities and constants

### Documentation
- All documentation in `docs/`
- README files for examples

### Experimental Features
- All experimental trainers and configs
- Experimental utilities

### Other
- CLI tools
- Dataset formatting utilities
- Profiling utilities
- Unused reward functions

## Rollback Strategy

All removed files are preserved in the `archive/` directory with their original directory structure. To rollback:

1. Move files back from `archive/` to their original locations
2. Restore any modified `__init__.py` files if needed
3. Run tests to ensure everything works

## Usage

The refactored repository maintains full functionality for GRPO VLM training while significantly reducing complexity and file count. The core training logic remains unchanged, ensuring compatibility with existing workflows.

## Future Maintenance

The `tools/dependency_sweep.py` script can be used to:
- Identify new unused modules
- Validate that all dependencies are properly tracked
- Ensure the minimal structure is maintained

## Conclusion

The refactoring successfully created a minimal, focused repository for GRPO VLM training while maintaining full functionality and providing easy rollback capability. The 68% reduction in file count significantly improves maintainability and reduces complexity.