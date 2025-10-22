# Attention Diagnostics Log

This file contains MDI attention diagnostics from GRPO training.


## === Rollout Step 1 ===
Step: 0/29790 | 2025-10-22 12:06:01

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
Step: 1/29790 | 2025-10-22 12:06:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.610 | 6.393 | 4.959 | 4.959 |
| MDI Std | 1.502 | 1.515 | 1.147 | 1.147 |
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
      "mdi": 13.112178,
      "aei_text": 2.776178,
      "aei_vision": 0.211725,
      "text_ratio": 0.929139,
      "vision_ratio": 0.070861
    },
    "middle": {
      "mdi": 4.877846,
      "aei_text": 2.225302,
      "aei_vision": 0.456206,
      "text_ratio": 0.82987,
      "vision_ratio": 0.17013
    },
    "late": {
      "mdi": 3.812393,
      "aei_text": 2.04474,
      "aei_vision": 0.53634,
      "text_ratio": 0.792203,
      "vision_ratio": 0.207797
    },
    "all": {
      "mdi": 3.812393,
      "aei_text": 2.34874,
      "aei_vision": 0.401424,
      "text_ratio": 0.792203,
      "vision_ratio": 0.207797
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.792203,
      0.207797
    ],
    "text_vision_ratio": "0.792203:0.207797"
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
      "mdi": 10.108754,
      "aei_text": 2.660271,
      "aei_vision": 0.263165,
      "text_ratio": 0.909981,
      "vision_ratio": 0.090019
    },
    "middle": {
      "mdi": 7.908638,
      "aei_text": 2.531888,
      "aei_vision": 0.320142,
      "text_ratio": 0.887749,
      "vision_ratio": 0.112251
    },
    "late": {
      "mdi": 6.105838,
      "aei_text": 2.376312,
      "aei_vision": 0.389187,
      "text_ratio": 0.859271,
      "vision_ratio": 0.140729
    },
    "all": {
      "mdi": 6.105838,
      "aei_text": 2.522824,
      "aei_vision": 0.324165,
      "text_ratio": 0.859271,
      "vision_ratio": 0.140729
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.859271,
      0.140729
    ],
    "text_vision_ratio": "0.859271:0.140729"
  }
}
```


## === Rollout Step 3 ===
Step: 2/29790 | 2025-10-22 12:06:20

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.978 | 6.252 | 5.513 | 5.513 |
| MDI Std | 0.349 | 1.057 | 0.795 | 0.795 |
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
      "mdi": 10.62833,
      "aei_text": 2.956423,
      "aei_vision": 0.278164,
      "text_ratio": 0.914003,
      "vision_ratio": 0.085997
    },
    "middle": {
      "mdi": 5.194918,
      "aei_text": 2.438241,
      "aei_vision": 0.469351,
      "text_ratio": 0.838577,
      "vision_ratio": 0.161423
    },
    "late": {
      "mdi": 4.717511,
      "aei_text": 2.35648,
      "aei_vision": 0.499518,
      "text_ratio": 0.825099,
      "vision_ratio": 0.174901
    },
    "all": {
      "mdi": 4.717511,
      "aei_text": 2.583715,
      "aei_vision": 0.415678,
      "text_ratio": 0.825099,
      "vision_ratio": 0.174901
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.825099,
      0.174901
    ],
    "text_vision_ratio": "0.825099:0.174901"
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
      "mdi": 11.327202,
      "aei_text": 2.993958,
      "aei_vision": 0.264316,
      "text_ratio": 0.918879,
      "vision_ratio": 0.081121
    },
    "middle": {
      "mdi": 7.309421,
      "aei_text": 2.706697,
      "aei_vision": 0.370303,
      "text_ratio": 0.879655,
      "vision_ratio": 0.120345
    },
    "late": {
      "mdi": 6.307528,
      "aei_text": 2.595191,
      "aei_vision": 0.411443,
      "text_ratio": 0.863155,
      "vision_ratio": 0.136845
    },
    "all": {
      "mdi": 6.307528,
      "aei_text": 2.765282,
      "aei_vision": 0.348687,
      "text_ratio": 0.863155,
      "vision_ratio": 0.136845
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.863155,
      0.136845
    ],
    "text_vision_ratio": "0.863155:0.136845"
  }
}
```


## === Rollout Step 4 ===
Step: 3/29790 | 2025-10-22 12:06:27

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.678 | 7.059 | 6.489 | 6.489 |
| MDI Std | 1.647 | 1.424 | 0.923 | 0.923 |
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
      "mdi": 8.031315,
      "aei_text": 2.158253,
      "aei_vision": 0.26873,
      "text_ratio": 0.889274,
      "vision_ratio": 0.110726
    },
    "middle": {
      "mdi": 5.634888,
      "aei_text": 2.016954,
      "aei_vision": 0.35794,
      "text_ratio": 0.849282,
      "vision_ratio": 0.150718
    },
    "late": {
      "mdi": 5.566217,
      "aei_text": 2.011509,
      "aei_vision": 0.361378,
      "text_ratio": 0.847705,
      "vision_ratio": 0.152295
    },
    "all": {
      "mdi": 5.566217,
      "aei_text": 2.062239,
      "aei_vision": 0.329349,
      "text_ratio": 0.847705,
      "vision_ratio": 0.152295
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.847705,
      0.152295
    ],
    "text_vision_ratio": "0.847705:0.152295"
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
      "mdi": 11.324663,
      "aei_text": 2.266846,
      "aei_vision": 0.200169,
      "text_ratio": 0.918862,
      "vision_ratio": 0.081138
    },
    "middle": {
      "mdi": 8.483463,
      "aei_text": 2.17737,
      "aei_vision": 0.256661,
      "text_ratio": 0.894553,
      "vision_ratio": 0.105447
    },
    "late": {
      "mdi": 7.41154,
      "aei_text": 2.128927,
      "aei_vision": 0.287245,
      "text_ratio": 0.881116,
      "vision_ratio": 0.118884
    },
    "all": {
      "mdi": 7.41154,
      "aei_text": 2.191048,
      "aei_vision": 0.248025,
      "text_ratio": 0.881116,
      "vision_ratio": 0.118884
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.881116,
      0.118884
    ],
    "text_vision_ratio": "0.881116:0.118884"
  }
}
```


## === Rollout Step 5 ===
Step: 4/29790 | 2025-10-22 12:06:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.629 | 8.421 | 6.194 | 6.194 |
| MDI Std | 1.341 | 1.376 | 1.125 | 1.125 |
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
      "mdi": 10.2876,
      "aei_text": 2.677664,
      "aei_vision": 0.260281,
      "text_ratio": 0.911407,
      "vision_ratio": 0.088593
    },
    "middle": {
      "mdi": 9.796349,
      "aei_text": 2.653627,
      "aei_vision": 0.270879,
      "text_ratio": 0.907376,
      "vision_ratio": 0.092624
    },
    "late": {
      "mdi": 7.318351,
      "aei_text": 2.494823,
      "aei_vision": 0.3409,
      "text_ratio": 0.879784,
      "vision_ratio": 0.120216
    },
    "all": {
      "mdi": 7.318351,
      "aei_text": 2.608705,
      "aei_vision": 0.290686,
      "text_ratio": 0.879784,
      "vision_ratio": 0.120216
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.879784,
      0.120216
    ],
    "text_vision_ratio": "0.879784:0.120216"
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
      "mdi": 12.97024,
      "aei_text": 2.781586,
      "aei_vision": 0.214459,
      "text_ratio": 0.928419,
      "vision_ratio": 0.071581
    },
    "middle": {
      "mdi": 7.044859,
      "aei_text": 2.472117,
      "aei_vision": 0.350911,
      "text_ratio": 0.875697,
      "vision_ratio": 0.124303
    },
    "late": {
      "mdi": 5.068773,
      "aei_text": 2.257761,
      "aei_vision": 0.445425,
      "text_ratio": 0.835222,
      "vision_ratio": 0.164778
    },
    "all": {
      "mdi": 5.068773,
      "aei_text": 2.503821,
      "aei_vision": 0.336932,
      "text_ratio": 0.835222,
      "vision_ratio": 0.164778
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.835222,
      0.164778
    ],
    "text_vision_ratio": "0.835222:0.164778"
  }
}
```


## === Rollout Step 6 ===
Step: 5/29790 | 2025-10-22 12:06:43

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.499 | 4.931 | 4.610 | 4.610 |
| MDI Std | 0.104 | 1.064 | 0.698 | 0.698 |
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
      "mdi": 10.603312,
      "aei_text": 2.322443,
      "aei_vision": 0.21903,
      "text_ratio": 0.913818,
      "vision_ratio": 0.086182
    },
    "middle": {
      "mdi": 3.867071,
      "aei_text": 1.873121,
      "aei_vision": 0.484377,
      "text_ratio": 0.794538,
      "vision_ratio": 0.205462
    },
    "late": {
      "mdi": 3.912437,
      "aei_text": 1.879759,
      "aei_vision": 0.480457,
      "text_ratio": 0.796435,
      "vision_ratio": 0.203565
    },
    "all": {
      "mdi": 3.912437,
      "aei_text": 2.025108,
      "aei_vision": 0.394622,
      "text_ratio": 0.796435,
      "vision_ratio": 0.203565
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.796435,
      0.203565
    ],
    "text_vision_ratio": "0.796435:0.203565"
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
      "mdi": 10.394445,
      "aei_text": 2.316034,
      "aei_vision": 0.222815,
      "text_ratio": 0.912238,
      "vision_ratio": 0.087762
    },
    "middle": {
      "mdi": 5.995048,
      "aei_text": 2.100138,
      "aei_vision": 0.350312,
      "text_ratio": 0.857042,
      "vision_ratio": 0.142958
    },
    "late": {
      "mdi": 5.307681,
      "aei_text": 2.041898,
      "aei_vision": 0.384706,
      "text_ratio": 0.841463,
      "vision_ratio": 0.158537
    },
    "all": {
      "mdi": 5.307681,
      "aei_text": 2.15269,
      "aei_vision": 0.319278,
      "text_ratio": 0.841463,
      "vision_ratio": 0.158537
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.841463,
      0.158537
    ],
    "text_vision_ratio": "0.841463:0.158537"
  }
}
```


## === Rollout Step 7 ===
Step: 6/29790 | 2025-10-22 12:06:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.194 | 8.709 | 11.410 | 11.410 |
| MDI Std | 3.945 | 0.061 | 3.639 | 3.639 |
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
      "mdi": 8.249333,
      "aei_text": 2.579455,
      "aei_vision": 0.312687,
      "text_ratio": 0.891884,
      "vision_ratio": 0.108116
    },
    "middle": {
      "mdi": 8.648139,
      "aei_text": 2.605635,
      "aei_vision": 0.301294,
      "text_ratio": 0.896353,
      "vision_ratio": 0.103647
    },
    "late": {
      "mdi": 7.771509,
      "aei_text": 2.545358,
      "aei_vision": 0.327524,
      "text_ratio": 0.885995,
      "vision_ratio": 0.114005
    },
    "all": {
      "mdi": 7.771509,
      "aei_text": 2.576816,
      "aei_vision": 0.313835,
      "text_ratio": 0.885995,
      "vision_ratio": 0.114005
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.885995,
      0.114005
    ],
    "text_vision_ratio": "0.885995:0.114005"
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
      "mdi": 16.138897,
      "aei_text": 2.886942,
      "aei_vision": 0.178881,
      "text_ratio": 0.941653,
      "vision_ratio": 0.058347
    },
    "middle": {
      "mdi": 8.76938,
      "aei_text": 2.61322,
      "aei_vision": 0.297994,
      "text_ratio": 0.897639,
      "vision_ratio": 0.102361
    },
    "late": {
      "mdi": 15.049234,
      "aei_text": 2.861121,
      "aei_vision": 0.190117,
      "text_ratio": 0.937692,
      "vision_ratio": 0.062308
    },
    "all": {
      "mdi": 15.049234,
      "aei_text": 2.787094,
      "aei_vision": 0.222331,
      "text_ratio": 0.937692,
      "vision_ratio": 0.062308
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937692,
      0.062308
    ],
    "text_vision_ratio": "0.937692:0.062308"
  }
}
```


## === Rollout Step 8 ===
Step: 7/29790 | 2025-10-22 12:06:53

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.411 | 7.649 | 7.946 | 7.946 |
| MDI Std | 2.251 | 0.785 | 0.746 | 0.746 |
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
      "mdi": 11.66267,
      "aei_text": 2.955951,
      "aei_vision": 0.253454,
      "text_ratio": 0.921028,
      "vision_ratio": 0.078972
    },
    "middle": {
      "mdi": 8.434091,
      "aei_text": 2.762001,
      "aei_vision": 0.327481,
      "text_ratio": 0.894001,
      "vision_ratio": 0.105999
    },
    "late": {
      "mdi": 8.692478,
      "aei_text": 2.781598,
      "aei_vision": 0.320001,
      "text_ratio": 0.896827,
      "vision_ratio": 0.103173
    },
    "all": {
      "mdi": 8.692478,
      "aei_text": 2.833183,
      "aei_vision": 0.300312,
      "text_ratio": 0.896827,
      "vision_ratio": 0.103173
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.896827,
      0.103173
    ],
    "text_vision_ratio": "0.896827:0.103173"
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
      "mdi": 7.159889,
      "aei_text": 2.650214,
      "aei_vision": 0.370147,
      "text_ratio": 0.877449,
      "vision_ratio": 0.122551
    },
    "middle": {
      "mdi": 6.864383,
      "aei_text": 2.619998,
      "aei_vision": 0.38168,
      "text_ratio": 0.872844,
      "vision_ratio": 0.127156
    },
    "late": {
      "mdi": 7.200305,
      "aei_text": 2.654205,
      "aei_vision": 0.368624,
      "text_ratio": 0.878053,
      "vision_ratio": 0.121947
    },
    "all": {
      "mdi": 7.200305,
      "aei_text": 2.641472,
      "aei_vision": 0.373484,
      "text_ratio": 0.878053,
      "vision_ratio": 0.121947
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.878053,
      0.121947
    ],
    "text_vision_ratio": "0.878053:0.121947"
  }
}
```


## === Rollout Step 9 ===
Step: 8/29790 | 2025-10-22 12:07:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.788 | 6.323 | 5.339 | 5.339 |
| MDI Std | 0.890 | 1.101 | 0.327 | 0.327 |
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
      "mdi": 14.678057,
      "aei_text": 2.862232,
      "aei_vision": 0.195001,
      "text_ratio": 0.936217,
      "vision_ratio": 0.063783
    },
    "middle": {
      "mdi": 5.221481,
      "aei_text": 2.296076,
      "aei_vision": 0.439737,
      "text_ratio": 0.839267,
      "vision_ratio": 0.160733
    },
    "late": {
      "mdi": 5.012039,
      "aei_text": 2.266991,
      "aei_vision": 0.452309,
      "text_ratio": 0.833667,
      "vision_ratio": 0.166333
    },
    "all": {
      "mdi": 5.012039,
      "aei_text": 2.4751,
      "aei_vision": 0.362349,
      "text_ratio": 0.833667,
      "vision_ratio": 0.166333
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.833667,
      0.166333
    ],
    "text_vision_ratio": "0.833667:0.166333"
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
      "mdi": 12.897373,
      "aei_text": 2.809422,
      "aei_vision": 0.217829,
      "text_ratio": 0.928044,
      "vision_ratio": 0.071956
    },
    "middle": {
      "mdi": 7.424125,
      "aei_text": 2.526183,
      "aei_vision": 0.340267,
      "text_ratio": 0.881293,
      "vision_ratio": 0.118707
    },
    "late": {
      "mdi": 5.666032,
      "aei_text": 2.35275,
      "aei_vision": 0.415238,
      "text_ratio": 0.849986,
      "vision_ratio": 0.150014
    },
    "all": {
      "mdi": 5.666032,
      "aei_text": 2.562785,
      "aei_vision": 0.324444,
      "text_ratio": 0.849986,
      "vision_ratio": 0.150014
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.849986,
      0.150014
    ],
    "text_vision_ratio": "0.849986:0.150014"
  }
}
```


## === Rollout Step 10 ===
Step: 9/29790 | 2025-10-22 12:07:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.309 | 6.103 | 5.931 | 5.931 |
| MDI Std | 2.573 | 0.493 | 0.289 | 0.289 |
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
      "mdi": 6.735967,
      "aei_text": 2.473637,
      "aei_vision": 0.367228,
      "text_ratio": 0.870734,
      "vision_ratio": 0.129266
    },
    "middle": {
      "mdi": 5.609305,
      "aei_text": 2.352255,
      "aei_vision": 0.419349,
      "text_ratio": 0.848698,
      "vision_ratio": 0.151302
    },
    "late": {
      "mdi": 5.64205,
      "aei_text": 2.356267,
      "aei_vision": 0.417626,
      "text_ratio": 0.849444,
      "vision_ratio": 0.150556
    },
    "all": {
      "mdi": 5.64205,
      "aei_text": 2.394053,
      "aei_vision": 0.401401,
      "text_ratio": 0.849444,
      "vision_ratio": 0.150556
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.849444,
      0.150556
    ],
    "text_vision_ratio": "0.849444:0.150556"
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
      "mdi": 11.882149,
      "aei_text": 2.783335,
      "aei_vision": 0.234245,
      "text_ratio": 0.922373,
      "vision_ratio": 0.077627
    },
    "middle": {
      "mdi": 6.595844,
      "aei_text": 2.460209,
      "aei_vision": 0.372994,
      "text_ratio": 0.868349,
      "vision_ratio": 0.131651
    },
    "late": {
      "mdi": 6.219464,
      "aei_text": 2.421963,
      "aei_vision": 0.389417,
      "text_ratio": 0.861486,
      "vision_ratio": 0.138514
    },
    "all": {
      "mdi": 6.219464,
      "aei_text": 2.555169,
      "aei_vision": 0.332219,
      "text_ratio": 0.861486,
      "vision_ratio": 0.138514
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.861486,
      0.138514
    ],
    "text_vision_ratio": "0.861486:0.138514"
  }
}
```


## === Rollout Step 11 ===
Step: 10/29790 | 2025-10-22 12:07:15

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 25.631 | 24.313 | 19.748 | 19.748 |
| MDI Std | 11.349 | 15.274 | 0.206 | 0.206 |
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
      "mdi": 14.281667,
      "aei_text": 3.118519,
      "aei_vision": 0.218358,
      "text_ratio": 0.934562,
      "vision_ratio": 0.065438
    },
    "middle": {
      "mdi": 9.038983,
      "aei_text": 2.854439,
      "aei_vision": 0.315792,
      "text_ratio": 0.900388,
      "vision_ratio": 0.099612
    },
    "late": {
      "mdi": 19.542192,
      "aei_text": 3.258427,
      "aei_vision": 0.166738,
      "text_ratio": 0.95132,
      "vision_ratio": 0.04868
    },
    "all": {
      "mdi": 19.542192,
      "aei_text": 3.077128,
      "aei_vision": 0.233629,
      "text_ratio": 0.95132,
      "vision_ratio": 0.04868
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95132,
      0.04868
    ],
    "text_vision_ratio": "0.951320:0.048680"
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
      "mdi": 36.979761,
      "aei_text": 3.456974,
      "aei_vision": 0.093483,
      "text_ratio": 0.97367,
      "vision_ratio": 0.02633
    },
    "middle": {
      "mdi": 39.586196,
      "aei_text": 3.472587,
      "aei_vision": 0.087722,
      "text_ratio": 0.975361,
      "vision_ratio": 0.024639
    },
    "late": {
      "mdi": 19.95411,
      "aei_text": 3.266641,
      "aei_vision": 0.163708,
      "text_ratio": 0.952277,
      "vision_ratio": 0.047723
    },
    "all": {
      "mdi": 19.95411,
      "aei_text": 3.398734,
      "aei_vision": 0.114971,
      "text_ratio": 0.952277,
      "vision_ratio": 0.047723
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952277,
      0.047723
    ],
    "text_vision_ratio": "0.952277:0.047723"
  }
}
```


## === Rollout Step 12 ===
Step: 11/29790 | 2025-10-22 12:07:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 13 ===
Step: 12/29790 | 2025-10-22 12:07:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 14 ===
Step: 13/29790 | 2025-10-22 12:07:24

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 186.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 186.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 186,
    "text_tokens": 0,
    "total_tokens": 186
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 186,
    "text_tokens": 0,
    "total_tokens": 186
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 15 ===
Step: 14/29790 | 2025-10-22 12:07:27

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.108 | 12.568 | 16.965 | 16.965 |
| MDI Std | 2.161 | 0.960 | 1.214 | 1.214 |
| Vision Tokens | 324.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 324.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 22.269321,
      "aei_text": 2.939533,
      "aei_vision": 0.131999,
      "text_ratio": 0.957025,
      "vision_ratio": 0.042975
    },
    "middle": {
      "mdi": 13.528223,
      "aei_text": 2.77597,
      "aei_vision": 0.205198,
      "text_ratio": 0.931168,
      "vision_ratio": 0.068832
    },
    "late": {
      "mdi": 18.178398,
      "aei_text": 2.880422,
      "aei_vision": 0.158453,
      "text_ratio": 0.947858,
      "vision_ratio": 0.052142
    },
    "all": {
      "mdi": 18.178398,
      "aei_text": 2.865308,
      "aei_vision": 0.165217,
      "text_ratio": 0.947858,
      "vision_ratio": 0.052142
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947858,
      0.052142
    ],
    "text_vision_ratio": "0.947858:0.052142"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.946436,
      "aei_text": 2.876353,
      "aei_vision": 0.160274,
      "text_ratio": 0.94722,
      "vision_ratio": 0.05278
    },
    "middle": {
      "mdi": 11.608193,
      "aei_text": 2.712373,
      "aei_vision": 0.23366,
      "text_ratio": 0.920686,
      "vision_ratio": 0.079314
    },
    "late": {
      "mdi": 15.75105,
      "aei_text": 2.832638,
      "aei_vision": 0.179838,
      "text_ratio": 0.940302,
      "vision_ratio": 0.059698
    },
    "all": {
      "mdi": 15.75105,
      "aei_text": 2.807121,
      "aei_vision": 0.191258,
      "text_ratio": 0.940302,
      "vision_ratio": 0.059698
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940302,
      0.059698
    ],
    "text_vision_ratio": "0.940302:0.059698"
  }
}
```


## === Rollout Step 16 ===
Step: 15/29790 | 2025-10-22 12:07:31

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.262 | 10.310 | 11.642 | 11.642 |
| MDI Std | 3.956 | 1.101 | 3.935 | 3.935 |
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
      "mdi": 16.218244,
      "aei_text": 2.968639,
      "aei_vision": 0.183043,
      "text_ratio": 0.941922,
      "vision_ratio": 0.058078
    },
    "middle": {
      "mdi": 11.410994,
      "aei_text": 2.815217,
      "aei_vision": 0.246711,
      "text_ratio": 0.919426,
      "vision_ratio": 0.080574
    },
    "late": {
      "mdi": 15.577098,
      "aei_text": 2.952916,
      "aei_vision": 0.189568,
      "text_ratio": 0.939676,
      "vision_ratio": 0.060324
    },
    "all": {
      "mdi": 15.577098,
      "aei_text": 2.912258,
      "aei_vision": 0.206441,
      "text_ratio": 0.939676,
      "vision_ratio": 0.060324
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939676,
      0.060324
    ],
    "text_vision_ratio": "0.939676:0.060324"
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
      "mdi": 8.30619,
      "aei_text": 2.642967,
      "aei_vision": 0.318192,
      "text_ratio": 0.892545,
      "vision_ratio": 0.107455
    },
    "middle": {
      "mdi": 9.209986,
      "aei_text": 2.702606,
      "aei_vision": 0.293443,
      "text_ratio": 0.902057,
      "vision_ratio": 0.097943
    },
    "late": {
      "mdi": 7.707311,
      "aei_text": 2.597579,
      "aei_vision": 0.337028,
      "text_ratio": 0.885154,
      "vision_ratio": 0.114846
    },
    "all": {
      "mdi": 7.707311,
      "aei_text": 2.647717,
      "aei_vision": 0.316221,
      "text_ratio": 0.885154,
      "vision_ratio": 0.114846
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.885154,
      0.114846
    ],
    "text_vision_ratio": "0.885154:0.114846"
  }
}
```


## === Rollout Step 17 ===
Step: 16/29790 | 2025-10-22 12:07:34

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 18 ===
Step: 17/29790 | 2025-10-22 12:07:37

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 19 ===
Step: 18/29790 | 2025-10-22 12:07:40

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 20 ===
Step: 19/29790 | 2025-10-22 12:07:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.203 | 11.244 | 9.127 | 9.127 |
| MDI Std | 5.946 | 3.689 | 3.802 | 3.802 |
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
      "mdi": 20.149037,
      "aei_text": 2.395579,
      "aei_vision": 0.118893,
      "text_ratio": 0.952717,
      "vision_ratio": 0.047283
    },
    "middle": {
      "mdi": 14.932639,
      "aei_text": 2.336104,
      "aei_vision": 0.156443,
      "text_ratio": 0.937236,
      "vision_ratio": 0.062764
    },
    "late": {
      "mdi": 12.928712,
      "aei_text": 2.301889,
      "aei_vision": 0.178045,
      "text_ratio": 0.928206,
      "vision_ratio": 0.071794
    },
    "all": {
      "mdi": 12.928712,
      "aei_text": 2.344524,
      "aei_vision": 0.151127,
      "text_ratio": 0.928206,
      "vision_ratio": 0.071794
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928206,
      0.071794
    ],
    "text_vision_ratio": "0.928206:0.071794"
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
      "mdi": 8.256887,
      "aei_text": 2.16801,
      "aei_vision": 0.26257,
      "text_ratio": 0.891972,
      "vision_ratio": 0.108028
    },
    "middle": {
      "mdi": 7.554823,
      "aei_text": 2.136061,
      "aei_vision": 0.282741,
      "text_ratio": 0.883107,
      "vision_ratio": 0.116893
    },
    "late": {
      "mdi": 5.324819,
      "aei_text": 1.991509,
      "aei_vision": 0.374005,
      "text_ratio": 0.841893,
      "vision_ratio": 0.158107
    },
    "all": {
      "mdi": 5.324819,
      "aei_text": 2.098527,
      "aei_vision": 0.306439,
      "text_ratio": 0.841893,
      "vision_ratio": 0.158107
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.841893,
      0.158107
    ],
    "text_vision_ratio": "0.841893:0.158107"
  }
}
```


## === Rollout Step 21 ===
Step: 20/29790 | 2025-10-22 12:07:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 22 ===
Step: 21/29790 | 2025-10-22 12:07:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.639 | 11.444 | 20.221 | 20.221 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.639422,
      "aei_text": 2.880599,
      "aei_vision": 0.154543,
      "text_ratio": 0.949082,
      "vision_ratio": 0.050918
    },
    "middle": {
      "mdi": 11.444234,
      "aei_text": 2.699643,
      "aei_vision": 0.235895,
      "text_ratio": 0.919641,
      "vision_ratio": 0.080359
    },
    "late": {
      "mdi": 20.221221,
      "aei_text": 2.904825,
      "aei_vision": 0.143652,
      "text_ratio": 0.952877,
      "vision_ratio": 0.047123
    },
    "all": {
      "mdi": 20.221221,
      "aei_text": 2.828356,
      "aei_vision": 0.17803,
      "text_ratio": 0.952877,
      "vision_ratio": 0.047123
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952877,
      0.047123
    ],
    "text_vision_ratio": "0.952877:0.047123"
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
      "mdi": 18.639422,
      "aei_text": 2.880599,
      "aei_vision": 0.154543,
      "text_ratio": 0.949082,
      "vision_ratio": 0.050918
    },
    "middle": {
      "mdi": 11.444234,
      "aei_text": 2.699643,
      "aei_vision": 0.235895,
      "text_ratio": 0.919641,
      "vision_ratio": 0.080359
    },
    "late": {
      "mdi": 20.221221,
      "aei_text": 2.904825,
      "aei_vision": 0.143652,
      "text_ratio": 0.952877,
      "vision_ratio": 0.047123
    },
    "all": {
      "mdi": 20.221221,
      "aei_text": 2.828356,
      "aei_vision": 0.17803,
      "text_ratio": 0.952877,
      "vision_ratio": 0.047123
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952877,
      0.047123
    ],
    "text_vision_ratio": "0.952877:0.047123"
  }
}
```


## === Rollout Step 23 ===
Step: 22/29790 | 2025-10-22 12:07:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.522 | 8.465 | 11.049 | 11.049 |
| MDI Std | 3.209 | 1.023 | 3.695 | 3.695 |
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
      "mdi": 15.730744,
      "aei_text": 2.888549,
      "aei_vision": 0.183624,
      "text_ratio": 0.94023,
      "vision_ratio": 0.05977
    },
    "middle": {
      "mdi": 7.44206,
      "aei_text": 2.52763,
      "aei_vision": 0.339641,
      "text_ratio": 0.881546,
      "vision_ratio": 0.118454
    },
    "late": {
      "mdi": 14.743733,
      "aei_text": 2.863969,
      "aei_vision": 0.19425,
      "text_ratio": 0.936483,
      "vision_ratio": 0.063517
    },
    "all": {
      "mdi": 14.743733,
      "aei_text": 2.760049,
      "aei_vision": 0.239172,
      "text_ratio": 0.936483,
      "vision_ratio": 0.063517
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936483,
      0.063517
    ],
    "text_vision_ratio": "0.936483:0.063517"
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
      "mdi": 9.312754,
      "aei_text": 2.654054,
      "aei_vision": 0.284991,
      "text_ratio": 0.903033,
      "vision_ratio": 0.096967
    },
    "middle": {
      "mdi": 9.487427,
      "aei_text": 2.663812,
      "aei_vision": 0.280773,
      "text_ratio": 0.904648,
      "vision_ratio": 0.095352
    },
    "late": {
      "mdi": 7.354054,
      "aei_text": 2.520478,
      "aei_vision": 0.342733,
      "text_ratio": 0.880298,
      "vision_ratio": 0.119702
    },
    "all": {
      "mdi": 7.354054,
      "aei_text": 2.612781,
      "aei_vision": 0.302832,
      "text_ratio": 0.880298,
      "vision_ratio": 0.119702
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.880298,
      0.119702
    ],
    "text_vision_ratio": "0.880298:0.119702"
  }
}
```


## === Rollout Step 24 ===
Step: 23/29790 | 2025-10-22 12:07:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 25 ===
Step: 24/29790 | 2025-10-22 12:07:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 26 ===
Step: 25/29790 | 2025-10-22 12:08:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.378 | 9.537 | 12.346 | 12.346 |
| MDI Std | 3.336 | 0.330 | 5.079 | 5.079 |
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
      "mdi": 9.041472,
      "aei_text": 2.621091,
      "aei_vision": 0.289897,
      "text_ratio": 0.900413,
      "vision_ratio": 0.099587
    },
    "middle": {
      "mdi": 9.867024,
      "aei_text": 2.666059,
      "aei_vision": 0.270199,
      "text_ratio": 0.907978,
      "vision_ratio": 0.092022
    },
    "late": {
      "mdi": 7.267109,
      "aei_text": 2.49813,
      "aei_vision": 0.343758,
      "text_ratio": 0.879039,
      "vision_ratio": 0.120961
    },
    "all": {
      "mdi": 7.267109,
      "aei_text": 2.595094,
      "aei_vision": 0.301285,
      "text_ratio": 0.879039,
      "vision_ratio": 0.120961
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.879039,
      0.120961
    ],
    "text_vision_ratio": "0.879039:0.120961"
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
      "mdi": 15.714053,
      "aei_text": 2.866463,
      "aei_vision": 0.182414,
      "text_ratio": 0.94017,
      "vision_ratio": 0.05983
    },
    "middle": {
      "mdi": 9.207233,
      "aei_text": 2.630639,
      "aei_vision": 0.285714,
      "text_ratio": 0.90203,
      "vision_ratio": 0.09797
    },
    "late": {
      "mdi": 17.424767,
      "aei_text": 2.902611,
      "aei_vision": 0.16658,
      "text_ratio": 0.945725,
      "vision_ratio": 0.054275
    },
    "all": {
      "mdi": 17.424767,
      "aei_text": 2.799904,
      "aei_vision": 0.211569,
      "text_ratio": 0.945725,
      "vision_ratio": 0.054275
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945725,
      0.054275
    ],
    "text_vision_ratio": "0.945725:0.054275"
  }
}
```


## === Rollout Step 27 ===
Step: 26/29790 | 2025-10-22 12:08:05

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 28 ===
Step: 27/29790 | 2025-10-22 12:08:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 29 ===
Step: 28/29790 | 2025-10-22 12:08:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 30 ===
Step: 29/29790 | 2025-10-22 12:08:15

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 31 ===
Step: 30/29790 | 2025-10-22 12:08:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.411 | 7.420 | 15.172 | 15.172 |
| MDI Std | 1.314 | 0.854 | 5.479 | 5.479 |
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
      "mdi": 8.096931,
      "aei_text": 2.717704,
      "aei_vision": 0.335646,
      "text_ratio": 0.890073,
      "vision_ratio": 0.109927
    },
    "middle": {
      "mdi": 8.273634,
      "aei_text": 2.731826,
      "aei_vision": 0.330185,
      "text_ratio": 0.892167,
      "vision_ratio": 0.107833
    },
    "late": {
      "mdi": 9.693432,
      "aei_text": 2.830538,
      "aei_vision": 0.292006,
      "text_ratio": 0.906485,
      "vision_ratio": 0.093515
    },
    "all": {
      "mdi": 9.693432,
      "aei_text": 2.760023,
      "aei_vision": 0.319279,
      "text_ratio": 0.906485,
      "vision_ratio": 0.093515
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.906485,
      0.093515
    ],
    "text_vision_ratio": "0.906485:0.093515"
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
      "mdi": 10.724886,
      "aei_text": 2.889044,
      "aei_vision": 0.269378,
      "text_ratio": 0.914711,
      "vision_ratio": 0.085289
    },
    "middle": {
      "mdi": 6.56568,
      "aei_text": 2.572493,
      "aei_vision": 0.391809,
      "text_ratio": 0.867824,
      "vision_ratio": 0.132176
    },
    "late": {
      "mdi": 20.650931,
      "aei_text": 3.186564,
      "aei_vision": 0.154306,
      "text_ratio": 0.953813,
      "vision_ratio": 0.046187
    },
    "all": {
      "mdi": 20.650931,
      "aei_text": 2.8827,
      "aei_vision": 0.271831,
      "text_ratio": 0.953813,
      "vision_ratio": 0.046187
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953813,
      0.046187
    ],
    "text_vision_ratio": "0.953813:0.046187"
  }
}
```


## === Rollout Step 32 ===
Step: 31/29790 | 2025-10-22 12:08:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 33 ===
Step: 32/29790 | 2025-10-22 12:08:25

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 34 ===
Step: 33/29790 | 2025-10-22 12:08:29

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 35 ===
Step: 34/29790 | 2025-10-22 12:08:32

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 370.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 370.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 36 ===
Step: 35/29790 | 2025-10-22 12:08:35

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 37 ===
Step: 36/29790 | 2025-10-22 12:08:38

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 38 ===
Step: 37/29790 | 2025-10-22 12:08:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.236 | 17.936 | 9.987 | 9.987 |
| MDI Std | 7.296 | 7.502 | 3.397 | 3.397 |
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
      "mdi": 24.532834,
      "aei_text": 3.270703,
      "aei_vision": 0.133319,
      "text_ratio": 0.960835,
      "vision_ratio": 0.039165
    },
    "middle": {
      "mdi": 25.437717,
      "aei_text": 3.281968,
      "aei_vision": 0.12902,
      "text_ratio": 0.962175,
      "vision_ratio": 0.037825
    },
    "late": {
      "mdi": 13.384342,
      "aei_text": 3.027386,
      "aei_vision": 0.226189,
      "text_ratio": 0.93048,
      "vision_ratio": 0.06952
    },
    "all": {
      "mdi": 13.384342,
      "aei_text": 3.193352,
      "aei_vision": 0.162843,
      "text_ratio": 0.93048,
      "vision_ratio": 0.06952
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.93048,
      0.06952
    ],
    "text_vision_ratio": "0.930480:0.069520"
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
      "mdi": 9.94014,
      "aei_text": 2.864881,
      "aei_vision": 0.288213,
      "text_ratio": 0.908593,
      "vision_ratio": 0.091407
    },
    "middle": {
      "mdi": 10.433891,
      "aei_text": 2.893443,
      "aei_vision": 0.277312,
      "text_ratio": 0.912541,
      "vision_ratio": 0.087459
    },
    "late": {
      "mdi": 6.590118,
      "aei_text": 2.59022,
      "aei_vision": 0.393046,
      "text_ratio": 0.86825,
      "vision_ratio": 0.13175
    },
    "all": {
      "mdi": 6.590118,
      "aei_text": 2.782848,
      "aei_vision": 0.319524,
      "text_ratio": 0.86825,
      "vision_ratio": 0.13175
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.86825,
      0.13175
    ],
    "text_vision_ratio": "0.868250:0.131750"
  }
}
```


## === Rollout Step 39 ===
Step: 38/29790 | 2025-10-22 12:08:45

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 370.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 370.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 40 ===
Step: 39/29790 | 2025-10-22 12:08:48

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 41 ===
Step: 40/29790 | 2025-10-22 12:08:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 42 ===
Step: 41/29790 | 2025-10-22 12:08:54

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.723 | 8.169 | 9.243 | 9.243 |
| MDI Std | 4.028 | 1.612 | 3.632 | 3.632 |
| Vision Tokens | 218.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 218.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "attention_metrics": {
    "early": {
      "mdi": 16.750926,
      "aei_text": 2.273091,
      "aei_vision": 0.135699,
      "text_ratio": 0.943665,
      "vision_ratio": 0.056335
    },
    "middle": {
      "mdi": 6.556789,
      "aei_text": 2.019333,
      "aei_vision": 0.307976,
      "text_ratio": 0.867669,
      "vision_ratio": 0.132331
    },
    "late": {
      "mdi": 12.875537,
      "aei_text": 2.219105,
      "aei_vision": 0.172351,
      "text_ratio": 0.927931,
      "vision_ratio": 0.072069
    },
    "all": {
      "mdi": 12.875537,
      "aei_text": 2.17051,
      "aei_vision": 0.205342,
      "text_ratio": 0.927931,
      "vision_ratio": 0.072069
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927931,
      0.072069
    ],
    "text_vision_ratio": "0.927931:0.072069"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.694803,
      "aei_text": 2.114721,
      "aei_vision": 0.243217,
      "text_ratio": 0.896852,
      "vision_ratio": 0.103148
    },
    "middle": {
      "mdi": 9.781239,
      "aei_text": 2.149306,
      "aei_vision": 0.219738,
      "text_ratio": 0.907246,
      "vision_ratio": 0.092754
    },
    "late": {
      "mdi": 5.611177,
      "aei_text": 1.95878,
      "aei_vision": 0.349085,
      "text_ratio": 0.848741,
      "vision_ratio": 0.151259
    },
    "all": {
      "mdi": 5.611177,
      "aei_text": 2.074269,
      "aei_vision": 0.27068,
      "text_ratio": 0.848741,
      "vision_ratio": 0.151259
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.848741,
      0.151259
    ],
    "text_vision_ratio": "0.848741:0.151259"
  }
}
```


## === Rollout Step 43 ===
Step: 42/29790 | 2025-10-22 12:08:58

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 44 ===
Step: 43/29790 | 2025-10-22 12:09:01

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 45 ===
Step: 44/29790 | 2025-10-22 12:09:04

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 46 ===
Step: 45/29790 | 2025-10-22 12:09:07

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 47 ===
Step: 46/29790 | 2025-10-22 12:09:10

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 48 ===
Step: 47/29790 | 2025-10-22 12:09:13

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.180 | 12.025 | 20.598 | 20.598 |
| MDI Std | 4.788 | 0.979 | 9.300 | 9.300 |
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
      "mdi": 10.391716,
      "aei_text": 2.738481,
      "aei_vision": 0.263525,
      "text_ratio": 0.912217,
      "vision_ratio": 0.087783
    },
    "middle": {
      "mdi": 13.004253,
      "aei_text": 2.844253,
      "aei_vision": 0.218717,
      "text_ratio": 0.928593,
      "vision_ratio": 0.071407
    },
    "late": {
      "mdi": 11.298015,
      "aei_text": 2.779757,
      "aei_vision": 0.246039,
      "text_ratio": 0.918686,
      "vision_ratio": 0.081314
    },
    "all": {
      "mdi": 11.298015,
      "aei_text": 2.787497,
      "aei_vision": 0.242761,
      "text_ratio": 0.918686,
      "vision_ratio": 0.081314
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.918686,
      0.081314
    ],
    "text_vision_ratio": "0.918686:0.081314"
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
      "mdi": 19.967806,
      "aei_text": 3.005269,
      "aei_vision": 0.150506,
      "text_ratio": 0.952308,
      "vision_ratio": 0.047692
    },
    "middle": {
      "mdi": 11.045852,
      "aei_text": 2.768833,
      "aei_vision": 0.250667,
      "text_ratio": 0.916984,
      "vision_ratio": 0.083016
    },
    "late": {
      "mdi": 29.897511,
      "aei_text": 3.11463,
      "aei_vision": 0.104177,
      "text_ratio": 0.967635,
      "vision_ratio": 0.032365
    },
    "all": {
      "mdi": 29.897511,
      "aei_text": 2.962911,
      "aei_vision": 0.16845,
      "text_ratio": 0.967635,
      "vision_ratio": 0.032365
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967635,
      0.032365
    ],
    "text_vision_ratio": "0.967635:0.032365"
  }
}
```


## === Rollout Step 49 ===
Step: 48/29790 | 2025-10-22 12:09:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 7.599 | 4.503 | 12.773 | 12.773 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 7.599017,
      "aei_text": 2.222525,
      "aei_vision": 0.292475,
      "text_ratio": 0.883708,
      "vision_ratio": 0.116292
    },
    "middle": {
      "mdi": 4.502604,
      "aei_text": 1.97137,
      "aei_vision": 0.437829,
      "text_ratio": 0.818268,
      "vision_ratio": 0.181732
    },
    "late": {
      "mdi": 12.773042,
      "aei_text": 2.402843,
      "aei_vision": 0.188118,
      "text_ratio": 0.927394,
      "vision_ratio": 0.072606
    },
    "all": {
      "mdi": 12.773042,
      "aei_text": 2.198913,
      "aei_vision": 0.306141,
      "text_ratio": 0.927394,
      "vision_ratio": 0.072606
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927394,
      0.072606
    ],
    "text_vision_ratio": "0.927394:0.072606"
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
      "mdi": 7.599017,
      "aei_text": 2.222525,
      "aei_vision": 0.292475,
      "text_ratio": 0.883708,
      "vision_ratio": 0.116292
    },
    "middle": {
      "mdi": 4.502604,
      "aei_text": 1.97137,
      "aei_vision": 0.437829,
      "text_ratio": 0.818268,
      "vision_ratio": 0.181732
    },
    "late": {
      "mdi": 12.773042,
      "aei_text": 2.402843,
      "aei_vision": 0.188118,
      "text_ratio": 0.927394,
      "vision_ratio": 0.072606
    },
    "all": {
      "mdi": 12.773042,
      "aei_text": 2.198913,
      "aei_vision": 0.306141,
      "text_ratio": 0.927394,
      "vision_ratio": 0.072606
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927394,
      0.072606
    ],
    "text_vision_ratio": "0.927394:0.072606"
  }
}
```


## === Rollout Step 50 ===
Step: 49/29790 | 2025-10-22 12:09:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 51 ===
Step: 50/29790 | 2025-10-22 12:09:23

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 52 ===
Step: 51/29790 | 2025-10-22 12:09:27

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 531.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 531.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 53 ===
Step: 52/29790 | 2025-10-22 12:09:30

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 218.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 218.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 54 ===
Step: 53/29790 | 2025-10-22 12:09:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.071 | 13.357 | 13.414 | 13.414 |
| MDI Std | 4.496 | 0.769 | 4.588 | 4.588 |
| Vision Tokens | 462.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 462.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 462,
    "text_tokens": 0,
    "total_tokens": 462
  },
  "attention_metrics": {
    "early": {
      "mdi": 20.56618,
      "aei_text": 3.578467,
      "aei_vision": 0.173998,
      "text_ratio": 0.953631,
      "vision_ratio": 0.046369
    },
    "middle": {
      "mdi": 14.126057,
      "aei_text": 3.375658,
      "aei_vision": 0.238967,
      "text_ratio": 0.933889,
      "vision_ratio": 0.066111
    },
    "late": {
      "mdi": 18.001194,
      "aei_text": 3.51251,
      "aei_vision": 0.195127,
      "text_ratio": 0.947372,
      "vision_ratio": 0.052628
    },
    "all": {
      "mdi": 18.001194,
      "aei_text": 3.488878,
      "aei_vision": 0.202697,
      "text_ratio": 0.947372,
      "vision_ratio": 0.052628
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947372,
      0.052628
    ],
    "text_vision_ratio": "0.947372:0.052628"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 462,
    "text_tokens": 0,
    "total_tokens": 462
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.57488,
      "aei_text": 3.246165,
      "aei_vision": 0.280449,
      "text_ratio": 0.920476,
      "vision_ratio": 0.079524
    },
    "middle": {
      "mdi": 12.588389,
      "aei_text": 3.302644,
      "aei_vision": 0.262356,
      "text_ratio": 0.926408,
      "vision_ratio": 0.073592
    },
    "late": {
      "mdi": 8.82604,
      "aei_text": 3.044746,
      "aei_vision": 0.344973,
      "text_ratio": 0.89823,
      "vision_ratio": 0.10177
    },
    "all": {
      "mdi": 8.82604,
      "aei_text": 3.197852,
      "aei_vision": 0.295926,
      "text_ratio": 0.89823,
      "vision_ratio": 0.10177
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.89823,
      0.10177
    ],
    "text_vision_ratio": "0.898230:0.101770"
  }
}
```


## === Rollout Step 55 ===
Step: 54/29790 | 2025-10-22 12:09:37

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 370.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 370.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 370,
    "text_tokens": 0,
    "total_tokens": 370
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 56 ===
Step: 55/29790 | 2025-10-22 12:09:39

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 206.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 206.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 206,
    "text_tokens": 0,
    "total_tokens": 206
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 206,
    "text_tokens": 0,
    "total_tokens": 206
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 57 ===
Step: 56/29790 | 2025-10-22 12:09:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.253 | 9.218 | 18.675 | 18.675 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.252897,
      "aei_text": 2.898979,
      "aei_vision": 0.190061,
      "text_ratio": 0.938473,
      "vision_ratio": 0.061527
    },
    "middle": {
      "mdi": 9.218112,
      "aei_text": 2.666404,
      "aei_vision": 0.289257,
      "text_ratio": 0.902135,
      "vision_ratio": 0.097865
    },
    "late": {
      "mdi": 18.674696,
      "aei_text": 2.971522,
      "aei_vision": 0.15912,
      "text_ratio": 0.949173,
      "vision_ratio": 0.050827
    },
    "all": {
      "mdi": 18.674696,
      "aei_text": 2.845635,
      "aei_vision": 0.212813,
      "text_ratio": 0.949173,
      "vision_ratio": 0.050827
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949173,
      0.050827
    ],
    "text_vision_ratio": "0.949173:0.050827"
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
      "mdi": 15.252897,
      "aei_text": 2.898979,
      "aei_vision": 0.190061,
      "text_ratio": 0.938473,
      "vision_ratio": 0.061527
    },
    "middle": {
      "mdi": 9.218112,
      "aei_text": 2.666404,
      "aei_vision": 0.289257,
      "text_ratio": 0.902135,
      "vision_ratio": 0.097865
    },
    "late": {
      "mdi": 18.674696,
      "aei_text": 2.971522,
      "aei_vision": 0.15912,
      "text_ratio": 0.949173,
      "vision_ratio": 0.050827
    },
    "all": {
      "mdi": 18.674696,
      "aei_text": 2.845635,
      "aei_vision": 0.212813,
      "text_ratio": 0.949173,
      "vision_ratio": 0.050827
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949173,
      0.050827
    ],
    "text_vision_ratio": "0.949173:0.050827"
  }
}
```


## === Rollout Step 58 ===
Step: 57/29790 | 2025-10-22 12:09:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 59 ===
Step: 58/29790 | 2025-10-22 12:09:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.167 | 8.690 | 11.375 | 11.375 |
| MDI Std | 2.410 | 0.645 | 3.194 | 3.194 |
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
      "mdi": 13.576616,
      "aei_text": 3.000877,
      "aei_vision": 0.221033,
      "text_ratio": 0.931397,
      "vision_ratio": 0.068603
    },
    "middle": {
      "mdi": 8.044553,
      "aei_text": 2.70494,
      "aei_vision": 0.336245,
      "text_ratio": 0.889436,
      "vision_ratio": 0.110564
    },
    "late": {
      "mdi": 14.56959,
      "aei_text": 3.033772,
      "aei_vision": 0.208226,
      "text_ratio": 0.935772,
      "vision_ratio": 0.064228
    },
    "all": {
      "mdi": 14.56959,
      "aei_text": 2.913196,
      "aei_vision": 0.255168,
      "text_ratio": 0.935772,
      "vision_ratio": 0.064228
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.935772,
      0.064228
    ],
    "text_vision_ratio": "0.935772:0.064228"
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
      "mdi": 8.756699,
      "aei_text": 2.759249,
      "aei_vision": 0.315102,
      "text_ratio": 0.897506,
      "vision_ratio": 0.102494
    },
    "middle": {
      "mdi": 9.334619,
      "aei_text": 2.798546,
      "aei_vision": 0.299803,
      "text_ratio": 0.903238,
      "vision_ratio": 0.096762
    },
    "late": {
      "mdi": 8.18122,
      "aei_text": 2.71592,
      "aei_vision": 0.33197,
      "text_ratio": 0.891082,
      "vision_ratio": 0.108918
    },
    "all": {
      "mdi": 8.18122,
      "aei_text": 2.757905,
      "aei_vision": 0.315625,
      "text_ratio": 0.891082,
      "vision_ratio": 0.108918
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.891082,
      0.108918
    ],
    "text_vision_ratio": "0.891082:0.108918"
  }
}
```


## === Rollout Step 60 ===
Step: 59/29790 | 2025-10-22 12:09:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 61 ===
Step: 60/29790 | 2025-10-22 12:09:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 218.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 218.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 62 ===
Step: 61/29790 | 2025-10-22 12:09:58

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 63 ===
Step: 62/29790 | 2025-10-22 12:10:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.455 | 10.411 | 12.559 | 12.559 |
| MDI Std | 4.049 | 1.040 | 4.236 | 4.236 |
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
      "mdi": 8.406568,
      "aei_text": 2.76885,
      "aei_vision": 0.329367,
      "text_ratio": 0.893691,
      "vision_ratio": 0.106309
    },
    "middle": {
      "mdi": 9.370636,
      "aei_text": 2.838595,
      "aei_vision": 0.302925,
      "text_ratio": 0.903574,
      "vision_ratio": 0.096426
    },
    "late": {
      "mdi": 8.322645,
      "aei_text": 2.762198,
      "aei_vision": 0.331889,
      "text_ratio": 0.892734,
      "vision_ratio": 0.107266
    },
    "all": {
      "mdi": 8.322645,
      "aei_text": 2.789881,
      "aei_vision": 0.321394,
      "text_ratio": 0.892734,
      "vision_ratio": 0.107266
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.892734,
      0.107266
    ],
    "text_vision_ratio": "0.892734:0.107266"
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
      "mdi": 16.5042,
      "aei_text": 3.136354,
      "aei_vision": 0.190034,
      "text_ratio": 0.942871,
      "vision_ratio": 0.057129
    },
    "middle": {
      "mdi": 11.45129,
      "aei_text": 2.95659,
      "aei_vision": 0.258188,
      "text_ratio": 0.919687,
      "vision_ratio": 0.080313
    },
    "late": {
      "mdi": 16.795394,
      "aei_text": 3.143865,
      "aei_vision": 0.187186,
      "text_ratio": 0.943806,
      "vision_ratio": 0.056194
    },
    "all": {
      "mdi": 16.795394,
      "aei_text": 3.078936,
      "aei_vision": 0.211803,
      "text_ratio": 0.943806,
      "vision_ratio": 0.056194
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943806,
      0.056194
    ],
    "text_vision_ratio": "0.943806:0.056194"
  }
}
```


## === Rollout Step 64 ===
Step: 63/29790 | 2025-10-22 12:10:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.339 | 8.179 | 9.781 | 9.781 |
| MDI Std | 2.865 | 0.657 | 2.469 | 2.469 |
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
      "mdi": 8.474622,
      "aei_text": 2.747339,
      "aei_vision": 0.324184,
      "text_ratio": 0.894455,
      "vision_ratio": 0.105545
    },
    "middle": {
      "mdi": 8.836038,
      "aei_text": 2.773862,
      "aei_vision": 0.313926,
      "text_ratio": 0.898333,
      "vision_ratio": 0.101667
    },
    "late": {
      "mdi": 7.311309,
      "aei_text": 2.648815,
      "aei_vision": 0.36229,
      "text_ratio": 0.879682,
      "vision_ratio": 0.120318
    },
    "all": {
      "mdi": 7.311309,
      "aei_text": 2.723339,
      "aei_vision": 0.333467,
      "text_ratio": 0.879682,
      "vision_ratio": 0.120318
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.879682,
      0.120318
    ],
    "text_vision_ratio": "0.879682:0.120318"
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
      "mdi": 14.204237,
      "aei_text": 3.033376,
      "aei_vision": 0.213554,
      "text_ratio": 0.934229,
      "vision_ratio": 0.065771
    },
    "middle": {
      "mdi": 7.522055,
      "aei_text": 2.668346,
      "aei_vision": 0.354736,
      "text_ratio": 0.882657,
      "vision_ratio": 0.117343
    },
    "late": {
      "mdi": 12.249981,
      "aei_text": 2.960642,
      "aei_vision": 0.241685,
      "text_ratio": 0.924528,
      "vision_ratio": 0.075472
    },
    "all": {
      "mdi": 12.249981,
      "aei_text": 2.887455,
      "aei_vision": 0.269992,
      "text_ratio": 0.924528,
      "vision_ratio": 0.075472
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.924528,
      0.075472
    ],
    "text_vision_ratio": "0.924528:0.075472"
  }
}
```


## === Rollout Step 65 ===
Step: 64/29790 | 2025-10-22 12:10:09

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 66 ===
Step: 65/29790 | 2025-10-22 12:10:13

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 67 ===
Step: 66/29790 | 2025-10-22 12:10:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 68 ===
Step: 67/29790 | 2025-10-22 12:10:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 69 ===
Step: 68/29790 | 2025-10-22 12:10:23

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.389 | 17.309 | 22.314 | 22.314 |
| MDI Std | 7.773 | 5.518 | 11.370 | 11.370 |
| Vision Tokens | 416.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 416.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 416,
    "text_tokens": 0,
    "total_tokens": 416
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.616451,
      "aei_text": 2.918781,
      "aei_vision": 0.30352,
      "text_ratio": 0.905807,
      "vision_ratio": 0.094193
    },
    "middle": {
      "mdi": 11.790806,
      "aei_text": 3.043777,
      "aei_vision": 0.258148,
      "text_ratio": 0.921819,
      "vision_ratio": 0.078181
    },
    "late": {
      "mdi": 10.944239,
      "aei_text": 2.999828,
      "aei_vision": 0.274101,
      "text_ratio": 0.916278,
      "vision_ratio": 0.083722
    },
    "all": {
      "mdi": 10.944239,
      "aei_text": 2.987462,
      "aei_vision": 0.27859,
      "text_ratio": 0.916278,
      "vision_ratio": 0.083722
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.916278,
      0.083722
    ],
    "text_vision_ratio": "0.916278:0.083722"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 416,
    "text_tokens": 0,
    "total_tokens": 416
  },
  "attention_metrics": {
    "early": {
      "mdi": 25.162275,
      "aei_text": 3.384414,
      "aei_vision": 0.134504,
      "text_ratio": 0.961777,
      "vision_ratio": 0.038223
    },
    "middle": {
      "mdi": 22.826816,
      "aei_text": 3.350585,
      "aei_vision": 0.146783,
      "text_ratio": 0.95803,
      "vision_ratio": 0.04197
    },
    "late": {
      "mdi": 33.684134,
      "aei_text": 3.471074,
      "aei_vision": 0.103048,
      "text_ratio": 0.971168,
      "vision_ratio": 0.028832
    },
    "all": {
      "mdi": 33.684134,
      "aei_text": 3.402024,
      "aei_vision": 0.128111,
      "text_ratio": 0.971168,
      "vision_ratio": 0.028832
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971168,
      0.028832
    ],
    "text_vision_ratio": "0.971168:0.028832"
  }
}
```


## === Rollout Step 70 ===
Step: 69/29790 | 2025-10-22 12:10:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 71 ===
Step: 70/29790 | 2025-10-22 12:10:29

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 72 ===
Step: 71/29790 | 2025-10-22 12:10:32

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.616 | 10.088 | 16.343 | 16.343 |
| MDI Std | 1.999 | 1.208 | 5.956 | 5.956 |
| Vision Tokens | 416.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 416.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 416,
    "text_tokens": 0,
    "total_tokens": 416
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.614502,
      "aei_text": 3.195568,
      "aei_vision": 0.234718,
      "text_ratio": 0.931575,
      "vision_ratio": 0.068425
    },
    "middle": {
      "mdi": 8.880857,
      "aei_text": 2.924276,
      "aei_vision": 0.329279,
      "text_ratio": 0.898794,
      "vision_ratio": 0.101206
    },
    "late": {
      "mdi": 22.298789,
      "aei_text": 3.427928,
      "aei_vision": 0.153727,
      "text_ratio": 0.957079,
      "vision_ratio": 0.042921
    },
    "all": {
      "mdi": 22.298789,
      "aei_text": 3.182591,
      "aei_vision": 0.239241,
      "text_ratio": 0.957079,
      "vision_ratio": 0.042921
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957079,
      0.042921
    ],
    "text_vision_ratio": "0.957079:0.042921"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 416,
    "text_tokens": 0,
    "total_tokens": 416
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.617438,
      "aei_text": 2.980004,
      "aei_vision": 0.309854,
      "text_ratio": 0.905815,
      "vision_ratio": 0.094185
    },
    "middle": {
      "mdi": 11.296024,
      "aei_text": 3.085348,
      "aei_vision": 0.273136,
      "text_ratio": 0.918673,
      "vision_ratio": 0.081327
    },
    "late": {
      "mdi": 10.38649,
      "aei_text": 3.03158,
      "aei_vision": 0.291877,
      "text_ratio": 0.912177,
      "vision_ratio": 0.087823
    },
    "all": {
      "mdi": 10.38649,
      "aei_text": 3.032311,
      "aei_vision": 0.291622,
      "text_ratio": 0.912177,
      "vision_ratio": 0.087823
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.912177,
      0.087823
    ],
    "text_vision_ratio": "0.912177:0.087823"
  }
}
```


## === Rollout Step 73 ===
Step: 72/29790 | 2025-10-22 12:10:36

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 74 ===
Step: 73/29790 | 2025-10-22 12:10:39

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 75 ===
Step: 74/29790 | 2025-10-22 12:10:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.308 | 8.831 | 13.147 | 13.147 |
| MDI Std | 1.643 | 0.049 | 4.653 | 4.653 |
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
      "mdi": 8.665721,
      "aei_text": 2.658844,
      "aei_vision": 0.306823,
      "text_ratio": 0.896542,
      "vision_ratio": 0.103458
    },
    "middle": {
      "mdi": 8.782562,
      "aei_text": 2.666521,
      "aei_vision": 0.303615,
      "text_ratio": 0.897777,
      "vision_ratio": 0.102223
    },
    "late": {
      "mdi": 8.493814,
      "aei_text": 2.64725,
      "aei_vision": 0.311668,
      "text_ratio": 0.894668,
      "vision_ratio": 0.105332
    },
    "all": {
      "mdi": 8.493814,
      "aei_text": 2.657538,
      "aei_vision": 0.307369,
      "text_ratio": 0.894668,
      "vision_ratio": 0.105332
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.894668,
      0.105332
    ],
    "text_vision_ratio": "0.894668:0.105332"
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
      "mdi": 11.951177,
      "aei_text": 2.827021,
      "aei_vision": 0.236547,
      "text_ratio": 0.922787,
      "vision_ratio": 0.077213
    },
    "middle": {
      "mdi": 8.879791,
      "aei_text": 2.672787,
      "aei_vision": 0.300997,
      "text_ratio": 0.898783,
      "vision_ratio": 0.101217
    },
    "late": {
      "mdi": 17.799834,
      "aei_text": 2.99098,
      "aei_vision": 0.168034,
      "text_ratio": 0.946808,
      "vision_ratio": 0.053192
    },
    "all": {
      "mdi": 17.799834,
      "aei_text": 2.830263,
      "aei_vision": 0.235193,
      "text_ratio": 0.946808,
      "vision_ratio": 0.053192
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946808,
      0.053192
    ],
    "text_vision_ratio": "0.946808:0.053192"
  }
}
```


## === Rollout Step 76 ===
Step: 75/29790 | 2025-10-22 12:10:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.272 | 8.115 | 9.593 | 9.593 |
| MDI Std | 3.500 | 0.174 | 2.392 | 2.392 |
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
      "mdi": 14.772146,
      "aei_text": 2.864716,
      "aei_vision": 0.193927,
      "text_ratio": 0.936597,
      "vision_ratio": 0.063403
    },
    "middle": {
      "mdi": 8.288998,
      "aei_text": 2.590394,
      "aei_vision": 0.31251,
      "text_ratio": 0.892346,
      "vision_ratio": 0.107654
    },
    "late": {
      "mdi": 11.985578,
      "aei_text": 2.777289,
      "aei_vision": 0.231719,
      "text_ratio": 0.922991,
      "vision_ratio": 0.077009
    },
    "all": {
      "mdi": 11.985578,
      "aei_text": 2.744133,
      "aei_vision": 0.246052,
      "text_ratio": 0.922991,
      "vision_ratio": 0.077009
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.922991,
      0.077009
    ],
    "text_vision_ratio": "0.922991:0.077009"
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
      "mdi": 7.771155,
      "aei_text": 2.553271,
      "aei_vision": 0.328557,
      "text_ratio": 0.88599,
      "vision_ratio": 0.11401
    },
    "middle": {
      "mdi": 7.94171,
      "aei_text": 2.565911,
      "aei_vision": 0.323093,
      "text_ratio": 0.888165,
      "vision_ratio": 0.111835
    },
    "late": {
      "mdi": 7.201054,
      "aei_text": 2.507728,
      "aei_vision": 0.348245,
      "text_ratio": 0.878064,
      "vision_ratio": 0.121936
    },
    "all": {
      "mdi": 7.201054,
      "aei_text": 2.542303,
      "aei_vision": 0.333298,
      "text_ratio": 0.878064,
      "vision_ratio": 0.121936
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.878064,
      0.121936
    ],
    "text_vision_ratio": "0.878064:0.121936"
  }
}
```


## === Rollout Step 77 ===
Step: 76/29790 | 2025-10-22 12:10:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 78 ===
Step: 77/29790 | 2025-10-22 12:10:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 79 ===
Step: 78/29790 | 2025-10-22 12:10:54

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 172.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 172.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 172,
    "text_tokens": 0,
    "total_tokens": 172
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 172,
    "text_tokens": 0,
    "total_tokens": 172
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 80 ===
Step: 79/29790 | 2025-10-22 12:10:58

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 486.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 486.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 81 ===
Step: 80/29790 | 2025-10-22 12:11:01

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 82 ===
Step: 81/29790 | 2025-10-22 12:11:04

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 83 ===
Step: 82/29790 | 2025-10-22 12:11:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 84 ===
Step: 83/29790 | 2025-10-22 12:11:11

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 85 ===
Step: 84/29790 | 2025-10-22 12:11:14

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 86 ===
Step: 85/29790 | 2025-10-22 12:11:17

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 87 ===
Step: 86/29790 | 2025-10-22 12:11:20

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 88 ===
Step: 87/29790 | 2025-10-22 12:11:24

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 89 ===
Step: 88/29790 | 2025-10-22 12:11:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 218.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 218.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
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
  "overall": {
    "balance_score": 1.0,
    "attention_distribution": [
      0.5,
      0.5
    ],
    "text_vision_ratio": "0.500000:0.500000"
  }
}
```


## === Rollout Step 90 ===
Step: 89/29790 | 2025-10-22 12:11:29

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.476 | 7.736 | 11.888 | 11.888 |
| MDI Std | 3.366 | 0.595 | 3.430 | 3.430 |
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
      "mdi": 14.841628,
      "aei_text": 2.834786,
      "aei_vision": 0.191002,
      "text_ratio": 0.936875,
      "vision_ratio": 0.063125
    },
    "middle": {
      "mdi": 7.141659,
      "aei_text": 2.480305,
      "aei_vision": 0.347301,
      "text_ratio": 0.877175,
      "vision_ratio": 0.122825
    },
    "late": {
      "mdi": 15.318043,
      "aei_text": 2.846521,
      "aei_vision": 0.185828,
      "text_ratio": 0.938718,
      "vision_ratio": 0.061282
    },
    "all": {
      "mdi": 15.318043,
      "aei_text": 2.720537,
      "aei_vision": 0.241377,
      "text_ratio": 0.938718,
      "vision_ratio": 0.061282
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.938718,
      0.061282
    ],
    "text_vision_ratio": "0.938718:0.061282"
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
      "mdi": 8.110387,
      "aei_text": 2.553826,
      "aei_vision": 0.314883,
      "text_ratio": 0.890235,
      "vision_ratio": 0.109765
    },
    "middle": {
      "mdi": 8.33078,
      "aei_text": 2.568677,
      "aei_vision": 0.308336,
      "text_ratio": 0.892828,
      "vision_ratio": 0.107172
    },
    "late": {
      "mdi": 8.457622,
      "aei_text": 2.576947,
      "aei_vision": 0.304689,
      "text_ratio": 0.894265,
      "vision_ratio": 0.105735
    },
    "all": {
      "mdi": 8.457622,
      "aei_text": 2.566483,
      "aei_vision": 0.309303,
      "text_ratio": 0.894265,
      "vision_ratio": 0.105735
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.894265,
      0.105735
    ],
    "text_vision_ratio": "0.894265:0.105735"
  }
}
```


## === Rollout Step 91 ===
Step: 90/29790 | 2025-10-22 12:11:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 22.381 | 13.226 | 22.682 | 22.682 |
| MDI Std | 0.995 | 0.264 | 1.042 | 1.042 |
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
      "mdi": 23.375959,
      "aei_text": 3.255159,
      "aei_vision": 0.139252,
      "text_ratio": 0.958976,
      "vision_ratio": 0.041024
    },
    "middle": {
      "mdi": 13.489541,
      "aei_text": 3.031256,
      "aei_vision": 0.224712,
      "text_ratio": 0.930985,
      "vision_ratio": 0.069015
    },
    "late": {
      "mdi": 23.724139,
      "aei_text": 3.259981,
      "aei_vision": 0.137412,
      "text_ratio": 0.959554,
      "vision_ratio": 0.040446
    },
    "all": {
      "mdi": 23.724139,
      "aei_text": 3.182132,
      "aei_vision": 0.167125,
      "text_ratio": 0.959554,
      "vision_ratio": 0.040446
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959554,
      0.040446
    ],
    "text_vision_ratio": "0.959554:0.040446"
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
      "mdi": 21.38556,
      "aei_text": 3.224908,
      "aei_vision": 0.150798,
      "text_ratio": 0.955328,
      "vision_ratio": 0.044672
    },
    "middle": {
      "mdi": 12.96247,
      "aei_text": 3.011342,
      "aei_vision": 0.232312,
      "text_ratio": 0.928379,
      "vision_ratio": 0.071621
    },
    "late": {
      "mdi": 21.64052,
      "aei_text": 3.22906,
      "aei_vision": 0.149214,
      "text_ratio": 0.955831,
      "vision_ratio": 0.044169
    },
    "all": {
      "mdi": 21.64052,
      "aei_text": 3.155103,
      "aei_vision": 0.177441,
      "text_ratio": 0.955831,
      "vision_ratio": 0.044169
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955831,
      0.044169
    ],
    "text_vision_ratio": "0.955831:0.044169"
  }
}
```


## === Rollout Step 92 ===
Step: 91/29790 | 2025-10-22 12:11:36

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.954 | 11.157 | 16.394 | 16.394 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 324.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 324.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.953848,
      "aei_text": 2.660936,
      "aei_vision": 0.205417,
      "text_ratio": 0.928335,
      "vision_ratio": 0.071665
    },
    "middle": {
      "mdi": 11.156976,
      "aei_text": 2.602693,
      "aei_vision": 0.233279,
      "text_ratio": 0.917743,
      "vision_ratio": 0.082257
    },
    "late": {
      "mdi": 16.394483,
      "aei_text": 2.740859,
      "aei_vision": 0.167182,
      "text_ratio": 0.942511,
      "vision_ratio": 0.057489
    },
    "all": {
      "mdi": 16.394483,
      "aei_text": 2.668163,
      "aei_vision": 0.201959,
      "text_ratio": 0.942511,
      "vision_ratio": 0.057489
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942511,
      0.057489
    ],
    "text_vision_ratio": "0.942511:0.057489"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.953848,
      "aei_text": 2.660936,
      "aei_vision": 0.205417,
      "text_ratio": 0.928335,
      "vision_ratio": 0.071665
    },
    "middle": {
      "mdi": 11.156976,
      "aei_text": 2.602693,
      "aei_vision": 0.233279,
      "text_ratio": 0.917743,
      "vision_ratio": 0.082257
    },
    "late": {
      "mdi": 16.394483,
      "aei_text": 2.740859,
      "aei_vision": 0.167182,
      "text_ratio": 0.942511,
      "vision_ratio": 0.057489
    },
    "all": {
      "mdi": 16.394483,
      "aei_text": 2.668163,
      "aei_vision": 0.201959,
      "text_ratio": 0.942511,
      "vision_ratio": 0.057489
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942511,
      0.057489
    ],
    "text_vision_ratio": "0.942511:0.057489"
  }
}
```


## === Rollout Step 93 ===
Step: 92/29790 | 2025-10-22 12:11:40

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.139 | 6.859 | 24.278 | 24.278 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.138581,
      "aei_text": 3.109907,
      "aei_vision": 0.205429,
      "text_ratio": 0.938037,
      "vision_ratio": 0.061963
    },
    "middle": {
      "mdi": 6.859179,
      "aei_text": 2.635226,
      "aei_vision": 0.38419,
      "text_ratio": 0.87276,
      "vision_ratio": 0.12724
    },
    "late": {
      "mdi": 24.277914,
      "aei_text": 3.295012,
      "aei_vision": 0.135721,
      "text_ratio": 0.96044,
      "vision_ratio": 0.03956
    },
    "all": {
      "mdi": 24.277914,
      "aei_text": 3.013382,
      "aei_vision": 0.24178,
      "text_ratio": 0.96044,
      "vision_ratio": 0.03956
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96044,
      0.03956
    ],
    "text_vision_ratio": "0.960440:0.039560"
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
      "mdi": 15.138581,
      "aei_text": 3.109907,
      "aei_vision": 0.205429,
      "text_ratio": 0.938037,
      "vision_ratio": 0.061963
    },
    "middle": {
      "mdi": 6.859179,
      "aei_text": 2.635226,
      "aei_vision": 0.38419,
      "text_ratio": 0.87276,
      "vision_ratio": 0.12724
    },
    "late": {
      "mdi": 24.277914,
      "aei_text": 3.295012,
      "aei_vision": 0.135721,
      "text_ratio": 0.96044,
      "vision_ratio": 0.03956
    },
    "all": {
      "mdi": 24.277914,
      "aei_text": 3.013382,
      "aei_vision": 0.24178,
      "text_ratio": 0.96044,
      "vision_ratio": 0.03956
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96044,
      0.03956
    ],
    "text_vision_ratio": "0.960440:0.039560"
  }
}
```


## === Rollout Step 94 ===
Step: 93/29790 | 2025-10-22 12:11:43

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.315 | 10.524 | 11.623 | 11.623 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 14.314508,
      "aei_text": 2.780826,
      "aei_vision": 0.194266,
      "text_ratio": 0.934702,
      "vision_ratio": 0.065298
    },
    "middle": {
      "mdi": 10.523508,
      "aei_text": 2.652997,
      "aei_vision": 0.252102,
      "text_ratio": 0.913221,
      "vision_ratio": 0.086779
    },
    "late": {
      "mdi": 11.623288,
      "aei_text": 2.697295,
      "aei_vision": 0.23206,
      "text_ratio": 0.920781,
      "vision_ratio": 0.079219
    },
    "all": {
      "mdi": 11.623288,
      "aei_text": 2.710373,
      "aei_vision": 0.226143,
      "text_ratio": 0.920781,
      "vision_ratio": 0.079219
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.920781,
      0.079219
    ],
    "text_vision_ratio": "0.920781:0.079219"
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
      "mdi": 14.314508,
      "aei_text": 2.780826,
      "aei_vision": 0.194266,
      "text_ratio": 0.934702,
      "vision_ratio": 0.065298
    },
    "middle": {
      "mdi": 10.523508,
      "aei_text": 2.652997,
      "aei_vision": 0.252102,
      "text_ratio": 0.913221,
      "vision_ratio": 0.086779
    },
    "late": {
      "mdi": 11.623288,
      "aei_text": 2.697295,
      "aei_vision": 0.23206,
      "text_ratio": 0.920781,
      "vision_ratio": 0.079219
    },
    "all": {
      "mdi": 11.623288,
      "aei_text": 2.710373,
      "aei_vision": 0.226143,
      "text_ratio": 0.920781,
      "vision_ratio": 0.079219
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.920781,
      0.079219
    ],
    "text_vision_ratio": "0.920781:0.079219"
  }
}
```


## === Rollout Step 95 ===
Step: 94/29790 | 2025-10-22 12:11:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.940 | 11.037 | 21.109 | 21.109 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.939628,
      "aei_text": 2.915716,
      "aei_vision": 0.182922,
      "text_ratio": 0.940967,
      "vision_ratio": 0.059033
    },
    "middle": {
      "mdi": 11.03707,
      "aei_text": 2.75859,
      "aei_vision": 0.249939,
      "text_ratio": 0.916923,
      "vision_ratio": 0.083077
    },
    "late": {
      "mdi": 21.108725,
      "aei_text": 3.01024,
      "aei_vision": 0.142606,
      "text_ratio": 0.954769,
      "vision_ratio": 0.045231
    },
    "all": {
      "mdi": 21.108725,
      "aei_text": 2.894849,
      "aei_vision": 0.191822,
      "text_ratio": 0.954769,
      "vision_ratio": 0.045231
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954769,
      0.045231
    ],
    "text_vision_ratio": "0.954769:0.045231"
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
      "mdi": 15.939628,
      "aei_text": 2.915716,
      "aei_vision": 0.182922,
      "text_ratio": 0.940967,
      "vision_ratio": 0.059033
    },
    "middle": {
      "mdi": 11.03707,
      "aei_text": 2.75859,
      "aei_vision": 0.249939,
      "text_ratio": 0.916923,
      "vision_ratio": 0.083077
    },
    "late": {
      "mdi": 21.108725,
      "aei_text": 3.01024,
      "aei_vision": 0.142606,
      "text_ratio": 0.954769,
      "vision_ratio": 0.045231
    },
    "all": {
      "mdi": 21.108725,
      "aei_text": 2.894849,
      "aei_vision": 0.191822,
      "text_ratio": 0.954769,
      "vision_ratio": 0.045231
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954769,
      0.045231
    ],
    "text_vision_ratio": "0.954769:0.045231"
  }
}
```


## === Rollout Step 96 ===
Step: 95/29790 | 2025-10-22 12:11:50

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 22.009 | 13.007 | 21.453 | 21.453 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 22.008992,
      "aei_text": 3.261859,
      "aei_vision": 0.148206,
      "text_ratio": 0.956539,
      "vision_ratio": 0.043461
    },
    "middle": {
      "mdi": 13.007371,
      "aei_text": 3.035682,
      "aei_vision": 0.233382,
      "text_ratio": 0.928609,
      "vision_ratio": 0.071391
    },
    "late": {
      "mdi": 21.45339,
      "aei_text": 3.25279,
      "aei_vision": 0.151621,
      "text_ratio": 0.955463,
      "vision_ratio": 0.044537
    },
    "all": {
      "mdi": 21.45339,
      "aei_text": 3.183444,
      "aei_vision": 0.177736,
      "text_ratio": 0.955463,
      "vision_ratio": 0.044537
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955463,
      0.044537
    ],
    "text_vision_ratio": "0.955463:0.044537"
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
      "mdi": 22.008992,
      "aei_text": 3.261859,
      "aei_vision": 0.148206,
      "text_ratio": 0.956539,
      "vision_ratio": 0.043461
    },
    "middle": {
      "mdi": 13.007371,
      "aei_text": 3.035682,
      "aei_vision": 0.233382,
      "text_ratio": 0.928609,
      "vision_ratio": 0.071391
    },
    "late": {
      "mdi": 21.45339,
      "aei_text": 3.25279,
      "aei_vision": 0.151621,
      "text_ratio": 0.955463,
      "vision_ratio": 0.044537
    },
    "all": {
      "mdi": 21.45339,
      "aei_text": 3.183444,
      "aei_vision": 0.177736,
      "text_ratio": 0.955463,
      "vision_ratio": 0.044537
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955463,
      0.044537
    ],
    "text_vision_ratio": "0.955463:0.044537"
  }
}
```


## === Rollout Step 97 ===
Step: 96/29790 | 2025-10-22 12:11:54

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 26.894 | 19.661 | 17.671 | 17.671 |
| MDI Std | 7.599 | 5.710 | 5.105 | 5.105 |
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
      "mdi": 34.492757,
      "aei_text": 3.335502,
      "aei_vision": 0.096702,
      "text_ratio": 0.971825,
      "vision_ratio": 0.028175
    },
    "middle": {
      "mdi": 25.370647,
      "aei_text": 3.253919,
      "aei_vision": 0.128255,
      "text_ratio": 0.962079,
      "vision_ratio": 0.037921
    },
    "late": {
      "mdi": 22.775571,
      "aei_text": 3.219987,
      "aei_vision": 0.141379,
      "text_ratio": 0.95794,
      "vision_ratio": 0.04206
    },
    "all": {
      "mdi": 22.775571,
      "aei_text": 3.269803,
      "aei_vision": 0.122112,
      "text_ratio": 0.95794,
      "vision_ratio": 0.04206
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95794,
      0.04206
    ],
    "text_vision_ratio": "0.957940:0.042060"
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
      "mdi": 19.295262,
      "aei_text": 3.161845,
      "aei_vision": 0.163866,
      "text_ratio": 0.950727,
      "vision_ratio": 0.049273
    },
    "middle": {
      "mdi": 13.950932,
      "aei_text": 3.024918,
      "aei_vision": 0.216826,
      "text_ratio": 0.933115,
      "vision_ratio": 0.066885
    },
    "late": {
      "mdi": 12.566057,
      "aei_text": 2.973678,
      "aei_vision": 0.236644,
      "text_ratio": 0.926287,
      "vision_ratio": 0.073713
    },
    "all": {
      "mdi": 12.566057,
      "aei_text": 3.053481,
      "aei_vision": 0.205779,
      "text_ratio": 0.926287,
      "vision_ratio": 0.073713
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.926287,
      0.073713
    ],
    "text_vision_ratio": "0.926287:0.073713"
  }
}
```


## === Rollout Step 98 ===
Step: 97/29790 | 2025-10-22 12:11:57

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.210 | 13.630 | 19.550 | 19.550 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.20979,
      "aei_text": 3.190201,
      "aei_vision": 0.175192,
      "text_ratio": 0.947943,
      "vision_ratio": 0.052057
    },
    "middle": {
      "mdi": 13.629857,
      "aei_text": 3.059371,
      "aei_vision": 0.224461,
      "text_ratio": 0.931647,
      "vision_ratio": 0.068353
    },
    "late": {
      "mdi": 19.550447,
      "aei_text": 3.218287,
      "aei_vision": 0.164615,
      "text_ratio": 0.951339,
      "vision_ratio": 0.048661
    },
    "all": {
      "mdi": 19.550447,
      "aei_text": 3.155953,
      "aei_vision": 0.188089,
      "text_ratio": 0.951339,
      "vision_ratio": 0.048661
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951339,
      0.048661
    ],
    "text_vision_ratio": "0.951339:0.048661"
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
      "mdi": 18.20979,
      "aei_text": 3.190201,
      "aei_vision": 0.175192,
      "text_ratio": 0.947943,
      "vision_ratio": 0.052057
    },
    "middle": {
      "mdi": 13.629857,
      "aei_text": 3.059371,
      "aei_vision": 0.224461,
      "text_ratio": 0.931647,
      "vision_ratio": 0.068353
    },
    "late": {
      "mdi": 19.550447,
      "aei_text": 3.218287,
      "aei_vision": 0.164615,
      "text_ratio": 0.951339,
      "vision_ratio": 0.048661
    },
    "all": {
      "mdi": 19.550447,
      "aei_text": 3.155953,
      "aei_vision": 0.188089,
      "text_ratio": 0.951339,
      "vision_ratio": 0.048661
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951339,
      0.048661
    ],
    "text_vision_ratio": "0.951339:0.048661"
  }
}
```


## === Rollout Step 99 ===
Step: 98/29790 | 2025-10-22 12:12:01

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.849 | 8.567 | 18.372 | 18.372 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 14.848943,
      "aei_text": 2.888509,
      "aei_vision": 0.194526,
      "text_ratio": 0.936904,
      "vision_ratio": 0.063096
    },
    "middle": {
      "mdi": 8.566588,
      "aei_text": 2.625908,
      "aei_vision": 0.306529,
      "text_ratio": 0.89547,
      "vision_ratio": 0.10453
    },
    "late": {
      "mdi": 18.372147,
      "aei_text": 2.966074,
      "aei_vision": 0.161444,
      "text_ratio": 0.948379,
      "vision_ratio": 0.051621
    },
    "all": {
      "mdi": 18.372147,
      "aei_text": 2.82683,
      "aei_vision": 0.220833,
      "text_ratio": 0.948379,
      "vision_ratio": 0.051621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948379,
      0.051621
    ],
    "text_vision_ratio": "0.948379:0.051621"
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
      "mdi": 14.848943,
      "aei_text": 2.888509,
      "aei_vision": 0.194526,
      "text_ratio": 0.936904,
      "vision_ratio": 0.063096
    },
    "middle": {
      "mdi": 8.566588,
      "aei_text": 2.625908,
      "aei_vision": 0.306529,
      "text_ratio": 0.89547,
      "vision_ratio": 0.10453
    },
    "late": {
      "mdi": 18.372147,
      "aei_text": 2.966074,
      "aei_vision": 0.161444,
      "text_ratio": 0.948379,
      "vision_ratio": 0.051621
    },
    "all": {
      "mdi": 18.372147,
      "aei_text": 2.82683,
      "aei_vision": 0.220833,
      "text_ratio": 0.948379,
      "vision_ratio": 0.051621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948379,
      0.051621
    ],
    "text_vision_ratio": "0.948379:0.051621"
  }
}
```


## === Rollout Step 100 ===
Step: 99/29790 | 2025-10-22 12:12:04

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.635 | 12.987 | 17.318 | 17.318 |
| MDI Std | 1.153 | 0.104 | 0.908 | 0.908 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 19.481856,
      "aei_text": 2.779677,
      "aei_vision": 0.14268,
      "text_ratio": 0.951176,
      "vision_ratio": 0.048824
    },
    "middle": {
      "mdi": 12.882525,
      "aei_text": 2.649007,
      "aei_vision": 0.205628,
      "text_ratio": 0.927967,
      "vision_ratio": 0.072033
    },
    "late": {
      "mdi": 16.410733,
      "aei_text": 2.730473,
      "aei_vision": 0.166383,
      "text_ratio": 0.942564,
      "vision_ratio": 0.057436
    },
    "all": {
      "mdi": 16.410733,
      "aei_text": 2.719719,
      "aei_vision": 0.171564,
      "text_ratio": 0.942564,
      "vision_ratio": 0.057436
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942564,
      0.057436
    ],
    "text_vision_ratio": "0.942564:0.057436"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 21.787342,
      "aei_text": 2.808293,
      "aei_vision": 0.128896,
      "text_ratio": 0.956116,
      "vision_ratio": 0.043884
    },
    "middle": {
      "mdi": 13.090813,
      "aei_text": 2.654869,
      "aei_vision": 0.202804,
      "text_ratio": 0.929032,
      "vision_ratio": 0.070968
    },
    "late": {
      "mdi": 18.22626,
      "aei_text": 2.76136,
      "aei_vision": 0.151504,
      "text_ratio": 0.947988,
      "vision_ratio": 0.052012
    },
    "all": {
      "mdi": 18.22626,
      "aei_text": 2.741507,
      "aei_vision": 0.161068,
      "text_ratio": 0.947988,
      "vision_ratio": 0.052012
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947988,
      0.052012
    ],
    "text_vision_ratio": "0.947988:0.052012"
  }
}
```


## === Rollout Step 101 ===
Step: 100/29790 | 2025-10-22 12:12:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 23.336 | 14.680 | 21.190 | 21.190 |
| MDI Std | 0.041 | 0.284 | 0.365 | 0.365 |
| Vision Tokens | 486.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 486.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.376913,
      "aei_text": 3.601996,
      "aei_vision": 0.154083,
      "text_ratio": 0.958978,
      "vision_ratio": 0.041022
    },
    "middle": {
      "mdi": 14.396015,
      "aei_text": 3.358376,
      "aei_vision": 0.233285,
      "text_ratio": 0.935048,
      "vision_ratio": 0.064952
    },
    "late": {
      "mdi": 20.825146,
      "aei_text": 3.551395,
      "aei_vision": 0.170534,
      "text_ratio": 0.954181,
      "vision_ratio": 0.045819
    },
    "all": {
      "mdi": 20.825146,
      "aei_text": 3.503923,
      "aei_vision": 0.185968,
      "text_ratio": 0.954181,
      "vision_ratio": 0.045819
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954181,
      0.045819
    ],
    "text_vision_ratio": "0.954181:0.045819"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.294236,
      "aei_text": 3.60051,
      "aei_vision": 0.154567,
      "text_ratio": 0.958838,
      "vision_ratio": 0.041162
    },
    "middle": {
      "mdi": 14.964296,
      "aei_text": 3.38098,
      "aei_vision": 0.225936,
      "text_ratio": 0.93736,
      "vision_ratio": 0.06264
    },
    "late": {
      "mdi": 21.554712,
      "aei_text": 3.566933,
      "aei_vision": 0.165483,
      "text_ratio": 0.955663,
      "vision_ratio": 0.044337
    },
    "all": {
      "mdi": 21.554712,
      "aei_text": 3.516141,
      "aei_vision": 0.181995,
      "text_ratio": 0.955663,
      "vision_ratio": 0.044337
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955663,
      0.044337
    ],
    "text_vision_ratio": "0.955663:0.044337"
  }
}
```


## === Rollout Step 102 ===
Step: 101/29790 | 2025-10-22 12:12:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.338 | 8.540 | 16.104 | 16.104 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.337887,
      "aei_text": 2.992356,
      "aei_vision": 0.22435,
      "text_ratio": 0.930255,
      "vision_ratio": 0.069745
    },
    "middle": {
      "mdi": 8.539553,
      "aei_text": 2.743427,
      "aei_vision": 0.321261,
      "text_ratio": 0.895173,
      "vision_ratio": 0.104827
    },
    "late": {
      "mdi": 16.104136,
      "aei_text": 3.077727,
      "aei_vision": 0.191114,
      "text_ratio": 0.941535,
      "vision_ratio": 0.058465
    },
    "all": {
      "mdi": 16.104136,
      "aei_text": 2.937836,
      "aei_vision": 0.245575,
      "text_ratio": 0.941535,
      "vision_ratio": 0.058465
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941535,
      0.058465
    ],
    "text_vision_ratio": "0.941535:0.058465"
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
      "mdi": 13.337887,
      "aei_text": 2.992356,
      "aei_vision": 0.22435,
      "text_ratio": 0.930255,
      "vision_ratio": 0.069745
    },
    "middle": {
      "mdi": 8.539553,
      "aei_text": 2.743427,
      "aei_vision": 0.321261,
      "text_ratio": 0.895173,
      "vision_ratio": 0.104827
    },
    "late": {
      "mdi": 16.104136,
      "aei_text": 3.077727,
      "aei_vision": 0.191114,
      "text_ratio": 0.941535,
      "vision_ratio": 0.058465
    },
    "all": {
      "mdi": 16.104136,
      "aei_text": 2.937836,
      "aei_vision": 0.245575,
      "text_ratio": 0.941535,
      "vision_ratio": 0.058465
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941535,
      0.058465
    ],
    "text_vision_ratio": "0.941535:0.058465"
  }
}
```


## === Rollout Step 103 ===
Step: 102/29790 | 2025-10-22 12:12:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 24.682 | 19.715 | 25.353 | 25.353 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 24.682403,
      "aei_text": 3.206136,
      "aei_vision": 0.129896,
      "text_ratio": 0.961063,
      "vision_ratio": 0.038937
    },
    "middle": {
      "mdi": 19.715045,
      "aei_text": 3.13261,
      "aei_vision": 0.158894,
      "text_ratio": 0.951726,
      "vision_ratio": 0.048274
    },
    "late": {
      "mdi": 25.353044,
      "aei_text": 3.214056,
      "aei_vision": 0.126772,
      "text_ratio": 0.962054,
      "vision_ratio": 0.037946
    },
    "all": {
      "mdi": 25.353044,
      "aei_text": 3.184267,
      "aei_vision": 0.138521,
      "text_ratio": 0.962054,
      "vision_ratio": 0.037946
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962054,
      0.037946
    ],
    "text_vision_ratio": "0.962054:0.037946"
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
      "mdi": 24.682403,
      "aei_text": 3.206136,
      "aei_vision": 0.129896,
      "text_ratio": 0.961063,
      "vision_ratio": 0.038937
    },
    "middle": {
      "mdi": 19.715045,
      "aei_text": 3.13261,
      "aei_vision": 0.158894,
      "text_ratio": 0.951726,
      "vision_ratio": 0.048274
    },
    "late": {
      "mdi": 25.353044,
      "aei_text": 3.214056,
      "aei_vision": 0.126772,
      "text_ratio": 0.962054,
      "vision_ratio": 0.037946
    },
    "all": {
      "mdi": 25.353044,
      "aei_text": 3.184267,
      "aei_vision": 0.138521,
      "text_ratio": 0.962054,
      "vision_ratio": 0.037946
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962054,
      0.037946
    ],
    "text_vision_ratio": "0.962054:0.037946"
  }
}
```


## === Rollout Step 104 ===
Step: 103/29790 | 2025-10-22 12:12:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.921 | 14.026 | 20.368 | 20.368 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.921114,
      "aei_text": 2.900861,
      "aei_vision": 0.161868,
      "text_ratio": 0.947149,
      "vision_ratio": 0.052851
    },
    "middle": {
      "mdi": 14.025826,
      "aei_text": 2.813097,
      "aei_vision": 0.200565,
      "text_ratio": 0.933448,
      "vision_ratio": 0.066552
    },
    "late": {
      "mdi": 20.367866,
      "aei_text": 2.940543,
      "aei_vision": 0.144372,
      "text_ratio": 0.953201,
      "vision_ratio": 0.046799
    },
    "all": {
      "mdi": 20.367866,
      "aei_text": 2.884833,
      "aei_vision": 0.168935,
      "text_ratio": 0.953201,
      "vision_ratio": 0.046799
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953201,
      0.046799
    ],
    "text_vision_ratio": "0.953201:0.046799"
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
      "mdi": 17.921114,
      "aei_text": 2.900861,
      "aei_vision": 0.161868,
      "text_ratio": 0.947149,
      "vision_ratio": 0.052851
    },
    "middle": {
      "mdi": 14.025826,
      "aei_text": 2.813097,
      "aei_vision": 0.200565,
      "text_ratio": 0.933448,
      "vision_ratio": 0.066552
    },
    "late": {
      "mdi": 20.367866,
      "aei_text": 2.940543,
      "aei_vision": 0.144372,
      "text_ratio": 0.953201,
      "vision_ratio": 0.046799
    },
    "all": {
      "mdi": 20.367866,
      "aei_text": 2.884833,
      "aei_vision": 0.168935,
      "text_ratio": 0.953201,
      "vision_ratio": 0.046799
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953201,
      0.046799
    ],
    "text_vision_ratio": "0.953201:0.046799"
  }
}
```


## === Rollout Step 105 ===
Step: 104/29790 | 2025-10-22 12:12:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.140 | 9.772 | 16.167 | 16.167 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 16.140032,
      "aei_text": 2.833813,
      "aei_vision": 0.175577,
      "text_ratio": 0.941657,
      "vision_ratio": 0.058343
    },
    "middle": {
      "mdi": 9.772471,
      "aei_text": 2.626523,
      "aei_vision": 0.268768,
      "text_ratio": 0.907171,
      "vision_ratio": 0.092829
    },
    "late": {
      "mdi": 16.167015,
      "aei_text": 2.834386,
      "aei_vision": 0.175319,
      "text_ratio": 0.941749,
      "vision_ratio": 0.058251
    },
    "all": {
      "mdi": 16.167015,
      "aei_text": 2.764908,
      "aei_vision": 0.206554,
      "text_ratio": 0.941749,
      "vision_ratio": 0.058251
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941749,
      0.058251
    ],
    "text_vision_ratio": "0.941749:0.058251"
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
      "mdi": 16.140032,
      "aei_text": 2.833813,
      "aei_vision": 0.175577,
      "text_ratio": 0.941657,
      "vision_ratio": 0.058343
    },
    "middle": {
      "mdi": 9.772471,
      "aei_text": 2.626523,
      "aei_vision": 0.268768,
      "text_ratio": 0.907171,
      "vision_ratio": 0.092829
    },
    "late": {
      "mdi": 16.167015,
      "aei_text": 2.834386,
      "aei_vision": 0.175319,
      "text_ratio": 0.941749,
      "vision_ratio": 0.058251
    },
    "all": {
      "mdi": 16.167015,
      "aei_text": 2.764908,
      "aei_vision": 0.206554,
      "text_ratio": 0.941749,
      "vision_ratio": 0.058251
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941749,
      0.058251
    ],
    "text_vision_ratio": "0.941749:0.058251"
  }
}
```


## === Rollout Step 106 ===
Step: 105/29790 | 2025-10-22 12:12:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 33.878 | 39.112 | 29.666 | 29.666 |
| MDI Std | 0.589 | 0.001 | 0.600 | 0.600 |
| Vision Tokens | 439.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 439.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 439,
    "text_tokens": 0,
    "total_tokens": 439
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.289486,
      "aei_text": 3.531776,
      "aei_vision": 0.106093,
      "text_ratio": 0.970837,
      "vision_ratio": 0.029163
    },
    "middle": {
      "mdi": 39.110927,
      "aei_text": 3.573481,
      "aei_vision": 0.091368,
      "text_ratio": 0.975069,
      "vision_ratio": 0.024931
    },
    "late": {
      "mdi": 30.265281,
      "aei_text": 3.50432,
      "aei_vision": 0.115787,
      "text_ratio": 0.968016,
      "vision_ratio": 0.031984
    },
    "all": {
      "mdi": 30.265281,
      "aei_text": 3.536526,
      "aei_vision": 0.104416,
      "text_ratio": 0.968016,
      "vision_ratio": 0.031984
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968016,
      0.031984
    ],
    "text_vision_ratio": "0.968016:0.031984"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 439,
    "text_tokens": 0,
    "total_tokens": 439
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.467163,
      "aei_text": 3.541263,
      "aei_vision": 0.102743,
      "text_ratio": 0.971805,
      "vision_ratio": 0.028195
    },
    "middle": {
      "mdi": 39.113687,
      "aei_text": 3.573498,
      "aei_vision": 0.091362,
      "text_ratio": 0.975071,
      "vision_ratio": 0.024929
    },
    "late": {
      "mdi": 29.066151,
      "aei_text": 3.491992,
      "aei_vision": 0.120139,
      "text_ratio": 0.96674,
      "vision_ratio": 0.03326
    },
    "all": {
      "mdi": 29.066151,
      "aei_text": 3.535584,
      "aei_vision": 0.104748,
      "text_ratio": 0.96674,
      "vision_ratio": 0.03326
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96674,
      0.03326
    ],
    "text_vision_ratio": "0.966740:0.033260"
  }
}
```


## === Rollout Step 107 ===
Step: 106/29790 | 2025-10-22 12:12:30

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.720 | 9.842 | 22.104 | 22.104 |
| MDI Std | 0.423 | 0.646 | 1.488 | 1.488 |
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
      "mdi": 16.296918,
      "aei_text": 3.118629,
      "aei_vision": 0.191363,
      "text_ratio": 0.942186,
      "vision_ratio": 0.057814
    },
    "middle": {
      "mdi": 9.196188,
      "aei_text": 2.817338,
      "aei_vision": 0.306359,
      "text_ratio": 0.901924,
      "vision_ratio": 0.098076
    },
    "late": {
      "mdi": 20.616118,
      "aei_text": 3.211825,
      "aei_vision": 0.155792,
      "text_ratio": 0.953738,
      "vision_ratio": 0.046262
    },
    "all": {
      "mdi": 20.616118,
      "aei_text": 3.049264,
      "aei_vision": 0.217838,
      "text_ratio": 0.953738,
      "vision_ratio": 0.046262
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953738,
      0.046262
    ],
    "text_vision_ratio": "0.953738:0.046262"
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
      "mdi": 17.143861,
      "aei_text": 3.140114,
      "aei_vision": 0.183163,
      "text_ratio": 0.944885,
      "vision_ratio": 0.055115
    },
    "middle": {
      "mdi": 10.488008,
      "aei_text": 2.896442,
      "aei_vision": 0.276167,
      "text_ratio": 0.912953,
      "vision_ratio": 0.087047
    },
    "late": {
      "mdi": 23.592111,
      "aei_text": 3.258167,
      "aei_vision": 0.138104,
      "text_ratio": 0.959337,
      "vision_ratio": 0.040663
    },
    "all": {
      "mdi": 23.592111,
      "aei_text": 3.098241,
      "aei_vision": 0.199145,
      "text_ratio": 0.959337,
      "vision_ratio": 0.040663
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959337,
      0.040663
    ],
    "text_vision_ratio": "0.959337:0.040663"
  }
}
```


## === Rollout Step 108 ===
Step: 107/29790 | 2025-10-22 12:12:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.198 | 11.514 | 16.616 | 16.616 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 16.197717,
      "aei_text": 3.068505,
      "aei_vision": 0.189441,
      "text_ratio": 0.941853,
      "vision_ratio": 0.058147
    },
    "middle": {
      "mdi": 11.51393,
      "aei_text": 2.907524,
      "aei_vision": 0.252522,
      "text_ratio": 0.920089,
      "vision_ratio": 0.079911
    },
    "late": {
      "mdi": 16.615954,
      "aei_text": 3.079054,
      "aei_vision": 0.185307,
      "text_ratio": 0.943233,
      "vision_ratio": 0.056767
    },
    "all": {
      "mdi": 16.615954,
      "aei_text": 3.018361,
      "aei_vision": 0.20909,
      "text_ratio": 0.943233,
      "vision_ratio": 0.056767
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943233,
      0.056767
    ],
    "text_vision_ratio": "0.943233:0.056767"
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
      "mdi": 16.197717,
      "aei_text": 3.068505,
      "aei_vision": 0.189441,
      "text_ratio": 0.941853,
      "vision_ratio": 0.058147
    },
    "middle": {
      "mdi": 11.51393,
      "aei_text": 2.907524,
      "aei_vision": 0.252522,
      "text_ratio": 0.920089,
      "vision_ratio": 0.079911
    },
    "late": {
      "mdi": 16.615954,
      "aei_text": 3.079054,
      "aei_vision": 0.185307,
      "text_ratio": 0.943233,
      "vision_ratio": 0.056767
    },
    "all": {
      "mdi": 16.615954,
      "aei_text": 3.018361,
      "aei_vision": 0.20909,
      "text_ratio": 0.943233,
      "vision_ratio": 0.056767
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943233,
      0.056767
    ],
    "text_vision_ratio": "0.943233:0.056767"
  }
}
```


## === Rollout Step 109 ===
Step: 108/29790 | 2025-10-22 12:12:37

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.572 | 14.506 | 18.401 | 18.401 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.572349,
      "aei_text": 3.185228,
      "aei_vision": 0.171504,
      "text_ratio": 0.948908,
      "vision_ratio": 0.051092
    },
    "middle": {
      "mdi": 14.506444,
      "aei_text": 3.077947,
      "aei_vision": 0.212178,
      "text_ratio": 0.935511,
      "vision_ratio": 0.064489
    },
    "late": {
      "mdi": 18.40054,
      "aei_text": 3.181534,
      "aei_vision": 0.172904,
      "text_ratio": 0.948455,
      "vision_ratio": 0.051545
    },
    "all": {
      "mdi": 18.40054,
      "aei_text": 3.148236,
      "aei_vision": 0.185529,
      "text_ratio": 0.948455,
      "vision_ratio": 0.051545
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948455,
      0.051545
    ],
    "text_vision_ratio": "0.948455:0.051545"
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
      "mdi": 18.572349,
      "aei_text": 3.185228,
      "aei_vision": 0.171504,
      "text_ratio": 0.948908,
      "vision_ratio": 0.051092
    },
    "middle": {
      "mdi": 14.506444,
      "aei_text": 3.077947,
      "aei_vision": 0.212178,
      "text_ratio": 0.935511,
      "vision_ratio": 0.064489
    },
    "late": {
      "mdi": 18.40054,
      "aei_text": 3.181534,
      "aei_vision": 0.172904,
      "text_ratio": 0.948455,
      "vision_ratio": 0.051545
    },
    "all": {
      "mdi": 18.40054,
      "aei_text": 3.148236,
      "aei_vision": 0.185529,
      "text_ratio": 0.948455,
      "vision_ratio": 0.051545
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948455,
      0.051545
    ],
    "text_vision_ratio": "0.948455:0.051545"
  }
}
```


## === Rollout Step 110 ===
Step: 109/29790 | 2025-10-22 12:12:41

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.125 | 10.473 | 16.585 | 16.585 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 14.1252,
      "aei_text": 2.83654,
      "aei_vision": 0.200814,
      "text_ratio": 0.933885,
      "vision_ratio": 0.066115
    },
    "middle": {
      "mdi": 10.473039,
      "aei_text": 2.704571,
      "aei_vision": 0.258241,
      "text_ratio": 0.912839,
      "vision_ratio": 0.087161
    },
    "late": {
      "mdi": 16.584514,
      "aei_text": 2.896643,
      "aei_vision": 0.17466,
      "text_ratio": 0.943132,
      "vision_ratio": 0.056868
    },
    "all": {
      "mdi": 16.584514,
      "aei_text": 2.812585,
      "aei_vision": 0.211238,
      "text_ratio": 0.943132,
      "vision_ratio": 0.056868
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943132,
      0.056868
    ],
    "text_vision_ratio": "0.943132:0.056868"
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
      "mdi": 14.1252,
      "aei_text": 2.83654,
      "aei_vision": 0.200814,
      "text_ratio": 0.933885,
      "vision_ratio": 0.066115
    },
    "middle": {
      "mdi": 10.473039,
      "aei_text": 2.704571,
      "aei_vision": 0.258241,
      "text_ratio": 0.912839,
      "vision_ratio": 0.087161
    },
    "late": {
      "mdi": 16.584514,
      "aei_text": 2.896643,
      "aei_vision": 0.17466,
      "text_ratio": 0.943132,
      "vision_ratio": 0.056868
    },
    "all": {
      "mdi": 16.584514,
      "aei_text": 2.812585,
      "aei_vision": 0.211238,
      "text_ratio": 0.943132,
      "vision_ratio": 0.056868
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943132,
      0.056868
    ],
    "text_vision_ratio": "0.943132:0.056868"
  }
}
```


## === Rollout Step 111 ===
Step: 110/29790 | 2025-10-22 12:12:44

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 23.902 | 13.303 | 17.755 | 17.755 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 23.901597,
      "aei_text": 3.071309,
      "aei_vision": 0.128498,
      "text_ratio": 0.959842,
      "vision_ratio": 0.040158
    },
    "middle": {
      "mdi": 13.303477,
      "aei_text": 2.86489,
      "aei_vision": 0.215349,
      "text_ratio": 0.930087,
      "vision_ratio": 0.069913
    },
    "late": {
      "mdi": 17.755331,
      "aei_text": 2.978071,
      "aei_vision": 0.167728,
      "text_ratio": 0.946682,
      "vision_ratio": 0.053318
    },
    "all": {
      "mdi": 17.755331,
      "aei_text": 2.971423,
      "aei_vision": 0.170525,
      "text_ratio": 0.946682,
      "vision_ratio": 0.053318
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946682,
      0.053318
    ],
    "text_vision_ratio": "0.946682:0.053318"
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
      "mdi": 23.901597,
      "aei_text": 3.071309,
      "aei_vision": 0.128498,
      "text_ratio": 0.959842,
      "vision_ratio": 0.040158
    },
    "middle": {
      "mdi": 13.303477,
      "aei_text": 2.86489,
      "aei_vision": 0.215349,
      "text_ratio": 0.930087,
      "vision_ratio": 0.069913
    },
    "late": {
      "mdi": 17.755331,
      "aei_text": 2.978071,
      "aei_vision": 0.167728,
      "text_ratio": 0.946682,
      "vision_ratio": 0.053318
    },
    "all": {
      "mdi": 17.755331,
      "aei_text": 2.971423,
      "aei_vision": 0.170525,
      "text_ratio": 0.946682,
      "vision_ratio": 0.053318
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946682,
      0.053318
    ],
    "text_vision_ratio": "0.946682:0.053318"
  }
}
```


## === Rollout Step 112 ===
Step: 111/29790 | 2025-10-22 12:12:47

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.872 | 6.534 | 17.793 | 17.793 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 12.872154,
      "aei_text": 2.87206,
      "aei_vision": 0.223122,
      "text_ratio": 0.927913,
      "vision_ratio": 0.072087
    },
    "middle": {
      "mdi": 6.534474,
      "aei_text": 2.491084,
      "aei_vision": 0.381222,
      "text_ratio": 0.867277,
      "vision_ratio": 0.132723
    },
    "late": {
      "mdi": 17.793246,
      "aei_text": 3.003025,
      "aei_vision": 0.168773,
      "text_ratio": 0.946789,
      "vision_ratio": 0.053211
    },
    "all": {
      "mdi": 17.793246,
      "aei_text": 2.788723,
      "aei_vision": 0.257706,
      "text_ratio": 0.946789,
      "vision_ratio": 0.053211
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946789,
      0.053211
    ],
    "text_vision_ratio": "0.946789:0.053211"
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
      "mdi": 12.872154,
      "aei_text": 2.87206,
      "aei_vision": 0.223122,
      "text_ratio": 0.927913,
      "vision_ratio": 0.072087
    },
    "middle": {
      "mdi": 6.534474,
      "aei_text": 2.491084,
      "aei_vision": 0.381222,
      "text_ratio": 0.867277,
      "vision_ratio": 0.132723
    },
    "late": {
      "mdi": 17.793246,
      "aei_text": 3.003025,
      "aei_vision": 0.168773,
      "text_ratio": 0.946789,
      "vision_ratio": 0.053211
    },
    "all": {
      "mdi": 17.793246,
      "aei_text": 2.788723,
      "aei_vision": 0.257706,
      "text_ratio": 0.946789,
      "vision_ratio": 0.053211
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946789,
      0.053211
    ],
    "text_vision_ratio": "0.946789:0.053211"
  }
}
```


## === Rollout Step 113 ===
Step: 112/29790 | 2025-10-22 12:12:51

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.368 | 8.054 | 16.923 | 16.923 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 16.367551,
      "aei_text": 2.96028,
      "aei_vision": 0.180863,
      "text_ratio": 0.942421,
      "vision_ratio": 0.057579
    },
    "middle": {
      "mdi": 8.054213,
      "aei_text": 2.615866,
      "aei_vision": 0.324782,
      "text_ratio": 0.889554,
      "vision_ratio": 0.110446
    },
    "late": {
      "mdi": 16.922751,
      "aei_text": 2.972721,
      "aei_vision": 0.175664,
      "text_ratio": 0.944205,
      "vision_ratio": 0.055795
    },
    "all": {
      "mdi": 16.922751,
      "aei_text": 2.849622,
      "aei_vision": 0.227103,
      "text_ratio": 0.944205,
      "vision_ratio": 0.055795
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.944205,
      0.055795
    ],
    "text_vision_ratio": "0.944205:0.055795"
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
      "mdi": 16.367551,
      "aei_text": 2.96028,
      "aei_vision": 0.180863,
      "text_ratio": 0.942421,
      "vision_ratio": 0.057579
    },
    "middle": {
      "mdi": 8.054213,
      "aei_text": 2.615866,
      "aei_vision": 0.324782,
      "text_ratio": 0.889554,
      "vision_ratio": 0.110446
    },
    "late": {
      "mdi": 16.922751,
      "aei_text": 2.972721,
      "aei_vision": 0.175664,
      "text_ratio": 0.944205,
      "vision_ratio": 0.055795
    },
    "all": {
      "mdi": 16.922751,
      "aei_text": 2.849622,
      "aei_vision": 0.227103,
      "text_ratio": 0.944205,
      "vision_ratio": 0.055795
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.944205,
      0.055795
    ],
    "text_vision_ratio": "0.944205:0.055795"
  }
}
```


## === Rollout Step 114 ===
Step: 113/29790 | 2025-10-22 12:12:54

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.689 | 11.367 | 16.026 | 16.026 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 272.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 272.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 272,
    "text_tokens": 0,
    "total_tokens": 272
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.688691,
      "aei_text": 2.515099,
      "aei_vision": 0.142187,
      "text_ratio": 0.946492,
      "vision_ratio": 0.053508
    },
    "middle": {
      "mdi": 11.367466,
      "aei_text": 2.394228,
      "aei_vision": 0.210621,
      "text_ratio": 0.919143,
      "vision_ratio": 0.080857
    },
    "late": {
      "mdi": 16.025758,
      "aei_text": 2.491626,
      "aei_vision": 0.155476,
      "text_ratio": 0.941265,
      "vision_ratio": 0.058735
    },
    "all": {
      "mdi": 16.025758,
      "aei_text": 2.466984,
      "aei_vision": 0.169428,
      "text_ratio": 0.941265,
      "vision_ratio": 0.058735
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941265,
      0.058735
    ],
    "text_vision_ratio": "0.941265:0.058735"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 272,
    "text_tokens": 0,
    "total_tokens": 272
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.688691,
      "aei_text": 2.515099,
      "aei_vision": 0.142187,
      "text_ratio": 0.946492,
      "vision_ratio": 0.053508
    },
    "middle": {
      "mdi": 11.367466,
      "aei_text": 2.394228,
      "aei_vision": 0.210621,
      "text_ratio": 0.919143,
      "vision_ratio": 0.080857
    },
    "late": {
      "mdi": 16.025758,
      "aei_text": 2.491626,
      "aei_vision": 0.155476,
      "text_ratio": 0.941265,
      "vision_ratio": 0.058735
    },
    "all": {
      "mdi": 16.025758,
      "aei_text": 2.466984,
      "aei_vision": 0.169428,
      "text_ratio": 0.941265,
      "vision_ratio": 0.058735
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941265,
      0.058735
    ],
    "text_vision_ratio": "0.941265:0.058735"
  }
}
```


## === Rollout Step 115 ===
Step: 114/29790 | 2025-10-22 12:12:56

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.865 | 6.757 | 13.287 | 13.287 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 218.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 218.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.864708,
      "aei_text": 2.125228,
      "aei_vision": 0.215437,
      "text_ratio": 0.907959,
      "vision_ratio": 0.092041
    },
    "middle": {
      "mdi": 6.756587,
      "aei_text": 2.00798,
      "aei_vision": 0.297188,
      "text_ratio": 0.871077,
      "vision_ratio": 0.128923
    },
    "late": {
      "mdi": 13.286548,
      "aei_text": 2.197051,
      "aei_vision": 0.165359,
      "text_ratio": 0.930004,
      "vision_ratio": 0.069996
    },
    "all": {
      "mdi": 13.286548,
      "aei_text": 2.110086,
      "aei_vision": 0.225995,
      "text_ratio": 0.930004,
      "vision_ratio": 0.069996
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.930004,
      0.069996
    ],
    "text_vision_ratio": "0.930004:0.069996"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 218,
    "text_tokens": 0,
    "total_tokens": 218
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.864708,
      "aei_text": 2.125228,
      "aei_vision": 0.215437,
      "text_ratio": 0.907959,
      "vision_ratio": 0.092041
    },
    "middle": {
      "mdi": 6.756587,
      "aei_text": 2.00798,
      "aei_vision": 0.297188,
      "text_ratio": 0.871077,
      "vision_ratio": 0.128923
    },
    "late": {
      "mdi": 13.286548,
      "aei_text": 2.197051,
      "aei_vision": 0.165359,
      "text_ratio": 0.930004,
      "vision_ratio": 0.069996
    },
    "all": {
      "mdi": 13.286548,
      "aei_text": 2.110086,
      "aei_vision": 0.225995,
      "text_ratio": 0.930004,
      "vision_ratio": 0.069996
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.930004,
      0.069996
    ],
    "text_vision_ratio": "0.930004:0.069996"
  }
}
```


## === Rollout Step 116 ===
Step: 115/29790 | 2025-10-22 12:12:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.778 | 11.064 | 18.020 | 18.020 |
| MDI Std | 0.926 | 0.381 | 0.096 | 0.096 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.703407,
      "aei_text": 2.706338,
      "aei_vision": 0.172341,
      "text_ratio": 0.940132,
      "vision_ratio": 0.059868
    },
    "middle": {
      "mdi": 10.683272,
      "aei_text": 2.566386,
      "aei_vision": 0.240225,
      "text_ratio": 0.914408,
      "vision_ratio": 0.085592
    },
    "late": {
      "mdi": 17.923999,
      "aei_text": 2.745816,
      "aei_vision": 0.153192,
      "text_ratio": 0.947157,
      "vision_ratio": 0.052843
    },
    "all": {
      "mdi": 17.923999,
      "aei_text": 2.672847,
      "aei_vision": 0.188586,
      "text_ratio": 0.947157,
      "vision_ratio": 0.052843
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947157,
      0.052843
    ],
    "text_vision_ratio": "0.947157:0.052843"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.851801,
      "aei_text": 2.664997,
      "aei_vision": 0.192394,
      "text_ratio": 0.932668,
      "vision_ratio": 0.067332
    },
    "middle": {
      "mdi": 11.445351,
      "aei_text": 2.594329,
      "aei_vision": 0.226671,
      "text_ratio": 0.919649,
      "vision_ratio": 0.080351
    },
    "late": {
      "mdi": 18.115587,
      "aei_text": 2.748815,
      "aei_vision": 0.151738,
      "text_ratio": 0.947687,
      "vision_ratio": 0.052313
    },
    "all": {
      "mdi": 18.115587,
      "aei_text": 2.66938,
      "aei_vision": 0.190267,
      "text_ratio": 0.947687,
      "vision_ratio": 0.052313
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947687,
      0.052313
    ],
    "text_vision_ratio": "0.947687:0.052313"
  }
}
```


## === Rollout Step 117 ===
Step: 116/29790 | 2025-10-22 12:13:03

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 21.015 | 11.419 | 18.581 | 18.581 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 21.01464,
      "aei_text": 3.231938,
      "aei_vision": 0.153795,
      "text_ratio": 0.954576,
      "vision_ratio": 0.045424
    },
    "middle": {
      "mdi": 11.418883,
      "aei_text": 2.95502,
      "aei_vision": 0.258784,
      "text_ratio": 0.919477,
      "vision_ratio": 0.080523
    },
    "late": {
      "mdi": 18.580895,
      "aei_text": 3.18541,
      "aei_vision": 0.171435,
      "text_ratio": 0.94893,
      "vision_ratio": 0.05107
    },
    "all": {
      "mdi": 18.580895,
      "aei_text": 3.124123,
      "aei_vision": 0.194671,
      "text_ratio": 0.94893,
      "vision_ratio": 0.05107
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94893,
      0.05107
    ],
    "text_vision_ratio": "0.948930:0.051070"
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
      "mdi": 21.01464,
      "aei_text": 3.231938,
      "aei_vision": 0.153795,
      "text_ratio": 0.954576,
      "vision_ratio": 0.045424
    },
    "middle": {
      "mdi": 11.418883,
      "aei_text": 2.95502,
      "aei_vision": 0.258784,
      "text_ratio": 0.919477,
      "vision_ratio": 0.080523
    },
    "late": {
      "mdi": 18.580895,
      "aei_text": 3.18541,
      "aei_vision": 0.171435,
      "text_ratio": 0.94893,
      "vision_ratio": 0.05107
    },
    "all": {
      "mdi": 18.580895,
      "aei_text": 3.124123,
      "aei_vision": 0.194671,
      "text_ratio": 0.94893,
      "vision_ratio": 0.05107
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94893,
      0.05107
    ],
    "text_vision_ratio": "0.948930:0.051070"
  }
}
```


## === Rollout Step 118 ===
Step: 117/29790 | 2025-10-22 12:13:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 22.327 | 14.705 | 18.049 | 18.049 |
| MDI Std | 1.608 | 0.308 | 0.123 | 0.123 |
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
      "mdi": 20.718331,
      "aei_text": 3.253625,
      "aei_vision": 0.157041,
      "text_ratio": 0.953956,
      "vision_ratio": 0.046044
    },
    "middle": {
      "mdi": 14.396723,
      "aei_text": 3.098144,
      "aei_vision": 0.215198,
      "text_ratio": 0.935051,
      "vision_ratio": 0.064949
    },
    "late": {
      "mdi": 17.926939,
      "aei_text": 3.196736,
      "aei_vision": 0.17832,
      "text_ratio": 0.947165,
      "vision_ratio": 0.052835
    },
    "all": {
      "mdi": 17.926939,
      "aei_text": 3.182835,
      "aei_vision": 0.18352,
      "text_ratio": 0.947165,
      "vision_ratio": 0.052835
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947165,
      0.052835
    ],
    "text_vision_ratio": "0.947165:0.052835"
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
      "mdi": 23.934784,
      "aei_text": 3.304377,
      "aei_vision": 0.138058,
      "text_ratio": 0.959895,
      "vision_ratio": 0.040105
    },
    "middle": {
      "mdi": 15.012493,
      "aei_text": 3.118175,
      "aei_vision": 0.207705,
      "text_ratio": 0.937549,
      "vision_ratio": 0.062451
    },
    "late": {
      "mdi": 18.172048,
      "aei_text": 3.202341,
      "aei_vision": 0.176223,
      "text_ratio": 0.947841,
      "vision_ratio": 0.052159
    },
    "all": {
      "mdi": 18.172048,
      "aei_text": 3.208298,
      "aei_vision": 0.173995,
      "text_ratio": 0.947841,
      "vision_ratio": 0.052159
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947841,
      0.052159
    ],
    "text_vision_ratio": "0.947841:0.052159"
  }
}
```


## === Rollout Step 119 ===
Step: 118/29790 | 2025-10-22 12:13:10

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.660 | 10.454 | 23.773 | 23.773 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.659904,
      "aei_text": 3.115482,
      "aei_vision": 0.176416,
      "text_ratio": 0.946409,
      "vision_ratio": 0.053591
    },
    "middle": {
      "mdi": 10.454352,
      "aei_text": 2.864758,
      "aei_vision": 0.274025,
      "text_ratio": 0.912697,
      "vision_ratio": 0.087303
    },
    "late": {
      "mdi": 23.772849,
      "aei_text": 3.220641,
      "aei_vision": 0.135476,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    },
    "all": {
      "mdi": 23.772849,
      "aei_text": 3.06696,
      "aei_vision": 0.195306,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959633,
      0.040367
    ],
    "text_vision_ratio": "0.959633:0.040367"
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
      "mdi": 17.659904,
      "aei_text": 3.115482,
      "aei_vision": 0.176416,
      "text_ratio": 0.946409,
      "vision_ratio": 0.053591
    },
    "middle": {
      "mdi": 10.454352,
      "aei_text": 2.864758,
      "aei_vision": 0.274025,
      "text_ratio": 0.912697,
      "vision_ratio": 0.087303
    },
    "late": {
      "mdi": 23.772849,
      "aei_text": 3.220641,
      "aei_vision": 0.135476,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    },
    "all": {
      "mdi": 23.772849,
      "aei_text": 3.06696,
      "aei_vision": 0.195306,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959633,
      0.040367
    ],
    "text_vision_ratio": "0.959633:0.040367"
  }
}
```


## === Rollout Step 120 ===
Step: 119/29790 | 2025-10-22 12:13:14

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.140 | 12.567 | 30.918 | 30.918 |
| MDI Std | 0.953 | 0.890 | 1.732 | 1.732 |
| Vision Tokens | 531.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 531.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.092972,
      "aei_text": 3.844662,
      "aei_vision": 0.212495,
      "text_ratio": 0.947625,
      "vision_ratio": 0.052375
    },
    "middle": {
      "mdi": 13.457078,
      "aei_text": 3.636192,
      "aei_vision": 0.270207,
      "text_ratio": 0.93083,
      "vision_ratio": 0.06917
    },
    "late": {
      "mdi": 29.185408,
      "aei_text": 4.104265,
      "aei_vision": 0.140627,
      "text_ratio": 0.966871,
      "vision_ratio": 0.033129
    },
    "all": {
      "mdi": 29.185408,
      "aei_text": 3.861706,
      "aei_vision": 0.207776,
      "text_ratio": 0.966871,
      "vision_ratio": 0.033129
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966871,
      0.033129
    ],
    "text_vision_ratio": "0.966871:0.033129"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
  },
  "attention_metrics": {
    "early": {
      "mdi": 16.186939,
      "aei_text": 3.770768,
      "aei_vision": 0.232951,
      "text_ratio": 0.941816,
      "vision_ratio": 0.058184
    },
    "middle": {
      "mdi": 11.676296,
      "aei_text": 3.522503,
      "aei_vision": 0.30168,
      "text_ratio": 0.921113,
      "vision_ratio": 0.078887
    },
    "late": {
      "mdi": 32.65037,
      "aei_text": 4.152803,
      "aei_vision": 0.12719,
      "text_ratio": 0.970283,
      "vision_ratio": 0.029717
    },
    "all": {
      "mdi": 32.65037,
      "aei_text": 3.815358,
      "aei_vision": 0.220607,
      "text_ratio": 0.970283,
      "vision_ratio": 0.029717
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970283,
      0.029717
    ],
    "text_vision_ratio": "0.970283:0.029717"
  }
}
```


## === Rollout Step 121 ===
Step: 120/29790 | 2025-10-22 12:13:18

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 27.381 | 14.386 | 18.397 | 18.397 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 27.381441,
      "aei_text": 3.017997,
      "aei_vision": 0.110221,
      "text_ratio": 0.964766,
      "vision_ratio": 0.035234
    },
    "middle": {
      "mdi": 14.385984,
      "aei_text": 2.822934,
      "aei_vision": 0.196228,
      "text_ratio": 0.935006,
      "vision_ratio": 0.064994
    },
    "late": {
      "mdi": 18.396905,
      "aei_text": 2.909313,
      "aei_vision": 0.158141,
      "text_ratio": 0.948445,
      "vision_ratio": 0.051555
    },
    "all": {
      "mdi": 18.396905,
      "aei_text": 2.916748,
      "aei_vision": 0.154863,
      "text_ratio": 0.948445,
      "vision_ratio": 0.051555
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948445,
      0.051555
    ],
    "text_vision_ratio": "0.948445:0.051555"
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
      "mdi": 27.381441,
      "aei_text": 3.017997,
      "aei_vision": 0.110221,
      "text_ratio": 0.964766,
      "vision_ratio": 0.035234
    },
    "middle": {
      "mdi": 14.385984,
      "aei_text": 2.822934,
      "aei_vision": 0.196228,
      "text_ratio": 0.935006,
      "vision_ratio": 0.064994
    },
    "late": {
      "mdi": 18.396905,
      "aei_text": 2.909313,
      "aei_vision": 0.158141,
      "text_ratio": 0.948445,
      "vision_ratio": 0.051555
    },
    "all": {
      "mdi": 18.396905,
      "aei_text": 2.916748,
      "aei_vision": 0.154863,
      "text_ratio": 0.948445,
      "vision_ratio": 0.051555
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948445,
      0.051555
    ],
    "text_vision_ratio": "0.948445:0.051555"
  }
}
```


## === Rollout Step 122 ===
Step: 121/29790 | 2025-10-22 12:13:21

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.417 | 12.651 | 17.858 | 17.858 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.416767,
      "aei_text": 3.122056,
      "aei_vision": 0.179256,
      "text_ratio": 0.945702,
      "vision_ratio": 0.054298
    },
    "middle": {
      "mdi": 12.65066,
      "aei_text": 2.977075,
      "aei_vision": 0.23533,
      "text_ratio": 0.926743,
      "vision_ratio": 0.073257
    },
    "late": {
      "mdi": 17.85758,
      "aei_text": 3.13205,
      "aei_vision": 0.17539,
      "text_ratio": 0.946971,
      "vision_ratio": 0.053029
    },
    "all": {
      "mdi": 17.85758,
      "aei_text": 3.07706,
      "aei_vision": 0.196659,
      "text_ratio": 0.946971,
      "vision_ratio": 0.053029
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946971,
      0.053029
    ],
    "text_vision_ratio": "0.946971:0.053029"
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
      "mdi": 17.416767,
      "aei_text": 3.122056,
      "aei_vision": 0.179256,
      "text_ratio": 0.945702,
      "vision_ratio": 0.054298
    },
    "middle": {
      "mdi": 12.65066,
      "aei_text": 2.977075,
      "aei_vision": 0.23533,
      "text_ratio": 0.926743,
      "vision_ratio": 0.073257
    },
    "late": {
      "mdi": 17.85758,
      "aei_text": 3.13205,
      "aei_vision": 0.17539,
      "text_ratio": 0.946971,
      "vision_ratio": 0.053029
    },
    "all": {
      "mdi": 17.85758,
      "aei_text": 3.07706,
      "aei_vision": 0.196659,
      "text_ratio": 0.946971,
      "vision_ratio": 0.053029
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946971,
      0.053029
    ],
    "text_vision_ratio": "0.946971:0.053029"
  }
}
```


## === Rollout Step 123 ===
Step: 122/29790 | 2025-10-22 12:13:25

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.809 | 14.188 | 22.097 | 22.097 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 20.809056,
      "aei_text": 3.215186,
      "aei_vision": 0.154509,
      "text_ratio": 0.954147,
      "vision_ratio": 0.045853
    },
    "middle": {
      "mdi": 14.188188,
      "aei_text": 3.055727,
      "aei_vision": 0.215371,
      "text_ratio": 0.934159,
      "vision_ratio": 0.065841
    },
    "late": {
      "mdi": 22.096634,
      "aei_text": 3.236275,
      "aei_vision": 0.14646,
      "text_ratio": 0.956704,
      "vision_ratio": 0.043296
    },
    "all": {
      "mdi": 22.096634,
      "aei_text": 3.169063,
      "aei_vision": 0.172113,
      "text_ratio": 0.956704,
      "vision_ratio": 0.043296
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956704,
      0.043296
    ],
    "text_vision_ratio": "0.956704:0.043296"
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
      "mdi": 20.809056,
      "aei_text": 3.215186,
      "aei_vision": 0.154509,
      "text_ratio": 0.954147,
      "vision_ratio": 0.045853
    },
    "middle": {
      "mdi": 14.188188,
      "aei_text": 3.055727,
      "aei_vision": 0.215371,
      "text_ratio": 0.934159,
      "vision_ratio": 0.065841
    },
    "late": {
      "mdi": 22.096634,
      "aei_text": 3.236275,
      "aei_vision": 0.14646,
      "text_ratio": 0.956704,
      "vision_ratio": 0.043296
    },
    "all": {
      "mdi": 22.096634,
      "aei_text": 3.169063,
      "aei_vision": 0.172113,
      "text_ratio": 0.956704,
      "vision_ratio": 0.043296
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956704,
      0.043296
    ],
    "text_vision_ratio": "0.956704:0.043296"
  }
}
```


## === Rollout Step 124 ===
Step: 123/29790 | 2025-10-22 12:13:28

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 24.155 | 15.016 | 23.075 | 23.075 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 24.155178,
      "aei_text": 2.941083,
      "aei_vision": 0.121758,
      "text_ratio": 0.960247,
      "vision_ratio": 0.039753
    },
    "middle": {
      "mdi": 15.01634,
      "aei_text": 2.798319,
      "aei_vision": 0.186352,
      "text_ratio": 0.937564,
      "vision_ratio": 0.062436
    },
    "late": {
      "mdi": 23.074608,
      "aei_text": 2.929582,
      "aei_vision": 0.126961,
      "text_ratio": 0.958462,
      "vision_ratio": 0.041538
    },
    "all": {
      "mdi": 23.074608,
      "aei_text": 2.889661,
      "aei_vision": 0.145024,
      "text_ratio": 0.958462,
      "vision_ratio": 0.041538
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958462,
      0.041538
    ],
    "text_vision_ratio": "0.958462:0.041538"
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
      "mdi": 24.155178,
      "aei_text": 2.941083,
      "aei_vision": 0.121758,
      "text_ratio": 0.960247,
      "vision_ratio": 0.039753
    },
    "middle": {
      "mdi": 15.01634,
      "aei_text": 2.798319,
      "aei_vision": 0.186352,
      "text_ratio": 0.937564,
      "vision_ratio": 0.062436
    },
    "late": {
      "mdi": 23.074608,
      "aei_text": 2.929582,
      "aei_vision": 0.126961,
      "text_ratio": 0.958462,
      "vision_ratio": 0.041538
    },
    "all": {
      "mdi": 23.074608,
      "aei_text": 2.889661,
      "aei_vision": 0.145024,
      "text_ratio": 0.958462,
      "vision_ratio": 0.041538
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958462,
      0.041538
    ],
    "text_vision_ratio": "0.958462:0.041538"
  }
}
```


## === Rollout Step 125 ===
Step: 124/29790 | 2025-10-22 12:13:31

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 8.959 | 5.433 | 17.266 | 17.266 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 301.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 301.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.959448,
      "aei_text": 2.480678,
      "aei_vision": 0.276878,
      "text_ratio": 0.899593,
      "vision_ratio": 0.100407
    },
    "middle": {
      "mdi": 5.432553,
      "aei_text": 2.213365,
      "aei_vision": 0.407426,
      "text_ratio": 0.844541,
      "vision_ratio": 0.155459
    },
    "late": {
      "mdi": 17.265907,
      "aei_text": 2.724511,
      "aei_vision": 0.157797,
      "text_ratio": 0.945253,
      "vision_ratio": 0.054747
    },
    "all": {
      "mdi": 17.265907,
      "aei_text": 2.472851,
      "aei_vision": 0.280701,
      "text_ratio": 0.945253,
      "vision_ratio": 0.054747
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945253,
      0.054747
    ],
    "text_vision_ratio": "0.945253:0.054747"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301,
    "text_tokens": 0,
    "total_tokens": 301
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.959448,
      "aei_text": 2.480678,
      "aei_vision": 0.276878,
      "text_ratio": 0.899593,
      "vision_ratio": 0.100407
    },
    "middle": {
      "mdi": 5.432553,
      "aei_text": 2.213365,
      "aei_vision": 0.407426,
      "text_ratio": 0.844541,
      "vision_ratio": 0.155459
    },
    "late": {
      "mdi": 17.265907,
      "aei_text": 2.724511,
      "aei_vision": 0.157797,
      "text_ratio": 0.945253,
      "vision_ratio": 0.054747
    },
    "all": {
      "mdi": 17.265907,
      "aei_text": 2.472851,
      "aei_vision": 0.280701,
      "text_ratio": 0.945253,
      "vision_ratio": 0.054747
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945253,
      0.054747
    ],
    "text_vision_ratio": "0.945253:0.054747"
  }
}
```


## === Rollout Step 126 ===
Step: 125/29790 | 2025-10-22 12:13:35

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.855 | 10.044 | 16.540 | 16.540 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.85512,
      "aei_text": 2.860529,
      "aei_vision": 0.20646,
      "text_ratio": 0.932683,
      "vision_ratio": 0.067317
    },
    "middle": {
      "mdi": 10.04403,
      "aei_text": 2.711617,
      "aei_vision": 0.269973,
      "text_ratio": 0.909453,
      "vision_ratio": 0.090547
    },
    "late": {
      "mdi": 16.539661,
      "aei_text": 2.929343,
      "aei_vision": 0.17711,
      "text_ratio": 0.942986,
      "vision_ratio": 0.057014
    },
    "all": {
      "mdi": 16.539661,
      "aei_text": 2.83383,
      "aei_vision": 0.217848,
      "text_ratio": 0.942986,
      "vision_ratio": 0.057014
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942986,
      0.057014
    ],
    "text_vision_ratio": "0.942986:0.057014"
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
      "mdi": 13.85512,
      "aei_text": 2.860529,
      "aei_vision": 0.20646,
      "text_ratio": 0.932683,
      "vision_ratio": 0.067317
    },
    "middle": {
      "mdi": 10.04403,
      "aei_text": 2.711617,
      "aei_vision": 0.269973,
      "text_ratio": 0.909453,
      "vision_ratio": 0.090547
    },
    "late": {
      "mdi": 16.539661,
      "aei_text": 2.929343,
      "aei_vision": 0.17711,
      "text_ratio": 0.942986,
      "vision_ratio": 0.057014
    },
    "all": {
      "mdi": 16.539661,
      "aei_text": 2.83383,
      "aei_vision": 0.217848,
      "text_ratio": 0.942986,
      "vision_ratio": 0.057014
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942986,
      0.057014
    ],
    "text_vision_ratio": "0.942986:0.057014"
  }
}
```


## === Rollout Step 127 ===
Step: 126/29790 | 2025-10-22 12:13:38

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.927 | 25.120 | 18.947 | 18.947 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 19.926912,
      "aei_text": 3.13641,
      "aei_vision": 0.157396,
      "text_ratio": 0.952215,
      "vision_ratio": 0.047785
    },
    "middle": {
      "mdi": 25.119546,
      "aei_text": 3.211342,
      "aei_vision": 0.127842,
      "text_ratio": 0.961714,
      "vision_ratio": 0.038286
    },
    "late": {
      "mdi": 18.946959,
      "aei_text": 3.118205,
      "aei_vision": 0.164576,
      "text_ratio": 0.949867,
      "vision_ratio": 0.050133
    },
    "all": {
      "mdi": 18.946959,
      "aei_text": 3.155319,
      "aei_vision": 0.149938,
      "text_ratio": 0.949867,
      "vision_ratio": 0.050133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949867,
      0.050133
    ],
    "text_vision_ratio": "0.949867:0.050133"
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
      "mdi": 19.926912,
      "aei_text": 3.13641,
      "aei_vision": 0.157396,
      "text_ratio": 0.952215,
      "vision_ratio": 0.047785
    },
    "middle": {
      "mdi": 25.119546,
      "aei_text": 3.211342,
      "aei_vision": 0.127842,
      "text_ratio": 0.961714,
      "vision_ratio": 0.038286
    },
    "late": {
      "mdi": 18.946959,
      "aei_text": 3.118205,
      "aei_vision": 0.164576,
      "text_ratio": 0.949867,
      "vision_ratio": 0.050133
    },
    "all": {
      "mdi": 18.946959,
      "aei_text": 3.155319,
      "aei_vision": 0.149938,
      "text_ratio": 0.949867,
      "vision_ratio": 0.050133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949867,
      0.050133
    ],
    "text_vision_ratio": "0.949867:0.050133"
  }
}
```


## === Rollout Step 128 ===
Step: 127/29790 | 2025-10-22 12:13:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.218 | 17.529 | 16.418 | 16.418 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.217586,
      "aei_text": 3.136906,
      "aei_vision": 0.206137,
      "text_ratio": 0.938339,
      "vision_ratio": 0.061661
    },
    "middle": {
      "mdi": 17.529082,
      "aei_text": 3.200335,
      "aei_vision": 0.182573,
      "text_ratio": 0.946031,
      "vision_ratio": 0.053969
    },
    "late": {
      "mdi": 16.417902,
      "aei_text": 3.171758,
      "aei_vision": 0.193189,
      "text_ratio": 0.942588,
      "vision_ratio": 0.057412
    },
    "all": {
      "mdi": 16.417902,
      "aei_text": 3.169666,
      "aei_vision": 0.193966,
      "text_ratio": 0.942588,
      "vision_ratio": 0.057412
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942588,
      0.057412
    ],
    "text_vision_ratio": "0.942588:0.057412"
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
      "mdi": 15.217586,
      "aei_text": 3.136906,
      "aei_vision": 0.206137,
      "text_ratio": 0.938339,
      "vision_ratio": 0.061661
    },
    "middle": {
      "mdi": 17.529082,
      "aei_text": 3.200335,
      "aei_vision": 0.182573,
      "text_ratio": 0.946031,
      "vision_ratio": 0.053969
    },
    "late": {
      "mdi": 16.417902,
      "aei_text": 3.171758,
      "aei_vision": 0.193189,
      "text_ratio": 0.942588,
      "vision_ratio": 0.057412
    },
    "all": {
      "mdi": 16.417902,
      "aei_text": 3.169666,
      "aei_vision": 0.193966,
      "text_ratio": 0.942588,
      "vision_ratio": 0.057412
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942588,
      0.057412
    ],
    "text_vision_ratio": "0.942588:0.057412"
  }
}
```


## === Rollout Step 129 ===
Step: 128/29790 | 2025-10-22 12:13:45

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.342 | 13.395 | 22.725 | 22.725 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 14.341849,
      "aei_text": 3.060839,
      "aei_vision": 0.21342,
      "text_ratio": 0.934819,
      "vision_ratio": 0.065181
    },
    "middle": {
      "mdi": 13.395191,
      "aei_text": 3.027787,
      "aei_vision": 0.226035,
      "text_ratio": 0.930532,
      "vision_ratio": 0.069468
    },
    "late": {
      "mdi": 22.725115,
      "aei_text": 3.24579,
      "aei_vision": 0.142828,
      "text_ratio": 0.957851,
      "vision_ratio": 0.042149
    },
    "all": {
      "mdi": 22.725115,
      "aei_text": 3.111472,
      "aei_vision": 0.194095,
      "text_ratio": 0.957851,
      "vision_ratio": 0.042149
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957851,
      0.042149
    ],
    "text_vision_ratio": "0.957851:0.042149"
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
      "mdi": 14.341849,
      "aei_text": 3.060839,
      "aei_vision": 0.21342,
      "text_ratio": 0.934819,
      "vision_ratio": 0.065181
    },
    "middle": {
      "mdi": 13.395191,
      "aei_text": 3.027787,
      "aei_vision": 0.226035,
      "text_ratio": 0.930532,
      "vision_ratio": 0.069468
    },
    "late": {
      "mdi": 22.725115,
      "aei_text": 3.24579,
      "aei_vision": 0.142828,
      "text_ratio": 0.957851,
      "vision_ratio": 0.042149
    },
    "all": {
      "mdi": 22.725115,
      "aei_text": 3.111472,
      "aei_vision": 0.194095,
      "text_ratio": 0.957851,
      "vision_ratio": 0.042149
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957851,
      0.042149
    ],
    "text_vision_ratio": "0.957851:0.042149"
  }
}
```


## === Rollout Step 130 ===
Step: 129/29790 | 2025-10-22 12:13:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.023 | 7.567 | 15.758 | 15.758 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.022677,
      "aei_text": 2.783254,
      "aei_vision": 0.213724,
      "text_ratio": 0.928687,
      "vision_ratio": 0.071313
    },
    "middle": {
      "mdi": 7.566979,
      "aei_text": 2.514368,
      "aei_vision": 0.332282,
      "text_ratio": 0.883273,
      "vision_ratio": 0.116727
    },
    "late": {
      "mdi": 15.757518,
      "aei_text": 2.856796,
      "aei_vision": 0.181297,
      "text_ratio": 0.940325,
      "vision_ratio": 0.059675
    },
    "all": {
      "mdi": 15.757518,
      "aei_text": 2.718139,
      "aei_vision": 0.242434,
      "text_ratio": 0.940325,
      "vision_ratio": 0.059675
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940325,
      0.059675
    ],
    "text_vision_ratio": "0.940325:0.059675"
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
      "mdi": 13.022677,
      "aei_text": 2.783254,
      "aei_vision": 0.213724,
      "text_ratio": 0.928687,
      "vision_ratio": 0.071313
    },
    "middle": {
      "mdi": 7.566979,
      "aei_text": 2.514368,
      "aei_vision": 0.332282,
      "text_ratio": 0.883273,
      "vision_ratio": 0.116727
    },
    "late": {
      "mdi": 15.757518,
      "aei_text": 2.856796,
      "aei_vision": 0.181297,
      "text_ratio": 0.940325,
      "vision_ratio": 0.059675
    },
    "all": {
      "mdi": 15.757518,
      "aei_text": 2.718139,
      "aei_vision": 0.242434,
      "text_ratio": 0.940325,
      "vision_ratio": 0.059675
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940325,
      0.059675
    ],
    "text_vision_ratio": "0.940325:0.059675"
  }
}
```


## === Rollout Step 131 ===
Step: 130/29790 | 2025-10-22 12:13:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.050 | 7.570 | 17.114 | 17.114 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.049886,
      "aei_text": 2.794105,
      "aei_vision": 0.21411,
      "text_ratio": 0.928825,
      "vision_ratio": 0.071175
    },
    "middle": {
      "mdi": 7.570404,
      "aei_text": 2.522286,
      "aei_vision": 0.333177,
      "text_ratio": 0.883319,
      "vision_ratio": 0.116681
    },
    "late": {
      "mdi": 17.114496,
      "aei_text": 2.896528,
      "aei_vision": 0.169244,
      "text_ratio": 0.944796,
      "vision_ratio": 0.055204
    },
    "all": {
      "mdi": 17.114496,
      "aei_text": 2.73764,
      "aei_vision": 0.238844,
      "text_ratio": 0.944796,
      "vision_ratio": 0.055204
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.944796,
      0.055204
    ],
    "text_vision_ratio": "0.944796:0.055204"
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
      "mdi": 13.049886,
      "aei_text": 2.794105,
      "aei_vision": 0.21411,
      "text_ratio": 0.928825,
      "vision_ratio": 0.071175
    },
    "middle": {
      "mdi": 7.570404,
      "aei_text": 2.522286,
      "aei_vision": 0.333177,
      "text_ratio": 0.883319,
      "vision_ratio": 0.116681
    },
    "late": {
      "mdi": 17.114496,
      "aei_text": 2.896528,
      "aei_vision": 0.169244,
      "text_ratio": 0.944796,
      "vision_ratio": 0.055204
    },
    "all": {
      "mdi": 17.114496,
      "aei_text": 2.73764,
      "aei_vision": 0.238844,
      "text_ratio": 0.944796,
      "vision_ratio": 0.055204
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.944796,
      0.055204
    ],
    "text_vision_ratio": "0.944796:0.055204"
  }
}
```


## === Rollout Step 132 ===
Step: 131/29790 | 2025-10-22 12:13:56

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 27.778 | 16.797 | 18.954 | 18.954 |
| MDI Std | 0.603 | 3.138 | 0.388 | 0.388 |
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
      "mdi": 28.381567,
      "aei_text": 3.342663,
      "aei_vision": 0.117776,
      "text_ratio": 0.965965,
      "vision_ratio": 0.034035
    },
    "middle": {
      "mdi": 19.935065,
      "aei_text": 3.225729,
      "aei_vision": 0.161812,
      "text_ratio": 0.952233,
      "vision_ratio": 0.047767
    },
    "late": {
      "mdi": 19.341614,
      "aei_text": 3.214137,
      "aei_vision": 0.166177,
      "text_ratio": 0.95084,
      "vision_ratio": 0.04916
    },
    "all": {
      "mdi": 19.341614,
      "aei_text": 3.260843,
      "aei_vision": 0.148588,
      "text_ratio": 0.95084,
      "vision_ratio": 0.04916
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95084,
      0.04916
    ],
    "text_vision_ratio": "0.950840:0.049160"
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
      "mdi": 27.174657,
      "aei_text": 3.330009,
      "aei_vision": 0.122541,
      "text_ratio": 0.964507,
      "vision_ratio": 0.035493
    },
    "middle": {
      "mdi": 13.658361,
      "aei_text": 3.060412,
      "aei_vision": 0.224069,
      "text_ratio": 0.93178,
      "vision_ratio": 0.06822
    },
    "late": {
      "mdi": 18.565773,
      "aei_text": 3.198005,
      "aei_vision": 0.172253,
      "text_ratio": 0.94889,
      "vision_ratio": 0.05111
    },
    "all": {
      "mdi": 18.565773,
      "aei_text": 3.196142,
      "aei_vision": 0.172954,
      "text_ratio": 0.94889,
      "vision_ratio": 0.05111
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94889,
      0.05111
    ],
    "text_vision_ratio": "0.948890:0.051110"
  }
}
```


## === Rollout Step 133 ===
Step: 132/29790 | 2025-10-22 12:13:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.020 | 8.056 | 15.924 | 15.924 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.019664,
      "aei_text": 2.408279,
      "aei_vision": 0.184972,
      "text_ratio": 0.928672,
      "vision_ratio": 0.071328
    },
    "middle": {
      "mdi": 8.055986,
      "aei_text": 2.246129,
      "aei_vision": 0.278815,
      "text_ratio": 0.889576,
      "vision_ratio": 0.110424
    },
    "late": {
      "mdi": 15.924239,
      "aei_text": 2.46087,
      "aei_vision": 0.154536,
      "text_ratio": 0.940913,
      "vision_ratio": 0.059087
    },
    "all": {
      "mdi": 15.924239,
      "aei_text": 2.371759,
      "aei_vision": 0.206108,
      "text_ratio": 0.940913,
      "vision_ratio": 0.059087
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940913,
      0.059087
    ],
    "text_vision_ratio": "0.940913:0.059087"
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
      "mdi": 13.019664,
      "aei_text": 2.408279,
      "aei_vision": 0.184972,
      "text_ratio": 0.928672,
      "vision_ratio": 0.071328
    },
    "middle": {
      "mdi": 8.055986,
      "aei_text": 2.246129,
      "aei_vision": 0.278815,
      "text_ratio": 0.889576,
      "vision_ratio": 0.110424
    },
    "late": {
      "mdi": 15.924239,
      "aei_text": 2.46087,
      "aei_vision": 0.154536,
      "text_ratio": 0.940913,
      "vision_ratio": 0.059087
    },
    "all": {
      "mdi": 15.924239,
      "aei_text": 2.371759,
      "aei_vision": 0.206108,
      "text_ratio": 0.940913,
      "vision_ratio": 0.059087
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940913,
      0.059087
    ],
    "text_vision_ratio": "0.940913:0.059087"
  }
}
```


## === Rollout Step 134 ===
Step: 133/29790 | 2025-10-22 12:14:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.345 | 15.809 | 15.240 | 15.240 |
| MDI Std | 2.947 | 4.301 | 2.657 | 2.657 |
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
      "mdi": 13.398393,
      "aei_text": 2.784902,
      "aei_vision": 0.207853,
      "text_ratio": 0.930548,
      "vision_ratio": 0.069452
    },
    "middle": {
      "mdi": 11.507856,
      "aei_text": 2.720559,
      "aei_vision": 0.236409,
      "text_ratio": 0.92005,
      "vision_ratio": 0.07995
    },
    "late": {
      "mdi": 12.582564,
      "aei_text": 2.759147,
      "aei_vision": 0.219283,
      "text_ratio": 0.926376,
      "vision_ratio": 0.073624
    },
    "all": {
      "mdi": 12.582564,
      "aei_text": 2.754869,
      "aei_vision": 0.221182,
      "text_ratio": 0.926376,
      "vision_ratio": 0.073624
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.926376,
      0.073624
    ],
    "text_vision_ratio": "0.926376:0.073624"
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
      "mdi": 19.292083,
      "aei_text": 2.913017,
      "aei_vision": 0.150995,
      "text_ratio": 0.95072,
      "vision_ratio": 0.04928
    },
    "middle": {
      "mdi": 20.109363,
      "aei_text": 2.925451,
      "aei_vision": 0.145477,
      "text_ratio": 0.952628,
      "vision_ratio": 0.047372
    },
    "late": {
      "mdi": 17.896614,
      "aei_text": 2.889454,
      "aei_vision": 0.161453,
      "text_ratio": 0.94708,
      "vision_ratio": 0.05292
    },
    "all": {
      "mdi": 17.896614,
      "aei_text": 2.909307,
      "aei_vision": 0.152642,
      "text_ratio": 0.94708,
      "vision_ratio": 0.05292
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94708,
      0.05292
    ],
    "text_vision_ratio": "0.947080:0.052920"
  }
}
```


## === Rollout Step 135 ===
Step: 134/29790 | 2025-10-22 12:14:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.328 | 7.728 | 19.377 | 19.377 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 12.327925,
      "aei_text": 3.018803,
      "aei_vision": 0.244875,
      "text_ratio": 0.92497,
      "vision_ratio": 0.07503
    },
    "middle": {
      "mdi": 7.728305,
      "aei_text": 2.729312,
      "aei_vision": 0.353158,
      "text_ratio": 0.88543,
      "vision_ratio": 0.11457
    },
    "late": {
      "mdi": 19.377249,
      "aei_text": 3.228091,
      "aei_vision": 0.166592,
      "text_ratio": 0.950926,
      "vision_ratio": 0.049074
    },
    "all": {
      "mdi": 19.377249,
      "aei_text": 2.992069,
      "aei_vision": 0.254875,
      "text_ratio": 0.950926,
      "vision_ratio": 0.049074
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950926,
      0.049074
    ],
    "text_vision_ratio": "0.950926:0.049074"
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
      "mdi": 12.327925,
      "aei_text": 3.018803,
      "aei_vision": 0.244875,
      "text_ratio": 0.92497,
      "vision_ratio": 0.07503
    },
    "middle": {
      "mdi": 7.728305,
      "aei_text": 2.729312,
      "aei_vision": 0.353158,
      "text_ratio": 0.88543,
      "vision_ratio": 0.11457
    },
    "late": {
      "mdi": 19.377249,
      "aei_text": 3.228091,
      "aei_vision": 0.166592,
      "text_ratio": 0.950926,
      "vision_ratio": 0.049074
    },
    "all": {
      "mdi": 19.377249,
      "aei_text": 2.992069,
      "aei_vision": 0.254875,
      "text_ratio": 0.950926,
      "vision_ratio": 0.049074
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950926,
      0.049074
    ],
    "text_vision_ratio": "0.950926:0.049074"
  }
}
```


## === Rollout Step 136 ===
Step: 135/29790 | 2025-10-22 12:14:09

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.487 | 19.116 | 19.072 | 19.072 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.487016,
      "aei_text": 2.960862,
      "aei_vision": 0.169318,
      "text_ratio": 0.945908,
      "vision_ratio": 0.054092
    },
    "middle": {
      "mdi": 19.115562,
      "aei_text": 2.99117,
      "aei_vision": 0.156478,
      "text_ratio": 0.950287,
      "vision_ratio": 0.049713
    },
    "late": {
      "mdi": 19.071817,
      "aei_text": 2.990416,
      "aei_vision": 0.156798,
      "text_ratio": 0.950179,
      "vision_ratio": 0.049821
    },
    "all": {
      "mdi": 19.071817,
      "aei_text": 2.980816,
      "aei_vision": 0.160865,
      "text_ratio": 0.950179,
      "vision_ratio": 0.049821
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950179,
      0.049821
    ],
    "text_vision_ratio": "0.950179:0.049821"
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
      "mdi": 17.487016,
      "aei_text": 2.960862,
      "aei_vision": 0.169318,
      "text_ratio": 0.945908,
      "vision_ratio": 0.054092
    },
    "middle": {
      "mdi": 19.115562,
      "aei_text": 2.99117,
      "aei_vision": 0.156478,
      "text_ratio": 0.950287,
      "vision_ratio": 0.049713
    },
    "late": {
      "mdi": 19.071817,
      "aei_text": 2.990416,
      "aei_vision": 0.156798,
      "text_ratio": 0.950179,
      "vision_ratio": 0.049821
    },
    "all": {
      "mdi": 19.071817,
      "aei_text": 2.980816,
      "aei_vision": 0.160865,
      "text_ratio": 0.950179,
      "vision_ratio": 0.049821
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950179,
      0.049821
    ],
    "text_vision_ratio": "0.950179:0.049821"
  }
}
```


## === Rollout Step 137 ===
Step: 136/29790 | 2025-10-22 12:14:13

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.262 | 9.757 | 22.270 | 22.270 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.261823,
      "aei_text": 3.066095,
      "aei_vision": 0.2009,
      "text_ratio": 0.938506,
      "vision_ratio": 0.061494
    },
    "middle": {
      "mdi": 9.757313,
      "aei_text": 2.834445,
      "aei_vision": 0.290494,
      "text_ratio": 0.90704,
      "vision_ratio": 0.09296
    },
    "late": {
      "mdi": 22.270073,
      "aei_text": 3.212553,
      "aei_vision": 0.144254,
      "text_ratio": 0.957026,
      "vision_ratio": 0.042974
    },
    "all": {
      "mdi": 22.270073,
      "aei_text": 3.037698,
      "aei_vision": 0.211883,
      "text_ratio": 0.957026,
      "vision_ratio": 0.042974
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957026,
      0.042974
    ],
    "text_vision_ratio": "0.957026:0.042974"
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
      "mdi": 15.261823,
      "aei_text": 3.066095,
      "aei_vision": 0.2009,
      "text_ratio": 0.938506,
      "vision_ratio": 0.061494
    },
    "middle": {
      "mdi": 9.757313,
      "aei_text": 2.834445,
      "aei_vision": 0.290494,
      "text_ratio": 0.90704,
      "vision_ratio": 0.09296
    },
    "late": {
      "mdi": 22.270073,
      "aei_text": 3.212553,
      "aei_vision": 0.144254,
      "text_ratio": 0.957026,
      "vision_ratio": 0.042974
    },
    "all": {
      "mdi": 22.270073,
      "aei_text": 3.037698,
      "aei_vision": 0.211883,
      "text_ratio": 0.957026,
      "vision_ratio": 0.042974
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957026,
      0.042974
    ],
    "text_vision_ratio": "0.957026:0.042974"
  }
}
```


## === Rollout Step 138 ===
Step: 137/29790 | 2025-10-22 12:14:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.991 | 11.257 | 15.540 | 15.540 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.991473,
      "aei_text": 2.93979,
      "aei_vision": 0.183835,
      "text_ratio": 0.941147,
      "vision_ratio": 0.058853
    },
    "middle": {
      "mdi": 11.257406,
      "aei_text": 2.788081,
      "aei_vision": 0.247666,
      "text_ratio": 0.918417,
      "vision_ratio": 0.081583
    },
    "late": {
      "mdi": 15.539775,
      "aei_text": 2.928774,
      "aei_vision": 0.18847,
      "text_ratio": 0.93954,
      "vision_ratio": 0.06046
    },
    "all": {
      "mdi": 15.539775,
      "aei_text": 2.885548,
      "aei_vision": 0.206657,
      "text_ratio": 0.93954,
      "vision_ratio": 0.06046
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.93954,
      0.06046
    ],
    "text_vision_ratio": "0.939540:0.060460"
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
      "mdi": 15.991473,
      "aei_text": 2.93979,
      "aei_vision": 0.183835,
      "text_ratio": 0.941147,
      "vision_ratio": 0.058853
    },
    "middle": {
      "mdi": 11.257406,
      "aei_text": 2.788081,
      "aei_vision": 0.247666,
      "text_ratio": 0.918417,
      "vision_ratio": 0.081583
    },
    "late": {
      "mdi": 15.539775,
      "aei_text": 2.928774,
      "aei_vision": 0.18847,
      "text_ratio": 0.93954,
      "vision_ratio": 0.06046
    },
    "all": {
      "mdi": 15.539775,
      "aei_text": 2.885548,
      "aei_vision": 0.206657,
      "text_ratio": 0.93954,
      "vision_ratio": 0.06046
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.93954,
      0.06046
    ],
    "text_vision_ratio": "0.939540:0.060460"
  }
}
```


## === Rollout Step 139 ===
Step: 138/29790 | 2025-10-22 12:14:20

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.346 | 13.138 | 20.183 | 20.183 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.34639,
      "aei_text": 3.144982,
      "aei_vision": 0.181305,
      "text_ratio": 0.945493,
      "vision_ratio": 0.054507
    },
    "middle": {
      "mdi": 13.138243,
      "aei_text": 3.018131,
      "aei_vision": 0.229721,
      "text_ratio": 0.92927,
      "vision_ratio": 0.07073
    },
    "late": {
      "mdi": 20.182988,
      "aei_text": 3.204072,
      "aei_vision": 0.158751,
      "text_ratio": 0.952792,
      "vision_ratio": 0.047208
    },
    "all": {
      "mdi": 20.182988,
      "aei_text": 3.122395,
      "aei_vision": 0.189926,
      "text_ratio": 0.952792,
      "vision_ratio": 0.047208
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952792,
      0.047208
    ],
    "text_vision_ratio": "0.952792:0.047208"
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
      "mdi": 17.34639,
      "aei_text": 3.144982,
      "aei_vision": 0.181305,
      "text_ratio": 0.945493,
      "vision_ratio": 0.054507
    },
    "middle": {
      "mdi": 13.138243,
      "aei_text": 3.018131,
      "aei_vision": 0.229721,
      "text_ratio": 0.92927,
      "vision_ratio": 0.07073
    },
    "late": {
      "mdi": 20.182988,
      "aei_text": 3.204072,
      "aei_vision": 0.158751,
      "text_ratio": 0.952792,
      "vision_ratio": 0.047208
    },
    "all": {
      "mdi": 20.182988,
      "aei_text": 3.122395,
      "aei_vision": 0.189926,
      "text_ratio": 0.952792,
      "vision_ratio": 0.047208
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952792,
      0.047208
    ],
    "text_vision_ratio": "0.952792:0.047208"
  }
}
```


## === Rollout Step 140 ===
Step: 139/29790 | 2025-10-22 12:14:23

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.051 | 6.507 | 16.327 | 16.327 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 10.051354,
      "aei_text": 2.711991,
      "aei_vision": 0.269814,
      "text_ratio": 0.909513,
      "vision_ratio": 0.090487
    },
    "middle": {
      "mdi": 6.506973,
      "aei_text": 2.458682,
      "aei_vision": 0.377853,
      "text_ratio": 0.866791,
      "vision_ratio": 0.133209
    },
    "late": {
      "mdi": 16.327426,
      "aei_text": 2.924623,
      "aei_vision": 0.179123,
      "text_ratio": 0.942288,
      "vision_ratio": 0.057712
    },
    "all": {
      "mdi": 16.327426,
      "aei_text": 2.698432,
      "aei_vision": 0.275597,
      "text_ratio": 0.942288,
      "vision_ratio": 0.057712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942288,
      0.057712
    ],
    "text_vision_ratio": "0.942288:0.057712"
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
      "mdi": 10.051354,
      "aei_text": 2.711991,
      "aei_vision": 0.269814,
      "text_ratio": 0.909513,
      "vision_ratio": 0.090487
    },
    "middle": {
      "mdi": 6.506973,
      "aei_text": 2.458682,
      "aei_vision": 0.377853,
      "text_ratio": 0.866791,
      "vision_ratio": 0.133209
    },
    "late": {
      "mdi": 16.327426,
      "aei_text": 2.924623,
      "aei_vision": 0.179123,
      "text_ratio": 0.942288,
      "vision_ratio": 0.057712
    },
    "all": {
      "mdi": 16.327426,
      "aei_text": 2.698432,
      "aei_vision": 0.275597,
      "text_ratio": 0.942288,
      "vision_ratio": 0.057712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942288,
      0.057712
    ],
    "text_vision_ratio": "0.942288:0.057712"
  }
}
```


## === Rollout Step 141 ===
Step: 140/29790 | 2025-10-22 12:14:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.780 | 6.066 | 13.050 | 13.050 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 11.780095,
      "aei_text": 2.262711,
      "aei_vision": 0.192079,
      "text_ratio": 0.921753,
      "vision_ratio": 0.078247
    },
    "middle": {
      "mdi": 6.065782,
      "aei_text": 2.037842,
      "aei_vision": 0.335957,
      "text_ratio": 0.858473,
      "vision_ratio": 0.141527
    },
    "late": {
      "mdi": 13.050283,
      "aei_text": 2.288805,
      "aei_vision": 0.175384,
      "text_ratio": 0.928827,
      "vision_ratio": 0.071173
    },
    "all": {
      "mdi": 13.050283,
      "aei_text": 2.196452,
      "aei_vision": 0.234473,
      "text_ratio": 0.928827,
      "vision_ratio": 0.071173
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928827,
      0.071173
    ],
    "text_vision_ratio": "0.928827:0.071173"
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
      "mdi": 11.780095,
      "aei_text": 2.262711,
      "aei_vision": 0.192079,
      "text_ratio": 0.921753,
      "vision_ratio": 0.078247
    },
    "middle": {
      "mdi": 6.065782,
      "aei_text": 2.037842,
      "aei_vision": 0.335957,
      "text_ratio": 0.858473,
      "vision_ratio": 0.141527
    },
    "late": {
      "mdi": 13.050283,
      "aei_text": 2.288805,
      "aei_vision": 0.175384,
      "text_ratio": 0.928827,
      "vision_ratio": 0.071173
    },
    "all": {
      "mdi": 13.050283,
      "aei_text": 2.196452,
      "aei_vision": 0.234473,
      "text_ratio": 0.928827,
      "vision_ratio": 0.071173
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928827,
      0.071173
    ],
    "text_vision_ratio": "0.928827:0.071173"
  }
}
```


## === Rollout Step 142 ===
Step: 141/29790 | 2025-10-22 12:14:30

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.114 | 19.752 | 24.043 | 24.043 |
| MDI Std | 0.217 | 0.659 | 0.088 | 0.088 |
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
      "mdi": 18.897339,
      "aei_text": 2.99256,
      "aei_vision": 0.158359,
      "text_ratio": 0.949742,
      "vision_ratio": 0.050258
    },
    "middle": {
      "mdi": 19.09376,
      "aei_text": 2.995991,
      "aei_vision": 0.156909,
      "text_ratio": 0.950233,
      "vision_ratio": 0.049767
    },
    "late": {
      "mdi": 24.13024,
      "aei_text": 3.066599,
      "aei_vision": 0.127085,
      "text_ratio": 0.960207,
      "vision_ratio": 0.039793
    },
    "all": {
      "mdi": 24.13024,
      "aei_text": 3.018384,
      "aei_vision": 0.147451,
      "text_ratio": 0.960207,
      "vision_ratio": 0.039793
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960207,
      0.039793
    ],
    "text_vision_ratio": "0.960207:0.039793"
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
      "mdi": 19.331011,
      "aei_text": 3.000053,
      "aei_vision": 0.155194,
      "text_ratio": 0.950814,
      "vision_ratio": 0.049186
    },
    "middle": {
      "mdi": 20.411009,
      "aei_text": 3.017474,
      "aei_vision": 0.147836,
      "text_ratio": 0.953295,
      "vision_ratio": 0.046705
    },
    "late": {
      "mdi": 23.95478,
      "aei_text": 3.064594,
      "aei_vision": 0.127932,
      "text_ratio": 0.959928,
      "vision_ratio": 0.040072
    },
    "all": {
      "mdi": 23.95478,
      "aei_text": 3.027373,
      "aei_vision": 0.143654,
      "text_ratio": 0.959928,
      "vision_ratio": 0.040072
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959928,
      0.040072
    ],
    "text_vision_ratio": "0.959928:0.040072"
  }
}
```


## === Rollout Step 143 ===
Step: 142/29790 | 2025-10-22 12:14:34

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.625 | 6.916 | 18.312 | 18.312 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 12.625039,
      "aei_text": 3.066318,
      "aei_vision": 0.242876,
      "text_ratio": 0.926606,
      "vision_ratio": 0.073394
    },
    "middle": {
      "mdi": 6.916363,
      "aei_text": 2.674013,
      "aei_vision": 0.386621,
      "text_ratio": 0.873679,
      "vision_ratio": 0.126321
    },
    "late": {
      "mdi": 18.312457,
      "aei_text": 3.245482,
      "aei_vision": 0.177228,
      "text_ratio": 0.94822,
      "vision_ratio": 0.05178
    },
    "all": {
      "mdi": 18.312457,
      "aei_text": 2.995271,
      "aei_vision": 0.268908,
      "text_ratio": 0.94822,
      "vision_ratio": 0.05178
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94822,
      0.05178
    ],
    "text_vision_ratio": "0.948220:0.051780"
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
      "mdi": 12.625039,
      "aei_text": 3.066318,
      "aei_vision": 0.242876,
      "text_ratio": 0.926606,
      "vision_ratio": 0.073394
    },
    "middle": {
      "mdi": 6.916363,
      "aei_text": 2.674013,
      "aei_vision": 0.386621,
      "text_ratio": 0.873679,
      "vision_ratio": 0.126321
    },
    "late": {
      "mdi": 18.312457,
      "aei_text": 3.245482,
      "aei_vision": 0.177228,
      "text_ratio": 0.94822,
      "vision_ratio": 0.05178
    },
    "all": {
      "mdi": 18.312457,
      "aei_text": 2.995271,
      "aei_vision": 0.268908,
      "text_ratio": 0.94822,
      "vision_ratio": 0.05178
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94822,
      0.05178
    ],
    "text_vision_ratio": "0.948220:0.051780"
  }
}
```


## === Rollout Step 144 ===
Step: 143/29790 | 2025-10-22 12:14:38

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.994 | 13.728 | 19.902 | 19.902 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.993732,
      "aei_text": 3.181186,
      "aei_vision": 0.167486,
      "text_ratio": 0.949984,
      "vision_ratio": 0.050016
    },
    "middle": {
      "mdi": 13.728059,
      "aei_text": 3.039846,
      "aei_vision": 0.221433,
      "text_ratio": 0.932102,
      "vision_ratio": 0.067898
    },
    "late": {
      "mdi": 19.902324,
      "aei_text": 3.198889,
      "aei_vision": 0.160729,
      "text_ratio": 0.952158,
      "vision_ratio": 0.047842
    },
    "all": {
      "mdi": 19.902324,
      "aei_text": 3.139974,
      "aei_vision": 0.183216,
      "text_ratio": 0.952158,
      "vision_ratio": 0.047842
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952158,
      0.047842
    ],
    "text_vision_ratio": "0.952158:0.047842"
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
      "mdi": 18.993732,
      "aei_text": 3.181186,
      "aei_vision": 0.167486,
      "text_ratio": 0.949984,
      "vision_ratio": 0.050016
    },
    "middle": {
      "mdi": 13.728059,
      "aei_text": 3.039846,
      "aei_vision": 0.221433,
      "text_ratio": 0.932102,
      "vision_ratio": 0.067898
    },
    "late": {
      "mdi": 19.902324,
      "aei_text": 3.198889,
      "aei_vision": 0.160729,
      "text_ratio": 0.952158,
      "vision_ratio": 0.047842
    },
    "all": {
      "mdi": 19.902324,
      "aei_text": 3.139974,
      "aei_vision": 0.183216,
      "text_ratio": 0.952158,
      "vision_ratio": 0.047842
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952158,
      0.047842
    ],
    "text_vision_ratio": "0.952158:0.047842"
  }
}
```


## === Rollout Step 145 ===
Step: 144/29790 | 2025-10-22 12:14:40

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.310 | 9.800 | 10.753 | 10.753 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.309513,
      "aei_text": 2.366567,
      "aei_vision": 0.154581,
      "text_ratio": 0.938686,
      "vision_ratio": 0.061314
    },
    "middle": {
      "mdi": 9.799525,
      "aei_text": 2.245965,
      "aei_vision": 0.229191,
      "text_ratio": 0.907403,
      "vision_ratio": 0.092597
    },
    "late": {
      "mdi": 10.752911,
      "aei_text": 2.27452,
      "aei_vision": 0.211526,
      "text_ratio": 0.914915,
      "vision_ratio": 0.085085
    },
    "all": {
      "mdi": 10.752911,
      "aei_text": 2.295684,
      "aei_vision": 0.198433,
      "text_ratio": 0.914915,
      "vision_ratio": 0.085085
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.914915,
      0.085085
    ],
    "text_vision_ratio": "0.914915:0.085085"
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
      "mdi": 15.309513,
      "aei_text": 2.366567,
      "aei_vision": 0.154581,
      "text_ratio": 0.938686,
      "vision_ratio": 0.061314
    },
    "middle": {
      "mdi": 9.799525,
      "aei_text": 2.245965,
      "aei_vision": 0.229191,
      "text_ratio": 0.907403,
      "vision_ratio": 0.092597
    },
    "late": {
      "mdi": 10.752911,
      "aei_text": 2.27452,
      "aei_vision": 0.211526,
      "text_ratio": 0.914915,
      "vision_ratio": 0.085085
    },
    "all": {
      "mdi": 10.752911,
      "aei_text": 2.295684,
      "aei_vision": 0.198433,
      "text_ratio": 0.914915,
      "vision_ratio": 0.085085
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.914915,
      0.085085
    ],
    "text_vision_ratio": "0.914915:0.085085"
  }
}
```


## === Rollout Step 146 ===
Step: 145/29790 | 2025-10-22 12:14:44

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.951 | 9.959 | 17.917 | 17.917 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.950562,
      "aei_text": 3.210369,
      "aei_vision": 0.178845,
      "text_ratio": 0.947231,
      "vision_ratio": 0.052769
    },
    "middle": {
      "mdi": 9.958542,
      "aei_text": 2.906231,
      "aei_vision": 0.291833,
      "text_ratio": 0.908747,
      "vision_ratio": 0.091253
    },
    "late": {
      "mdi": 17.917389,
      "aei_text": 3.209594,
      "aei_vision": 0.179133,
      "text_ratio": 0.947139,
      "vision_ratio": 0.052861
    },
    "all": {
      "mdi": 17.917389,
      "aei_text": 3.108731,
      "aei_vision": 0.216604,
      "text_ratio": 0.947139,
      "vision_ratio": 0.052861
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947139,
      0.052861
    ],
    "text_vision_ratio": "0.947139:0.052861"
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
      "mdi": 17.950562,
      "aei_text": 3.210369,
      "aei_vision": 0.178845,
      "text_ratio": 0.947231,
      "vision_ratio": 0.052769
    },
    "middle": {
      "mdi": 9.958542,
      "aei_text": 2.906231,
      "aei_vision": 0.291833,
      "text_ratio": 0.908747,
      "vision_ratio": 0.091253
    },
    "late": {
      "mdi": 17.917389,
      "aei_text": 3.209594,
      "aei_vision": 0.179133,
      "text_ratio": 0.947139,
      "vision_ratio": 0.052861
    },
    "all": {
      "mdi": 17.917389,
      "aei_text": 3.108731,
      "aei_vision": 0.216604,
      "text_ratio": 0.947139,
      "vision_ratio": 0.052861
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947139,
      0.052861
    ],
    "text_vision_ratio": "0.947139:0.052861"
  }
}
```


## === Rollout Step 147 ===
Step: 146/29790 | 2025-10-22 12:14:47

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.170 | 9.832 | 13.924 | 13.924 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.169668,
      "aei_text": 3.04046,
      "aei_vision": 0.20043,
      "text_ratio": 0.938156,
      "vision_ratio": 0.061844
    },
    "middle": {
      "mdi": 9.832261,
      "aei_text": 2.820017,
      "aei_vision": 0.286813,
      "text_ratio": 0.907683,
      "vision_ratio": 0.092317
    },
    "late": {
      "mdi": 13.923564,
      "aei_text": 3.001775,
      "aei_vision": 0.21559,
      "text_ratio": 0.932992,
      "vision_ratio": 0.067008
    },
    "all": {
      "mdi": 13.923564,
      "aei_text": 2.954084,
      "aei_vision": 0.234277,
      "text_ratio": 0.932992,
      "vision_ratio": 0.067008
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.932992,
      0.067008
    ],
    "text_vision_ratio": "0.932992:0.067008"
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
      "mdi": 15.169668,
      "aei_text": 3.04046,
      "aei_vision": 0.20043,
      "text_ratio": 0.938156,
      "vision_ratio": 0.061844
    },
    "middle": {
      "mdi": 9.832261,
      "aei_text": 2.820017,
      "aei_vision": 0.286813,
      "text_ratio": 0.907683,
      "vision_ratio": 0.092317
    },
    "late": {
      "mdi": 13.923564,
      "aei_text": 3.001775,
      "aei_vision": 0.21559,
      "text_ratio": 0.932992,
      "vision_ratio": 0.067008
    },
    "all": {
      "mdi": 13.923564,
      "aei_text": 2.954084,
      "aei_vision": 0.234277,
      "text_ratio": 0.932992,
      "vision_ratio": 0.067008
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.932992,
      0.067008
    ],
    "text_vision_ratio": "0.932992:0.067008"
  }
}
```


## === Rollout Step 148 ===
Step: 147/29790 | 2025-10-22 12:14:51

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.435 | 8.003 | 19.268 | 19.268 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 16.434528,
      "aei_text": 3.18507,
      "aei_vision": 0.193804,
      "text_ratio": 0.942643,
      "vision_ratio": 0.057357
    },
    "middle": {
      "mdi": 8.002845,
      "aei_text": 2.77166,
      "aei_vision": 0.346334,
      "text_ratio": 0.888924,
      "vision_ratio": 0.111076
    },
    "late": {
      "mdi": 19.267773,
      "aei_text": 3.252785,
      "aei_vision": 0.16882,
      "text_ratio": 0.950661,
      "vision_ratio": 0.049339
    },
    "all": {
      "mdi": 19.267773,
      "aei_text": 3.069838,
      "aei_vision": 0.236319,
      "text_ratio": 0.950661,
      "vision_ratio": 0.049339
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950661,
      0.049339
    ],
    "text_vision_ratio": "0.950661:0.049339"
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
      "mdi": 16.434528,
      "aei_text": 3.18507,
      "aei_vision": 0.193804,
      "text_ratio": 0.942643,
      "vision_ratio": 0.057357
    },
    "middle": {
      "mdi": 8.002845,
      "aei_text": 2.77166,
      "aei_vision": 0.346334,
      "text_ratio": 0.888924,
      "vision_ratio": 0.111076
    },
    "late": {
      "mdi": 19.267773,
      "aei_text": 3.252785,
      "aei_vision": 0.16882,
      "text_ratio": 0.950661,
      "vision_ratio": 0.049339
    },
    "all": {
      "mdi": 19.267773,
      "aei_text": 3.069838,
      "aei_vision": 0.236319,
      "text_ratio": 0.950661,
      "vision_ratio": 0.049339
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950661,
      0.049339
    ],
    "text_vision_ratio": "0.950661:0.049339"
  }
}
```


## === Rollout Step 149 ===
Step: 148/29790 | 2025-10-22 12:14:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.502 | 17.069 | 19.369 | 19.369 |
| MDI Std | 0.413 | 0.720 | 0.159 | 0.159 |
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
      "mdi": 16.9148,
      "aei_text": 2.914707,
      "aei_vision": 0.172317,
      "text_ratio": 0.94418,
      "vision_ratio": 0.05582
    },
    "middle": {
      "mdi": 17.789337,
      "aei_text": 2.932048,
      "aei_vision": 0.164821,
      "text_ratio": 0.946778,
      "vision_ratio": 0.053222
    },
    "late": {
      "mdi": 19.2101,
      "aei_text": 2.957217,
      "aei_vision": 0.153941,
      "text_ratio": 0.95052,
      "vision_ratio": 0.04948
    },
    "all": {
      "mdi": 19.2101,
      "aei_text": 2.934657,
      "aei_vision": 0.163693,
      "text_ratio": 0.95052,
      "vision_ratio": 0.04948
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95052,
      0.04948
    ],
    "text_vision_ratio": "0.950520:0.049480"
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
      "mdi": 16.088631,
      "aei_text": 2.89681,
      "aei_vision": 0.180053,
      "text_ratio": 0.941482,
      "vision_ratio": 0.058518
    },
    "middle": {
      "mdi": 16.349442,
      "aei_text": 2.902631,
      "aei_vision": 0.177537,
      "text_ratio": 0.942361,
      "vision_ratio": 0.057639
    },
    "late": {
      "mdi": 19.528738,
      "aei_text": 2.962412,
      "aei_vision": 0.151695,
      "text_ratio": 0.951288,
      "vision_ratio": 0.048712
    },
    "all": {
      "mdi": 19.528738,
      "aei_text": 2.920618,
      "aei_vision": 0.169762,
      "text_ratio": 0.951288,
      "vision_ratio": 0.048712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951288,
      0.048712
    ],
    "text_vision_ratio": "0.951288:0.048712"
  }
}
```


## === Rollout Step 150 ===
Step: 149/29790 | 2025-10-22 12:14:58

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 22.939 | 20.202 | 15.433 | 15.433 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 22.939272,
      "aei_text": 3.15852,
      "aei_vision": 0.137691,
      "text_ratio": 0.958228,
      "vision_ratio": 0.041772
    },
    "middle": {
      "mdi": 20.202312,
      "aei_text": 3.116973,
      "aei_vision": 0.154288,
      "text_ratio": 0.952835,
      "vision_ratio": 0.047165
    },
    "late": {
      "mdi": 15.433475,
      "aei_text": 3.014291,
      "aei_vision": 0.195309,
      "text_ratio": 0.939149,
      "vision_ratio": 0.060851
    },
    "all": {
      "mdi": 15.433475,
      "aei_text": 3.096595,
      "aei_vision": 0.162429,
      "text_ratio": 0.939149,
      "vision_ratio": 0.060851
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939149,
      0.060851
    ],
    "text_vision_ratio": "0.939149:0.060851"
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
      "mdi": 22.939272,
      "aei_text": 3.15852,
      "aei_vision": 0.137691,
      "text_ratio": 0.958228,
      "vision_ratio": 0.041772
    },
    "middle": {
      "mdi": 20.202312,
      "aei_text": 3.116973,
      "aei_vision": 0.154288,
      "text_ratio": 0.952835,
      "vision_ratio": 0.047165
    },
    "late": {
      "mdi": 15.433475,
      "aei_text": 3.014291,
      "aei_vision": 0.195309,
      "text_ratio": 0.939149,
      "vision_ratio": 0.060851
    },
    "all": {
      "mdi": 15.433475,
      "aei_text": 3.096595,
      "aei_vision": 0.162429,
      "text_ratio": 0.939149,
      "vision_ratio": 0.060851
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939149,
      0.060851
    ],
    "text_vision_ratio": "0.939149:0.060851"
  }
}
```


## === Rollout Step 151 ===
Step: 150/29790 | 2025-10-22 12:15:01

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 7.992 | 5.737 | 12.176 | 12.176 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 7.992429,
      "aei_text": 2.169628,
      "aei_vision": 0.27146,
      "text_ratio": 0.888795,
      "vision_ratio": 0.111205
    },
    "middle": {
      "mdi": 5.736901,
      "aei_text": 2.035748,
      "aei_vision": 0.354852,
      "text_ratio": 0.851564,
      "vision_ratio": 0.148436
    },
    "late": {
      "mdi": 12.17612,
      "aei_text": 2.301929,
      "aei_vision": 0.189053,
      "text_ratio": 0.924105,
      "vision_ratio": 0.075895
    },
    "all": {
      "mdi": 12.17612,
      "aei_text": 2.169102,
      "aei_vision": 0.271788,
      "text_ratio": 0.924105,
      "vision_ratio": 0.075895
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.924105,
      0.075895
    ],
    "text_vision_ratio": "0.924105:0.075895"
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
      "mdi": 7.992429,
      "aei_text": 2.169628,
      "aei_vision": 0.27146,
      "text_ratio": 0.888795,
      "vision_ratio": 0.111205
    },
    "middle": {
      "mdi": 5.736901,
      "aei_text": 2.035748,
      "aei_vision": 0.354852,
      "text_ratio": 0.851564,
      "vision_ratio": 0.148436
    },
    "late": {
      "mdi": 12.17612,
      "aei_text": 2.301929,
      "aei_vision": 0.189053,
      "text_ratio": 0.924105,
      "vision_ratio": 0.075895
    },
    "all": {
      "mdi": 12.17612,
      "aei_text": 2.169102,
      "aei_vision": 0.271788,
      "text_ratio": 0.924105,
      "vision_ratio": 0.075895
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.924105,
      0.075895
    ],
    "text_vision_ratio": "0.924105:0.075895"
  }
}
```


## === Rollout Step 152 ===
Step: 151/29790 | 2025-10-22 12:15:05

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.389 | 7.068 | 19.738 | 19.738 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.38926,
      "aei_text": 3.154735,
      "aei_vision": 0.204996,
      "text_ratio": 0.938984,
      "vision_ratio": 0.061016
    },
    "middle": {
      "mdi": 7.067888,
      "aei_text": 2.681906,
      "aei_vision": 0.379449,
      "text_ratio": 0.876052,
      "vision_ratio": 0.123948
    },
    "late": {
      "mdi": 19.738033,
      "aei_text": 3.26237,
      "aei_vision": 0.165283,
      "text_ratio": 0.951779,
      "vision_ratio": 0.048221
    },
    "all": {
      "mdi": 19.738033,
      "aei_text": 3.033004,
      "aei_vision": 0.24991,
      "text_ratio": 0.951779,
      "vision_ratio": 0.048221
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951779,
      0.048221
    ],
    "text_vision_ratio": "0.951779:0.048221"
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
      "mdi": 15.38926,
      "aei_text": 3.154735,
      "aei_vision": 0.204996,
      "text_ratio": 0.938984,
      "vision_ratio": 0.061016
    },
    "middle": {
      "mdi": 7.067888,
      "aei_text": 2.681906,
      "aei_vision": 0.379449,
      "text_ratio": 0.876052,
      "vision_ratio": 0.123948
    },
    "late": {
      "mdi": 19.738033,
      "aei_text": 3.26237,
      "aei_vision": 0.165283,
      "text_ratio": 0.951779,
      "vision_ratio": 0.048221
    },
    "all": {
      "mdi": 19.738033,
      "aei_text": 3.033004,
      "aei_vision": 0.24991,
      "text_ratio": 0.951779,
      "vision_ratio": 0.048221
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951779,
      0.048221
    ],
    "text_vision_ratio": "0.951779:0.048221"
  }
}
```


## === Rollout Step 153 ===
Step: 152/29790 | 2025-10-22 12:15:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.324 | 8.206 | 14.833 | 14.833 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 16.323586,
      "aei_text": 2.837678,
      "aei_vision": 0.173839,
      "text_ratio": 0.942275,
      "vision_ratio": 0.057725
    },
    "middle": {
      "mdi": 8.206292,
      "aei_text": 2.536757,
      "aei_vision": 0.309123,
      "text_ratio": 0.891379,
      "vision_ratio": 0.108621
    },
    "late": {
      "mdi": 14.833081,
      "aei_text": 2.80389,
      "aei_vision": 0.189029,
      "text_ratio": 0.936841,
      "vision_ratio": 0.063159
    },
    "all": {
      "mdi": 14.833081,
      "aei_text": 2.726108,
      "aei_vision": 0.223997,
      "text_ratio": 0.936841,
      "vision_ratio": 0.063159
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936841,
      0.063159
    ],
    "text_vision_ratio": "0.936841:0.063159"
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
      "mdi": 16.323586,
      "aei_text": 2.837678,
      "aei_vision": 0.173839,
      "text_ratio": 0.942275,
      "vision_ratio": 0.057725
    },
    "middle": {
      "mdi": 8.206292,
      "aei_text": 2.536757,
      "aei_vision": 0.309123,
      "text_ratio": 0.891379,
      "vision_ratio": 0.108621
    },
    "late": {
      "mdi": 14.833081,
      "aei_text": 2.80389,
      "aei_vision": 0.189029,
      "text_ratio": 0.936841,
      "vision_ratio": 0.063159
    },
    "all": {
      "mdi": 14.833081,
      "aei_text": 2.726108,
      "aei_vision": 0.223997,
      "text_ratio": 0.936841,
      "vision_ratio": 0.063159
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936841,
      0.063159
    ],
    "text_vision_ratio": "0.936841:0.063159"
  }
}
```


## === Rollout Step 154 ===
Step: 153/29790 | 2025-10-22 12:15:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.710 | 11.788 | 15.857 | 15.857 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 19.709625,
      "aei_text": 3.144772,
      "aei_vision": 0.159555,
      "text_ratio": 0.951713,
      "vision_ratio": 0.048287
    },
    "middle": {
      "mdi": 11.787579,
      "aei_text": 2.919822,
      "aei_vision": 0.247703,
      "text_ratio": 0.921799,
      "vision_ratio": 0.078201
    },
    "late": {
      "mdi": 15.856945,
      "aei_text": 3.059556,
      "aei_vision": 0.192947,
      "text_ratio": 0.940677,
      "vision_ratio": 0.059323
    },
    "all": {
      "mdi": 15.856945,
      "aei_text": 3.041383,
      "aei_vision": 0.200069,
      "text_ratio": 0.940677,
      "vision_ratio": 0.059323
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940677,
      0.059323
    ],
    "text_vision_ratio": "0.940677:0.059323"
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
      "mdi": 19.709625,
      "aei_text": 3.144772,
      "aei_vision": 0.159555,
      "text_ratio": 0.951713,
      "vision_ratio": 0.048287
    },
    "middle": {
      "mdi": 11.787579,
      "aei_text": 2.919822,
      "aei_vision": 0.247703,
      "text_ratio": 0.921799,
      "vision_ratio": 0.078201
    },
    "late": {
      "mdi": 15.856945,
      "aei_text": 3.059556,
      "aei_vision": 0.192947,
      "text_ratio": 0.940677,
      "vision_ratio": 0.059323
    },
    "all": {
      "mdi": 15.856945,
      "aei_text": 3.041383,
      "aei_vision": 0.200069,
      "text_ratio": 0.940677,
      "vision_ratio": 0.059323
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940677,
      0.059323
    ],
    "text_vision_ratio": "0.940677:0.059323"
  }
}
```


## === Rollout Step 155 ===
Step: 154/29790 | 2025-10-22 12:15:15

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.924 | 6.751 | 14.947 | 14.947 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.924365,
      "aei_text": 2.884384,
      "aei_vision": 0.207147,
      "text_ratio": 0.932995,
      "vision_ratio": 0.067005
    },
    "middle": {
      "mdi": 6.751185,
      "aei_text": 2.497488,
      "aei_vision": 0.369933,
      "text_ratio": 0.870987,
      "vision_ratio": 0.129013
    },
    "late": {
      "mdi": 14.947249,
      "aei_text": 2.913454,
      "aei_vision": 0.194916,
      "text_ratio": 0.937293,
      "vision_ratio": 0.062707
    },
    "all": {
      "mdi": 14.947249,
      "aei_text": 2.765109,
      "aei_vision": 0.257332,
      "text_ratio": 0.937293,
      "vision_ratio": 0.062707
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937293,
      0.062707
    ],
    "text_vision_ratio": "0.937293:0.062707"
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
      "mdi": 13.924365,
      "aei_text": 2.884384,
      "aei_vision": 0.207147,
      "text_ratio": 0.932995,
      "vision_ratio": 0.067005
    },
    "middle": {
      "mdi": 6.751185,
      "aei_text": 2.497488,
      "aei_vision": 0.369933,
      "text_ratio": 0.870987,
      "vision_ratio": 0.129013
    },
    "late": {
      "mdi": 14.947249,
      "aei_text": 2.913454,
      "aei_vision": 0.194916,
      "text_ratio": 0.937293,
      "vision_ratio": 0.062707
    },
    "all": {
      "mdi": 14.947249,
      "aei_text": 2.765109,
      "aei_vision": 0.257332,
      "text_ratio": 0.937293,
      "vision_ratio": 0.062707
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937293,
      0.062707
    ],
    "text_vision_ratio": "0.937293:0.062707"
  }
}
```


## === Rollout Step 156 ===
Step: 155/29790 | 2025-10-22 12:15:18

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.609 | 7.618 | 18.102 | 18.102 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.608644,
      "aei_text": 2.94698,
      "aei_vision": 0.158366,
      "text_ratio": 0.949002,
      "vision_ratio": 0.050998
    },
    "middle": {
      "mdi": 7.618352,
      "aei_text": 2.541577,
      "aei_vision": 0.333612,
      "text_ratio": 0.883969,
      "vision_ratio": 0.116031
    },
    "late": {
      "mdi": 18.102071,
      "aei_text": 2.937889,
      "aei_vision": 0.162296,
      "text_ratio": 0.94765,
      "vision_ratio": 0.05235
    },
    "all": {
      "mdi": 18.102071,
      "aei_text": 2.808815,
      "aei_vision": 0.218091,
      "text_ratio": 0.94765,
      "vision_ratio": 0.05235
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94765,
      0.05235
    ],
    "text_vision_ratio": "0.947650:0.052350"
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
      "mdi": 18.608644,
      "aei_text": 2.94698,
      "aei_vision": 0.158366,
      "text_ratio": 0.949002,
      "vision_ratio": 0.050998
    },
    "middle": {
      "mdi": 7.618352,
      "aei_text": 2.541577,
      "aei_vision": 0.333612,
      "text_ratio": 0.883969,
      "vision_ratio": 0.116031
    },
    "late": {
      "mdi": 18.102071,
      "aei_text": 2.937889,
      "aei_vision": 0.162296,
      "text_ratio": 0.94765,
      "vision_ratio": 0.05235
    },
    "all": {
      "mdi": 18.102071,
      "aei_text": 2.808815,
      "aei_vision": 0.218091,
      "text_ratio": 0.94765,
      "vision_ratio": 0.05235
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94765,
      0.05235
    ],
    "text_vision_ratio": "0.947650:0.052350"
  }
}
```


## === Rollout Step 157 ===
Step: 156/29790 | 2025-10-22 12:15:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 23.176 | 14.236 | 25.956 | 25.956 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 485.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 485.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 485,
    "text_tokens": 0,
    "total_tokens": 485
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.175747,
      "aei_text": 3.74718,
      "aei_vision": 0.161685,
      "text_ratio": 0.958636,
      "vision_ratio": 0.041364
    },
    "middle": {
      "mdi": 14.235828,
      "aei_text": 3.476704,
      "aei_vision": 0.244222,
      "text_ratio": 0.934365,
      "vision_ratio": 0.065635
    },
    "late": {
      "mdi": 25.955803,
      "aei_text": 3.797568,
      "aei_vision": 0.146309,
      "text_ratio": 0.962902,
      "vision_ratio": 0.037098
    },
    "all": {
      "mdi": 25.955803,
      "aei_text": 3.673817,
      "aei_vision": 0.184072,
      "text_ratio": 0.962902,
      "vision_ratio": 0.037098
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962902,
      0.037098
    ],
    "text_vision_ratio": "0.962902:0.037098"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 485,
    "text_tokens": 0,
    "total_tokens": 485
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.175747,
      "aei_text": 3.74718,
      "aei_vision": 0.161685,
      "text_ratio": 0.958636,
      "vision_ratio": 0.041364
    },
    "middle": {
      "mdi": 14.235828,
      "aei_text": 3.476704,
      "aei_vision": 0.244222,
      "text_ratio": 0.934365,
      "vision_ratio": 0.065635
    },
    "late": {
      "mdi": 25.955803,
      "aei_text": 3.797568,
      "aei_vision": 0.146309,
      "text_ratio": 0.962902,
      "vision_ratio": 0.037098
    },
    "all": {
      "mdi": 25.955803,
      "aei_text": 3.673817,
      "aei_vision": 0.184072,
      "text_ratio": 0.962902,
      "vision_ratio": 0.037098
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962902,
      0.037098
    ],
    "text_vision_ratio": "0.962902:0.037098"
  }
}
```


## === Rollout Step 158 ===
Step: 157/29790 | 2025-10-22 12:15:26

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.506 | 11.208 | 18.478 | 18.478 |
| MDI Std | 0.531 | 0.603 | 0.171 | 0.171 |
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
      "mdi": 19.975499,
      "aei_text": 3.239855,
      "aei_vision": 0.162191,
      "text_ratio": 0.952325,
      "vision_ratio": 0.047675
    },
    "middle": {
      "mdi": 10.604826,
      "aei_text": 2.933848,
      "aei_vision": 0.276652,
      "text_ratio": 0.913829,
      "vision_ratio": 0.086171
    },
    "late": {
      "mdi": 18.648793,
      "aei_text": 3.212875,
      "aei_vision": 0.172283,
      "text_ratio": 0.949106,
      "vision_ratio": 0.050894
    },
    "all": {
      "mdi": 18.648793,
      "aei_text": 3.12886,
      "aei_vision": 0.203709,
      "text_ratio": 0.949106,
      "vision_ratio": 0.050894
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949106,
      0.050894
    ],
    "text_vision_ratio": "0.949106:0.050894"
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
      "mdi": 21.037312,
      "aei_text": 3.259274,
      "aei_vision": 0.154928,
      "text_ratio": 0.954622,
      "vision_ratio": 0.045378
    },
    "middle": {
      "mdi": 11.810351,
      "aei_text": 2.995409,
      "aei_vision": 0.253626,
      "text_ratio": 0.921938,
      "vision_ratio": 0.078062
    },
    "late": {
      "mdi": 18.306367,
      "aei_text": 3.205358,
      "aei_vision": 0.175095,
      "text_ratio": 0.948204,
      "vision_ratio": 0.051796
    },
    "all": {
      "mdi": 18.306367,
      "aei_text": 3.153347,
      "aei_vision": 0.19455,
      "text_ratio": 0.948204,
      "vision_ratio": 0.051796
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948204,
      0.051796
    ],
    "text_vision_ratio": "0.948204:0.051796"
  }
}
```


## === Rollout Step 159 ===
Step: 158/29790 | 2025-10-22 12:15:29

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.302 | 12.130 | 18.763 | 18.763 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 324.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 324.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.302078,
      "aei_text": 2.804902,
      "aei_vision": 0.153256,
      "text_ratio": 0.948192,
      "vision_ratio": 0.051808
    },
    "middle": {
      "mdi": 12.129672,
      "aei_text": 2.663513,
      "aei_vision": 0.219587,
      "text_ratio": 0.923837,
      "vision_ratio": 0.076163
    },
    "late": {
      "mdi": 18.76301,
      "aei_text": 2.812108,
      "aei_vision": 0.149875,
      "text_ratio": 0.9494,
      "vision_ratio": 0.0506
    },
    "all": {
      "mdi": 18.76301,
      "aei_text": 2.760174,
      "aei_vision": 0.174239,
      "text_ratio": 0.9494,
      "vision_ratio": 0.0506
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9494,
      0.0506
    ],
    "text_vision_ratio": "0.949400:0.050600"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.302078,
      "aei_text": 2.804902,
      "aei_vision": 0.153256,
      "text_ratio": 0.948192,
      "vision_ratio": 0.051808
    },
    "middle": {
      "mdi": 12.129672,
      "aei_text": 2.663513,
      "aei_vision": 0.219587,
      "text_ratio": 0.923837,
      "vision_ratio": 0.076163
    },
    "late": {
      "mdi": 18.76301,
      "aei_text": 2.812108,
      "aei_vision": 0.149875,
      "text_ratio": 0.9494,
      "vision_ratio": 0.0506
    },
    "all": {
      "mdi": 18.76301,
      "aei_text": 2.760174,
      "aei_vision": 0.174239,
      "text_ratio": 0.9494,
      "vision_ratio": 0.0506
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9494,
      0.0506
    ],
    "text_vision_ratio": "0.949400:0.050600"
  }
}
```


## === Rollout Step 160 ===
Step: 159/29790 | 2025-10-22 12:15:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.336 | 7.203 | 19.953 | 19.953 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.335748,
      "aei_text": 2.912274,
      "aei_vision": 0.189901,
      "text_ratio": 0.938785,
      "vision_ratio": 0.061215
    },
    "middle": {
      "mdi": 7.202884,
      "aei_text": 2.53106,
      "aei_vision": 0.351395,
      "text_ratio": 0.878092,
      "vision_ratio": 0.121908
    },
    "late": {
      "mdi": 19.952989,
      "aei_text": 3.005033,
      "aei_vision": 0.150606,
      "text_ratio": 0.952274,
      "vision_ratio": 0.047726
    },
    "all": {
      "mdi": 19.952989,
      "aei_text": 2.816122,
      "aei_vision": 0.230634,
      "text_ratio": 0.952274,
      "vision_ratio": 0.047726
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952274,
      0.047726
    ],
    "text_vision_ratio": "0.952274:0.047726"
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
      "mdi": 15.335748,
      "aei_text": 2.912274,
      "aei_vision": 0.189901,
      "text_ratio": 0.938785,
      "vision_ratio": 0.061215
    },
    "middle": {
      "mdi": 7.202884,
      "aei_text": 2.53106,
      "aei_vision": 0.351395,
      "text_ratio": 0.878092,
      "vision_ratio": 0.121908
    },
    "late": {
      "mdi": 19.952989,
      "aei_text": 3.005033,
      "aei_vision": 0.150606,
      "text_ratio": 0.952274,
      "vision_ratio": 0.047726
    },
    "all": {
      "mdi": 19.952989,
      "aei_text": 2.816122,
      "aei_vision": 0.230634,
      "text_ratio": 0.952274,
      "vision_ratio": 0.047726
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952274,
      0.047726
    ],
    "text_vision_ratio": "0.952274:0.047726"
  }
}
```


## === Rollout Step 161 ===
Step: 160/29790 | 2025-10-22 12:15:36

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.935 | 11.652 | 19.153 | 19.153 |
| MDI Std | 0.877 | 0.406 | 0.569 | 0.569 |
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
      "mdi": 19.811607,
      "aei_text": 3.223368,
      "aei_vision": 0.162701,
      "text_ratio": 0.95195,
      "vision_ratio": 0.04805
    },
    "middle": {
      "mdi": 12.057603,
      "aei_text": 2.995677,
      "aei_vision": 0.248447,
      "text_ratio": 0.923416,
      "vision_ratio": 0.076584
    },
    "late": {
      "mdi": 19.722402,
      "aei_text": 3.221646,
      "aei_vision": 0.16335,
      "text_ratio": 0.951743,
      "vision_ratio": 0.048257
    },
    "all": {
      "mdi": 19.722402,
      "aei_text": 3.146897,
      "aei_vision": 0.191499,
      "text_ratio": 0.951743,
      "vision_ratio": 0.048257
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951743,
      0.048257
    ],
    "text_vision_ratio": "0.951743:0.048257"
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
      "mdi": 18.058059,
      "aei_text": 3.186793,
      "aei_vision": 0.176475,
      "text_ratio": 0.947529,
      "vision_ratio": 0.052471
    },
    "middle": {
      "mdi": 11.245895,
      "aei_text": 2.957155,
      "aei_vision": 0.262954,
      "text_ratio": 0.91834,
      "vision_ratio": 0.08166
    },
    "late": {
      "mdi": 18.584004,
      "aei_text": 3.198397,
      "aei_vision": 0.172105,
      "text_ratio": 0.948938,
      "vision_ratio": 0.051062
    },
    "all": {
      "mdi": 18.584004,
      "aei_text": 3.114115,
      "aei_vision": 0.203845,
      "text_ratio": 0.948938,
      "vision_ratio": 0.051062
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948938,
      0.051062
    ],
    "text_vision_ratio": "0.948938:0.051062"
  }
}
```


## === Rollout Step 162 ===
Step: 161/29790 | 2025-10-22 12:15:40

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.904 | 10.899 | 21.295 | 21.295 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.9045,
      "aei_text": 3.154141,
      "aei_vision": 0.166846,
      "text_ratio": 0.94976,
      "vision_ratio": 0.05024
    },
    "middle": {
      "mdi": 10.899254,
      "aei_text": 2.89805,
      "aei_vision": 0.265894,
      "text_ratio": 0.915961,
      "vision_ratio": 0.084039
    },
    "late": {
      "mdi": 21.295032,
      "aei_text": 3.197325,
      "aei_vision": 0.150144,
      "text_ratio": 0.955147,
      "vision_ratio": 0.044853
    },
    "all": {
      "mdi": 21.295032,
      "aei_text": 3.083172,
      "aei_vision": 0.194295,
      "text_ratio": 0.955147,
      "vision_ratio": 0.044853
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955147,
      0.044853
    ],
    "text_vision_ratio": "0.955147:0.044853"
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
      "mdi": 18.9045,
      "aei_text": 3.154141,
      "aei_vision": 0.166846,
      "text_ratio": 0.94976,
      "vision_ratio": 0.05024
    },
    "middle": {
      "mdi": 10.899254,
      "aei_text": 2.89805,
      "aei_vision": 0.265894,
      "text_ratio": 0.915961,
      "vision_ratio": 0.084039
    },
    "late": {
      "mdi": 21.295032,
      "aei_text": 3.197325,
      "aei_vision": 0.150144,
      "text_ratio": 0.955147,
      "vision_ratio": 0.044853
    },
    "all": {
      "mdi": 21.295032,
      "aei_text": 3.083172,
      "aei_vision": 0.194295,
      "text_ratio": 0.955147,
      "vision_ratio": 0.044853
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955147,
      0.044853
    ],
    "text_vision_ratio": "0.955147:0.044853"
  }
}
```


## === Rollout Step 163 ===
Step: 162/29790 | 2025-10-22 12:15:44

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.728 | 15.543 | 14.634 | 14.634 |
| MDI Std | 5.421 | 4.818 | 3.216 | 3.216 |
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
      "mdi": 26.148516,
      "aei_text": 3.082292,
      "aei_vision": 0.117876,
      "text_ratio": 0.963166,
      "vision_ratio": 0.036834
    },
    "middle": {
      "mdi": 20.360647,
      "aei_text": 3.011411,
      "aei_vision": 0.147904,
      "text_ratio": 0.953185,
      "vision_ratio": 0.046815
    },
    "late": {
      "mdi": 17.850215,
      "aei_text": 2.968045,
      "aei_vision": 0.166275,
      "text_ratio": 0.94695,
      "vision_ratio": 0.05305
    },
    "all": {
      "mdi": 17.850215,
      "aei_text": 3.020583,
      "aei_vision": 0.144018,
      "text_ratio": 0.94695,
      "vision_ratio": 0.05305
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94695,
      0.05305
    ],
    "text_vision_ratio": "0.946950:0.053050"
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
      "mdi": 15.30674,
      "aei_text": 2.911538,
      "aei_vision": 0.190213,
      "text_ratio": 0.938676,
      "vision_ratio": 0.061324
    },
    "middle": {
      "mdi": 10.724694,
      "aei_text": 2.75431,
      "aei_vision": 0.256819,
      "text_ratio": 0.91471,
      "vision_ratio": 0.08529
    },
    "late": {
      "mdi": 11.417969,
      "aei_text": 2.784814,
      "aei_vision": 0.243897,
      "text_ratio": 0.919472,
      "vision_ratio": 0.080528
    },
    "all": {
      "mdi": 11.417969,
      "aei_text": 2.816887,
      "aei_vision": 0.23031,
      "text_ratio": 0.919472,
      "vision_ratio": 0.080528
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.919472,
      0.080528
    ],
    "text_vision_ratio": "0.919472:0.080528"
  }
}
```


## === Rollout Step 164 ===
Step: 163/29790 | 2025-10-22 12:15:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 8.969 | 5.437 | 13.916 | 13.916 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 8.968606,
      "aei_text": 2.223986,
      "aei_vision": 0.247975,
      "text_ratio": 0.899685,
      "vision_ratio": 0.100315
    },
    "middle": {
      "mdi": 5.437157,
      "aei_text": 2.022239,
      "aei_vision": 0.371929,
      "text_ratio": 0.844652,
      "vision_ratio": 0.155348
    },
    "late": {
      "mdi": 13.916349,
      "aei_text": 2.352455,
      "aei_vision": 0.169043,
      "text_ratio": 0.932959,
      "vision_ratio": 0.067041
    },
    "all": {
      "mdi": 13.916349,
      "aei_text": 2.19956,
      "aei_vision": 0.262982,
      "text_ratio": 0.932959,
      "vision_ratio": 0.067041
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.932959,
      0.067041
    ],
    "text_vision_ratio": "0.932959:0.067041"
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
      "mdi": 8.968606,
      "aei_text": 2.223986,
      "aei_vision": 0.247975,
      "text_ratio": 0.899685,
      "vision_ratio": 0.100315
    },
    "middle": {
      "mdi": 5.437157,
      "aei_text": 2.022239,
      "aei_vision": 0.371929,
      "text_ratio": 0.844652,
      "vision_ratio": 0.155348
    },
    "late": {
      "mdi": 13.916349,
      "aei_text": 2.352455,
      "aei_vision": 0.169043,
      "text_ratio": 0.932959,
      "vision_ratio": 0.067041
    },
    "all": {
      "mdi": 13.916349,
      "aei_text": 2.19956,
      "aei_vision": 0.262982,
      "text_ratio": 0.932959,
      "vision_ratio": 0.067041
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.932959,
      0.067041
    ],
    "text_vision_ratio": "0.932959:0.067041"
  }
}
```


## === Rollout Step 165 ===
Step: 164/29790 | 2025-10-22 12:15:50

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 21.310 | 15.521 | 17.233 | 17.233 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 21.310025,
      "aei_text": 2.976984,
      "aei_vision": 0.139699,
      "text_ratio": 0.955177,
      "vision_ratio": 0.044823
    },
    "middle": {
      "mdi": 15.520679,
      "aei_text": 2.87268,
      "aei_vision": 0.185087,
      "text_ratio": 0.93947,
      "vision_ratio": 0.06053
    },
    "late": {
      "mdi": 17.232865,
      "aei_text": 2.909967,
      "aei_vision": 0.168861,
      "text_ratio": 0.945154,
      "vision_ratio": 0.054846
    },
    "all": {
      "mdi": 17.232865,
      "aei_text": 2.919877,
      "aei_vision": 0.164549,
      "text_ratio": 0.945154,
      "vision_ratio": 0.054846
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945154,
      0.054846
    ],
    "text_vision_ratio": "0.945154:0.054846"
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
      "mdi": 21.310025,
      "aei_text": 2.976984,
      "aei_vision": 0.139699,
      "text_ratio": 0.955177,
      "vision_ratio": 0.044823
    },
    "middle": {
      "mdi": 15.520679,
      "aei_text": 2.87268,
      "aei_vision": 0.185087,
      "text_ratio": 0.93947,
      "vision_ratio": 0.06053
    },
    "late": {
      "mdi": 17.232865,
      "aei_text": 2.909967,
      "aei_vision": 0.168861,
      "text_ratio": 0.945154,
      "vision_ratio": 0.054846
    },
    "all": {
      "mdi": 17.232865,
      "aei_text": 2.919877,
      "aei_vision": 0.164549,
      "text_ratio": 0.945154,
      "vision_ratio": 0.054846
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945154,
      0.054846
    ],
    "text_vision_ratio": "0.945154:0.054846"
  }
}
```


## === Rollout Step 166 ===
Step: 165/29790 | 2025-10-22 12:15:53

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 9.627 | 6.125 | 15.400 | 15.400 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 9.627204,
      "aei_text": 2.211859,
      "aei_vision": 0.229751,
      "text_ratio": 0.905902,
      "vision_ratio": 0.094098
    },
    "middle": {
      "mdi": 6.124814,
      "aei_text": 2.0474,
      "aei_vision": 0.33428,
      "text_ratio": 0.859645,
      "vision_ratio": 0.140355
    },
    "late": {
      "mdi": 15.400467,
      "aei_text": 2.334806,
      "aei_vision": 0.151606,
      "text_ratio": 0.939026,
      "vision_ratio": 0.060974
    },
    "all": {
      "mdi": 15.400467,
      "aei_text": 2.198022,
      "aei_vision": 0.238546,
      "text_ratio": 0.939026,
      "vision_ratio": 0.060974
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939026,
      0.060974
    ],
    "text_vision_ratio": "0.939026:0.060974"
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
      "mdi": 9.627204,
      "aei_text": 2.211859,
      "aei_vision": 0.229751,
      "text_ratio": 0.905902,
      "vision_ratio": 0.094098
    },
    "middle": {
      "mdi": 6.124814,
      "aei_text": 2.0474,
      "aei_vision": 0.33428,
      "text_ratio": 0.859645,
      "vision_ratio": 0.140355
    },
    "late": {
      "mdi": 15.400467,
      "aei_text": 2.334806,
      "aei_vision": 0.151606,
      "text_ratio": 0.939026,
      "vision_ratio": 0.060974
    },
    "all": {
      "mdi": 15.400467,
      "aei_text": 2.198022,
      "aei_vision": 0.238546,
      "text_ratio": 0.939026,
      "vision_ratio": 0.060974
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939026,
      0.060974
    ],
    "text_vision_ratio": "0.939026:0.060974"
  }
}
```


## === Rollout Step 167 ===
Step: 166/29790 | 2025-10-22 12:15:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 13.108 | 6.511 | 18.755 | 18.755 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 13.107662,
      "aei_text": 2.329201,
      "aei_vision": 0.177698,
      "text_ratio": 0.929117,
      "vision_ratio": 0.070883
    },
    "middle": {
      "mdi": 6.510864,
      "aei_text": 2.096055,
      "aei_vision": 0.321932,
      "text_ratio": 0.86686,
      "vision_ratio": 0.13314
    },
    "late": {
      "mdi": 18.754759,
      "aei_text": 2.408826,
      "aei_vision": 0.128438,
      "text_ratio": 0.949379,
      "vision_ratio": 0.050621
    },
    "all": {
      "mdi": 18.754759,
      "aei_text": 2.278027,
      "aei_vision": 0.209356,
      "text_ratio": 0.949379,
      "vision_ratio": 0.050621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949379,
      0.050621
    ],
    "text_vision_ratio": "0.949379:0.050621"
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
      "mdi": 13.107662,
      "aei_text": 2.329201,
      "aei_vision": 0.177698,
      "text_ratio": 0.929117,
      "vision_ratio": 0.070883
    },
    "middle": {
      "mdi": 6.510864,
      "aei_text": 2.096055,
      "aei_vision": 0.321932,
      "text_ratio": 0.86686,
      "vision_ratio": 0.13314
    },
    "late": {
      "mdi": 18.754759,
      "aei_text": 2.408826,
      "aei_vision": 0.128438,
      "text_ratio": 0.949379,
      "vision_ratio": 0.050621
    },
    "all": {
      "mdi": 18.754759,
      "aei_text": 2.278027,
      "aei_vision": 0.209356,
      "text_ratio": 0.949379,
      "vision_ratio": 0.050621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949379,
      0.050621
    ],
    "text_vision_ratio": "0.949379:0.050621"
  }
}
```


## === Rollout Step 168 ===
Step: 167/29790 | 2025-10-22 12:15:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.377 | 10.866 | 14.600 | 14.600 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 12.377126,
      "aei_text": 2.791577,
      "aei_vision": 0.225543,
      "text_ratio": 0.925246,
      "vision_ratio": 0.074754
    },
    "middle": {
      "mdi": 10.865876,
      "aei_text": 2.731747,
      "aei_vision": 0.251406,
      "text_ratio": 0.915725,
      "vision_ratio": 0.084275
    },
    "late": {
      "mdi": 14.599657,
      "aei_text": 2.860141,
      "aei_vision": 0.195905,
      "text_ratio": 0.935896,
      "vision_ratio": 0.064104
    },
    "all": {
      "mdi": 14.599657,
      "aei_text": 2.794488,
      "aei_vision": 0.224285,
      "text_ratio": 0.935896,
      "vision_ratio": 0.064104
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.935896,
      0.064104
    ],
    "text_vision_ratio": "0.935896:0.064104"
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
      "mdi": 12.377126,
      "aei_text": 2.791577,
      "aei_vision": 0.225543,
      "text_ratio": 0.925246,
      "vision_ratio": 0.074754
    },
    "middle": {
      "mdi": 10.865876,
      "aei_text": 2.731747,
      "aei_vision": 0.251406,
      "text_ratio": 0.915725,
      "vision_ratio": 0.084275
    },
    "late": {
      "mdi": 14.599657,
      "aei_text": 2.860141,
      "aei_vision": 0.195905,
      "text_ratio": 0.935896,
      "vision_ratio": 0.064104
    },
    "all": {
      "mdi": 14.599657,
      "aei_text": 2.794488,
      "aei_vision": 0.224285,
      "text_ratio": 0.935896,
      "vision_ratio": 0.064104
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.935896,
      0.064104
    ],
    "text_vision_ratio": "0.935896:0.064104"
  }
}
```


## === Rollout Step 169 ===
Step: 168/29790 | 2025-10-22 12:16:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.077 | 6.757 | 18.415 | 18.415 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.076666,
      "aei_text": 3.144971,
      "aei_vision": 0.208599,
      "text_ratio": 0.937798,
      "vision_ratio": 0.062202
    },
    "middle": {
      "mdi": 6.75663,
      "aei_text": 2.648093,
      "aei_vision": 0.391925,
      "text_ratio": 0.871078,
      "vision_ratio": 0.128922
    },
    "late": {
      "mdi": 18.414713,
      "aei_text": 3.234308,
      "aei_vision": 0.175637,
      "text_ratio": 0.948493,
      "vision_ratio": 0.051507
    },
    "all": {
      "mdi": 18.414713,
      "aei_text": 3.009124,
      "aei_vision": 0.25872,
      "text_ratio": 0.948493,
      "vision_ratio": 0.051507
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948493,
      0.051507
    ],
    "text_vision_ratio": "0.948493:0.051507"
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
      "mdi": 15.076666,
      "aei_text": 3.144971,
      "aei_vision": 0.208599,
      "text_ratio": 0.937798,
      "vision_ratio": 0.062202
    },
    "middle": {
      "mdi": 6.75663,
      "aei_text": 2.648093,
      "aei_vision": 0.391925,
      "text_ratio": 0.871078,
      "vision_ratio": 0.128922
    },
    "late": {
      "mdi": 18.414713,
      "aei_text": 3.234308,
      "aei_vision": 0.175637,
      "text_ratio": 0.948493,
      "vision_ratio": 0.051507
    },
    "all": {
      "mdi": 18.414713,
      "aei_text": 3.009124,
      "aei_vision": 0.25872,
      "text_ratio": 0.948493,
      "vision_ratio": 0.051507
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948493,
      0.051507
    ],
    "text_vision_ratio": "0.948493:0.051507"
  }
}
```


## === Rollout Step 170 ===
Step: 169/29790 | 2025-10-22 12:16:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.069 | 12.590 | 24.160 | 24.160 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 19.069257,
      "aei_text": 3.221782,
      "aei_vision": 0.168952,
      "text_ratio": 0.950173,
      "vision_ratio": 0.049827
    },
    "middle": {
      "mdi": 12.590135,
      "aei_text": 3.030049,
      "aei_vision": 0.240669,
      "text_ratio": 0.926417,
      "vision_ratio": 0.073583
    },
    "late": {
      "mdi": 24.160334,
      "aei_text": 3.307479,
      "aei_vision": 0.136897,
      "text_ratio": 0.960255,
      "vision_ratio": 0.039745
    },
    "all": {
      "mdi": 24.160334,
      "aei_text": 3.186437,
      "aei_vision": 0.182172,
      "text_ratio": 0.960255,
      "vision_ratio": 0.039745
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960255,
      0.039745
    ],
    "text_vision_ratio": "0.960255:0.039745"
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
      "mdi": 19.069257,
      "aei_text": 3.221782,
      "aei_vision": 0.168952,
      "text_ratio": 0.950173,
      "vision_ratio": 0.049827
    },
    "middle": {
      "mdi": 12.590135,
      "aei_text": 3.030049,
      "aei_vision": 0.240669,
      "text_ratio": 0.926417,
      "vision_ratio": 0.073583
    },
    "late": {
      "mdi": 24.160334,
      "aei_text": 3.307479,
      "aei_vision": 0.136897,
      "text_ratio": 0.960255,
      "vision_ratio": 0.039745
    },
    "all": {
      "mdi": 24.160334,
      "aei_text": 3.186437,
      "aei_vision": 0.182172,
      "text_ratio": 0.960255,
      "vision_ratio": 0.039745
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960255,
      0.039745
    ],
    "text_vision_ratio": "0.960255:0.039745"
  }
}
```


## === Rollout Step 171 ===
Step: 170/29790 | 2025-10-22 12:16:09

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.351 | 13.940 | 18.259 | 18.259 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.350735,
      "aei_text": 2.965682,
      "aei_vision": 0.161611,
      "text_ratio": 0.948322,
      "vision_ratio": 0.051678
    },
    "middle": {
      "mdi": 13.939777,
      "aei_text": 2.863046,
      "aei_vision": 0.205387,
      "text_ratio": 0.933065,
      "vision_ratio": 0.066935
    },
    "late": {
      "mdi": 18.259277,
      "aei_text": 2.964,
      "aei_vision": 0.162328,
      "text_ratio": 0.948077,
      "vision_ratio": 0.051923
    },
    "all": {
      "mdi": 18.259277,
      "aei_text": 2.930909,
      "aei_vision": 0.176442,
      "text_ratio": 0.948077,
      "vision_ratio": 0.051923
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948077,
      0.051923
    ],
    "text_vision_ratio": "0.948077:0.051923"
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
      "mdi": 18.350735,
      "aei_text": 2.965682,
      "aei_vision": 0.161611,
      "text_ratio": 0.948322,
      "vision_ratio": 0.051678
    },
    "middle": {
      "mdi": 13.939777,
      "aei_text": 2.863046,
      "aei_vision": 0.205387,
      "text_ratio": 0.933065,
      "vision_ratio": 0.066935
    },
    "late": {
      "mdi": 18.259277,
      "aei_text": 2.964,
      "aei_vision": 0.162328,
      "text_ratio": 0.948077,
      "vision_ratio": 0.051923
    },
    "all": {
      "mdi": 18.259277,
      "aei_text": 2.930909,
      "aei_vision": 0.176442,
      "text_ratio": 0.948077,
      "vision_ratio": 0.051923
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948077,
      0.051923
    ],
    "text_vision_ratio": "0.948077:0.051923"
  }
}
```


## === Rollout Step 172 ===
Step: 171/29790 | 2025-10-22 12:16:13

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 23.773 | 19.542 | 19.320 | 19.320 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 23.772628,
      "aei_text": 2.995259,
      "aei_vision": 0.125996,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    },
    "middle": {
      "mdi": 19.541807,
      "aei_text": 2.939499,
      "aei_vision": 0.150421,
      "text_ratio": 0.951319,
      "vision_ratio": 0.048681
    },
    "late": {
      "mdi": 19.319704,
      "aei_text": 2.935969,
      "aei_vision": 0.151968,
      "text_ratio": 0.950787,
      "vision_ratio": 0.049213
    },
    "all": {
      "mdi": 19.319704,
      "aei_text": 2.956909,
      "aei_vision": 0.142795,
      "text_ratio": 0.950787,
      "vision_ratio": 0.049213
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950787,
      0.049213
    ],
    "text_vision_ratio": "0.950787:0.049213"
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
      "mdi": 23.772628,
      "aei_text": 2.995259,
      "aei_vision": 0.125996,
      "text_ratio": 0.959633,
      "vision_ratio": 0.040367
    },
    "middle": {
      "mdi": 19.541807,
      "aei_text": 2.939499,
      "aei_vision": 0.150421,
      "text_ratio": 0.951319,
      "vision_ratio": 0.048681
    },
    "late": {
      "mdi": 19.319704,
      "aei_text": 2.935969,
      "aei_vision": 0.151968,
      "text_ratio": 0.950787,
      "vision_ratio": 0.049213
    },
    "all": {
      "mdi": 19.319704,
      "aei_text": 2.956909,
      "aei_vision": 0.142795,
      "text_ratio": 0.950787,
      "vision_ratio": 0.049213
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950787,
      0.049213
    ],
    "text_vision_ratio": "0.950787:0.049213"
  }
}
```


## === Rollout Step 173 ===
Step: 172/29790 | 2025-10-22 12:16:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 20.448 | 15.769 | 16.437 | 16.437 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 20.44848,
      "aei_text": 3.018048,
      "aei_vision": 0.147593,
      "text_ratio": 0.953377,
      "vision_ratio": 0.046623
    },
    "middle": {
      "mdi": 15.768881,
      "aei_text": 2.92789,
      "aei_vision": 0.185675,
      "text_ratio": 0.940366,
      "vision_ratio": 0.059634
    },
    "late": {
      "mdi": 16.436722,
      "aei_text": 2.943501,
      "aei_vision": 0.179081,
      "text_ratio": 0.94265,
      "vision_ratio": 0.05735
    },
    "all": {
      "mdi": 16.436722,
      "aei_text": 2.963146,
      "aei_vision": 0.170783,
      "text_ratio": 0.94265,
      "vision_ratio": 0.05735
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94265,
      0.05735
    ],
    "text_vision_ratio": "0.942650:0.057350"
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
      "mdi": 20.44848,
      "aei_text": 3.018048,
      "aei_vision": 0.147593,
      "text_ratio": 0.953377,
      "vision_ratio": 0.046623
    },
    "middle": {
      "mdi": 15.768881,
      "aei_text": 2.92789,
      "aei_vision": 0.185675,
      "text_ratio": 0.940366,
      "vision_ratio": 0.059634
    },
    "late": {
      "mdi": 16.436722,
      "aei_text": 2.943501,
      "aei_vision": 0.179081,
      "text_ratio": 0.94265,
      "vision_ratio": 0.05735
    },
    "all": {
      "mdi": 16.436722,
      "aei_text": 2.963146,
      "aei_vision": 0.170783,
      "text_ratio": 0.94265,
      "vision_ratio": 0.05735
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94265,
      0.05735
    ],
    "text_vision_ratio": "0.942650:0.057350"
  }
}
```


## === Rollout Step 174 ===
Step: 173/29790 | 2025-10-22 12:16:19

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.063 | 6.074 | 14.596 | 14.596 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 10.063074,
      "aei_text": 2.232504,
      "aei_vision": 0.221851,
      "text_ratio": 0.909609,
      "vision_ratio": 0.090391
    },
    "middle": {
      "mdi": 6.073849,
      "aei_text": 2.049452,
      "aei_vision": 0.337422,
      "text_ratio": 0.858634,
      "vision_ratio": 0.141366
    },
    "late": {
      "mdi": 14.595582,
      "aei_text": 2.330942,
      "aei_vision": 0.159702,
      "text_ratio": 0.935879,
      "vision_ratio": 0.064121
    },
    "all": {
      "mdi": 14.595582,
      "aei_text": 2.204299,
      "aei_vision": 0.239658,
      "text_ratio": 0.935879,
      "vision_ratio": 0.064121
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.935879,
      0.064121
    ],
    "text_vision_ratio": "0.935879:0.064121"
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
      "mdi": 10.063074,
      "aei_text": 2.232504,
      "aei_vision": 0.221851,
      "text_ratio": 0.909609,
      "vision_ratio": 0.090391
    },
    "middle": {
      "mdi": 6.073849,
      "aei_text": 2.049452,
      "aei_vision": 0.337422,
      "text_ratio": 0.858634,
      "vision_ratio": 0.141366
    },
    "late": {
      "mdi": 14.595582,
      "aei_text": 2.330942,
      "aei_vision": 0.159702,
      "text_ratio": 0.935879,
      "vision_ratio": 0.064121
    },
    "all": {
      "mdi": 14.595582,
      "aei_text": 2.204299,
      "aei_vision": 0.239658,
      "text_ratio": 0.935879,
      "vision_ratio": 0.064121
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.935879,
      0.064121
    ],
    "text_vision_ratio": "0.935879:0.064121"
  }
}
```


## === Rollout Step 175 ===
Step: 174/29790 | 2025-10-22 12:16:24

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.113 | 10.118 | 16.751 | 16.751 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 531.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 531.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.113129,
      "aei_text": 3.731653,
      "aei_vision": 0.218058,
      "text_ratio": 0.944791,
      "vision_ratio": 0.055209
    },
    "middle": {
      "mdi": 10.118245,
      "aei_text": 3.340189,
      "aei_vision": 0.330115,
      "text_ratio": 0.910058,
      "vision_ratio": 0.089942
    },
    "late": {
      "mdi": 16.750786,
      "aei_text": 3.718018,
      "aei_vision": 0.221961,
      "text_ratio": 0.943664,
      "vision_ratio": 0.056336
    },
    "all": {
      "mdi": 16.750786,
      "aei_text": 3.59662,
      "aei_vision": 0.256711,
      "text_ratio": 0.943664,
      "vision_ratio": 0.056336
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943664,
      0.056336
    ],
    "text_vision_ratio": "0.943664:0.056336"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 531,
    "text_tokens": 0,
    "total_tokens": 531
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.113129,
      "aei_text": 3.731653,
      "aei_vision": 0.218058,
      "text_ratio": 0.944791,
      "vision_ratio": 0.055209
    },
    "middle": {
      "mdi": 10.118245,
      "aei_text": 3.340189,
      "aei_vision": 0.330115,
      "text_ratio": 0.910058,
      "vision_ratio": 0.089942
    },
    "late": {
      "mdi": 16.750786,
      "aei_text": 3.718018,
      "aei_vision": 0.221961,
      "text_ratio": 0.943664,
      "vision_ratio": 0.056336
    },
    "all": {
      "mdi": 16.750786,
      "aei_text": 3.59662,
      "aei_vision": 0.256711,
      "text_ratio": 0.943664,
      "vision_ratio": 0.056336
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943664,
      0.056336
    ],
    "text_vision_ratio": "0.943664:0.056336"
  }
}
```


## === Rollout Step 176 ===
Step: 175/29790 | 2025-10-22 12:16:27

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.178 | 16.864 | 17.036 | 17.036 |
| MDI Std | 3.392 | 3.197 | 3.605 | 3.605 |
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
      "mdi": 15.786202,
      "aei_text": 3.14145,
      "aei_vision": 0.199,
      "text_ratio": 0.940427,
      "vision_ratio": 0.059573
    },
    "middle": {
      "mdi": 13.667324,
      "aei_text": 3.072464,
      "aei_vision": 0.224804,
      "text_ratio": 0.931821,
      "vision_ratio": 0.068179
    },
    "late": {
      "mdi": 13.430811,
      "aei_text": 3.063637,
      "aei_vision": 0.228105,
      "text_ratio": 0.930704,
      "vision_ratio": 0.069296
    },
    "all": {
      "mdi": 13.430811,
      "aei_text": 3.092517,
      "aei_vision": 0.217303,
      "text_ratio": 0.930704,
      "vision_ratio": 0.069296
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.930704,
      0.069296
    ],
    "text_vision_ratio": "0.930704:0.069296"
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
      "mdi": 22.569489,
      "aei_text": 3.284414,
      "aei_vision": 0.145525,
      "text_ratio": 0.957572,
      "vision_ratio": 0.042428
    },
    "middle": {
      "mdi": 20.06088,
      "aei_text": 3.241484,
      "aei_vision": 0.161582,
      "text_ratio": 0.952519,
      "vision_ratio": 0.047481
    },
    "late": {
      "mdi": 20.641094,
      "aei_text": 3.252234,
      "aei_vision": 0.157561,
      "text_ratio": 0.953792,
      "vision_ratio": 0.046208
    },
    "all": {
      "mdi": 20.641094,
      "aei_text": 3.259377,
      "aei_vision": 0.154889,
      "text_ratio": 0.953792,
      "vision_ratio": 0.046208
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953792,
      0.046208
    ],
    "text_vision_ratio": "0.953792:0.046208"
  }
}
```


## === Rollout Step 177 ===
Step: 176/29790 | 2025-10-22 12:16:31

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 10.902 | 9.659 | 17.952 | 17.952 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 10.902038,
      "aei_text": 2.939446,
      "aei_vision": 0.269624,
      "text_ratio": 0.915981,
      "vision_ratio": 0.084019
    },
    "middle": {
      "mdi": 9.658513,
      "aei_text": 2.867144,
      "aei_vision": 0.296852,
      "text_ratio": 0.906178,
      "vision_ratio": 0.093822
    },
    "late": {
      "mdi": 17.951502,
      "aei_text": 3.18437,
      "aei_vision": 0.177387,
      "text_ratio": 0.947234,
      "vision_ratio": 0.052766
    },
    "all": {
      "mdi": 17.951502,
      "aei_text": 2.996987,
      "aei_vision": 0.247954,
      "text_ratio": 0.947234,
      "vision_ratio": 0.052766
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947234,
      0.052766
    ],
    "text_vision_ratio": "0.947234:0.052766"
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
      "mdi": 10.902038,
      "aei_text": 2.939446,
      "aei_vision": 0.269624,
      "text_ratio": 0.915981,
      "vision_ratio": 0.084019
    },
    "middle": {
      "mdi": 9.658513,
      "aei_text": 2.867144,
      "aei_vision": 0.296852,
      "text_ratio": 0.906178,
      "vision_ratio": 0.093822
    },
    "late": {
      "mdi": 17.951502,
      "aei_text": 3.18437,
      "aei_vision": 0.177387,
      "text_ratio": 0.947234,
      "vision_ratio": 0.052766
    },
    "all": {
      "mdi": 17.951502,
      "aei_text": 2.996987,
      "aei_vision": 0.247954,
      "text_ratio": 0.947234,
      "vision_ratio": 0.052766
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947234,
      0.052766
    ],
    "text_vision_ratio": "0.947234:0.052766"
  }
}
```


## === Rollout Step 178 ===
Step: 177/29790 | 2025-10-22 12:16:34

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 19.376 | 11.885 | 19.376 | 19.376 |
| MDI Std | 2.334 | 1.503 | 0.302 | 0.302 |
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
      "mdi": 21.710163,
      "aei_text": 2.982334,
      "aei_vision": 0.13737,
      "text_ratio": 0.955967,
      "vision_ratio": 0.044033
    },
    "middle": {
      "mdi": 13.387601,
      "aei_text": 2.814839,
      "aei_vision": 0.210257,
      "text_ratio": 0.930496,
      "vision_ratio": 0.069504
    },
    "late": {
      "mdi": 19.677417,
      "aei_text": 2.953134,
      "aei_vision": 0.150077,
      "text_ratio": 0.951638,
      "vision_ratio": 0.048362
    },
    "all": {
      "mdi": 19.677417,
      "aei_text": 2.916769,
      "aei_vision": 0.165902,
      "text_ratio": 0.951638,
      "vision_ratio": 0.048362
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951638,
      0.048362
    ],
    "text_vision_ratio": "0.951638:0.048362"
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
      "mdi": 17.04221,
      "aei_text": 2.906142,
      "aei_vision": 0.170526,
      "text_ratio": 0.944574,
      "vision_ratio": 0.055426
    },
    "middle": {
      "mdi": 10.382418,
      "aei_text": 2.70033,
      "aei_vision": 0.260087,
      "text_ratio": 0.912145,
      "vision_ratio": 0.087855
    },
    "late": {
      "mdi": 19.074023,
      "aei_text": 2.943397,
      "aei_vision": 0.154314,
      "text_ratio": 0.950184,
      "vision_ratio": 0.049816
    },
    "all": {
      "mdi": 19.074023,
      "aei_text": 2.849956,
      "aei_vision": 0.194976,
      "text_ratio": 0.950184,
      "vision_ratio": 0.049816
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950184,
      0.049816
    ],
    "text_vision_ratio": "0.950184:0.049816"
  }
}
```


## === Rollout Step 179 ===
Step: 178/29790 | 2025-10-22 12:16:38

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.265 | 9.688 | 20.646 | 20.646 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.264711,
      "aei_text": 3.113747,
      "aei_vision": 0.203983,
      "text_ratio": 0.938517,
      "vision_ratio": 0.061483
    },
    "middle": {
      "mdi": 9.688254,
      "aei_text": 2.869044,
      "aei_vision": 0.296136,
      "text_ratio": 0.906439,
      "vision_ratio": 0.093561
    },
    "late": {
      "mdi": 20.645908,
      "aei_text": 3.238837,
      "aei_vision": 0.156876,
      "text_ratio": 0.953802,
      "vision_ratio": 0.046198
    },
    "all": {
      "mdi": 20.645908,
      "aei_text": 3.073876,
      "aei_vision": 0.218998,
      "text_ratio": 0.953802,
      "vision_ratio": 0.046198
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953802,
      0.046198
    ],
    "text_vision_ratio": "0.953802:0.046198"
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
      "mdi": 15.264711,
      "aei_text": 3.113747,
      "aei_vision": 0.203983,
      "text_ratio": 0.938517,
      "vision_ratio": 0.061483
    },
    "middle": {
      "mdi": 9.688254,
      "aei_text": 2.869044,
      "aei_vision": 0.296136,
      "text_ratio": 0.906439,
      "vision_ratio": 0.093561
    },
    "late": {
      "mdi": 20.645908,
      "aei_text": 3.238837,
      "aei_vision": 0.156876,
      "text_ratio": 0.953802,
      "vision_ratio": 0.046198
    },
    "all": {
      "mdi": 20.645908,
      "aei_text": 3.073876,
      "aei_vision": 0.218998,
      "text_ratio": 0.953802,
      "vision_ratio": 0.046198
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953802,
      0.046198
    ],
    "text_vision_ratio": "0.953802:0.046198"
  }
}
```


## === Rollout Step 180 ===
Step: 179/29790 | 2025-10-22 12:16:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 32.853 | 36.617 | 19.753 | 19.753 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 32.853117,
      "aei_text": 3.26859,
      "aei_vision": 0.099491,
      "text_ratio": 0.970461,
      "vision_ratio": 0.029539
    },
    "middle": {
      "mdi": 36.617172,
      "aei_text": 3.292696,
      "aei_vision": 0.089922,
      "text_ratio": 0.973416,
      "vision_ratio": 0.026584
    },
    "late": {
      "mdi": 19.752576,
      "aei_text": 3.12116,
      "aei_vision": 0.158013,
      "text_ratio": 0.951813,
      "vision_ratio": 0.048187
    },
    "all": {
      "mdi": 19.752576,
      "aei_text": 3.227482,
      "aei_vision": 0.115809,
      "text_ratio": 0.951813,
      "vision_ratio": 0.048187
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951813,
      0.048187
    ],
    "text_vision_ratio": "0.951813:0.048187"
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
      "mdi": 32.853117,
      "aei_text": 3.26859,
      "aei_vision": 0.099491,
      "text_ratio": 0.970461,
      "vision_ratio": 0.029539
    },
    "middle": {
      "mdi": 36.617172,
      "aei_text": 3.292696,
      "aei_vision": 0.089922,
      "text_ratio": 0.973416,
      "vision_ratio": 0.026584
    },
    "late": {
      "mdi": 19.752576,
      "aei_text": 3.12116,
      "aei_vision": 0.158013,
      "text_ratio": 0.951813,
      "vision_ratio": 0.048187
    },
    "all": {
      "mdi": 19.752576,
      "aei_text": 3.227482,
      "aei_vision": 0.115809,
      "text_ratio": 0.951813,
      "vision_ratio": 0.048187
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951813,
      0.048187
    ],
    "text_vision_ratio": "0.951813:0.048187"
  }
}
```


## === Rollout Step 181 ===
Step: 180/29790 | 2025-10-22 12:16:45

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.031 | 10.040 | 19.565 | 19.565 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 14.031061,
      "aei_text": 3.10966,
      "aei_vision": 0.221627,
      "text_ratio": 0.933471,
      "vision_ratio": 0.066529
    },
    "middle": {
      "mdi": 10.039832,
      "aei_text": 2.921625,
      "aei_vision": 0.291003,
      "text_ratio": 0.909419,
      "vision_ratio": 0.090581
    },
    "late": {
      "mdi": 19.564997,
      "aei_text": 3.25889,
      "aei_vision": 0.166567,
      "text_ratio": 0.951374,
      "vision_ratio": 0.048626
    },
    "all": {
      "mdi": 19.564997,
      "aei_text": 3.096725,
      "aei_vision": 0.226399,
      "text_ratio": 0.951374,
      "vision_ratio": 0.048626
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951374,
      0.048626
    ],
    "text_vision_ratio": "0.951374:0.048626"
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
      "mdi": 14.031061,
      "aei_text": 3.10966,
      "aei_vision": 0.221627,
      "text_ratio": 0.933471,
      "vision_ratio": 0.066529
    },
    "middle": {
      "mdi": 10.039832,
      "aei_text": 2.921625,
      "aei_vision": 0.291003,
      "text_ratio": 0.909419,
      "vision_ratio": 0.090581
    },
    "late": {
      "mdi": 19.564997,
      "aei_text": 3.25889,
      "aei_vision": 0.166567,
      "text_ratio": 0.951374,
      "vision_ratio": 0.048626
    },
    "all": {
      "mdi": 19.564997,
      "aei_text": 3.096725,
      "aei_vision": 0.226399,
      "text_ratio": 0.951374,
      "vision_ratio": 0.048626
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951374,
      0.048626
    ],
    "text_vision_ratio": "0.951374:0.048626"
  }
}
```


## === Rollout Step 182 ===
Step: 181/29790 | 2025-10-22 12:16:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 26.453 | 18.575 | 21.324 | 21.324 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 26.45253,
      "aei_text": 3.034405,
      "aei_vision": 0.114711,
      "text_ratio": 0.963573,
      "vision_ratio": 0.036427
    },
    "middle": {
      "mdi": 18.574774,
      "aei_text": 2.934915,
      "aei_vision": 0.158005,
      "text_ratio": 0.948914,
      "vision_ratio": 0.051086
    },
    "late": {
      "mdi": 21.32381,
      "aei_text": 2.977171,
      "aei_vision": 0.139617,
      "text_ratio": 0.955205,
      "vision_ratio": 0.044795
    },
    "all": {
      "mdi": 21.32381,
      "aei_text": 2.982164,
      "aei_vision": 0.137445,
      "text_ratio": 0.955205,
      "vision_ratio": 0.044795
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955205,
      0.044795
    ],
    "text_vision_ratio": "0.955205:0.044795"
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
      "mdi": 26.45253,
      "aei_text": 3.034405,
      "aei_vision": 0.114711,
      "text_ratio": 0.963573,
      "vision_ratio": 0.036427
    },
    "middle": {
      "mdi": 18.574774,
      "aei_text": 2.934915,
      "aei_vision": 0.158005,
      "text_ratio": 0.948914,
      "vision_ratio": 0.051086
    },
    "late": {
      "mdi": 21.32381,
      "aei_text": 2.977171,
      "aei_vision": 0.139617,
      "text_ratio": 0.955205,
      "vision_ratio": 0.044795
    },
    "all": {
      "mdi": 21.32381,
      "aei_text": 2.982164,
      "aei_vision": 0.137445,
      "text_ratio": 0.955205,
      "vision_ratio": 0.044795
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955205,
      0.044795
    ],
    "text_vision_ratio": "0.955205:0.044795"
  }
}
```


## === Rollout Step 183 ===
Step: 182/29790 | 2025-10-22 12:16:52

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 18.020 | 9.753 | 19.368 | 19.368 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 18.020461,
      "aei_text": 2.925009,
      "aei_vision": 0.162316,
      "text_ratio": 0.947425,
      "vision_ratio": 0.052575
    },
    "middle": {
      "mdi": 9.753115,
      "aei_text": 2.66912,
      "aei_vision": 0.273668,
      "text_ratio": 0.907004,
      "vision_ratio": 0.092996
    },
    "late": {
      "mdi": 19.368316,
      "aei_text": 2.948213,
      "aei_vision": 0.152218,
      "text_ratio": 0.950904,
      "vision_ratio": 0.049096
    },
    "all": {
      "mdi": 19.368316,
      "aei_text": 2.847447,
      "aei_vision": 0.196068,
      "text_ratio": 0.950904,
      "vision_ratio": 0.049096
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950904,
      0.049096
    ],
    "text_vision_ratio": "0.950904:0.049096"
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
      "mdi": 18.020461,
      "aei_text": 2.925009,
      "aei_vision": 0.162316,
      "text_ratio": 0.947425,
      "vision_ratio": 0.052575
    },
    "middle": {
      "mdi": 9.753115,
      "aei_text": 2.66912,
      "aei_vision": 0.273668,
      "text_ratio": 0.907004,
      "vision_ratio": 0.092996
    },
    "late": {
      "mdi": 19.368316,
      "aei_text": 2.948213,
      "aei_vision": 0.152218,
      "text_ratio": 0.950904,
      "vision_ratio": 0.049096
    },
    "all": {
      "mdi": 19.368316,
      "aei_text": 2.847447,
      "aei_vision": 0.196068,
      "text_ratio": 0.950904,
      "vision_ratio": 0.049096
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950904,
      0.049096
    ],
    "text_vision_ratio": "0.950904:0.049096"
  }
}
```


## === Rollout Step 184 ===
Step: 183/29790 | 2025-10-22 12:16:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.367 | 9.548 | 19.688 | 19.688 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.366821,
      "aei_text": 2.91306,
      "aei_vision": 0.189568,
      "text_ratio": 0.938901,
      "vision_ratio": 0.061099
    },
    "middle": {
      "mdi": 9.547599,
      "aei_text": 2.694386,
      "aei_vision": 0.282206,
      "text_ratio": 0.905192,
      "vision_ratio": 0.094808
    },
    "late": {
      "mdi": 19.688136,
      "aei_text": 3.000762,
      "aei_vision": 0.152415,
      "text_ratio": 0.951663,
      "vision_ratio": 0.048337
    },
    "all": {
      "mdi": 19.688136,
      "aei_text": 2.869403,
      "aei_vision": 0.208063,
      "text_ratio": 0.951663,
      "vision_ratio": 0.048337
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951663,
      0.048337
    ],
    "text_vision_ratio": "0.951663:0.048337"
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
      "mdi": 15.366821,
      "aei_text": 2.91306,
      "aei_vision": 0.189568,
      "text_ratio": 0.938901,
      "vision_ratio": 0.061099
    },
    "middle": {
      "mdi": 9.547599,
      "aei_text": 2.694386,
      "aei_vision": 0.282206,
      "text_ratio": 0.905192,
      "vision_ratio": 0.094808
    },
    "late": {
      "mdi": 19.688136,
      "aei_text": 3.000762,
      "aei_vision": 0.152415,
      "text_ratio": 0.951663,
      "vision_ratio": 0.048337
    },
    "all": {
      "mdi": 19.688136,
      "aei_text": 2.869403,
      "aei_vision": 0.208063,
      "text_ratio": 0.951663,
      "vision_ratio": 0.048337
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951663,
      0.048337
    ],
    "text_vision_ratio": "0.951663:0.048337"
  }
}
```


## === Rollout Step 185 ===
Step: 184/29790 | 2025-10-22 12:16:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 17.937 | 11.330 | 21.055 | 21.055 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 17.93677,
      "aei_text": 3.250252,
      "aei_vision": 0.181206,
      "text_ratio": 0.947193,
      "vision_ratio": 0.052807
    },
    "middle": {
      "mdi": 11.330323,
      "aei_text": 3.016563,
      "aei_vision": 0.266238,
      "text_ratio": 0.918899,
      "vision_ratio": 0.081101
    },
    "late": {
      "mdi": 21.055211,
      "aei_text": 3.315494,
      "aei_vision": 0.157467,
      "text_ratio": 0.954659,
      "vision_ratio": 0.045341
    },
    "all": {
      "mdi": 21.055211,
      "aei_text": 3.194103,
      "aei_vision": 0.201637,
      "text_ratio": 0.954659,
      "vision_ratio": 0.045341
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954659,
      0.045341
    ],
    "text_vision_ratio": "0.954659:0.045341"
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
      "mdi": 17.93677,
      "aei_text": 3.250252,
      "aei_vision": 0.181206,
      "text_ratio": 0.947193,
      "vision_ratio": 0.052807
    },
    "middle": {
      "mdi": 11.330323,
      "aei_text": 3.016563,
      "aei_vision": 0.266238,
      "text_ratio": 0.918899,
      "vision_ratio": 0.081101
    },
    "late": {
      "mdi": 21.055211,
      "aei_text": 3.315494,
      "aei_vision": 0.157467,
      "text_ratio": 0.954659,
      "vision_ratio": 0.045341
    },
    "all": {
      "mdi": 21.055211,
      "aei_text": 3.194103,
      "aei_vision": 0.201637,
      "text_ratio": 0.954659,
      "vision_ratio": 0.045341
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954659,
      0.045341
    ],
    "text_vision_ratio": "0.954659:0.045341"
  }
}
```


## === Rollout Step 186 ===
Step: 185/29790 | 2025-10-22 12:17:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.190 | 14.173 | 14.873 | 14.873 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 15.189775,
      "aei_text": 3.029756,
      "aei_vision": 0.19946,
      "text_ratio": 0.938233,
      "vision_ratio": 0.061767
    },
    "middle": {
      "mdi": 14.172964,
      "aei_text": 2.998979,
      "aei_vision": 0.211599,
      "text_ratio": 0.934093,
      "vision_ratio": 0.065907
    },
    "late": {
      "mdi": 14.872858,
      "aei_text": 3.020549,
      "aei_vision": 0.203091,
      "text_ratio": 0.936999,
      "vision_ratio": 0.063001
    },
    "all": {
      "mdi": 14.872858,
      "aei_text": 3.016428,
      "aei_vision": 0.204717,
      "text_ratio": 0.936999,
      "vision_ratio": 0.063001
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936999,
      0.063001
    ],
    "text_vision_ratio": "0.936999:0.063001"
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
      "mdi": 15.189775,
      "aei_text": 3.029756,
      "aei_vision": 0.19946,
      "text_ratio": 0.938233,
      "vision_ratio": 0.061767
    },
    "middle": {
      "mdi": 14.172964,
      "aei_text": 2.998979,
      "aei_vision": 0.211599,
      "text_ratio": 0.934093,
      "vision_ratio": 0.065907
    },
    "late": {
      "mdi": 14.872858,
      "aei_text": 3.020549,
      "aei_vision": 0.203091,
      "text_ratio": 0.936999,
      "vision_ratio": 0.063001
    },
    "all": {
      "mdi": 14.872858,
      "aei_text": 3.016428,
      "aei_vision": 0.204717,
      "text_ratio": 0.936999,
      "vision_ratio": 0.063001
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936999,
      0.063001
    ],
    "text_vision_ratio": "0.936999:0.063001"
  }
}
```


## === Rollout Step 187 ===
Step: 186/29790 | 2025-10-22 12:17:07

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 15.789 | 17.398 | 22.463 | 22.463 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
| Vision Tokens | 486.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Total Tokens | 486.0 ± 0.0 |
| Vision Ratio | 1.000 |
| Text Ratio | 1.000 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.788742,
      "aei_text": 3.476956,
      "aei_vision": 0.220217,
      "text_ratio": 0.940436,
      "vision_ratio": 0.059564
    },
    "middle": {
      "mdi": 17.397783,
      "aei_text": 3.531663,
      "aei_vision": 0.202995,
      "text_ratio": 0.945646,
      "vision_ratio": 0.054354
    },
    "late": {
      "mdi": 22.46345,
      "aei_text": 3.659057,
      "aei_vision": 0.162889,
      "text_ratio": 0.957381,
      "vision_ratio": 0.042619
    },
    "all": {
      "mdi": 22.46345,
      "aei_text": 3.555892,
      "aei_vision": 0.195367,
      "text_ratio": 0.957381,
      "vision_ratio": 0.042619
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957381,
      0.042619
    ],
    "text_vision_ratio": "0.957381:0.042619"
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 486,
    "text_tokens": 0,
    "total_tokens": 486
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.788742,
      "aei_text": 3.476956,
      "aei_vision": 0.220217,
      "text_ratio": 0.940436,
      "vision_ratio": 0.059564
    },
    "middle": {
      "mdi": 17.397783,
      "aei_text": 3.531663,
      "aei_vision": 0.202995,
      "text_ratio": 0.945646,
      "vision_ratio": 0.054354
    },
    "late": {
      "mdi": 22.46345,
      "aei_text": 3.659057,
      "aei_vision": 0.162889,
      "text_ratio": 0.957381,
      "vision_ratio": 0.042619
    },
    "all": {
      "mdi": 22.46345,
      "aei_text": 3.555892,
      "aei_vision": 0.195367,
      "text_ratio": 0.957381,
      "vision_ratio": 0.042619
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957381,
      0.042619
    ],
    "text_vision_ratio": "0.957381:0.042619"
  }
}
```


## === Rollout Step 188 ===
Step: 187/29790 | 2025-10-22 12:17:10

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 11.744 | 7.099 | 19.659 | 19.659 |
| MDI Std | 0.000 | 0.000 | 0.000 | 0.000 |
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
      "mdi": 11.743941,
      "aei_text": 2.787992,
      "aei_vision": 0.237398,
      "text_ratio": 0.921531,
      "vision_ratio": 0.078469
    },
    "middle": {
      "mdi": 7.099352,
      "aei_text": 2.514251,
      "aei_vision": 0.354152,
      "text_ratio": 0.876533,
      "vision_ratio": 0.123467
    },
    "late": {
      "mdi": 19.658804,
      "aei_text": 2.988208,
      "aei_vision": 0.152004,
      "text_ratio": 0.951594,
      "vision_ratio": 0.048406
    },
    "all": {
      "mdi": 19.658804,
      "aei_text": 2.763484,
      "aei_vision": 0.247851,
      "text_ratio": 0.951594,
      "vision_ratio": 0.048406
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951594,
      0.048406
    ],
    "text_vision_ratio": "0.951594:0.048406"
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
      "mdi": 11.743941,
      "aei_text": 2.787992,
      "aei_vision": 0.237398,
      "text_ratio": 0.921531,
      "vision_ratio": 0.078469
    },
    "middle": {
      "mdi": 7.099352,
      "aei_text": 2.514251,
      "aei_vision": 0.354152,
      "text_ratio": 0.876533,
      "vision_ratio": 0.123467
    },
    "late": {
      "mdi": 19.658804,
      "aei_text": 2.988208,
      "aei_vision": 0.152004,
      "text_ratio": 0.951594,
      "vision_ratio": 0.048406
    },
    "all": {
      "mdi": 19.658804,
      "aei_text": 2.763484,
      "aei_vision": 0.247851,
      "text_ratio": 0.951594,
      "vision_ratio": 0.048406
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951594,
      0.048406
    ],
    "text_vision_ratio": "0.951594:0.048406"
  }
}
```


## === Rollout Step 189 ===
Step: 188/29790 | 2025-10-22 12:17:13

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.490 | 6.781 | 18.592 | 18.592 |
| MDI Std | 0.135 | 0.779 | 0.205 | 0.205 |
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
      "mdi": 12.354881,
      "aei_text": 2.831933,
      "aei_vision": 0.229216,
      "text_ratio": 0.925121,
      "vision_ratio": 0.074879
    },
    "middle": {
      "mdi": 7.559688,
      "aei_text": 2.569028,
      "aei_vision": 0.339833,
      "text_ratio": 0.883173,
      "vision_ratio": 0.116827
    },
    "late": {
      "mdi": 18.797339,
      "aei_text": 2.997688,
      "aei_vision": 0.159474,
      "text_ratio": 0.949488,
      "vision_ratio": 0.050512
    },
    "all": {
      "mdi": 18.797339,
      "aei_text": 2.79955,
      "aei_vision": 0.242841,
      "text_ratio": 0.949488,
      "vision_ratio": 0.050512
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949488,
      0.050512
    ],
    "text_vision_ratio": "0.949488:0.050512"
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
      "mdi": 12.625289,
      "aei_text": 2.841752,
      "aei_vision": 0.225084,
      "text_ratio": 0.926607,
      "vision_ratio": 0.073393
    },
    "middle": {
      "mdi": 6.00142,
      "aei_text": 2.418805,
      "aei_vision": 0.403039,
      "text_ratio": 0.857172,
      "vision_ratio": 0.142828
    },
    "late": {
      "mdi": 18.386466,
      "aei_text": 2.990188,
      "aei_vision": 0.16263,
      "text_ratio": 0.948418,
      "vision_ratio": 0.051582
    },
    "all": {
      "mdi": 18.386466,
      "aei_text": 2.750248,
      "aei_vision": 0.263584,
      "text_ratio": 0.948418,
      "vision_ratio": 0.051582
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948418,
      0.051582
    ],
    "text_vision_ratio": "0.948418:0.051582"
  }
}
```

