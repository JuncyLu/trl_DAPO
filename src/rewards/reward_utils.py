"""
Reward utility functions for DAPO training.
Handles reward weight management and total reward calculation.
"""

import torch
from typing import List, Optional, Tuple, Dict, Any
from dataclasses import dataclass


@dataclass
class RewardWeightConfig:
    """Configuration for reward weights."""
    use_segmented_weights: bool = False
    early_weights: Optional[List[float]] = None
    late_weights: Optional[List[float]] = None
    static_weights: Optional[List[float]] = None
    reward_func_names: Optional[List[str]] = None


class RewardWeightManager:
    """Manages reward weights and calculates total rewards."""
    
    def __init__(self, config: RewardWeightConfig):
        self.config = config
        self.reward_func_names = config.reward_func_names or []
        
        # Initialize weights
        self._init_weights()
        
    def _init_weights(self):
        """Initialize reward weights based on configuration."""
        if self.config.use_segmented_weights:
            # 设置分段权重的默认值
            self.early_weights = torch.tensor(
                self.config.early_weights or [2.5, 1.0, 0.5], 
                dtype=torch.float32
            )
            self.late_weights = torch.tensor(
                self.config.late_weights or [0.5, 1.0, 2.5], 
                dtype=torch.float32
            )
            # 初始使用early weights
            self.current_weights = self.early_weights.clone()
        elif self.config.static_weights is not None:
            self.current_weights = torch.tensor(
                self.config.static_weights, 
                dtype=torch.float32
            )
        else:
            # 默认等权重
            num_funcs = len(self.reward_func_names)
            self.current_weights = torch.ones(num_funcs, dtype=torch.float32)
    
    def update_weights(self, global_step: int, max_steps: int) -> Dict[str, float]:
        """
        Update weights based on training progress.
        
        Args:
            global_step: Current training step
            max_steps: Total training steps
            
        Returns:
            Dictionary mapping reward function names to their current weights
        """
        if not self.config.use_segmented_weights:
            return self._get_weight_dict()
            
        # 计算训练进度 (0.0 到 1.0)
        progress = global_step / max_steps if max_steps > 0 else 0.0
        
        # 在10%处切换权重
        if progress <= 0.1:
            # 前10%使用early weights
            self.current_weights = self.early_weights.to(self.current_weights.device)
        else:
            # 后90%使用late weights
            self.current_weights = self.late_weights.to(self.current_weights.device)
            
        return self._get_weight_dict()
    
    def _get_weight_dict(self) -> Dict[str, float]:
        """Get current weights as a dictionary."""
        weight_dict = {}
        for i, name in enumerate(self.reward_func_names):
            if i < len(self.current_weights):
                weight_dict[f"reward_weights/{name}"] = self.current_weights[i].item()
        return weight_dict
    
    def get_current_weights(self) -> torch.Tensor:
        """Get current weights as a tensor."""
        return self.current_weights
    
    def calculate_total_reward(
        self, 
        rewards_per_func: torch.Tensor, 
        device: Optional[torch.device] = None
    ) -> torch.Tensor:
        """
        Calculate total reward by applying weights to individual reward functions.
        
        Args:
            rewards_per_func: Tensor of shape (batch_size, num_reward_funcs)
            device: Device to place the result on
            
        Returns:
            Total rewards tensor of shape (batch_size,)
        """
        if device is not None:
            weights = self.current_weights.to(device)
        else:
            weights = self.current_weights
            
        # Apply weights and sum across reward functions
        total_rewards = (rewards_per_func * weights.unsqueeze(0)).nansum(dim=1)
        return total_rewards


def create_reward_weight_manager(
    use_segmented_weights: bool = False,
    early_weights: Optional[List[float]] = None,
    late_weights: Optional[List[float]] = None,
    static_weights: Optional[List[float]] = None,
    reward_func_names: Optional[List[str]] = None
) -> RewardWeightManager:
    """
    Create a RewardWeightManager instance.
    
    Args:
        use_segmented_weights: Whether to use segmented weights
        early_weights: Weights for first 10% of training
        late_weights: Weights for last 90% of training
        static_weights: Static weights (used when not segmented)
        reward_func_names: Names of reward functions
        
    Returns:
        RewardWeightManager instance
    """
    config = RewardWeightConfig(
        use_segmented_weights=use_segmented_weights,
        early_weights=early_weights,
        late_weights=late_weights,
        static_weights=static_weights,
        reward_func_names=reward_func_names
    )
    return RewardWeightManager(config)


def calculate_reward_metrics(
    rewards_per_func: torch.Tensor,
    reward_func_names: List[str],
    device: torch.device
) -> Dict[str, float]:
    """
    Calculate reward metrics for logging.
    
    Args:
        rewards_per_func: Tensor of shape (batch_size, num_reward_funcs)
        reward_func_names: Names of reward functions
        device: Device for calculations
        
    Returns:
        Dictionary of reward metrics
    """
    metrics = {}
    
    # Calculate mean and std for each reward function
    for i, name in enumerate(reward_func_names):
        if i < rewards_per_func.shape[1]:
            mean_rewards = torch.nanmean(rewards_per_func[:, i]).item()
            # Calculate std manually to handle NaN values
            values = rewards_per_func[:, i]
            valid_values = values[~torch.isnan(values)]
            if len(valid_values) > 0:
                std_rewards = torch.std(valid_values).item()
            else:
                std_rewards = 0.0
            metrics[f"rewards/{name}/mean"] = mean_rewards
            metrics[f"rewards/{name}/std"] = std_rewards
    
    return metrics
