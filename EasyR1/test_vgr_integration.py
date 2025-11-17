#!/usr/bin/env python3
"""
Simple test script to validate VGR token weights integration in EasyR1.
This script performs basic sanity checks without running full training.
"""

import sys
import torch


def test_imports():
    """Test that all VGR-related imports work correctly."""
    print("Testing imports...")
    try:
        from verl.utils import (
            build_token_vgr_weights_for_batch,
            get_qwen_special_token_ids,
            extract_vision_token_spans_qwen,
        )
        print("✓ VGR utils imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_config():
    """Test that config additions work."""
    print("\nTesting config extensions...")
    try:
        from verl.trainer.config import AlgorithmConfig, PPOConfig
        from verl.workers.rollout.config import RolloutConfig
        
        # Test AlgorithmConfig
        algo_config = AlgorithmConfig()
        assert hasattr(algo_config, "enable_token_weights"), "Missing enable_token_weights"
        assert hasattr(algo_config, "token_weight_clip"), "Missing token_weight_clip"
        assert hasattr(algo_config, "token_weight_smooth_sigma"), "Missing token_weight_smooth_sigma"
        assert hasattr(algo_config, "token_weight_last_k_layers"), "Missing token_weight_last_k_layers"
        print("✓ AlgorithmConfig has VGR fields")
        
        # Test RolloutConfig
        rollout_config = RolloutConfig()
        assert hasattr(rollout_config, "collect_attentions"), "Missing collect_attentions"
        print("✓ RolloutConfig has collect_attentions field")
        
        # Test default values
        assert algo_config.enable_token_weights == False, "Default enable_token_weights should be False"
        assert algo_config.token_weight_clip == (0.2, 3.0), "Default clip range incorrect"
        assert rollout_config.collect_attentions == False, "Default collect_attentions should be False"
        print("✓ Default config values correct")
        
        return True
    except Exception as e:
        print(f"✗ Config test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_attention_metrics():
    """Test basic attention metrics computation."""
    print("\nTesting attention metrics...")
    try:
        from verl.utils.attention_metrics import (
            _build_modality_masks,
            get_qwen_special_token_ids,
        )
        
        # Create dummy processor-like object
        class DummyTokenizer:
            bos_token_id = 1
            eos_token_id = 2
            pad_token_id = 0
            unk_token_id = 3
            
            def convert_tokens_to_ids(self, token_str):
                token_map = {
                    "<|im_start|>": 4,
                    "<|im_end|>": 5,
                    "<|vision_start|>": 6,
                    "<|vision_end|>": 7,
                }
                return token_map.get(token_str, self.unk_token_id)
        
        class DummyProcessor:
            def __init__(self):
                self.tokenizer = DummyTokenizer()
        
        processor = DummyProcessor()
        special_ids = get_qwen_special_token_ids(processor)
        
        assert "bos" in special_ids, "Missing bos token"
        assert "eos" in special_ids, "Missing eos token"
        print("✓ Special token extraction works")
        
        # Test mask building
        input_ids = torch.tensor([1, 4, 100, 101, 5, 6, 200, 201, 7, 102, 2])
        vision_spans = [(5, 9)]  # vision_start at 5, vision_end at 8 (exclusive 9)
        
        instruction_mask, vision_mask = _build_modality_masks(input_ids, vision_spans, special_ids)
        
        assert instruction_mask.shape[0] == input_ids.shape[0], "Instruction mask size mismatch"
        assert vision_mask.shape[0] == input_ids.shape[0], "Vision mask size mismatch"
        print("✓ Modality mask building works")
        
        return True
    except Exception as e:
        print(f"✗ Attention metrics test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_token_weights_computation():
    """Test token weights computation with dummy data."""
    print("\nTesting token weights computation...")
    try:
        from verl.utils.attention_token_weights import build_token_vgr_weights_for_batch
        
        # Create minimal dummy data
        class DummyTokenizer:
            bos_token_id = 1
            eos_token_id = 2
            pad_token_id = 0
            unk_token_id = 3
            
            def convert_tokens_to_ids(self, token_str):
                return 3
        
        class DummyProcessor:
            def __init__(self):
                self.tokenizer = DummyTokenizer()
        
        processor = DummyProcessor()
        
        # Create dummy attention outputs (empty case)
        outputs_attentions = []
        input_ids = torch.randint(10, 100, (2, 20))
        sequences = torch.randint(10, 100, (2, 30))
        
        weights, debug = build_token_vgr_weights_for_batch(
            outputs_attentions=outputs_attentions,
            input_ids=input_ids,
            sequences=sequences,
            processor=processor,
            image_grid_thw=None,
            exclude_special=True,
            smooth_sigma=0.0,
            clip_range=(0.2, 3.0),
            last_k_layers=None,
        )
        
        assert isinstance(weights, list), "Weights should be a list"
        assert len(weights) == 2, "Should have weights for 2 samples"
        print("✓ Token weights computation runs (empty attention case)")
        
        return True
    except Exception as e:
        print(f"✗ Token weights test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("VGR Integration Test Suite for EasyR1")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Config", test_config),
        ("Attention Metrics", test_attention_metrics),
        ("Token Weights", test_token_weights_computation),
    ]
    
    results = []
    for name, test_func in tests:
        success = test_func()
        results.append((name, success))
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for name, success in results:
        status = "PASS" if success else "FAIL"
        print(f"{name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ All tests passed! VGR integration is ready.")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())





