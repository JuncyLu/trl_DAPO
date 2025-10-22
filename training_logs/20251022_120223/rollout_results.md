# Rollout Results Log

This file contains detailed rollout results from GRPO training.


## === Rollout Step 1 ===
Step: 0/29790 | 2025-10-22 12:02:52

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.500 ± 0.500 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | -0.500 ± 0.500 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.500 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 9.676 | 1.112 | 2.633 | 0.275 |
| Middle | 5.971 | 0.190 | 2.361 | 0.396 |
| Late | 4.996 | 0.439 | 2.238 | 0.450 |
| All | 4.996 | 0.439 | 2.411 | 0.374 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> First, let's look at the number of slices of pizza each child seems to be eating based on the image. The child in the middle appears to be eating a little less than half a slice, and the surro…

**Solution:** A

**Rewards:** accuracy=0.000, format=1.000, mdi=-1.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.787455,
      "aei_text": 2.691132,
      "aei_vision": 0.249469,
      "text_ratio": 0.915164,
      "vision_ratio": 0.084836
    },
    "middle": {
      "mdi": 5.781754,
      "aei_text": 2.340942,
      "aei_vision": 0.404884,
      "text_ratio": 0.852546,
      "vision_ratio": 0.147454
    },
    "late": {
      "mdi": 4.556698,
      "aei_text": 2.176826,
      "aei_vision": 0.47772,
      "text_ratio": 0.820037,
      "vision_ratio": 0.179963
    },
    "all": {
      "mdi": 4.556698,
      "aei_text": 2.402967,
      "aei_vision": 0.377358,
      "text_ratio": 0.820037,
      "vision_ratio": 0.179963
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.820037,
      0.179963
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** I will think about it.  A reasonable amount for a child would be one-third of a pizza.   Based on standard portion sizes for children and considering they are young, a piece that is half of a slice sh…

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=-1.000, total=-1.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": -1.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.563887,
      "aei_text": 2.575584,
      "aei_vision": 0.300749,
      "text_ratio": 0.89544,
      "vision_ratio": 0.10456
    },
    "middle": {
      "mdi": 6.160949,
      "aei_text": 2.382056,
      "aei_vision": 0.386638,
      "text_ratio": 0.860354,
      "vision_ratio": 0.139646
    },
    "late": {
      "mdi": 5.435494,
      "aei_text": 2.299857,
      "aei_vision": 0.423118,
      "text_ratio": 0.844612,
      "vision_ratio": 0.155388
    },
    "all": {
      "mdi": 5.435494,
      "aei_text": 2.419166,
      "aei_vision": 0.370169,
      "text_ratio": 0.844612,
      "vision_ratio": 0.155388
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.844612,
      0.155388
    ]
  }
}
```

---


## === Rollout Step 2 ===
Step: 1/29790 | 2025-10-22 12:02:56

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 1.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 14.472 | 4.967 | 2.773 | 0.213 |
| Middle | 9.683 | 1.514 | 2.629 | 0.277 |
| Late | 6.696 | 0.577 | 2.431 | 0.365 |
| All | 6.696 | 0.577 | 2.611 | 0.285 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.505373,
      "aei_text": 2.629843,
      "aei_vision": 0.276669,
      "text_ratio": 0.904811,
      "vision_ratio": 0.095189
    },
    "middle": {
      "mdi": 8.169589,
      "aei_text": 2.549948,
      "aei_vision": 0.312127,
      "text_ratio": 0.890944,
      "vision_ratio": 0.109056
    },
    "late": {
      "mdi": 6.118999,
      "aei_text": 2.377691,
      "aei_vision": 0.388575,
      "text_ratio": 0.859531,
      "vision_ratio": 0.140469
    },
    "all": {
      "mdi": 6.118999,
      "aei_text": 2.519161,
      "aei_vision": 0.32579,
      "text_ratio": 0.859531,
      "vision_ratio": 0.140469
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.859531,
      0.140469
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <thinking> The parka in the image appears to be blue.  Answer: A

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=-1.000, total=-1.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": -1.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 19.438709,
      "aei_text": 2.915317,
      "aei_vision": 0.149975,
      "text_ratio": 0.951073,
      "vision_ratio": 0.048927
    },
    "middle": {
      "mdi": 11.196969,
      "aei_text": 2.708247,
      "aei_vision": 0.241873,
      "text_ratio": 0.918012,
      "vision_ratio": 0.081988
    },
    "late": {
      "mdi": 7.272452,
      "aei_text": 2.483711,
      "aei_vision": 0.341523,
      "text_ratio": 0.879117,
      "vision_ratio": 0.120883
    },
    "all": {
      "mdi": 7.272452,
      "aei_text": 2.702425,
      "aei_vision": 0.244457,
      "text_ratio": 0.879117,
      "vision_ratio": 0.120883
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.879117,
      0.120883
    ]
  }
}
```

---


## === Rollout Step 3 ===
Step: 2/29790 | 2025-10-22 12:03:00

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 3.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 24.276 | 16.029 | 3.135 | 0.212 |
| Middle | 21.927 | 13.038 | 3.143 | 0.209 |
| Late | 11.834 | 3.686 | 2.971 | 0.273 |
| All | 11.834 | 3.686 | 3.083 | 0.231 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.246278,
      "aei_text": 2.792515,
      "aei_vision": 0.338639,
      "text_ratio": 0.891848,
      "vision_ratio": 0.108152
    },
    "middle": {
      "mdi": 8.888902,
      "aei_text": 2.843365,
      "aei_vision": 0.319878,
      "text_ratio": 0.898877,
      "vision_ratio": 0.101123
    },
    "late": {
      "mdi": 8.148352,
      "aei_text": 2.784238,
      "aei_vision": 0.341693,
      "text_ratio": 0.890691,
      "vision_ratio": 0.109309
    },
    "all": {
      "mdi": 8.148352,
      "aei_text": 2.806706,
      "aei_vision": 0.333404,
      "text_ratio": 0.890691,
      "vision_ratio": 0.109309
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.890691,
      0.109309
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** Answer: A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.305262,
      "aei_text": 3.476562,
      "aei_vision": 0.086256,
      "text_ratio": 0.97579,
      "vision_ratio": 0.02421
    },
    "middle": {
      "mdi": 34.965481,
      "aei_text": 3.443428,
      "aei_vision": 0.098481,
      "text_ratio": 0.972196,
      "vision_ratio": 0.027804
    },
    "late": {
      "mdi": 15.520255,
      "aei_text": 3.158728,
      "aei_vision": 0.203523,
      "text_ratio": 0.939468,
      "vision_ratio": 0.060532
    },
    "all": {
      "mdi": 15.520255,
      "aei_text": 3.359572,
      "aei_vision": 0.12942,
      "text_ratio": 0.939468,
      "vision_ratio": 0.060532
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939468,
      0.060532
    ]
  }
}
```

---


## === Rollout Step 4 ===
Step: 3/29790 | 2025-10-22 12:03:03

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 3.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 14.313 | 5.832 | 2.286 | 0.188 |
| Middle | 9.285 | 4.221 | 2.140 | 0.280 |
| Late | 8.826 | 0.807 | 2.188 | 0.250 |
| All | 8.826 | 0.807 | 2.205 | 0.239 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 20.144997,
      "aei_text": 2.395544,
      "aei_vision": 0.118915,
      "text_ratio": 0.952707,
      "vision_ratio": 0.047293
    },
    "middle": {
      "mdi": 13.506301,
      "aei_text": 2.312683,
      "aei_vision": 0.17123,
      "text_ratio": 0.931064,
      "vision_ratio": 0.068936
    },
    "late": {
      "mdi": 8.019498,
      "aei_text": 2.15773,
      "aei_vision": 0.26906,
      "text_ratio": 0.889129,
      "vision_ratio": 0.110871
    },
    "all": {
      "mdi": 8.019498,
      "aei_text": 2.288652,
      "aei_vision": 0.186402,
      "text_ratio": 0.889129,
      "vision_ratio": 0.110871
    }
  },
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.889129,
      0.110871
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C. wine bottles

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.480856,
      "aei_text": 2.177265,
      "aei_vision": 0.256727,
      "text_ratio": 0.894524,
      "vision_ratio": 0.105476
    },
    "middle": {
      "mdi": 5.063668,
      "aei_text": 1.968237,
      "aei_vision": 0.388698,
      "text_ratio": 0.835083,
      "vision_ratio": 0.164917
    },
    "late": {
      "mdi": 9.633263,
      "aei_text": 2.21904,
      "aei_vision": 0.230352,
      "text_ratio": 0.905955,
      "vision_ratio": 0.094045
    },
    "all": {
      "mdi": 9.633263,
      "aei_text": 2.121514,
      "aei_vision": 0.291926,
      "text_ratio": 0.905955,
      "vision_ratio": 0.094045
    }
  },
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.905955,
      0.094045
    ]
  }
}
```

---


## === Rollout Step 5 ===
Step: 4/29790 | 2025-10-22 12:03:06

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 1.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 25.424 | 7.512 | 2.979 | 0.127 |
| Middle | 23.805 | 13.845 | 2.872 | 0.175 |
| Late | 14.910 | 0.032 | 2.837 | 0.190 |
| All | 14.910 | 0.032 | 2.896 | 0.164 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C. blue

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.911614,
      "aei_text": 2.900688,
      "aei_vision": 0.161945,
      "text_ratio": 0.947122,
      "vision_ratio": 0.052878
    },
    "middle": {
      "mdi": 9.959563,
      "aei_text": 2.661827,
      "aei_vision": 0.267263,
      "text_ratio": 0.908755,
      "vision_ratio": 0.091245
    },
    "late": {
      "mdi": 14.94133,
      "aei_text": 2.837295,
      "aei_vision": 0.189896,
      "text_ratio": 0.93727,
      "vision_ratio": 0.06273
    },
    "all": {
      "mdi": 14.94133,
      "aei_text": 2.799937,
      "aei_vision": 0.206368,
      "text_ratio": 0.93727,
      "vision_ratio": 0.06273
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.93727,
      0.06273
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** Answer: D

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=-1.000, total=-1.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": -1.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.936089,
      "aei_text": 3.057439,
      "aei_vision": 0.092829,
      "text_ratio": 0.970533,
      "vision_ratio": 0.029467
    },
    "middle": {
      "mdi": 37.649727,
      "aei_text": 3.0823,
      "aei_vision": 0.081868,
      "text_ratio": 0.974127,
      "vision_ratio": 0.025873
    },
    "late": {
      "mdi": 14.878209,
      "aei_text": 2.83571,
      "aei_vision": 0.190595,
      "text_ratio": 0.937021,
      "vision_ratio": 0.062979
    },
    "all": {
      "mdi": 14.878209,
      "aei_text": 2.991816,
      "aei_vision": 0.121764,
      "text_ratio": 0.937021,
      "vision_ratio": 0.062979
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937021,
      0.062979
    ]
  }
}
```

---


## === Rollout Step 6 ===
Step: 5/29790 | 2025-10-22 12:03:09

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 3.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 16.428 | 0.000 | 2.442 | 0.149 |
| Middle | 8.704 | 0.000 | 2.255 | 0.259 |
| Late | 10.585 | 0.000 | 2.322 | 0.219 |
| All | 10.585 | 0.000 | 2.339 | 0.209 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C. christmas

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 16.427634,
      "aei_text": 2.441652,
      "aei_vision": 0.148631,
      "text_ratio": 0.94262,
      "vision_ratio": 0.05738
    },
    "middle": {
      "mdi": 8.704352,
      "aei_text": 2.254706,
      "aei_vision": 0.259032,
      "text_ratio": 0.896953,
      "vision_ratio": 0.103047
    },
    "late": {
      "mdi": 10.584949,
      "aei_text": 2.321888,
      "aei_vision": 0.219358,
      "text_ratio": 0.913681,
      "vision_ratio": 0.086319
    },
    "all": {
      "mdi": 10.584949,
      "aei_text": 2.339415,
      "aei_vision": 0.209007,
      "text_ratio": 0.913681,
      "vision_ratio": 0.086319
    }
  },
  "token_counts": {
    "vision_tokens": 254,
    "text_tokens": 0,
    "total_tokens": 254
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.913681,
      0.086319
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C. christmas

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 16.427634,
      "aei_text": 2.441652,
      "aei_vision": 0.148631,
      "text_ratio": 0.94262,
      "vision_ratio": 0.05738
    },
    "middle": {
      "mdi": 8.704352,
      "aei_text": 2.254706,
      "aei_vision": 0.259032,
      "text_ratio": 0.896953,
      "vision_ratio": 0.103047
    },
    "late": {
      "mdi": 10.584949,
      "aei_text": 2.321888,
      "aei_vision": 0.219358,
      "text_ratio": 0.913681,
      "vision_ratio": 0.086319
    },
    "all": {
      "mdi": 10.584949,
      "aei_text": 2.339415,
      "aei_vision": 0.209007,
      "text_ratio": 0.913681,
      "vision_ratio": 0.086319
    }
  },
  "token_counts": {
    "vision_tokens": 254,
    "text_tokens": 0,
    "total_tokens": 254
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.913681,
      0.086319
    ]
  }
}
```

---


## === Rollout Step 7 ===
Step: 6/29790 | 2025-10-22 12:03:12

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 1.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 12.726 | 4.599 | 2.741 | 0.242 |
| Middle | 9.492 | 1.307 | 2.647 | 0.283 |
| Late | 8.986 | 3.058 | 2.573 | 0.315 |
| All | 8.986 | 3.058 | 2.654 | 0.280 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.127065,
      "aei_text": 2.571028,
      "aei_vision": 0.316354,
      "text_ratio": 0.890436,
      "vision_ratio": 0.109564
    },
    "middle": {
      "mdi": 8.184593,
      "aei_text": 2.575018,
      "aei_vision": 0.314618,
      "text_ratio": 0.891122,
      "vision_ratio": 0.108878
    },
    "late": {
      "mdi": 5.927864,
      "aei_text": 2.376667,
      "aei_vision": 0.400932,
      "text_ratio": 0.855655,
      "vision_ratio": 0.144345
    },
    "all": {
      "mdi": 5.927864,
      "aei_text": 2.507571,
      "aei_vision": 0.343968,
      "text_ratio": 0.855655,
      "vision_ratio": 0.144345
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.855655,
      0.144345
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B. multiple showers

**Solution:** D

**Rewards:** accuracy=0.000, format=0.000, mdi=-1.000, total=-1.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": -1.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.325885,
      "aei_text": 2.911807,
      "aei_vision": 0.168061,
      "text_ratio": 0.945432,
      "vision_ratio": 0.054568
    },
    "middle": {
      "mdi": 10.799234,
      "aei_text": 2.719351,
      "aei_vision": 0.25181,
      "text_ratio": 0.915249,
      "vision_ratio": 0.084751
    },
    "late": {
      "mdi": 12.043703,
      "aei_text": 2.769563,
      "aei_vision": 0.229959,
      "text_ratio": 0.923335,
      "vision_ratio": 0.076665
    },
    "all": {
      "mdi": 12.043703,
      "aei_text": 2.80024,
      "aei_vision": 0.21661,
      "text_ratio": 0.923335,
      "vision_ratio": 0.076665
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.923335,
      0.076665
    ]
  }
}
```

---


## === Rollout Step 8 ===
Step: 7/29790 | 2025-10-22 12:03:16

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 3.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 14.888 | 0.000 | 3.078 | 0.207 |
| Middle | 11.742 | 0.000 | 2.960 | 0.252 |
| Late | 15.767 | 0.000 | 3.104 | 0.197 |
| All | 15.767 | 0.000 | 3.047 | 0.219 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D. sun protection

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.888112,
      "aei_text": 3.078285,
      "aei_vision": 0.206761,
      "text_ratio": 0.93706,
      "vision_ratio": 0.06294
    },
    "middle": {
      "mdi": 11.742191,
      "aei_text": 2.959627,
      "aei_vision": 0.252051,
      "text_ratio": 0.921521,
      "vision_ratio": 0.078479
    },
    "late": {
      "mdi": 15.766954,
      "aei_text": 3.104178,
      "aei_vision": 0.196879,
      "text_ratio": 0.940359,
      "vision_ratio": 0.059641
    },
    "all": {
      "mdi": 15.766954,
      "aei_text": 3.047363,
      "aei_vision": 0.218564,
      "text_ratio": 0.940359,
      "vision_ratio": 0.059641
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940359,
      0.059641
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D. sun protection

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=-1.000, total=3.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": -1.0,
    "total": 3.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.888112,
      "aei_text": 3.078285,
      "aei_vision": 0.206761,
      "text_ratio": 0.93706,
      "vision_ratio": 0.06294
    },
    "middle": {
      "mdi": 11.742191,
      "aei_text": 2.959627,
      "aei_vision": 0.252051,
      "text_ratio": 0.921521,
      "vision_ratio": 0.078479
    },
    "late": {
      "mdi": 15.766954,
      "aei_text": 3.104178,
      "aei_vision": 0.196879,
      "text_ratio": 0.940359,
      "vision_ratio": 0.059641
    },
    "all": {
      "mdi": 15.766954,
      "aei_text": 3.047363,
      "aei_vision": 0.218564,
      "text_ratio": 0.940359,
      "vision_ratio": 0.059641
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940359,
      0.059641
    ]
  }
}
```

---


## === Rollout Step 9 ===
Step: 8/29790 | 2025-10-22 12:03:19

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 10 ===
Step: 9/29790 | 2025-10-22 12:03:22

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 11 ===
Step: 10/29790 | 2025-10-22 12:03:25

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 12 ===
Step: 11/29790 | 2025-10-22 12:03:29

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 13 ===
Step: 12/29790 | 2025-10-22 12:03:32

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 14 ===
Step: 13/29790 | 2025-10-22 12:03:35

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 186,
    "text_tokens": 0,
    "total_tokens": 186
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 186,
    "text_tokens": 0,
    "total_tokens": 186
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 15 ===
Step: 14/29790 | 2025-10-22 12:03:37

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 16 ===
Step: 15/29790 | 2025-10-22 12:03:40

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 17 ===
Step: 16/29790 | 2025-10-22 12:03:43

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** B

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 18 ===
Step: 17/29790 | 2025-10-22 12:03:47

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 19 ===
Step: 18/29790 | 2025-10-22 12:03:50

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 20 ===
Step: 19/29790 | 2025-10-22 12:03:52

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 21 ===
Step: 20/29790 | 2025-10-22 12:03:55

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 22 ===
Step: 21/29790 | 2025-10-22 12:03:58

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 23 ===
Step: 22/29790 | 2025-10-22 12:04:01

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 24 ===
Step: 23/29790 | 2025-10-22 12:04:05

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 25 ===
Step: 24/29790 | 2025-10-22 12:04:08

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 26 ===
Step: 25/29790 | 2025-10-22 12:04:11

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 27 ===
Step: 26/29790 | 2025-10-22 12:04:14

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 28 ===
Step: 27/29790 | 2025-10-22 12:04:17

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** D

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 29 ===
Step: 28/29790 | 2025-10-22 12:04:21

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** B

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 30 ===
Step: 29/29790 | 2025-10-22 12:04:24

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** C

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 31 ===
Step: 30/29790 | 2025-10-22 12:04:27

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 32 ===
Step: 31/29790 | 2025-10-22 12:04:31

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 33 ===
Step: 32/29790 | 2025-10-22 12:04:34

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 34 ===
Step: 33/29790 | 2025-10-22 12:04:37

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 35 ===
Step: 34/29790 | 2025-10-22 12:04:40

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** D

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 36 ===
Step: 35/29790 | 2025-10-22 12:04:43

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** A

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 37 ===
Step: 36/29790 | 2025-10-22 12:04:46

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** A

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 38 ===
Step: 37/29790 | 2025-10-22 12:04:50

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 39 ===
Step: 38/29790 | 2025-10-22 12:04:53

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 40 ===
Step: 39/29790 | 2025-10-22 12:04:56

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 0.000 ± 0.000 |
| Accuracy Rate | 0.000 |
| Format Rate | 0.000 |
| Success Rate | 0.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** D

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** A

**Solution:** D

**Rewards:** accuracy=0.000, format=0.000, mdi=0.000, total=0.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 0.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 0.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 41 ===
Step: 40/29790 | 2025-10-22 12:04:59

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 42 ===
Step: 41/29790 | 2025-10-22 12:05:02

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** B

**Solution:** B

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 43 ===
Step: 42/29790 | 2025-10-22 12:05:05

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** D

**Solution:** D

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---


## === Rollout Step 44 ===
Step: 43/29790 | 2025-10-22 12:05:08

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 0.000 ± 0.000 |
| MDI Mean | 0.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 0.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 1.000 | 0.000 | 0.000 | 0.000 |
| Middle | 1.000 | 0.000 | 0.000 | 0.000 |
| Late | 1.000 | 0.000 | 0.000 | 0.000 |
| All | 1.000 | 0.000 | 0.000 | 0.000 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** C

**Solution:** C

**Rewards:** accuracy=1.000, format=0.000, mdi=0.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 0.0,
    "mdi": 0.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "middle": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "late": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    },
    "all": {
      "mdi": 1.0,
      "aei_text": 0.0,
      "aei_vision": 0.0,
      "text_ratio": 0.5,
      "vision_ratio": 0.5
    }
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  },
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ]
  }
}
```

---

