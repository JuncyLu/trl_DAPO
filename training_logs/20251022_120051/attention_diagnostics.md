# Attention Diagnostics Log

This file contains MDI attention diagnostics from GRPO training.


## === Rollout Step 1 ===
Step: 0/29790 | 2025-10-22 12:01:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.676 | 5.971 | 4.996 | 4.996 |
| MDI Std | 1.112 | 0.190 | 0.439 | 0.439 |
| Vision Tokens | 347.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 347.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.820037,
      0.179963
    ],
    "text_vision_ratio": "0.820037:0.179963"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.844612,
      0.155388
    ],
    "text_vision_ratio": "0.844612:0.155388"
  }
}
```


## === Rollout Step 2 ===
Step: 1/29790 | 2025-10-22 12:01:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.119 | 7.458 | 5.555 | 5.555 |
| MDI Std | 1.979 | 1.163 | 0.835 | 0.835 |
| Vision Tokens | 347.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 347.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.825188,
      0.174812
    ],
    "text_vision_ratio": "0.825188:0.174812"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.864687,
      0.135313
    ],
    "text_vision_ratio": "0.864687:0.135313"
  }
}
```


## === Rollout Step 3 ===
Step: 2/29790 | 2025-10-22 12:01:36

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.824 | 4.765 | 3.612 | 3.612 |
| MDI Std | 0.676 | 1.282 | 0.900 | 0.900 |
| Vision Tokens | 393.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 393.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.818549,
      0.181451
    ],
    "text_vision_ratio": "0.818549:0.181451"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393,
    "text_tokens": 0,
    "total_tokens": 393
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.730598,
      0.269402
    ],
    "text_vision_ratio": "0.730598:0.269402"
  }
}
```


## === Rollout Step 4 ===
Step: 3/29790 | 2025-10-22 12:01:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.935 | 5.593 | 4.068 | 4.068 |
| MDI Std | 0.317 | 0.667 | 0.370 | 0.370 |
| Vision Tokens | 236.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 236.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.816082,
      0.183918
    ],
    "text_vision_ratio": "0.816082:0.183918"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 236,
    "text_tokens": 0,
    "total_tokens": 236
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.787145,
      0.212855
    ],
    "text_vision_ratio": "0.787145:0.212855"
  }
}
```


## === Rollout Step 5 ===
Step: 4/29790 | 2025-10-22 12:01:50

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.454 | 7.309 | 4.799 | 4.799 |
| MDI Std | 1.007 | 1.482 | 0.828 | 0.828 |
| Vision Tokens | 347.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 347.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.798824,
      0.201176
    ],
    "text_vision_ratio": "0.798824:0.201176"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.849108,
      0.150892
    ],
    "text_vision_ratio": "0.849108:0.150892"
  }
}
```


## === Rollout Step 6 ===
Step: 5/29790 | 2025-10-22 12:01:56

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.711 | 6.648 | 3.266 | 3.266 |
| MDI Std | 0.562 | 0.363 | 0.192 | 0.192 |
| Vision Tokens | 254.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 254.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 254,
    "text_tokens": 0,
    "total_tokens": 254
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.754583,
      0.245417
    ],
    "text_vision_ratio": "0.754583:0.245417"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 254,
    "text_tokens": 0,
    "total_tokens": 254
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.775675,
      0.224325
    ],
    "text_vision_ratio": "0.775675:0.224325"
  }
}
```

