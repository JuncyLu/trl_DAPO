# Rollout Results Log

This file contains detailed rollout results from GRPO training.


## === Rollout Step 1 ===
Step: 0/29790 | 2025-10-22 12:01:19

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
Step: 1/29790 | 2025-10-22 12:01:26

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 0.500 ± 0.500 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 1.500 ± 2.500 |
| Accuracy Rate | 0.500 |
| Format Rate | 0.500 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 13.119 | 1.979 | 2.768 | 0.215 |
| Middle | 7.458 | 1.163 | 2.487 | 0.340 |
| Late | 5.555 | 0.835 | 2.304 | 0.421 |
| All | 5.555 | 0.835 | 2.520 | 0.326 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The man in the left is wearing a bright orange parka. The jackets of the other individuals are not visible in the visible part of the image. </think> Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.097649,
      "aei_text": 2.830769,
      "aei_vision": 0.187497,
      "text_ratio": 0.937879,
      "vision_ratio": 0.062121
    },
    "middle": {
      "mdi": 6.295076,
      "aei_text": 2.395726,
      "aei_vision": 0.380571,
      "text_ratio": 0.862921,
      "vision_ratio": 0.137079
    },
    "late": {
      "mdi": 4.720437,
      "aei_text": 2.2021,
      "aei_vision": 0.466503,
      "text_ratio": 0.825188,
      "vision_ratio": 0.174812
    },
    "all": {
      "mdi": 4.720437,
      "aei_text": 2.476198,
      "aei_vision": 0.344857,
      "text_ratio": 0.825188,
      "vision_ratio": 0.174812
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
      0.825188,
      0.174812
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
      "mdi": 11.139593,
      "aei_text": 2.705912,
      "aei_vision": 0.242909,
      "text_ratio": 0.917625,
      "vision_ratio": 0.082375
    },
    "middle": {
      "mdi": 8.621512,
      "aei_text": 2.579175,
      "aei_vision": 0.299156,
      "text_ratio": 0.896066,
      "vision_ratio": 0.103934
    },
    "late": {
      "mdi": 6.390258,
      "aei_text": 2.405169,
      "aei_vision": 0.376381,
      "text_ratio": 0.864687,
      "vision_ratio": 0.135313
    },
    "all": {
      "mdi": 6.390258,
      "aei_text": 2.563419,
      "aei_vision": 0.306149,
      "text_ratio": 0.864687,
      "vision_ratio": 0.135313
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
      0.864687,
      0.135313
    ]
  }
}
```

---


## === Rollout Step 3 ===
Step: 2/29790 | 2025-10-22 12:01:36

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.500 ± 0.500 |
| Format Mean | 1.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 2.000 ± 2.000 |
| Accuracy Rate | 0.500 |
| Format Rate | 1.000 |
| Success Rate | 0.500 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 10.824 | 0.676 | 2.965 | 0.275 |
| Middle | 4.765 | 1.282 | 2.324 | 0.511 |
| Late | 3.612 | 0.900 | 2.087 | 0.599 |
| All | 3.612 | 0.900 | 2.459 | 0.462 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The man is seated at a desk with a computer keyboard, mouse, and a mug in front of him, which suggests that he is in an office setting. He seems to be eating pizza in the office, where similar…

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
      "mdi": 11.500035,
      "aei_text": 3.002671,
      "aei_vision": 0.261101,
      "text_ratio": 0.92,
      "vision_ratio": 0.08
    },
    "middle": {
      "mdi": 6.047029,
      "aei_text": 2.562019,
      "aei_vision": 0.423682,
      "text_ratio": 0.858096,
      "vision_ratio": 0.141904
    },
    "late": {
      "mdi": 4.511115,
      "aei_text": 2.317785,
      "aei_vision": 0.513794,
      "text_ratio": 0.818549,
      "vision_ratio": 0.181451
    },
    "all": {
      "mdi": 4.511115,
      "aei_text": 2.627492,
      "aei_vision": 0.399526,
      "text_ratio": 0.818549,
      "vision_ratio": 0.181451
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
      0.818549,
      0.181451
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The man is eating pizza on a desk that has accessories typical of an office, such as a keyboard, a computer mouse, and a monitor. TheDTF TAFE Tech branding on his shirt and the signage on the …

**Solution:** A

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.147727,
      "aei_text": 2.928244,
      "aei_vision": 0.288562,
      "text_ratio": 0.910296,
      "vision_ratio": 0.089704
    },
    "middle": {
      "mdi": 3.483794,
      "aei_text": 2.086824,
      "aei_vision": 0.599009,
      "text_ratio": 0.776975,
      "vision_ratio": 0.223025
    },
    "late": {
      "mdi": 2.711925,
      "aei_text": 1.855713,
      "aei_vision": 0.684279,
      "text_ratio": 0.730598,
      "vision_ratio": 0.269402
    },
    "all": {
      "mdi": 2.711925,
      "aei_text": 2.29026,
      "aei_vision": 0.52395,
      "text_ratio": 0.730598,
      "vision_ratio": 0.269402
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
      0.730598,
      0.269402
    ]
  }
}
```

---


## === Rollout Step 4 ===
Step: 3/29790 | 2025-10-22 12:01:42

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 1.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 1.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 9.935 | 0.317 | 2.228 | 0.224 |
| Middle | 5.593 | 0.667 | 2.009 | 0.363 |
| Late | 4.068 | 0.370 | 1.857 | 0.459 |
| All | 4.068 | 0.370 | 2.031 | 0.349 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The question asks about what is on the table to the left. Considering the arrangement and context of the image, the answer is most likely wine bottles. </think> Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.251675,
      "aei_text": 2.238104,
      "aei_vision": 0.218316,
      "text_ratio": 0.911124,
      "vision_ratio": 0.088876
    },
    "middle": {
      "mdi": 6.25972,
      "aei_text": 2.062117,
      "aei_vision": 0.329426,
      "text_ratio": 0.862254,
      "vision_ratio": 0.137746
    },
    "late": {
      "mdi": 4.437217,
      "aei_text": 1.904183,
      "aei_vision": 0.429139,
      "text_ratio": 0.816082,
      "vision_ratio": 0.183918
    },
    "all": {
      "mdi": 4.437217,
      "aei_text": 2.068134,
      "aei_vision": 0.325627,
      "text_ratio": 0.816082,
      "vision_ratio": 0.183918
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
      0.816082,
      0.183918
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The question asks what is on the table to the left, and it mentions wine bottles a few sentences ago. The table to the left is the table where the wine glasses and bottles are placed. </think>…

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.618365,
      "aei_text": 2.218555,
      "aei_vision": 0.230658,
      "text_ratio": 0.905824,
      "vision_ratio": 0.094176
    },
    "middle": {
      "mdi": 4.925869,
      "aei_text": 1.955205,
      "aei_vision": 0.396926,
      "text_ratio": 0.831248,
      "vision_ratio": 0.168752
    },
    "late": {
      "mdi": 3.698038,
      "aei_text": 1.809061,
      "aei_vision": 0.489195,
      "text_ratio": 0.787145,
      "vision_ratio": 0.212855
    },
    "all": {
      "mdi": 3.698038,
      "aei_text": 1.994273,
      "aei_vision": 0.37226,
      "text_ratio": 0.787145,
      "vision_ratio": 0.212855
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
      0.787145,
      0.212855
    ]
  }
}
```

---


## === Rollout Step 5 ===
Step: 4/29790 | 2025-10-22 12:01:50

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 1.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 1.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 12.454 | 1.007 | 2.762 | 0.223 |
| Middle | 7.309 | 1.482 | 2.475 | 0.350 |
| Late | 4.799 | 0.828 | 2.205 | 0.469 |
| All | 4.799 | 0.828 | 2.481 | 0.347 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The image shows the boats lined up along the beach with the interior sections painted in two colors. The interior sections, including the seats, are visible and appear in two different colors …

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.446975,
      "aei_text": 2.727565,
      "aei_vision": 0.238278,
      "text_ratio": 0.919659,
      "vision_ratio": 0.080341
    },
    "middle": {
      "mdi": 5.826839,
      "aei_text": 2.352365,
      "aei_vision": 0.403712,
      "text_ratio": 0.853519,
      "vision_ratio": 0.146481
    },
    "late": {
      "mdi": 3.970763,
      "aei_text": 2.079964,
      "aei_vision": 0.52382,
      "text_ratio": 0.798824,
      "vision_ratio": 0.201176
    },
    "all": {
      "mdi": 3.970763,
      "aei_text": 2.386632,
      "aei_vision": 0.388603,
      "text_ratio": 0.798824,
      "vision_ratio": 0.201176
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
      0.798824,
      0.201176
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The task is a visual comprehension one but focuses on identifying the interior sections of the boats, noting a specific color. Despite this constraint, these boats displayed along the sandy be…

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.460268,
      "aei_text": 2.79674,
      "aei_vision": 0.207777,
      "text_ratio": 0.930845,
      "vision_ratio": 0.069155
    },
    "middle": {
      "mdi": 8.79042,
      "aei_text": 2.597743,
      "aei_vision": 0.29552,
      "text_ratio": 0.897859,
      "vision_ratio": 0.102141
    },
    "late": {
      "mdi": 5.627266,
      "aei_text": 2.329221,
      "aei_vision": 0.413917,
      "text_ratio": 0.849108,
      "vision_ratio": 0.150892
    },
    "all": {
      "mdi": 5.627266,
      "aei_text": 2.574568,
      "aei_vision": 0.305738,
      "text_ratio": 0.849108,
      "vision_ratio": 0.150892
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
      0.849108,
      0.150892
    ]
  }
}
```

---


## === Rollout Step 6 ===
Step: 5/29790 | 2025-10-22 12:01:56

### Overall Statistics

| Metric | Value |
|--------|-------|
| Accuracy Mean | 1.000 ± 0.000 |
| Format Mean | 1.000 ± 0.000 |
| MDI Mean | -1.000 ± 0.000 |
| Total Reward Mean | 4.000 ± 0.000 |
| Accuracy Rate | 1.000 |
| Format Rate | 1.000 |
| Success Rate | 1.000 |

### MDI Statistics

| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 12.711 | 0.562 | 2.376 | 0.187 |
| Middle | 6.648 | 0.363 | 2.146 | 0.323 |
| Late | 3.266 | 0.192 | 1.772 | 0.544 |
| All | 3.266 | 0.192 | 2.098 | 0.352 |

### Sample 1

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The man is wearing a Santa hat, which is typically associated with the Christmas holiday season. There is no indication of any other time of the year in the image provided. </think> Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.27365,
      "aei_text": 2.388615,
      "aei_vision": 0.179952,
      "text_ratio": 0.929941,
      "vision_ratio": 0.070059
    },
    "middle": {
      "mdi": 6.284715,
      "aei_text": 2.121676,
      "aei_vision": 0.337593,
      "text_ratio": 0.862726,
      "vision_ratio": 0.137274
    },
    "late": {
      "mdi": 3.074704,
      "aei_text": 1.736816,
      "aei_vision": 0.564873,
      "text_ratio": 0.754583,
      "vision_ratio": 0.245417
    },
    "all": {
      "mdi": 3.074704,
      "aei_text": 2.082369,
      "aei_vision": 0.360806,
      "text_ratio": 0.754583,
      "vision_ratio": 0.245417
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
      0.754583,
      0.245417
    ]
  }
}
```

---

### Sample 2

**Prompt:** system A conversation between user and assistant. The user asks a question, and the assistant solves…

**Completion:** <think> The man is wearing a Santa hat, which is a symbol typically associated with the Christmas holiday. This suggests that the season is currently Christmas. </think> Answer: C

**Solution:** C

**Rewards:** accuracy=1.000, format=1.000, mdi=-1.000, total=4.000

**Detailed Metrics:**

```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0,
    "mdi": -1.0,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.148779,
      "aei_text": 2.363852,
      "aei_vision": 0.194575,
      "text_ratio": 0.923947,
      "vision_ratio": 0.076053
    },
    "middle": {
      "mdi": 7.011588,
      "aei_text": 2.16941,
      "aei_vision": 0.309404,
      "text_ratio": 0.875181,
      "vision_ratio": 0.124819
    },
    "late": {
      "mdi": 3.457809,
      "aei_text": 1.807955,
      "aei_vision": 0.522861,
      "text_ratio": 0.775675,
      "vision_ratio": 0.224325
    },
    "all": {
      "mdi": 3.457809,
      "aei_text": 2.113739,
      "aei_vision": 0.34228,
      "text_ratio": 0.775675,
      "vision_ratio": 0.224325
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
      0.775675,
      0.224325
    ]
  }
}
```

---

