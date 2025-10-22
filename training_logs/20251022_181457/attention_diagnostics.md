# Attention Diagnostics Log

This file contains MDI attention diagnostics from GRPO training.


## === Rollout Step 1 ===
Step: 0/43 | 2025-10-22 18:16:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 35.089 | 34.179 | 26.922 | 26.922 |
| MDI Std | 12.077 | 16.523 | 11.382 | 11.382 |
| Vision Tokens | 363.8 ± 115.5 |
| Text Tokens | 161.9 ± 4.2 |
| Total Tokens | 525.6 ± 116.6 |
| Vision Ratio | 0.667 |
| Text Ratio | 0.333 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.207103,
      "aei_text": 3.275241,
      "aei_vision": 0.079482,
      "text_ratio": 0.976307,
      "vision_ratio": 0.023693
    },
    "middle": {
      "mdi": 56.030843,
      "aei_text": 3.325021,
      "aei_vision": 0.059343,
      "text_ratio": 0.982466,
      "vision_ratio": 0.017534
    },
    "late": {
      "mdi": 31.12037,
      "aei_text": 3.216251,
      "aei_vision": 0.103349,
      "text_ratio": 0.968867,
      "vision_ratio": 0.031133
    },
    "all": {
      "mdi": 31.12037,
      "aei_text": 3.272177,
      "aei_vision": 0.080722,
      "text_ratio": 0.968867,
      "vision_ratio": 0.031133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968867,
      0.031133
    ],
    "text_vision_ratio": "0.968867:0.031133",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.036773,
      "aei_text": 3.305104,
      "aei_vision": 0.067401,
      "text_ratio": 0.980015,
      "vision_ratio": 0.019985
    },
    "middle": {
      "mdi": 30.56318,
      "aei_text": 3.211943,
      "aei_vision": 0.105092,
      "text_ratio": 0.968318,
      "vision_ratio": 0.031682
    },
    "late": {
      "mdi": 21.417734,
      "aei_text": 3.112502,
      "aei_vision": 0.145324,
      "text_ratio": 0.955392,
      "vision_ratio": 0.044608
    },
    "all": {
      "mdi": 21.417734,
      "aei_text": 3.209834,
      "aei_vision": 0.105945,
      "text_ratio": 0.955392,
      "vision_ratio": 0.044608
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955392,
      0.044608
    ],
    "text_vision_ratio": "0.955392:0.044608",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.265384,
      "aei_text": 3.269138,
      "aei_vision": 0.087726,
      "text_ratio": 0.973867,
      "vision_ratio": 0.026133
    },
    "middle": {
      "mdi": 38.513238,
      "aei_text": 3.275779,
      "aei_vision": 0.085056,
      "text_ratio": 0.974692,
      "vision_ratio": 0.025308
    },
    "late": {
      "mdi": 40.11687,
      "aei_text": 3.283742,
      "aei_vision": 0.081854,
      "text_ratio": 0.975679,
      "vision_ratio": 0.024321
    },
    "all": {
      "mdi": 40.11687,
      "aei_text": 3.276221,
      "aei_vision": 0.084878,
      "text_ratio": 0.975679,
      "vision_ratio": 0.024321
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975679,
      0.024321
    ],
    "text_vision_ratio": "0.975679:0.024321",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.090512,
      "aei_text": 3.278716,
      "aei_vision": 0.083875,
      "text_ratio": 0.975056,
      "vision_ratio": 0.024944
    },
    "middle": {
      "mdi": 44.101997,
      "aei_text": 3.301157,
      "aei_vision": 0.074853,
      "text_ratio": 0.977828,
      "vision_ratio": 0.022172
    },
    "late": {
      "mdi": 28.911259,
      "aei_text": 3.211081,
      "aei_vision": 0.111067,
      "text_ratio": 0.966568,
      "vision_ratio": 0.033432
    },
    "all": {
      "mdi": 28.911259,
      "aei_text": 3.263645,
      "aei_vision": 0.089934,
      "text_ratio": 0.966568,
      "vision_ratio": 0.033432
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966568,
      0.033432
    ],
    "text_vision_ratio": "0.966568:0.033432",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.842048,
      "aei_text": 3.109403,
      "aei_vision": 0.082168,
      "text_ratio": 0.974255,
      "vision_ratio": 0.025745
    },
    "middle": {
      "mdi": 36.526007,
      "aei_text": 3.103002,
      "aei_vision": 0.084953,
      "text_ratio": 0.973352,
      "vision_ratio": 0.026648
    },
    "late": {
      "mdi": 27.716529,
      "aei_text": 3.045697,
      "aei_vision": 0.109887,
      "text_ratio": 0.965177,
      "vision_ratio": 0.034823
    },
    "all": {
      "mdi": 27.716529,
      "aei_text": 3.086037,
      "aei_vision": 0.092335,
      "text_ratio": 0.965177,
      "vision_ratio": 0.034823
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965177,
      0.034823
    ],
    "text_vision_ratio": "0.965177:0.034823",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.246464,
      "aei_text": 3.115787,
      "aei_vision": 0.07939,
      "text_ratio": 0.975153,
      "vision_ratio": 0.024847
    },
    "middle": {
      "mdi": 54.668932,
      "aei_text": 3.165183,
      "aei_vision": 0.057897,
      "text_ratio": 0.982037,
      "vision_ratio": 0.017963
    },
    "late": {
      "mdi": 34.079526,
      "aei_text": 3.089872,
      "aei_vision": 0.090667,
      "text_ratio": 0.971493,
      "vision_ratio": 0.028507
    },
    "all": {
      "mdi": 34.079526,
      "aei_text": 3.123615,
      "aei_vision": 0.075984,
      "text_ratio": 0.971493,
      "vision_ratio": 0.028507
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971493,
      0.028507
    ],
    "text_vision_ratio": "0.971493:0.028507",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.915515,
      "aei_text": 2.947723,
      "aei_vision": 0.073849,
      "text_ratio": 0.975559,
      "vision_ratio": 0.024441
    },
    "middle": {
      "mdi": 21.65379,
      "aei_text": 2.82834,
      "aei_vision": 0.130616,
      "text_ratio": 0.955857,
      "vision_ratio": 0.044143
    },
    "late": {
      "mdi": 19.521313,
      "aei_text": 2.801252,
      "aei_vision": 0.143497,
      "text_ratio": 0.95127,
      "vision_ratio": 0.04873
    },
    "all": {
      "mdi": 19.521313,
      "aei_text": 2.859082,
      "aei_vision": 0.115998,
      "text_ratio": 0.95127,
      "vision_ratio": 0.04873
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95127,
      0.04873
    ],
    "text_vision_ratio": "0.951270:0.048730",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.531614,
      "aei_text": 2.949968,
      "aei_vision": 0.072782,
      "text_ratio": 0.975922,
      "vision_ratio": 0.024078
    },
    "middle": {
      "mdi": 31.238676,
      "aei_text": 2.907306,
      "aei_vision": 0.093068,
      "text_ratio": 0.968981,
      "vision_ratio": 0.031019
    },
    "late": {
      "mdi": 35.468253,
      "aei_text": 2.92934,
      "aei_vision": 0.08259,
      "text_ratio": 0.972579,
      "vision_ratio": 0.027421
    },
    "all": {
      "mdi": 35.468253,
      "aei_text": 2.928868,
      "aei_vision": 0.082815,
      "text_ratio": 0.972579,
      "vision_ratio": 0.027421
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972579,
      0.027421
    ],
    "text_vision_ratio": "0.972579:0.027421",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 162.0,
    "total_tokens": 693.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.976999,
      "aei_text": 3.219925,
      "aei_vision": 0.322735,
      "text_ratio": 0.9089,
      "vision_ratio": 0.0911
    },
    "middle": {
      "mdi": 8.304476,
      "aei_text": 3.067167,
      "aei_vision": 0.369339,
      "text_ratio": 0.892525,
      "vision_ratio": 0.107475
    },
    "late": {
      "mdi": 14.141996,
      "aei_text": 3.472853,
      "aei_vision": 0.24557,
      "text_ratio": 0.933959,
      "vision_ratio": 0.066041
    },
    "all": {
      "mdi": 14.141996,
      "aei_text": 3.253305,
      "aei_vision": 0.312551,
      "text_ratio": 0.933959,
      "vision_ratio": 0.066041
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.933959,
      0.066041
    ],
    "text_vision_ratio": "0.933959:0.066041",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 162.0,
    "total_tokens": 693.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.739949,
      "aei_text": 3.344108,
      "aei_vision": 0.284849,
      "text_ratio": 0.921507,
      "vision_ratio": 0.078493
    },
    "middle": {
      "mdi": 8.248738,
      "aei_text": 3.061313,
      "aei_vision": 0.371125,
      "text_ratio": 0.891877,
      "vision_ratio": 0.108123
    },
    "late": {
      "mdi": 11.822649,
      "aei_text": 3.349221,
      "aei_vision": 0.283289,
      "text_ratio": 0.922013,
      "vision_ratio": 0.077987
    },
    "all": {
      "mdi": 11.822649,
      "aei_text": 3.251586,
      "aei_vision": 0.313075,
      "text_ratio": 0.922013,
      "vision_ratio": 0.077987
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.922013,
      0.077987
    ],
    "text_vision_ratio": "0.922013:0.077987",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 90.0,
    "text_tokens": 158.0,
    "total_tokens": 248.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.526874,
      "aei_text": 1.522801,
      "aei_vision": 0.082194,
      "text_ratio": 0.948789,
      "vision_ratio": 0.051211
    },
    "middle": {
      "mdi": 11.192401,
      "aei_text": 1.493605,
      "aei_vision": 0.133448,
      "text_ratio": 0.917982,
      "vision_ratio": 0.082018
    },
    "late": {
      "mdi": 7.435745,
      "aei_text": 1.457934,
      "aei_vision": 0.196071,
      "text_ratio": 0.881457,
      "vision_ratio": 0.118543
    },
    "all": {
      "mdi": 7.435745,
      "aei_text": 1.49145,
      "aei_vision": 0.137232,
      "text_ratio": 0.881457,
      "vision_ratio": 0.118543
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.881457,
      0.118543
    ],
    "text_vision_ratio": "0.881457:0.118543",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 90.0,
    "text_tokens": 158.0,
    "total_tokens": 248.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 20.248543,
      "aei_text": 1.526673,
      "aei_vision": 0.075397,
      "text_ratio": 0.952938,
      "vision_ratio": 0.047062
    },
    "middle": {
      "mdi": 14.128786,
      "aei_text": 1.508791,
      "aei_vision": 0.106788,
      "text_ratio": 0.933901,
      "vision_ratio": 0.066099
    },
    "late": {
      "mdi": 7.622455,
      "aei_text": 1.46048,
      "aei_vision": 0.191602,
      "text_ratio": 0.884024,
      "vision_ratio": 0.115976
    },
    "all": {
      "mdi": 7.622455,
      "aei_text": 1.498652,
      "aei_vision": 0.124589,
      "text_ratio": 0.884024,
      "vision_ratio": 0.115976
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.884024,
      0.115976
    ],
    "text_vision_ratio": "0.884024:0.115976",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 163.0,
    "total_tokens": 533.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.679865,
      "aei_text": 3.111843,
      "aei_vision": 0.069648,
      "text_ratio": 0.978109,
      "vision_ratio": 0.021891
    },
    "middle": {
      "mdi": 55.047357,
      "aei_text": 3.140439,
      "aei_vision": 0.05705,
      "text_ratio": 0.982158,
      "vision_ratio": 0.017842
    },
    "late": {
      "mdi": 36.952984,
      "aei_text": 3.080698,
      "aei_vision": 0.083368,
      "text_ratio": 0.973652,
      "vision_ratio": 0.026348
    },
    "all": {
      "mdi": 36.952984,
      "aei_text": 3.110984,
      "aei_vision": 0.070026,
      "text_ratio": 0.973652,
      "vision_ratio": 0.026348
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973652,
      0.026348
    ],
    "text_vision_ratio": "0.973652:0.026348",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 163.0,
    "total_tokens": 533.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.678655,
      "aei_text": 3.111839,
      "aei_vision": 0.069649,
      "text_ratio": 0.978108,
      "vision_ratio": 0.021892
    },
    "middle": {
      "mdi": 46.824655,
      "aei_text": 3.11875,
      "aei_vision": 0.066605,
      "text_ratio": 0.97909,
      "vision_ratio": 0.02091
    },
    "late": {
      "mdi": 37.60853,
      "aei_text": 3.083809,
      "aei_vision": 0.081998,
      "text_ratio": 0.974099,
      "vision_ratio": 0.025901
    },
    "all": {
      "mdi": 37.60853,
      "aei_text": 3.104792,
      "aei_vision": 0.072754,
      "text_ratio": 0.974099,
      "vision_ratio": 0.025901
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974099,
      0.025901
    ],
    "text_vision_ratio": "0.974099:0.025901",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.879519,
      "aei_text": 3.286568,
      "aei_vision": 0.0749,
      "text_ratio": 0.977718,
      "vision_ratio": 0.022282
    },
    "middle": {
      "mdi": 38.940237,
      "aei_text": 3.264488,
      "aei_vision": 0.083833,
      "text_ratio": 0.974963,
      "vision_ratio": 0.025037
    },
    "late": {
      "mdi": 43.146518,
      "aei_text": 3.283594,
      "aei_vision": 0.076103,
      "text_ratio": 0.977348,
      "vision_ratio": 0.022652
    },
    "all": {
      "mdi": 43.146518,
      "aei_text": 3.278213,
      "aei_vision": 0.07828,
      "text_ratio": 0.977348,
      "vision_ratio": 0.022652
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977348,
      0.022652
    ],
    "text_vision_ratio": "0.977348:0.022652",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.56254,
      "aei_text": 3.285294,
      "aei_vision": 0.075416,
      "text_ratio": 0.97756,
      "vision_ratio": 0.02244
    },
    "middle": {
      "mdi": 50.885744,
      "aei_text": 3.310877,
      "aei_vision": 0.065065,
      "text_ratio": 0.980727,
      "vision_ratio": 0.019273
    },
    "late": {
      "mdi": 33.666908,
      "aei_text": 3.234251,
      "aei_vision": 0.096066,
      "text_ratio": 0.971154,
      "vision_ratio": 0.028846
    },
    "all": {
      "mdi": 33.666908,
      "aei_text": 3.27681,
      "aei_vision": 0.078848,
      "text_ratio": 0.971154,
      "vision_ratio": 0.028846
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971154,
      0.028846
    ],
    "text_vision_ratio": "0.971154:0.028846",
    "skip_reason": null
  }
}
```


## === Rollout Step 2 ===
Step: 1/43 | 2025-10-22 18:18:27

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 34.352 | 32.597 | 23.895 | 23.895 |
| MDI Std | 9.782 | 13.339 | 9.470 | 9.470 |
| Vision Tokens | 338.9 ± 62.1 |
| Text Tokens | 163.2 ± 3.7 |
| Total Tokens | 502.1 ± 63.0 |
| Vision Ratio | 0.670 |
| Text Ratio | 0.330 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 157.0,
    "total_tokens": 550.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.695077,
      "aei_text": 3.31337,
      "aei_vision": 0.075829,
      "text_ratio": 0.977626,
      "vision_ratio": 0.022374
    },
    "middle": {
      "mdi": 27.895457,
      "aei_text": 3.214714,
      "aei_vision": 0.115241,
      "text_ratio": 0.965392,
      "vision_ratio": 0.034608
    },
    "late": {
      "mdi": 21.272097,
      "aei_text": 3.134351,
      "aei_vision": 0.147346,
      "text_ratio": 0.955101,
      "vision_ratio": 0.044899
    },
    "all": {
      "mdi": 21.272097,
      "aei_text": 3.220795,
      "aei_vision": 0.112812,
      "text_ratio": 0.955101,
      "vision_ratio": 0.044899
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955101,
      0.044899
    ],
    "text_vision_ratio": "0.955101:0.044899",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 157.0,
    "total_tokens": 550.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.283138,
      "aei_text": 3.311662,
      "aei_vision": 0.076512,
      "text_ratio": 0.977418,
      "vision_ratio": 0.022582
    },
    "middle": {
      "mdi": 37.3384,
      "aei_text": 3.283085,
      "aei_vision": 0.087928,
      "text_ratio": 0.973916,
      "vision_ratio": 0.026084
    },
    "late": {
      "mdi": 26.904876,
      "aei_text": 3.204997,
      "aei_vision": 0.119123,
      "text_ratio": 0.964164,
      "vision_ratio": 0.035836
    },
    "all": {
      "mdi": 26.904876,
      "aei_text": 3.266583,
      "aei_vision": 0.09452,
      "text_ratio": 0.964164,
      "vision_ratio": 0.035836
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964164,
      0.035836
    ],
    "text_vision_ratio": "0.964164:0.035836",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.025276,
      "aei_text": 2.644154,
      "aei_vision": 0.292972,
      "text_ratio": 0.900252,
      "vision_ratio": 0.099748
    },
    "middle": {
      "mdi": 7.904986,
      "aei_text": 2.569549,
      "aei_vision": 0.325054,
      "text_ratio": 0.887703,
      "vision_ratio": 0.112297
    },
    "late": {
      "mdi": 13.08004,
      "aei_text": 2.823471,
      "aei_vision": 0.215861,
      "text_ratio": 0.928977,
      "vision_ratio": 0.071023
    },
    "all": {
      "mdi": 13.08004,
      "aei_text": 2.679091,
      "aei_vision": 0.277948,
      "text_ratio": 0.928977,
      "vision_ratio": 0.071023
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928977,
      0.071023
    ],
    "text_vision_ratio": "0.928977:0.071023",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.77309,
      "aei_text": 2.813266,
      "aei_vision": 0.220249,
      "text_ratio": 0.927395,
      "vision_ratio": 0.072605
    },
    "middle": {
      "mdi": 7.588096,
      "aei_text": 2.545386,
      "aei_vision": 0.335445,
      "text_ratio": 0.88356,
      "vision_ratio": 0.11644
    },
    "late": {
      "mdi": 9.371386,
      "aei_text": 2.664313,
      "aei_vision": 0.284303,
      "text_ratio": 0.903581,
      "vision_ratio": 0.096419
    },
    "all": {
      "mdi": 9.371386,
      "aei_text": 2.674289,
      "aei_vision": 0.280013,
      "text_ratio": 0.903581,
      "vision_ratio": 0.096419
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.903581,
      0.096419
    ],
    "text_vision_ratio": "0.903581:0.096419",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 161.0,
    "total_tokens": 416.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.738368,
      "aei_text": 2.464615,
      "aei_vision": 0.075282,
      "text_ratio": 0.97036,
      "vision_ratio": 0.02964
    },
    "middle": {
      "mdi": 34.67445,
      "aei_text": 2.470982,
      "aei_vision": 0.071262,
      "text_ratio": 0.971969,
      "vision_ratio": 0.028031
    },
    "late": {
      "mdi": 20.928729,
      "aei_text": 2.402067,
      "aei_vision": 0.114774,
      "text_ratio": 0.954398,
      "vision_ratio": 0.045602
    },
    "all": {
      "mdi": 20.928729,
      "aei_text": 2.445905,
      "aei_vision": 0.087095,
      "text_ratio": 0.954398,
      "vision_ratio": 0.045602
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954398,
      0.045602
    ],
    "text_vision_ratio": "0.954398:0.045602",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 161.0,
    "total_tokens": 416.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.397813,
      "aei_text": 2.46342,
      "aei_vision": 0.076037,
      "text_ratio": 0.970058,
      "vision_ratio": 0.029942
    },
    "middle": {
      "mdi": 35.510016,
      "aei_text": 2.473524,
      "aei_vision": 0.069657,
      "text_ratio": 0.97261,
      "vision_ratio": 0.02739
    },
    "late": {
      "mdi": 19.951061,
      "aei_text": 2.393814,
      "aei_vision": 0.119984,
      "text_ratio": 0.95227,
      "vision_ratio": 0.04773
    },
    "all": {
      "mdi": 19.951061,
      "aei_text": 2.443588,
      "aei_vision": 0.088558,
      "text_ratio": 0.95227,
      "vision_ratio": 0.04773
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95227,
      0.04773
    ],
    "text_vision_ratio": "0.952270:0.047730",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.694491,
      "aei_text": 3.24165,
      "aei_vision": 0.081665,
      "text_ratio": 0.975427,
      "vision_ratio": 0.024573
    },
    "middle": {
      "mdi": 49.714563,
      "aei_text": 3.279948,
      "aei_vision": 0.065976,
      "text_ratio": 0.980282,
      "vision_ratio": 0.019718
    },
    "late": {
      "mdi": 37.226308,
      "aei_text": 3.229246,
      "aei_vision": 0.086746,
      "text_ratio": 0.97384,
      "vision_ratio": 0.02616
    },
    "all": {
      "mdi": 37.226308,
      "aei_text": 3.250283,
      "aei_vision": 0.078129,
      "text_ratio": 0.97384,
      "vision_ratio": 0.02616
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97384,
      0.02616
    ],
    "text_vision_ratio": "0.973840:0.026160",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.595628,
      "aei_text": 3.241181,
      "aei_vision": 0.081857,
      "text_ratio": 0.975367,
      "vision_ratio": 0.024633
    },
    "middle": {
      "mdi": 44.871614,
      "aei_text": 3.263463,
      "aei_vision": 0.072729,
      "text_ratio": 0.9782,
      "vision_ratio": 0.0218
    },
    "late": {
      "mdi": 47.885849,
      "aei_text": 3.274096,
      "aei_vision": 0.068373,
      "text_ratio": 0.979544,
      "vision_ratio": 0.020456
    },
    "all": {
      "mdi": 47.885849,
      "aei_text": 3.259581,
      "aei_vision": 0.074319,
      "text_ratio": 0.979544,
      "vision_ratio": 0.020456
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979544,
      0.020456
    ],
    "text_vision_ratio": "0.979544:0.020456",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 164.0,
    "total_tokens": 465.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.613023,
      "aei_text": 2.712771,
      "aei_vision": 0.066796,
      "text_ratio": 0.975969,
      "vision_ratio": 0.024031
    },
    "middle": {
      "mdi": 54.557561,
      "aei_text": 2.743086,
      "aei_vision": 0.050279,
      "text_ratio": 0.982001,
      "vision_ratio": 0.017999
    },
    "late": {
      "mdi": 31.067335,
      "aei_text": 2.677205,
      "aei_vision": 0.086174,
      "text_ratio": 0.968816,
      "vision_ratio": 0.031184
    },
    "all": {
      "mdi": 31.067335,
      "aei_text": 2.711023,
      "aei_vision": 0.067748,
      "text_ratio": 0.968816,
      "vision_ratio": 0.031184
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968816,
      0.031184
    ],
    "text_vision_ratio": "0.968816:0.031184",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 164.0,
    "total_tokens": 465.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.400881,
      "aei_text": 2.720327,
      "aei_vision": 0.062679,
      "text_ratio": 0.977478,
      "vision_ratio": 0.022522
    },
    "middle": {
      "mdi": 41.086646,
      "aei_text": 2.714124,
      "aei_vision": 0.066059,
      "text_ratio": 0.976239,
      "vision_ratio": 0.023761
    },
    "late": {
      "mdi": 25.871637,
      "aei_text": 2.647546,
      "aei_vision": 0.102334,
      "text_ratio": 0.962786,
      "vision_ratio": 0.037214
    },
    "all": {
      "mdi": 25.871637,
      "aei_text": 2.693999,
      "aei_vision": 0.077024,
      "text_ratio": 0.962786,
      "vision_ratio": 0.037214
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962786,
      0.037214
    ],
    "text_vision_ratio": "0.962786:0.037214",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.224265,
      "aei_text": 3.166105,
      "aei_vision": 0.085055,
      "text_ratio": 0.973839,
      "vision_ratio": 0.026161
    },
    "middle": {
      "mdi": 26.943088,
      "aei_text": 3.095473,
      "aei_vision": 0.114889,
      "text_ratio": 0.964213,
      "vision_ratio": 0.035787
    },
    "late": {
      "mdi": 18.762899,
      "aei_text": 2.990175,
      "aei_vision": 0.159366,
      "text_ratio": 0.9494,
      "vision_ratio": 0.0506
    },
    "all": {
      "mdi": 18.762899,
      "aei_text": 3.083924,
      "aei_vision": 0.119768,
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
    "text_vision_ratio": "0.949400:0.050600",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.508877,
      "aei_text": 3.167542,
      "aei_vision": 0.084448,
      "text_ratio": 0.974032,
      "vision_ratio": 0.025968
    },
    "middle": {
      "mdi": 33.430939,
      "aei_text": 3.144768,
      "aei_vision": 0.094068,
      "text_ratio": 0.970956,
      "vision_ratio": 0.029044
    },
    "late": {
      "mdi": 24.914727,
      "aei_text": 3.075251,
      "aei_vision": 0.123431,
      "text_ratio": 0.961412,
      "vision_ratio": 0.038588
    },
    "all": {
      "mdi": 24.914727,
      "aei_text": 3.129193,
      "aei_vision": 0.100646,
      "text_ratio": 0.961412,
      "vision_ratio": 0.038588
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961412,
      0.038588
    ],
    "text_vision_ratio": "0.961412:0.038588",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 161.0,
    "total_tokens": 397.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 30.787295,
      "aei_text": 2.353771,
      "aei_vision": 0.076453,
      "text_ratio": 0.968541,
      "vision_ratio": 0.031459
    },
    "middle": {
      "mdi": 17.494866,
      "aei_text": 2.275206,
      "aei_vision": 0.13005,
      "text_ratio": 0.945931,
      "vision_ratio": 0.054069
    },
    "late": {
      "mdi": 13.581242,
      "aei_text": 2.225624,
      "aei_vision": 0.163875,
      "text_ratio": 0.931419,
      "vision_ratio": 0.068581
    },
    "all": {
      "mdi": 13.581242,
      "aei_text": 2.284885,
      "aei_vision": 0.123447,
      "text_ratio": 0.931419,
      "vision_ratio": 0.068581
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931419,
      0.068581
    ],
    "text_vision_ratio": "0.931419:0.068581",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 161.0,
    "total_tokens": 397.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 30.642054,
      "aei_text": 2.353264,
      "aei_vision": 0.076799,
      "text_ratio": 0.968396,
      "vision_ratio": 0.031604
    },
    "middle": {
      "mdi": 22.746527,
      "aei_text": 2.316554,
      "aei_vision": 0.101842,
      "text_ratio": 0.957889,
      "vision_ratio": 0.042111
    },
    "late": {
      "mdi": 16.264377,
      "aei_text": 2.261976,
      "aei_vision": 0.139075,
      "text_ratio": 0.942077,
      "vision_ratio": 0.057923
    },
    "all": {
      "mdi": 16.264377,
      "aei_text": 2.310596,
      "aei_vision": 0.105907,
      "text_ratio": 0.942077,
      "vision_ratio": 0.057923
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942077,
      0.057923
    ],
    "text_vision_ratio": "0.942077:0.057923",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.026835,
      "aei_text": 2.91838,
      "aei_vision": 0.076745,
      "text_ratio": 0.974377,
      "vision_ratio": 0.025623
    },
    "middle": {
      "mdi": 33.127571,
      "aei_text": 2.896188,
      "aei_vision": 0.087425,
      "text_ratio": 0.970698,
      "vision_ratio": 0.029302
    },
    "late": {
      "mdi": 23.246895,
      "aei_text": 2.825313,
      "aei_vision": 0.121535,
      "text_ratio": 0.958758,
      "vision_ratio": 0.041242
    },
    "all": {
      "mdi": 23.246895,
      "aei_text": 2.879955,
      "aei_vision": 0.095238,
      "text_ratio": 0.958758,
      "vision_ratio": 0.041242
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958758,
      0.041242
    ],
    "text_vision_ratio": "0.958758:0.041242",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.228214,
      "aei_text": 2.919176,
      "aei_vision": 0.076362,
      "text_ratio": 0.974508,
      "vision_ratio": 0.025492
    },
    "middle": {
      "mdi": 46.672452,
      "aei_text": 2.94666,
      "aei_vision": 0.063135,
      "text_ratio": 0.979024,
      "vision_ratio": 0.020976
    },
    "late": {
      "mdi": 31.991201,
      "aei_text": 2.890129,
      "aei_vision": 0.090341,
      "text_ratio": 0.969689,
      "vision_ratio": 0.030311
    },
    "all": {
      "mdi": 31.991201,
      "aei_text": 2.918654,
      "aei_vision": 0.076613,
      "text_ratio": 0.969689,
      "vision_ratio": 0.030311
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969689,
      0.030311
    ],
    "text_vision_ratio": "0.969689:0.030311",
    "skip_reason": null
  }
}
```


## === Rollout Step 3 ===
Step: 2/43 | 2025-10-22 18:19:28

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 33.613 | 26.479 | 25.888 | 25.888 |
| MDI Std | 10.020 | 9.831 | 8.227 | 8.227 |
| Vision Tokens | 358.5 ± 30.4 |
| Text Tokens | 165.8 ± 4.7 |
| Total Tokens | 524.2 ± 30.7 |
| Vision Ratio | 0.683 |
| Text Ratio | 0.317 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.093186,
      "aei_text": 2.900894,
      "aei_vision": 0.074205,
      "text_ratio": 0.975058,
      "vision_ratio": 0.024942
    },
    "middle": {
      "mdi": 27.437947,
      "aei_text": 2.840679,
      "aei_vision": 0.103531,
      "text_ratio": 0.964836,
      "vision_ratio": 0.035164
    },
    "late": {
      "mdi": 21.319368,
      "aei_text": 2.78503,
      "aei_vision": 0.130634,
      "text_ratio": 0.955196,
      "vision_ratio": 0.044804
    },
    "all": {
      "mdi": 21.319368,
      "aei_text": 2.842222,
      "aei_vision": 0.102779,
      "text_ratio": 0.955196,
      "vision_ratio": 0.044804
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955196,
      0.044804
    ],
    "text_vision_ratio": "0.955196:0.044804",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.80492,
      "aei_text": 2.903484,
      "aei_vision": 0.072943,
      "text_ratio": 0.975493,
      "vision_ratio": 0.024507
    },
    "middle": {
      "mdi": 29.385013,
      "aei_text": 2.853844,
      "aei_vision": 0.097119,
      "text_ratio": 0.967089,
      "vision_ratio": 0.032911
    },
    "late": {
      "mdi": 38.478063,
      "aei_text": 2.898581,
      "aei_vision": 0.075331,
      "text_ratio": 0.974669,
      "vision_ratio": 0.025331
    },
    "all": {
      "mdi": 38.478063,
      "aei_text": 2.885303,
      "aei_vision": 0.081798,
      "text_ratio": 0.974669,
      "vision_ratio": 0.025331
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974669,
      0.025331
    ],
    "text_vision_ratio": "0.974669:0.025331",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.598244,
      "aei_text": 2.924392,
      "aei_vision": 0.073852,
      "text_ratio": 0.975368,
      "vision_ratio": 0.024632
    },
    "middle": {
      "mdi": 22.536395,
      "aei_text": 2.818024,
      "aei_vision": 0.125043,
      "text_ratio": 0.957513,
      "vision_ratio": 0.042487
    },
    "late": {
      "mdi": 21.823223,
      "aei_text": 2.810271,
      "aei_vision": 0.128774,
      "text_ratio": 0.956185,
      "vision_ratio": 0.043815
    },
    "all": {
      "mdi": 21.823223,
      "aei_text": 2.8509,
      "aei_vision": 0.109221,
      "text_ratio": 0.956185,
      "vision_ratio": 0.043815
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956185,
      0.043815
    ],
    "text_vision_ratio": "0.956185:0.043815",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.827091,
      "aei_text": 2.913462,
      "aei_vision": 0.079112,
      "text_ratio": 0.973564,
      "vision_ratio": 0.026436
    },
    "middle": {
      "mdi": 36.995797,
      "aei_text": 2.914172,
      "aei_vision": 0.07877,
      "text_ratio": 0.973681,
      "vision_ratio": 0.026319
    },
    "late": {
      "mdi": 31.268651,
      "aei_text": 2.886062,
      "aei_vision": 0.092299,
      "text_ratio": 0.96901,
      "vision_ratio": 0.03099
    },
    "all": {
      "mdi": 31.268651,
      "aei_text": 2.904568,
      "aei_vision": 0.083392,
      "text_ratio": 0.96901,
      "vision_ratio": 0.03099
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96901,
      0.03099
    ],
    "text_vision_ratio": "0.969010:0.030990",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.116013,
      "aei_text": 3.21029,
      "aei_vision": 0.088888,
      "text_ratio": 0.973057,
      "vision_ratio": 0.026943
    },
    "middle": {
      "mdi": 27.657388,
      "aei_text": 3.149658,
      "aei_vision": 0.113881,
      "text_ratio": 0.965105,
      "vision_ratio": 0.034895
    },
    "late": {
      "mdi": 22.128631,
      "aei_text": 3.087453,
      "aei_vision": 0.139523,
      "text_ratio": 0.956764,
      "vision_ratio": 0.043236
    },
    "all": {
      "mdi": 22.128631,
      "aei_text": 3.149154,
      "aei_vision": 0.114089,
      "text_ratio": 0.956764,
      "vision_ratio": 0.043236
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956764,
      0.043236
    ],
    "text_vision_ratio": "0.956764:0.043236",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.935762,
      "aei_text": 3.220012,
      "aei_vision": 0.084881,
      "text_ratio": 0.974317,
      "vision_ratio": 0.025683
    },
    "middle": {
      "mdi": 31.466513,
      "aei_text": 3.180708,
      "aei_vision": 0.101082,
      "text_ratio": 0.969199,
      "vision_ratio": 0.030801
    },
    "late": {
      "mdi": 30.359839,
      "aei_text": 3.17243,
      "aei_vision": 0.104494,
      "text_ratio": 0.968112,
      "vision_ratio": 0.031888
    },
    "all": {
      "mdi": 30.359839,
      "aei_text": 3.191053,
      "aei_vision": 0.096818,
      "text_ratio": 0.968112,
      "vision_ratio": 0.031888
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968112,
      0.031888
    ],
    "text_vision_ratio": "0.968112:0.031888",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.490932,
      "aei_text": 2.640987,
      "aei_vision": 0.311036,
      "text_ratio": 0.894636,
      "vision_ratio": 0.105364
    },
    "middle": {
      "mdi": 8.294128,
      "aei_text": 2.62733,
      "aei_vision": 0.31677,
      "text_ratio": 0.892405,
      "vision_ratio": 0.107595
    },
    "late": {
      "mdi": 16.754547,
      "aei_text": 2.960898,
      "aei_vision": 0.176722,
      "text_ratio": 0.943676,
      "vision_ratio": 0.056324
    },
    "all": {
      "mdi": 16.754547,
      "aei_text": 2.743137,
      "aei_vision": 0.268149,
      "text_ratio": 0.943676,
      "vision_ratio": 0.056324
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943676,
      0.056324
    ],
    "text_vision_ratio": "0.943676:0.056324",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 6.483439,
      "aei_text": 2.473229,
      "aei_vision": 0.381469,
      "text_ratio": 0.866372,
      "vision_ratio": 0.133628
    },
    "middle": {
      "mdi": 4.766537,
      "aei_text": 2.255003,
      "aei_vision": 0.47309,
      "text_ratio": 0.826586,
      "vision_ratio": 0.173414
    },
    "late": {
      "mdi": 10.035164,
      "aei_text": 2.73312,
      "aei_vision": 0.272354,
      "text_ratio": 0.909381,
      "vision_ratio": 0.090619
    },
    "all": {
      "mdi": 10.035164,
      "aei_text": 2.487073,
      "aei_vision": 0.375656,
      "text_ratio": 0.909381,
      "vision_ratio": 0.090619
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.909381,
      0.090619
    ],
    "text_vision_ratio": "0.909381:0.090619",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.950169,
      "aei_text": 2.949197,
      "aei_vision": 0.084383,
      "text_ratio": 0.972184,
      "vision_ratio": 0.027816
    },
    "middle": {
      "mdi": 23.739304,
      "aei_text": 2.871345,
      "aei_vision": 0.120953,
      "text_ratio": 0.959578,
      "vision_ratio": 0.040422
    },
    "late": {
      "mdi": 22.18959,
      "aei_text": 2.854936,
      "aei_vision": 0.128661,
      "text_ratio": 0.956877,
      "vision_ratio": 0.043123
    },
    "all": {
      "mdi": 22.18959,
      "aei_text": 2.891818,
      "aei_vision": 0.111336,
      "text_ratio": 0.956877,
      "vision_ratio": 0.043123
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956877,
      0.043123
    ],
    "text_vision_ratio": "0.956877:0.043123",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.508768,
      "aei_text": 2.960793,
      "aei_vision": 0.078936,
      "text_ratio": 0.974032,
      "vision_ratio": 0.025968
    },
    "middle": {
      "mdi": 30.439302,
      "aei_text": 2.924316,
      "aei_vision": 0.09607,
      "text_ratio": 0.968193,
      "vision_ratio": 0.031807
    },
    "late": {
      "mdi": 25.501195,
      "aei_text": 2.887764,
      "aei_vision": 0.11324,
      "text_ratio": 0.962266,
      "vision_ratio": 0.037734
    },
    "all": {
      "mdi": 25.501195,
      "aei_text": 2.924283,
      "aei_vision": 0.096086,
      "text_ratio": 0.962266,
      "vision_ratio": 0.037734
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962266,
      0.037734
    ],
    "text_vision_ratio": "0.962266:0.037734",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 160.0,
    "total_tokens": 461.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.962307,
      "aei_text": 2.738019,
      "aei_vision": 0.076136,
      "text_ratio": 0.972945,
      "vision_ratio": 0.027055
    },
    "middle": {
      "mdi": 25.395492,
      "aei_text": 2.682533,
      "aei_vision": 0.10563,
      "text_ratio": 0.962115,
      "vision_ratio": 0.037885
    },
    "late": {
      "mdi": 35.966298,
      "aei_text": 2.738035,
      "aei_vision": 0.076128,
      "text_ratio": 0.972948,
      "vision_ratio": 0.027052
    },
    "all": {
      "mdi": 35.966298,
      "aei_text": 2.719514,
      "aei_vision": 0.085973,
      "text_ratio": 0.972948,
      "vision_ratio": 0.027052
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972948,
      0.027052
    ],
    "text_vision_ratio": "0.972948:0.027052",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 160.0,
    "total_tokens": 461.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.196786,
      "aei_text": 2.726727,
      "aei_vision": 0.082138,
      "text_ratio": 0.970757,
      "vision_ratio": 0.029243
    },
    "middle": {
      "mdi": 21.552616,
      "aei_text": 2.649946,
      "aei_vision": 0.122952,
      "text_ratio": 0.955659,
      "vision_ratio": 0.044341
    },
    "late": {
      "mdi": 18.5554,
      "aei_text": 2.616023,
      "aei_vision": 0.140984,
      "text_ratio": 0.948863,
      "vision_ratio": 0.051137
    },
    "all": {
      "mdi": 18.5554,
      "aei_text": 2.664252,
      "aei_vision": 0.115348,
      "text_ratio": 0.948863,
      "vision_ratio": 0.051137
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948863,
      0.051137
    ],
    "text_vision_ratio": "0.948863:0.051137",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.490781,
      "aei_text": 3.197286,
      "aei_vision": 0.083066,
      "text_ratio": 0.974678,
      "vision_ratio": 0.025322
    },
    "middle": {
      "mdi": 29.043212,
      "aei_text": 3.13747,
      "aei_vision": 0.108028,
      "text_ratio": 0.966715,
      "vision_ratio": 0.033285
    },
    "late": {
      "mdi": 23.442946,
      "aei_text": 3.081364,
      "aei_vision": 0.131441,
      "text_ratio": 0.959088,
      "vision_ratio": 0.040912
    },
    "all": {
      "mdi": 23.442946,
      "aei_text": 3.138729,
      "aei_vision": 0.107502,
      "text_ratio": 0.959088,
      "vision_ratio": 0.040912
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959088,
      0.040912
    ],
    "text_vision_ratio": "0.959088:0.040912",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.084138,
      "aei_text": 3.195287,
      "aei_vision": 0.083901,
      "text_ratio": 0.974414,
      "vision_ratio": 0.025586
    },
    "middle": {
      "mdi": 23.720736,
      "aei_text": 3.084714,
      "aei_vision": 0.130043,
      "text_ratio": 0.959548,
      "vision_ratio": 0.040452
    },
    "late": {
      "mdi": 20.666984,
      "aei_text": 3.043452,
      "aei_vision": 0.147262,
      "text_ratio": 0.953847,
      "vision_ratio": 0.046153
    },
    "all": {
      "mdi": 20.666984,
      "aei_text": 3.107798,
      "aei_vision": 0.12041,
      "text_ratio": 0.953847,
      "vision_ratio": 0.046153
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953847,
      0.046153
    ],
    "text_vision_ratio": "0.953847:0.046153",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 176.0,
    "total_tokens": 523.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.36329,
      "aei_text": 2.826338,
      "aei_vision": 0.073673,
      "text_ratio": 0.974596,
      "vision_ratio": 0.025404
    },
    "middle": {
      "mdi": 48.363793,
      "aei_text": 2.855196,
      "aei_vision": 0.059036,
      "text_ratio": 0.979742,
      "vision_ratio": 0.020258
    },
    "late": {
      "mdi": 38.241526,
      "aei_text": 2.825898,
      "aei_vision": 0.073896,
      "text_ratio": 0.974517,
      "vision_ratio": 0.025483
    },
    "all": {
      "mdi": 38.241526,
      "aei_text": 2.835807,
      "aei_vision": 0.06887,
      "text_ratio": 0.974517,
      "vision_ratio": 0.025483
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974517,
      0.025483
    ],
    "text_vision_ratio": "0.974517:0.025483",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 176.0,
    "total_tokens": 523.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.909182,
      "aei_text": 2.820906,
      "aei_vision": 0.076428,
      "text_ratio": 0.973621,
      "vision_ratio": 0.026379
    },
    "middle": {
      "mdi": 32.868678,
      "aei_text": 2.80343,
      "aei_vision": 0.085292,
      "text_ratio": 0.970474,
      "vision_ratio": 0.029526
    },
    "late": {
      "mdi": 37.471917,
      "aei_text": 2.823055,
      "aei_vision": 0.075338,
      "text_ratio": 0.974007,
      "vision_ratio": 0.025993
    },
    "all": {
      "mdi": 37.471917,
      "aei_text": 2.815788,
      "aei_vision": 0.079024,
      "text_ratio": 0.974007,
      "vision_ratio": 0.025993
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974007,
      0.025993
    ],
    "text_vision_ratio": "0.974007:0.025993",
    "skip_reason": null
  }
}
```


## === Rollout Step 4 ===
Step: 3/43 | 2025-10-22 18:20:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 43.016 | 23.480 | 19.838 | 19.838 |
| MDI Std | 15.530 | 10.131 | 5.002 | 5.002 |
| Vision Tokens | 359.0 ± 50.2 |
| Text Tokens | 162.5 ± 3.5 |
| Total Tokens | 521.5 ± 49.4 |
| Vision Ratio | 0.685 |
| Text Ratio | 0.315 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 158.0,
    "total_tokens": 505.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.970725,
      "aei_text": 3.012287,
      "aei_vision": 0.083743,
      "text_ratio": 0.972952,
      "vision_ratio": 0.027048
    },
    "middle": {
      "mdi": 25.384869,
      "aei_text": 2.941698,
      "aei_vision": 0.115884,
      "text_ratio": 0.962099,
      "vision_ratio": 0.037901
    },
    "late": {
      "mdi": 19.263843,
      "aei_text": 2.869106,
      "aei_vision": 0.148937,
      "text_ratio": 0.950651,
      "vision_ratio": 0.049349
    },
    "all": {
      "mdi": 19.263843,
      "aei_text": 2.941023,
      "aei_vision": 0.116191,
      "text_ratio": 0.950651,
      "vision_ratio": 0.049349
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950651,
      0.049349
    ],
    "text_vision_ratio": "0.950651:0.049349",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 158.0,
    "total_tokens": 505.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.335198,
      "aei_text": 3.014026,
      "aei_vision": 0.082951,
      "text_ratio": 0.973216,
      "vision_ratio": 0.026784
    },
    "middle": {
      "mdi": 16.167268,
      "aei_text": 2.813949,
      "aei_vision": 0.174052,
      "text_ratio": 0.94175,
      "vision_ratio": 0.05825
    },
    "late": {
      "mdi": 14.789541,
      "aei_text": 2.782944,
      "aei_vision": 0.18817,
      "text_ratio": 0.936667,
      "vision_ratio": 0.063333
    },
    "all": {
      "mdi": 14.789541,
      "aei_text": 2.870286,
      "aei_vision": 0.1484,
      "text_ratio": 0.936667,
      "vision_ratio": 0.063333
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936667,
      0.063333
    ],
    "text_vision_ratio": "0.936667:0.063333",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.537547,
      "aei_text": 2.673573,
      "aei_vision": 0.280321,
      "text_ratio": 0.905101,
      "vision_ratio": 0.094899
    },
    "middle": {
      "mdi": 9.931961,
      "aei_text": 2.694549,
      "aei_vision": 0.271301,
      "text_ratio": 0.908525,
      "vision_ratio": 0.091475
    },
    "late": {
      "mdi": 16.21938,
      "aei_text": 2.908447,
      "aei_vision": 0.179319,
      "text_ratio": 0.941926,
      "vision_ratio": 0.058074
    },
    "all": {
      "mdi": 16.21938,
      "aei_text": 2.758852,
      "aei_vision": 0.243649,
      "text_ratio": 0.941926,
      "vision_ratio": 0.058074
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941926,
      0.058074
    ],
    "text_vision_ratio": "0.941926:0.058074",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.369557,
      "aei_text": 2.760775,
      "aei_vision": 0.242822,
      "text_ratio": 0.919156,
      "vision_ratio": 0.080844
    },
    "middle": {
      "mdi": 11.879254,
      "aei_text": 2.781037,
      "aei_vision": 0.234109,
      "text_ratio": 0.922356,
      "vision_ratio": 0.077644
    },
    "late": {
      "mdi": 17.390681,
      "aei_text": 2.93322,
      "aei_vision": 0.168666,
      "text_ratio": 0.945625,
      "vision_ratio": 0.054375
    },
    "all": {
      "mdi": 17.390681,
      "aei_text": 2.825014,
      "aei_vision": 0.215197,
      "text_ratio": 0.945625,
      "vision_ratio": 0.054375
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945625,
      0.054375
    ],
    "text_vision_ratio": "0.945625:0.054375",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.724593,
      "aei_text": 3.260204,
      "aei_vision": 0.068313,
      "text_ratio": 0.979476,
      "vision_ratio": 0.020524
    },
    "middle": {
      "mdi": 26.312359,
      "aei_text": 3.136728,
      "aei_vision": 0.119211,
      "text_ratio": 0.963387,
      "vision_ratio": 0.036613
    },
    "late": {
      "mdi": 18.495982,
      "aei_text": 3.028685,
      "aei_vision": 0.163748,
      "text_ratio": 0.948707,
      "vision_ratio": 0.051293
    },
    "all": {
      "mdi": 18.495982,
      "aei_text": 3.141879,
      "aei_vision": 0.117088,
      "text_ratio": 0.948707,
      "vision_ratio": 0.051293
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948707,
      0.051293
    ],
    "text_vision_ratio": "0.948707:0.051293",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.176008,
      "aei_text": 3.267927,
      "aei_vision": 0.065129,
      "text_ratio": 0.98046,
      "vision_ratio": 0.01954
    },
    "middle": {
      "mdi": 25.760864,
      "aei_text": 3.13107,
      "aei_vision": 0.121544,
      "text_ratio": 0.962632,
      "vision_ratio": 0.037368
    },
    "late": {
      "mdi": 21.007361,
      "aei_text": 3.071258,
      "aei_vision": 0.146199,
      "text_ratio": 0.954561,
      "vision_ratio": 0.045439
    },
    "all": {
      "mdi": 21.007361,
      "aei_text": 3.15675,
      "aei_vision": 0.110958,
      "text_ratio": 0.954561,
      "vision_ratio": 0.045439
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954561,
      0.045439
    ],
    "text_vision_ratio": "0.954561:0.045439",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.845177,
      "aei_text": 3.302738,
      "aei_vision": 0.062498,
      "text_ratio": 0.981428,
      "vision_ratio": 0.018572
    },
    "middle": {
      "mdi": 24.821733,
      "aei_text": 3.145031,
      "aei_vision": 0.126705,
      "text_ratio": 0.961273,
      "vision_ratio": 0.038727
    },
    "late": {
      "mdi": 24.17492,
      "aei_text": 3.137473,
      "aei_vision": 0.129782,
      "text_ratio": 0.960278,
      "vision_ratio": 0.039722
    },
    "all": {
      "mdi": 24.17492,
      "aei_text": 3.195077,
      "aei_vision": 0.10633,
      "text_ratio": 0.960278,
      "vision_ratio": 0.039722
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960278,
      0.039722
    ],
    "text_vision_ratio": "0.960278:0.039722",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.229674,
      "aei_text": 3.316359,
      "aei_vision": 0.056953,
      "text_ratio": 0.983117,
      "vision_ratio": 0.016883
    },
    "middle": {
      "mdi": 17.786101,
      "aei_text": 3.036861,
      "aei_vision": 0.170744,
      "text_ratio": 0.946769,
      "vision_ratio": 0.053231
    },
    "late": {
      "mdi": 18.928039,
      "aei_text": 3.059257,
      "aei_vision": 0.161626,
      "text_ratio": 0.949819,
      "vision_ratio": 0.050181
    },
    "all": {
      "mdi": 18.928039,
      "aei_text": 3.137492,
      "aei_vision": 0.129774,
      "text_ratio": 0.949819,
      "vision_ratio": 0.050181
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949819,
      0.050181
    ],
    "text_vision_ratio": "0.949819:0.050181",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.960198,
      "aei_text": 3.050526,
      "aei_vision": 0.054512,
      "text_ratio": 0.982444,
      "vision_ratio": 0.017556
    },
    "middle": {
      "mdi": 18.747116,
      "aei_text": 2.840185,
      "aei_vision": 0.1515,
      "text_ratio": 0.94936,
      "vision_ratio": 0.05064
    },
    "late": {
      "mdi": 18.45911,
      "aei_text": 2.835597,
      "aei_vision": 0.153615,
      "text_ratio": 0.94861,
      "vision_ratio": 0.05139
    },
    "all": {
      "mdi": 18.45911,
      "aei_text": 2.908812,
      "aei_vision": 0.119856,
      "text_ratio": 0.94861,
      "vision_ratio": 0.05139
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.94861,
      0.05139
    ],
    "text_vision_ratio": "0.948610:0.051390",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.883634,
      "aei_text": 3.043919,
      "aei_vision": 0.057559,
      "text_ratio": 0.981441,
      "vision_ratio": 0.018559
    },
    "middle": {
      "mdi": 19.545096,
      "aei_text": 2.852259,
      "aei_vision": 0.145932,
      "text_ratio": 0.951327,
      "vision_ratio": 0.048673
    },
    "late": {
      "mdi": 17.391673,
      "aei_text": 2.817417,
      "aei_vision": 0.161998,
      "text_ratio": 0.945628,
      "vision_ratio": 0.054372
    },
    "all": {
      "mdi": 17.391673,
      "aei_text": 2.904557,
      "aei_vision": 0.121818,
      "text_ratio": 0.945628,
      "vision_ratio": 0.054372
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945628,
      0.054372
    ],
    "text_vision_ratio": "0.945628:0.054372",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.980624,
      "aei_text": 3.257008,
      "aei_vision": 0.063887,
      "text_ratio": 0.980762,
      "vision_ratio": 0.019238
    },
    "middle": {
      "mdi": 30.230769,
      "aei_text": 3.159091,
      "aei_vision": 0.104499,
      "text_ratio": 0.96798,
      "vision_ratio": 0.03202
    },
    "late": {
      "mdi": 21.43714,
      "aei_text": 3.066188,
      "aei_vision": 0.143032,
      "text_ratio": 0.955431,
      "vision_ratio": 0.044569
    },
    "all": {
      "mdi": 21.43714,
      "aei_text": 3.160776,
      "aei_vision": 0.1038,
      "text_ratio": 0.955431,
      "vision_ratio": 0.044569
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955431,
      0.044569
    ],
    "text_vision_ratio": "0.955431:0.044569",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.160798,
      "aei_text": 3.257526,
      "aei_vision": 0.063672,
      "text_ratio": 0.980829,
      "vision_ratio": 0.019171
    },
    "middle": {
      "mdi": 39.237213,
      "aei_text": 3.213576,
      "aei_vision": 0.081901,
      "text_ratio": 0.975147,
      "vision_ratio": 0.024853
    },
    "late": {
      "mdi": 24.978551,
      "aei_text": 3.110777,
      "aei_vision": 0.124538,
      "text_ratio": 0.961507,
      "vision_ratio": 0.038493
    },
    "all": {
      "mdi": 24.978551,
      "aei_text": 3.193962,
      "aei_vision": 0.090036,
      "text_ratio": 0.961507,
      "vision_ratio": 0.038493
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961507,
      0.038493
    ],
    "text_vision_ratio": "0.961507:0.038493",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 161.0,
    "total_tokens": 531.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.976391,
      "aei_text": 3.176424,
      "aei_vision": 0.052961,
      "text_ratio": 0.9836,
      "vision_ratio": 0.0164
    },
    "middle": {
      "mdi": 24.526152,
      "aei_text": 3.015573,
      "aei_vision": 0.122953,
      "text_ratio": 0.960824,
      "vision_ratio": 0.039176
    },
    "late": {
      "mdi": 20.845572,
      "aei_text": 2.970636,
      "aei_vision": 0.142507,
      "text_ratio": 0.954224,
      "vision_ratio": 0.045776
    },
    "all": {
      "mdi": 20.845572,
      "aei_text": 3.054208,
      "aei_vision": 0.106142,
      "text_ratio": 0.954224,
      "vision_ratio": 0.045776
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954224,
      0.045776
    ],
    "text_vision_ratio": "0.954224:0.045776",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 161.0,
    "total_tokens": 531.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.477447,
      "aei_text": 3.169179,
      "aei_vision": 0.056114,
      "text_ratio": 0.982602,
      "vision_ratio": 0.017398
    },
    "middle": {
      "mdi": 51.451556,
      "aei_text": 3.157121,
      "aei_vision": 0.061361,
      "text_ratio": 0.980935,
      "vision_ratio": 0.019065
    },
    "late": {
      "mdi": 35.156059,
      "aei_text": 3.095768,
      "aei_vision": 0.088058,
      "text_ratio": 0.972342,
      "vision_ratio": 0.027658
    },
    "all": {
      "mdi": 35.156059,
      "aei_text": 3.140694,
      "aei_vision": 0.068509,
      "text_ratio": 0.972342,
      "vision_ratio": 0.027658
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972342,
      0.027658
    ],
    "text_vision_ratio": "0.972342:0.027658",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 167.0,
    "total_tokens": 403.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 28.337341,
      "aei_text": 2.298546,
      "aei_vision": 0.081114,
      "text_ratio": 0.965914,
      "vision_ratio": 0.034086
    },
    "middle": {
      "mdi": 20.027415,
      "aei_text": 2.254119,
      "aei_vision": 0.112552,
      "text_ratio": 0.952443,
      "vision_ratio": 0.047557
    },
    "late": {
      "mdi": 15.314042,
      "aei_text": 2.2093,
      "aei_vision": 0.144266,
      "text_ratio": 0.938703,
      "vision_ratio": 0.061297
    },
    "all": {
      "mdi": 15.314042,
      "aei_text": 2.254002,
      "aei_vision": 0.112634,
      "text_ratio": 0.938703,
      "vision_ratio": 0.061297
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.938703,
      0.061297
    ],
    "text_vision_ratio": "0.938703:0.061297",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 167.0,
    "total_tokens": 403.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 30.297992,
      "aei_text": 2.305633,
      "aei_vision": 0.076099,
      "text_ratio": 0.968049,
      "vision_ratio": 0.031951
    },
    "middle": {
      "mdi": 13.874796,
      "aei_text": 2.190107,
      "aei_vision": 0.157848,
      "text_ratio": 0.932772,
      "vision_ratio": 0.067228
    },
    "late": {
      "mdi": 13.548761,
      "aei_text": 2.185246,
      "aei_vision": 0.161288,
      "text_ratio": 0.931266,
      "vision_ratio": 0.068734
    },
    "all": {
      "mdi": 13.548761,
      "aei_text": 2.226966,
      "aei_vision": 0.131765,
      "text_ratio": 0.931266,
      "vision_ratio": 0.068734
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931266,
      0.068734
    ],
    "text_vision_ratio": "0.931266:0.068734",
    "skip_reason": null
  }
}
```


## === Rollout Step 5 ===
Step: 4/43 | 2025-10-22 18:22:25

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 38.732 | 32.824 | 30.242 | 30.242 |
| MDI Std | 12.022 | 14.588 | 9.377 | 9.377 |
| Vision Tokens | 395.9 ± 67.5 |
| Text Tokens | 163.1 ± 2.8 |
| Total Tokens | 559.0 ± 66.7 |
| Vision Ratio | 0.704 |
| Text Ratio | 0.296 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.939308,
      "aei_text": 2.962732,
      "aei_vision": 0.072369,
      "text_ratio": 0.976156,
      "vision_ratio": 0.023844
    },
    "middle": {
      "mdi": 28.542265,
      "aei_text": 2.900815,
      "aei_vision": 0.101632,
      "text_ratio": 0.96615,
      "vision_ratio": 0.03385
    },
    "late": {
      "mdi": 31.960105,
      "aei_text": 2.922383,
      "aei_vision": 0.091438,
      "text_ratio": 0.96966,
      "vision_ratio": 0.03034
    },
    "all": {
      "mdi": 31.960105,
      "aei_text": 2.928653,
      "aei_vision": 0.088475,
      "text_ratio": 0.96966,
      "vision_ratio": 0.03034
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96966,
      0.03034
    ],
    "text_vision_ratio": "0.969660:0.030340",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.820923,
      "aei_text": 2.96231,
      "aei_vision": 0.072568,
      "text_ratio": 0.976089,
      "vision_ratio": 0.023911
    },
    "middle": {
      "mdi": 36.03615,
      "aei_text": 2.943053,
      "aei_vision": 0.081669,
      "text_ratio": 0.972999,
      "vision_ratio": 0.027001
    },
    "late": {
      "mdi": 29.084382,
      "aei_text": 2.904551,
      "aei_vision": 0.099866,
      "text_ratio": 0.96676,
      "vision_ratio": 0.03324
    },
    "all": {
      "mdi": 29.084382,
      "aei_text": 2.936649,
      "aei_vision": 0.084696,
      "text_ratio": 0.96676,
      "vision_ratio": 0.03324
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96676,
      0.03324
    ],
    "text_vision_ratio": "0.966760:0.033240",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.672604,
      "aei_text": 2.972941,
      "aei_vision": 0.078915,
      "text_ratio": 0.974142,
      "vision_ratio": 0.025858
    },
    "middle": {
      "mdi": 29.087468,
      "aei_text": 2.926472,
      "aei_vision": 0.100609,
      "text_ratio": 0.966764,
      "vision_ratio": 0.033236
    },
    "late": {
      "mdi": 23.046166,
      "aei_text": 2.874785,
      "aei_vision": 0.12474,
      "text_ratio": 0.958413,
      "vision_ratio": 0.041587
    },
    "all": {
      "mdi": 23.046166,
      "aei_text": 2.924718,
      "aei_vision": 0.101429,
      "text_ratio": 0.958413,
      "vision_ratio": 0.041587
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958413,
      0.041587
    ],
    "text_vision_ratio": "0.958413:0.041587",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.608718,
      "aei_text": 2.9683,
      "aei_vision": 0.081082,
      "text_ratio": 0.97341,
      "vision_ratio": 0.02659
    },
    "middle": {
      "mdi": 16.380783,
      "aei_text": 2.778637,
      "aei_vision": 0.169628,
      "text_ratio": 0.942465,
      "vision_ratio": 0.057535
    },
    "late": {
      "mdi": 20.413882,
      "aei_text": 2.843603,
      "aei_vision": 0.139298,
      "text_ratio": 0.953301,
      "vision_ratio": 0.046699
    },
    "all": {
      "mdi": 20.413882,
      "aei_text": 2.863557,
      "aei_vision": 0.129982,
      "text_ratio": 0.953301,
      "vision_ratio": 0.046699
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953301,
      0.046699
    ],
    "text_vision_ratio": "0.953301:0.046699",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 485.0,
    "text_tokens": 166.0,
    "total_tokens": 651.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.812113,
      "aei_text": 3.716103,
      "aei_vision": 0.070365,
      "text_ratio": 0.981417,
      "vision_ratio": 0.018583
    },
    "middle": {
      "mdi": 48.998094,
      "aei_text": 3.701001,
      "aei_vision": 0.075534,
      "text_ratio": 0.979999,
      "vision_ratio": 0.020001
    },
    "late": {
      "mdi": 39.578478,
      "aei_text": 3.652089,
      "aei_vision": 0.092275,
      "text_ratio": 0.975356,
      "vision_ratio": 0.024644
    },
    "all": {
      "mdi": 39.578478,
      "aei_text": 3.689736,
      "aei_vision": 0.079389,
      "text_ratio": 0.975356,
      "vision_ratio": 0.024644
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975356,
      0.024644
    ],
    "text_vision_ratio": "0.975356:0.024644",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 485.0,
    "text_tokens": 166.0,
    "total_tokens": 651.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.549836,
      "aei_text": 3.722319,
      "aei_vision": 0.068237,
      "text_ratio": 0.981998,
      "vision_ratio": 0.018002
    },
    "middle": {
      "mdi": 59.847454,
      "aei_text": 3.739146,
      "aei_vision": 0.062478,
      "text_ratio": 0.983565,
      "vision_ratio": 0.016435
    },
    "late": {
      "mdi": 45.868423,
      "aei_text": 3.686845,
      "aei_vision": 0.080379,
      "text_ratio": 0.978664,
      "vision_ratio": 0.021336
    },
    "all": {
      "mdi": 45.868423,
      "aei_text": 3.716098,
      "aei_vision": 0.070366,
      "text_ratio": 0.978664,
      "vision_ratio": 0.021336
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978664,
      0.021336
    ],
    "text_vision_ratio": "0.978664:0.021336",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.675176,
      "aei_text": 2.89897,
      "aei_vision": 0.086086,
      "text_ratio": 0.971161,
      "vision_ratio": 0.028839
    },
    "middle": {
      "mdi": 25.462444,
      "aei_text": 2.845629,
      "aei_vision": 0.111758,
      "text_ratio": 0.962211,
      "vision_ratio": 0.037789
    },
    "late": {
      "mdi": 32.749112,
      "aei_text": 2.894214,
      "aei_vision": 0.088375,
      "text_ratio": 0.97037,
      "vision_ratio": 0.02963
    },
    "all": {
      "mdi": 32.749112,
      "aei_text": 2.879614,
      "aei_vision": 0.095402,
      "text_ratio": 0.97037,
      "vision_ratio": 0.02963
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97037,
      0.02963
    ],
    "text_vision_ratio": "0.970370:0.029630",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.438913,
      "aei_text": 2.897781,
      "aei_vision": 0.086659,
      "text_ratio": 0.970963,
      "vision_ratio": 0.029037
    },
    "middle": {
      "mdi": 34.025602,
      "aei_text": 2.900707,
      "aei_vision": 0.085251,
      "text_ratio": 0.971449,
      "vision_ratio": 0.028551
    },
    "late": {
      "mdi": 30.883198,
      "aei_text": 2.883819,
      "aei_vision": 0.093378,
      "text_ratio": 0.968636,
      "vision_ratio": 0.031364
    },
    "all": {
      "mdi": 30.883198,
      "aei_text": 2.894098,
      "aei_vision": 0.088431,
      "text_ratio": 0.968636,
      "vision_ratio": 0.031364
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968636,
      0.031364
    ],
    "text_vision_ratio": "0.968636:0.031364",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 159.0,
    "total_tokens": 529.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.698574,
      "aei_text": 3.158829,
      "aei_vision": 0.072287,
      "text_ratio": 0.977628,
      "vision_ratio": 0.022372
    },
    "middle": {
      "mdi": 40.01008,
      "aei_text": 3.144174,
      "aei_vision": 0.078585,
      "text_ratio": 0.975616,
      "vision_ratio": 0.024384
    },
    "late": {
      "mdi": 42.073206,
      "aei_text": 3.152672,
      "aei_vision": 0.074933,
      "text_ratio": 0.976784,
      "vision_ratio": 0.023216
    },
    "all": {
      "mdi": 42.073206,
      "aei_text": 3.15189,
      "aei_vision": 0.075269,
      "text_ratio": 0.976784,
      "vision_ratio": 0.023216
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976784,
      0.023216
    ],
    "text_vision_ratio": "0.976784:0.023216",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 159.0,
    "total_tokens": 529.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.225294,
      "aei_text": 3.160733,
      "aei_vision": 0.071469,
      "text_ratio": 0.977888,
      "vision_ratio": 0.022112
    },
    "middle": {
      "mdi": 36.532677,
      "aei_text": 3.12781,
      "aei_vision": 0.085617,
      "text_ratio": 0.973357,
      "vision_ratio": 0.026643
    },
    "late": {
      "mdi": 38.128963,
      "aei_text": 3.135671,
      "aei_vision": 0.082239,
      "text_ratio": 0.974443,
      "vision_ratio": 0.025557
    },
    "all": {
      "mdi": 38.128963,
      "aei_text": 3.14141,
      "aei_vision": 0.079773,
      "text_ratio": 0.974443,
      "vision_ratio": 0.025557
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974443,
      0.025557
    ],
    "text_vision_ratio": "0.974443:0.025557",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.754782,
      "aei_text": 3.215999,
      "aei_vision": 0.080896,
      "text_ratio": 0.975463,
      "vision_ratio": 0.024537
    },
    "middle": {
      "mdi": 30.284846,
      "aei_text": 3.159508,
      "aei_vision": 0.104326,
      "text_ratio": 0.968036,
      "vision_ratio": 0.031964
    },
    "late": {
      "mdi": 27.907751,
      "aei_text": 3.139786,
      "aei_vision": 0.112506,
      "text_ratio": 0.965407,
      "vision_ratio": 0.034593
    },
    "all": {
      "mdi": 27.907751,
      "aei_text": 3.171781,
      "aei_vision": 0.099236,
      "text_ratio": 0.965407,
      "vision_ratio": 0.034593
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965407,
      0.034593
    ],
    "text_vision_ratio": "0.965407:0.034593",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.344149,
      "aei_text": 3.214081,
      "aei_vision": 0.081691,
      "text_ratio": 0.975213,
      "vision_ratio": 0.024787
    },
    "middle": {
      "mdi": 27.767514,
      "aei_text": 3.138526,
      "aei_vision": 0.113029,
      "text_ratio": 0.965239,
      "vision_ratio": 0.034761
    },
    "late": {
      "mdi": 29.719856,
      "aei_text": 3.155085,
      "aei_vision": 0.106161,
      "text_ratio": 0.967448,
      "vision_ratio": 0.032552
    },
    "all": {
      "mdi": 29.719856,
      "aei_text": 3.16924,
      "aei_vision": 0.10029,
      "text_ratio": 0.967448,
      "vision_ratio": 0.032552
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967448,
      0.032552
    ],
    "text_vision_ratio": "0.967448:0.032552",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 159.0,
    "total_tokens": 690.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.578673,
      "aei_text": 3.42918,
      "aei_vision": 0.272619,
      "text_ratio": 0.926355,
      "vision_ratio": 0.073645
    },
    "middle": {
      "mdi": 9.04975,
      "aei_text": 3.169854,
      "aei_vision": 0.35027,
      "text_ratio": 0.900495,
      "vision_ratio": 0.099505
    },
    "late": {
      "mdi": 13.674649,
      "aei_text": 3.487826,
      "aei_vision": 0.255058,
      "text_ratio": 0.931855,
      "vision_ratio": 0.068145
    },
    "all": {
      "mdi": 13.674649,
      "aei_text": 3.362247,
      "aei_vision": 0.29266,
      "text_ratio": 0.931855,
      "vision_ratio": 0.068145
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931855,
      0.068145
    ],
    "text_vision_ratio": "0.931855:0.068145",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 159.0,
    "total_tokens": 690.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.19992,
      "aei_text": 3.269224,
      "aei_vision": 0.320515,
      "text_ratio": 0.910714,
      "vision_ratio": 0.089286
    },
    "middle": {
      "mdi": 6.55112,
      "aei_text": 2.874343,
      "aei_vision": 0.438756,
      "text_ratio": 0.867569,
      "vision_ratio": 0.132431
    },
    "late": {
      "mdi": 12.138802,
      "aei_text": 3.403306,
      "aei_vision": 0.280366,
      "text_ratio": 0.92389,
      "vision_ratio": 0.07611
    },
    "all": {
      "mdi": 12.138802,
      "aei_text": 3.182349,
      "aei_vision": 0.346528,
      "text_ratio": 0.92389,
      "vision_ratio": 0.07611
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.92389,
      0.07611
    ],
    "text_vision_ratio": "0.923890:0.076110",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.347155,
      "aei_text": 2.978612,
      "aei_vision": 0.059161,
      "text_ratio": 0.980525,
      "vision_ratio": 0.019475
    },
    "middle": {
      "mdi": 37.989012,
      "aei_text": 2.940261,
      "aei_vision": 0.077398,
      "text_ratio": 0.974352,
      "vision_ratio": 0.025648
    },
    "late": {
      "mdi": 26.732634,
      "aei_text": 2.876721,
      "aei_vision": 0.107611,
      "text_ratio": 0.963941,
      "vision_ratio": 0.036059
    },
    "all": {
      "mdi": 26.732634,
      "aei_text": 2.931856,
      "aei_vision": 0.081394,
      "text_ratio": 0.963941,
      "vision_ratio": 0.036059
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963941,
      0.036059
    ],
    "text_vision_ratio": "0.963941:0.036059",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.044503,
      "aei_text": 2.975443,
      "aei_vision": 0.060668,
      "text_ratio": 0.980018,
      "vision_ratio": 0.019982
    },
    "middle": {
      "mdi": 58.611284,
      "aei_text": 2.995547,
      "aei_vision": 0.051109,
      "text_ratio": 0.983225,
      "vision_ratio": 0.016775
    },
    "late": {
      "mdi": 39.917654,
      "aei_text": 2.947731,
      "aei_vision": 0.073845,
      "text_ratio": 0.975561,
      "vision_ratio": 0.024439
    },
    "all": {
      "mdi": 39.917654,
      "aei_text": 2.972904,
      "aei_vision": 0.061876,
      "text_ratio": 0.975561,
      "vision_ratio": 0.024439
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975561,
      0.024439
    ],
    "text_vision_ratio": "0.975561:0.024439",
    "skip_reason": null
  }
}
```


## === Rollout Step 6 ===
Step: 5/43 | 2025-10-22 18:24:10

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 36.961 | 26.718 | 31.855 | 31.855 |
| MDI Std | 12.772 | 11.875 | 13.109 | 13.109 |
| Vision Tokens | 370.5 ± 61.9 |
| Text Tokens | 163.1 ± 2.1 |
| Total Tokens | 533.6 ± 61.8 |
| Vision Ratio | 0.690 |
| Text Ratio | 0.310 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 165.0,
    "total_tokens": 627.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 7.362563,
      "aei_text": 2.75302,
      "aei_vision": 0.373921,
      "text_ratio": 0.880419,
      "vision_ratio": 0.119581
    },
    "middle": {
      "mdi": 4.066814,
      "aei_text": 2.250519,
      "aei_vision": 0.553386,
      "text_ratio": 0.802637,
      "vision_ratio": 0.197363
    },
    "late": {
      "mdi": 8.42108,
      "aei_text": 2.851785,
      "aei_vision": 0.338648,
      "text_ratio": 0.893855,
      "vision_ratio": 0.106145
    },
    "all": {
      "mdi": 8.42108,
      "aei_text": 2.618392,
      "aei_vision": 0.422003,
      "text_ratio": 0.893855,
      "vision_ratio": 0.106145
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.893855,
      0.106145
    ],
    "text_vision_ratio": "0.893855:0.106145",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 165.0,
    "total_tokens": 627.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.665283,
      "aei_text": 2.871981,
      "aei_vision": 0.331435,
      "text_ratio": 0.896537,
      "vision_ratio": 0.103463
    },
    "middle": {
      "mdi": 6.101688,
      "aei_text": 2.604721,
      "aei_vision": 0.426885,
      "text_ratio": 0.859188,
      "vision_ratio": 0.140812
    },
    "late": {
      "mdi": 10.926501,
      "aei_text": 3.024857,
      "aei_vision": 0.276837,
      "text_ratio": 0.916153,
      "vision_ratio": 0.083847
    },
    "all": {
      "mdi": 10.926501,
      "aei_text": 2.833856,
      "aei_vision": 0.345051,
      "text_ratio": 0.916153,
      "vision_ratio": 0.083847
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.916153,
      0.083847
    ],
    "text_vision_ratio": "0.916153:0.083847",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.083485,
      "aei_text": 3.017167,
      "aei_vision": 0.064081,
      "text_ratio": 0.979203,
      "vision_ratio": 0.020797
    },
    "middle": {
      "mdi": 36.708867,
      "aei_text": 2.980298,
      "aei_vision": 0.081187,
      "text_ratio": 0.973481,
      "vision_ratio": 0.026519
    },
    "late": {
      "mdi": 32.805367,
      "aei_text": 2.960761,
      "aei_vision": 0.090252,
      "text_ratio": 0.970419,
      "vision_ratio": 0.029581
    },
    "all": {
      "mdi": 32.805367,
      "aei_text": 2.986082,
      "aei_vision": 0.078504,
      "text_ratio": 0.970419,
      "vision_ratio": 0.029581
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970419,
      0.029581
    ],
    "text_vision_ratio": "0.970419:0.029581",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.762788,
      "aei_text": 3.019046,
      "aei_vision": 0.063209,
      "text_ratio": 0.979493,
      "vision_ratio": 0.020507
    },
    "middle": {
      "mdi": 31.963123,
      "aei_text": 2.955959,
      "aei_vision": 0.09248,
      "text_ratio": 0.969663,
      "vision_ratio": 0.030337
    },
    "late": {
      "mdi": 24.681869,
      "aei_text": 2.90188,
      "aei_vision": 0.117571,
      "text_ratio": 0.961062,
      "vision_ratio": 0.038938
    },
    "all": {
      "mdi": 24.681869,
      "aei_text": 2.958958,
      "aei_vision": 0.091089,
      "text_ratio": 0.961062,
      "vision_ratio": 0.038938
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961062,
      0.038938
    ],
    "text_vision_ratio": "0.961062:0.038938",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.00993,
      "aei_text": 3.001301,
      "aei_vision": 0.071443,
      "text_ratio": 0.97675,
      "vision_ratio": 0.02325
    },
    "middle": {
      "mdi": 22.793922,
      "aei_text": 2.882705,
      "aei_vision": 0.126468,
      "text_ratio": 0.957972,
      "vision_ratio": 0.042028
    },
    "late": {
      "mdi": 34.454553,
      "aei_text": 2.969523,
      "aei_vision": 0.086187,
      "text_ratio": 0.971795,
      "vision_ratio": 0.028205
    },
    "all": {
      "mdi": 34.454553,
      "aei_text": 2.951199,
      "aei_vision": 0.094689,
      "text_ratio": 0.971795,
      "vision_ratio": 0.028205
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971795,
      0.028205
    ],
    "text_vision_ratio": "0.971795:0.028205",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.203747,
      "aei_text": 3.005353,
      "aei_vision": 0.069562,
      "text_ratio": 0.977377,
      "vision_ratio": 0.022623
    },
    "middle": {
      "mdi": 34.058446,
      "aei_text": 2.967491,
      "aei_vision": 0.087129,
      "text_ratio": 0.971476,
      "vision_ratio": 0.028524
    },
    "late": {
      "mdi": 37.512156,
      "aei_text": 2.983841,
      "aei_vision": 0.079543,
      "text_ratio": 0.974034,
      "vision_ratio": 0.025966
    },
    "all": {
      "mdi": 37.512156,
      "aei_text": 2.985565,
      "aei_vision": 0.078744,
      "text_ratio": 0.974034,
      "vision_ratio": 0.025966
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974034,
      0.025966
    ],
    "text_vision_ratio": "0.974034:0.025966",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.553215,
      "aei_text": 3.225591,
      "aei_vision": 0.088244,
      "text_ratio": 0.973371,
      "vision_ratio": 0.026629
    },
    "middle": {
      "mdi": 30.428146,
      "aei_text": 3.185452,
      "aei_vision": 0.104688,
      "text_ratio": 0.968181,
      "vision_ratio": 0.031819
    },
    "late": {
      "mdi": 41.209824,
      "aei_text": 3.24857,
      "aei_vision": 0.07883,
      "text_ratio": 0.976309,
      "vision_ratio": 0.023691
    },
    "all": {
      "mdi": 41.209824,
      "aei_text": 3.219876,
      "aei_vision": 0.090585,
      "text_ratio": 0.976309,
      "vision_ratio": 0.023691
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976309,
      0.023691
    ],
    "text_vision_ratio": "0.976309:0.023691",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.907974,
      "aei_text": 3.232824,
      "aei_vision": 0.085281,
      "text_ratio": 0.974298,
      "vision_ratio": 0.025702
    },
    "middle": {
      "mdi": 25.681726,
      "aei_text": 3.142323,
      "aei_vision": 0.122356,
      "text_ratio": 0.962521,
      "vision_ratio": 0.037479
    },
    "late": {
      "mdi": 39.411452,
      "aei_text": 3.240302,
      "aei_vision": 0.082217,
      "text_ratio": 0.975255,
      "vision_ratio": 0.024745
    },
    "all": {
      "mdi": 39.411452,
      "aei_text": 3.205156,
      "aei_vision": 0.096616,
      "text_ratio": 0.975255,
      "vision_ratio": 0.024745
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975255,
      0.024745
    ],
    "text_vision_ratio": "0.975255:0.024745",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 162.0,
    "total_tokens": 578.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.720792,
      "aei_text": 3.402189,
      "aei_vision": 0.064532,
      "text_ratio": 0.981385,
      "vision_ratio": 0.018615
    },
    "middle": {
      "mdi": 41.592054,
      "aei_text": 3.360428,
      "aei_vision": 0.080795,
      "text_ratio": 0.976521,
      "vision_ratio": 0.023479
    },
    "late": {
      "mdi": 54.938413,
      "aei_text": 3.408579,
      "aei_vision": 0.062044,
      "text_ratio": 0.982123,
      "vision_ratio": 0.017877
    },
    "all": {
      "mdi": 54.938413,
      "aei_text": 3.39041,
      "aei_vision": 0.069119,
      "text_ratio": 0.982123,
      "vision_ratio": 0.017877
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982123,
      0.017877
    ],
    "text_vision_ratio": "0.982123:0.017877",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 162.0,
    "total_tokens": 578.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.239252,
      "aei_text": 3.397626,
      "aei_vision": 0.066309,
      "text_ratio": 0.980857,
      "vision_ratio": 0.019143
    },
    "middle": {
      "mdi": 20.84914,
      "aei_text": 3.176647,
      "aei_vision": 0.152363,
      "text_ratio": 0.954232,
      "vision_ratio": 0.045768
    },
    "late": {
      "mdi": 30.627861,
      "aei_text": 3.291902,
      "aei_vision": 0.107481,
      "text_ratio": 0.968382,
      "vision_ratio": 0.031618
    },
    "all": {
      "mdi": 30.627861,
      "aei_text": 3.28868,
      "aei_vision": 0.108735,
      "text_ratio": 0.968382,
      "vision_ratio": 0.031618
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968382,
      0.031618
    ],
    "text_vision_ratio": "0.968382:0.031618",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 167.0,
    "total_tokens": 537.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.477393,
      "aei_text": 3.048696,
      "aei_vision": 0.075318,
      "text_ratio": 0.97589,
      "vision_ratio": 0.02411
    },
    "middle": {
      "mdi": 25.073212,
      "aei_text": 2.954498,
      "aei_vision": 0.117835,
      "text_ratio": 0.961646,
      "vision_ratio": 0.038354
    },
    "late": {
      "mdi": 41.67529,
      "aei_text": 3.05325,
      "aei_vision": 0.073263,
      "text_ratio": 0.976567,
      "vision_ratio": 0.023433
    },
    "all": {
      "mdi": 41.67529,
      "aei_text": 3.018796,
      "aei_vision": 0.088813,
      "text_ratio": 0.976567,
      "vision_ratio": 0.023433
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976567,
      0.023433
    ],
    "text_vision_ratio": "0.976567:0.023433",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 167.0,
    "total_tokens": 537.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.581228,
      "aei_text": 3.0491,
      "aei_vision": 0.075136,
      "text_ratio": 0.975951,
      "vision_ratio": 0.024049
    },
    "middle": {
      "mdi": 29.248976,
      "aei_text": 2.989145,
      "aei_vision": 0.102197,
      "text_ratio": 0.966941,
      "vision_ratio": 0.033059
    },
    "late": {
      "mdi": 31.951606,
      "aei_text": 3.007055,
      "aei_vision": 0.094113,
      "text_ratio": 0.969652,
      "vision_ratio": 0.030348
    },
    "all": {
      "mdi": 31.951606,
      "aei_text": 3.015084,
      "aei_vision": 0.090489,
      "text_ratio": 0.969652,
      "vision_ratio": 0.030348
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969652,
      0.030348
    ],
    "text_vision_ratio": "0.969652:0.030348",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.436077,
      "aei_text": 3.223478,
      "aei_vision": 0.077794,
      "text_ratio": 0.976435,
      "vision_ratio": 0.023565
    },
    "middle": {
      "mdi": 29.663889,
      "aei_text": 3.154638,
      "aei_vision": 0.106346,
      "text_ratio": 0.967388,
      "vision_ratio": 0.032612
    },
    "late": {
      "mdi": 26.213804,
      "aei_text": 3.123734,
      "aei_vision": 0.119164,
      "text_ratio": 0.963254,
      "vision_ratio": 0.036746
    },
    "all": {
      "mdi": 26.213804,
      "aei_text": 3.167287,
      "aei_vision": 0.1011,
      "text_ratio": 0.963254,
      "vision_ratio": 0.036746
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963254,
      0.036746
    ],
    "text_vision_ratio": "0.963254:0.036746",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.710255,
      "aei_text": 3.20606,
      "aei_vision": 0.085018,
      "text_ratio": 0.974167,
      "vision_ratio": 0.025833
    },
    "middle": {
      "mdi": 52.875225,
      "aei_text": 3.262287,
      "aei_vision": 0.061698,
      "text_ratio": 0.981439,
      "vision_ratio": 0.018561
    },
    "late": {
      "mdi": 55.198244,
      "aei_text": 3.268285,
      "aei_vision": 0.05921,
      "text_ratio": 0.982206,
      "vision_ratio": 0.017794
    },
    "all": {
      "mdi": 55.198244,
      "aei_text": 3.24554,
      "aei_vision": 0.068644,
      "text_ratio": 0.982206,
      "vision_ratio": 0.017794
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982206,
      0.017794
    ],
    "text_vision_ratio": "0.982206:0.017794",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 29.162021,
      "aei_text": 2.316677,
      "aei_vision": 0.079442,
      "text_ratio": 0.966846,
      "vision_ratio": 0.033154
    },
    "middle": {
      "mdi": 16.853716,
      "aei_text": 2.240188,
      "aei_vision": 0.13292,
      "text_ratio": 0.943989,
      "vision_ratio": 0.056011
    },
    "late": {
      "mdi": 23.672566,
      "aei_text": 2.29183,
      "aei_vision": 0.096814,
      "text_ratio": 0.959469,
      "vision_ratio": 0.040531
    },
    "all": {
      "mdi": 23.672566,
      "aei_text": 2.282912,
      "aei_vision": 0.103049,
      "text_ratio": 0.959469,
      "vision_ratio": 0.040531
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959469,
      0.040531
    ],
    "text_vision_ratio": "0.959469:0.040531",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 27.507191,
      "aei_text": 2.31018,
      "aei_vision": 0.083985,
      "text_ratio": 0.964921,
      "vision_ratio": 0.035079
    },
    "middle": {
      "mdi": 19.535345,
      "aei_text": 2.264505,
      "aei_vision": 0.115918,
      "text_ratio": 0.951303,
      "vision_ratio": 0.048697
    },
    "late": {
      "mdi": 15.979275,
      "aei_text": 2.230639,
      "aei_vision": 0.139596,
      "text_ratio": 0.941105,
      "vision_ratio": 0.058895
    },
    "all": {
      "mdi": 15.979275,
      "aei_text": 2.268449,
      "aei_vision": 0.11316,
      "text_ratio": 0.941105,
      "vision_ratio": 0.058895
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941105,
      0.058895
    ],
    "text_vision_ratio": "0.941105:0.058895",
    "skip_reason": null
  }
}
```


## === Rollout Step 7 ===
Step: 6/43 | 2025-10-22 18:25:32

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 39.417 | 26.882 | 24.241 | 24.241 |
| MDI Std | 12.302 | 11.501 | 5.738 | 5.738 |
| Vision Tokens | 384.4 ± 60.8 |
| Text Tokens | 162.0 ± 3.4 |
| Total Tokens | 546.4 ± 61.3 |
| Vision Ratio | 0.700 |
| Text Ratio | 0.300 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 157.0,
    "total_tokens": 504.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.297761,
      "aei_text": 3.043278,
      "aei_vision": 0.07552,
      "text_ratio": 0.975786,
      "vision_ratio": 0.024214
    },
    "middle": {
      "mdi": 27.513236,
      "aei_text": 2.971486,
      "aei_vision": 0.108002,
      "text_ratio": 0.964929,
      "vision_ratio": 0.035071
    },
    "late": {
      "mdi": 24.041729,
      "aei_text": 2.93992,
      "aei_vision": 0.122284,
      "text_ratio": 0.960067,
      "vision_ratio": 0.039933
    },
    "all": {
      "mdi": 24.041729,
      "aei_text": 2.98489,
      "aei_vision": 0.101937,
      "text_ratio": 0.960067,
      "vision_ratio": 0.039933
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960067,
      0.039933
    ],
    "text_vision_ratio": "0.960067:0.039933",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 157.0,
    "total_tokens": 504.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.994356,
      "aei_text": 3.037998,
      "aei_vision": 0.077909,
      "text_ratio": 0.974996,
      "vision_ratio": 0.025004
    },
    "middle": {
      "mdi": 31.646452,
      "aei_text": 3.000627,
      "aei_vision": 0.094817,
      "text_ratio": 0.969369,
      "vision_ratio": 0.030631
    },
    "late": {
      "mdi": 25.268316,
      "aei_text": 2.951984,
      "aei_vision": 0.116826,
      "text_ratio": 0.961931,
      "vision_ratio": 0.038069
    },
    "all": {
      "mdi": 25.268316,
      "aei_text": 2.996877,
      "aei_vision": 0.096514,
      "text_ratio": 0.961931,
      "vision_ratio": 0.038069
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961931,
      0.038069
    ],
    "text_vision_ratio": "0.961931:0.038069",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.660958,
      "aei_text": 2.945391,
      "aei_vision": 0.058139,
      "text_ratio": 0.980643,
      "vision_ratio": 0.019357
    },
    "middle": {
      "mdi": 31.081337,
      "aei_text": 2.874457,
      "aei_vision": 0.092482,
      "text_ratio": 0.968829,
      "vision_ratio": 0.031171
    },
    "late": {
      "mdi": 19.690666,
      "aei_text": 2.774447,
      "aei_vision": 0.140902,
      "text_ratio": 0.951669,
      "vision_ratio": 0.048331
    },
    "all": {
      "mdi": 19.690666,
      "aei_text": 2.864767,
      "aei_vision": 0.097173,
      "text_ratio": 0.951669,
      "vision_ratio": 0.048331
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951669,
      0.048331
    ],
    "text_vision_ratio": "0.951669:0.048331",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.924581,
      "aei_text": 2.921542,
      "aei_vision": 0.069686,
      "text_ratio": 0.976703,
      "vision_ratio": 0.023297
    },
    "middle": {
      "mdi": 34.331945,
      "aei_text": 2.891517,
      "aei_vision": 0.084222,
      "text_ratio": 0.971697,
      "vision_ratio": 0.028303
    },
    "late": {
      "mdi": 30.310855,
      "aei_text": 2.869911,
      "aei_vision": 0.094683,
      "text_ratio": 0.968062,
      "vision_ratio": 0.031938
    },
    "all": {
      "mdi": 30.310855,
      "aei_text": 2.894321,
      "aei_vision": 0.082865,
      "text_ratio": 0.968062,
      "vision_ratio": 0.031938
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968062,
      0.031938
    ],
    "text_vision_ratio": "0.968062:0.031938",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.32787,
      "aei_text": 2.968166,
      "aei_vision": 0.075472,
      "text_ratio": 0.975203,
      "vision_ratio": 0.024797
    },
    "middle": {
      "mdi": 9.886118,
      "aei_text": 2.574461,
      "aei_vision": 0.260412,
      "text_ratio": 0.90814,
      "vision_ratio": 0.09186
    },
    "late": {
      "mdi": 18.143098,
      "aei_text": 2.800263,
      "aei_vision": 0.154343,
      "text_ratio": 0.947762,
      "vision_ratio": 0.052238
    },
    "all": {
      "mdi": 18.143098,
      "aei_text": 2.780992,
      "aei_vision": 0.163396,
      "text_ratio": 0.947762,
      "vision_ratio": 0.052238
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947762,
      0.052238
    ],
    "text_vision_ratio": "0.947762:0.052238",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.381249,
      "aei_text": 2.982476,
      "aei_vision": 0.06875,
      "text_ratio": 0.977468,
      "vision_ratio": 0.022532
    },
    "middle": {
      "mdi": 35.710376,
      "aei_text": 2.952806,
      "aei_vision": 0.082688,
      "text_ratio": 0.97276,
      "vision_ratio": 0.02724
    },
    "late": {
      "mdi": 31.122873,
      "aei_text": 2.928521,
      "aei_vision": 0.094095,
      "text_ratio": 0.96887,
      "vision_ratio": 0.03113
    },
    "all": {
      "mdi": 31.122873,
      "aei_text": 2.954592,
      "aei_vision": 0.081849,
      "text_ratio": 0.96887,
      "vision_ratio": 0.03113
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96887,
      0.03113
    ],
    "text_vision_ratio": "0.968870:0.031130",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.689381,
      "aei_text": 3.312716,
      "aei_vision": 0.058436,
      "text_ratio": 0.982666,
      "vision_ratio": 0.017334
    },
    "middle": {
      "mdi": 21.255386,
      "aei_text": 3.098223,
      "aei_vision": 0.145762,
      "text_ratio": 0.955067,
      "vision_ratio": 0.044933
    },
    "late": {
      "mdi": 25.396784,
      "aei_text": 3.151457,
      "aei_vision": 0.124089,
      "text_ratio": 0.962117,
      "vision_ratio": 0.037883
    },
    "all": {
      "mdi": 25.396784,
      "aei_text": 3.187458,
      "aei_vision": 0.109432,
      "text_ratio": 0.962117,
      "vision_ratio": 0.037883
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962117,
      0.037883
    ],
    "text_vision_ratio": "0.962117:0.037883",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.968733,
      "aei_text": 3.315755,
      "aei_vision": 0.057199,
      "text_ratio": 0.983042,
      "vision_ratio": 0.016958
    },
    "middle": {
      "mdi": 30.559473,
      "aei_text": 3.199118,
      "aei_vision": 0.104685,
      "text_ratio": 0.968314,
      "vision_ratio": 0.031686
    },
    "late": {
      "mdi": 26.682481,
      "aei_text": 3.164905,
      "aei_vision": 0.118614,
      "text_ratio": 0.963876,
      "vision_ratio": 0.036124
    },
    "all": {
      "mdi": 26.682481,
      "aei_text": 3.226628,
      "aei_vision": 0.093485,
      "text_ratio": 0.963876,
      "vision_ratio": 0.036124
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963876,
      0.036124
    ],
    "text_vision_ratio": "0.963876:0.036124",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 164.0,
    "total_tokens": 488.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 28.431898,
      "aei_text": 2.782281,
      "aei_vision": 0.097858,
      "text_ratio": 0.966023,
      "vision_ratio": 0.033977
    },
    "middle": {
      "mdi": 8.576932,
      "aei_text": 2.418527,
      "aei_vision": 0.28198,
      "text_ratio": 0.895582,
      "vision_ratio": 0.104418
    },
    "late": {
      "mdi": 17.67013,
      "aei_text": 2.676377,
      "aei_vision": 0.151463,
      "text_ratio": 0.946439,
      "vision_ratio": 0.053561
    },
    "all": {
      "mdi": 17.67013,
      "aei_text": 2.625791,
      "aei_vision": 0.177069,
      "text_ratio": 0.946439,
      "vision_ratio": 0.053561
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.946439,
      0.053561
    ],
    "text_vision_ratio": "0.946439:0.053561",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 164.0,
    "total_tokens": 488.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.106984,
      "aei_text": 2.797914,
      "aei_vision": 0.089945,
      "text_ratio": 0.968854,
      "vision_ratio": 0.031146
    },
    "middle": {
      "mdi": 23.665417,
      "aei_text": 2.746343,
      "aei_vision": 0.116049,
      "text_ratio": 0.959457,
      "vision_ratio": 0.040543
    },
    "late": {
      "mdi": 19.864912,
      "aei_text": 2.706448,
      "aei_vision": 0.136243,
      "text_ratio": 0.952073,
      "vision_ratio": 0.047927
    },
    "all": {
      "mdi": 19.864912,
      "aei_text": 2.750229,
      "aei_vision": 0.114082,
      "text_ratio": 0.952073,
      "vision_ratio": 0.047927
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952073,
      0.047927
    ],
    "text_vision_ratio": "0.952073:0.047927",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.600024,
      "aei_text": 3.281313,
      "aei_vision": 0.077026,
      "text_ratio": 0.977064,
      "vision_ratio": 0.022936
    },
    "middle": {
      "mdi": 41.084088,
      "aei_text": 3.274687,
      "aei_vision": 0.079707,
      "text_ratio": 0.976238,
      "vision_ratio": 0.023762
    },
    "late": {
      "mdi": 27.227451,
      "aei_text": 3.182768,
      "aei_vision": 0.116896,
      "text_ratio": 0.964573,
      "vision_ratio": 0.035427
    },
    "all": {
      "mdi": 27.227451,
      "aei_text": 3.246229,
      "aei_vision": 0.09122,
      "text_ratio": 0.964573,
      "vision_ratio": 0.035427
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964573,
      0.035427
    ],
    "text_vision_ratio": "0.964573:0.035427",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.279586,
      "aei_text": 3.284141,
      "aei_vision": 0.075882,
      "text_ratio": 0.977416,
      "vision_ratio": 0.022584
    },
    "middle": {
      "mdi": 38.720048,
      "aei_text": 3.26338,
      "aei_vision": 0.084281,
      "text_ratio": 0.974824,
      "vision_ratio": 0.025176
    },
    "late": {
      "mdi": 28.238657,
      "aei_text": 3.192281,
      "aei_vision": 0.113046,
      "text_ratio": 0.965799,
      "vision_ratio": 0.034201
    },
    "all": {
      "mdi": 28.238657,
      "aei_text": 3.246616,
      "aei_vision": 0.091064,
      "text_ratio": 0.965799,
      "vision_ratio": 0.034201
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965799,
      0.034201
    ],
    "text_vision_ratio": "0.965799:0.034201",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.134171,
      "aei_text": 3.277865,
      "aei_vision": 0.072625,
      "text_ratio": 0.978324,
      "vision_ratio": 0.021676
    },
    "middle": {
      "mdi": 41.123269,
      "aei_text": 3.261447,
      "aei_vision": 0.079309,
      "text_ratio": 0.97626,
      "vision_ratio": 0.02374
    },
    "late": {
      "mdi": 34.944194,
      "aei_text": 3.229263,
      "aei_vision": 0.092412,
      "text_ratio": 0.972179,
      "vision_ratio": 0.027821
    },
    "all": {
      "mdi": 34.944194,
      "aei_text": 3.256191,
      "aei_vision": 0.081449,
      "text_ratio": 0.972179,
      "vision_ratio": 0.027821
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972179,
      0.027821
    ],
    "text_vision_ratio": "0.972179:0.027821",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.113488,
      "aei_text": 3.273955,
      "aei_vision": 0.074217,
      "text_ratio": 0.977834,
      "vision_ratio": 0.022166
    },
    "middle": {
      "mdi": 36.530601,
      "aei_text": 3.238499,
      "aei_vision": 0.088652,
      "text_ratio": 0.973355,
      "vision_ratio": 0.026645
    },
    "late": {
      "mdi": 28.449563,
      "aei_text": 3.181563,
      "aei_vision": 0.111832,
      "text_ratio": 0.966044,
      "vision_ratio": 0.033956
    },
    "all": {
      "mdi": 28.449563,
      "aei_text": 3.231333,
      "aei_vision": 0.091569,
      "text_ratio": 0.966044,
      "vision_ratio": 0.033956
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966044,
      0.033956
    ],
    "text_vision_ratio": "0.966044:0.033956",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 165.0,
    "total_tokens": 696.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.97186,
      "aei_text": 3.324512,
      "aei_vision": 0.277694,
      "text_ratio": 0.92291,
      "vision_ratio": 0.07709
    },
    "middle": {
      "mdi": 8.645167,
      "aei_text": 3.073912,
      "aei_vision": 0.355564,
      "text_ratio": 0.896321,
      "vision_ratio": 0.103679
    },
    "late": {
      "mdi": 14.943228,
      "aei_text": 3.470725,
      "aei_vision": 0.232261,
      "text_ratio": 0.937277,
      "vision_ratio": 0.062723
    },
    "all": {
      "mdi": 14.943228,
      "aei_text": 3.289729,
      "aei_vision": 0.288502,
      "text_ratio": 0.937277,
      "vision_ratio": 0.062723
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937277,
      0.062723
    ],
    "text_vision_ratio": "0.937277:0.062723",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 165.0,
    "total_tokens": 696.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.788189,
      "aei_text": 3.464289,
      "aei_vision": 0.234261,
      "text_ratio": 0.936662,
      "vision_ratio": 0.063338
    },
    "middle": {
      "mdi": 9.785141,
      "aei_text": 3.174227,
      "aei_vision": 0.324393,
      "text_ratio": 0.90728,
      "vision_ratio": 0.09272
    },
    "late": {
      "mdi": 15.853419,
      "aei_text": 3.506397,
      "aei_vision": 0.221176,
      "text_ratio": 0.940665,
      "vision_ratio": 0.059335
    },
    "all": {
      "mdi": 15.853419,
      "aei_text": 3.381619,
      "aei_vision": 0.259949,
      "text_ratio": 0.940665,
      "vision_ratio": 0.059335
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940665,
      0.059335
    ],
    "text_vision_ratio": "0.940665:0.059335",
    "skip_reason": null
  }
}
```


## === Rollout Step 8 ===
Step: 7/43 | 2025-10-22 18:26:55

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 38.410 | 32.606 | 29.130 | 29.130 |
| MDI Std | 12.293 | 16.405 | 10.353 | 10.353 |
| Vision Tokens | 372.9 ± 26.8 |
| Text Tokens | 164.2 ± 3.1 |
| Total Tokens | 537.1 ± 26.2 |
| Vision Ratio | 0.693 |
| Text Ratio | 0.307 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.393534,
      "aei_text": 2.966567,
      "aei_vision": 0.053554,
      "text_ratio": 0.982267,
      "vision_ratio": 0.017733
    },
    "middle": {
      "mdi": 26.943762,
      "aei_text": 2.857482,
      "aei_vision": 0.106054,
      "text_ratio": 0.964214,
      "vision_ratio": 0.035786
    },
    "late": {
      "mdi": 27.848003,
      "aei_text": 2.86414,
      "aei_vision": 0.102849,
      "text_ratio": 0.965336,
      "vision_ratio": 0.034664
    },
    "all": {
      "mdi": 27.848003,
      "aei_text": 2.896075,
      "aei_vision": 0.08748,
      "text_ratio": 0.965336,
      "vision_ratio": 0.034664
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965336,
      0.034664
    ],
    "text_vision_ratio": "0.965336:0.034664",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.780957,
      "aei_text": 2.944216,
      "aei_vision": 0.064311,
      "text_ratio": 0.978624,
      "vision_ratio": 0.021376
    },
    "middle": {
      "mdi": 83.431494,
      "aei_text": 3.003054,
      "aei_vision": 0.035994,
      "text_ratio": 0.988156,
      "vision_ratio": 0.011844
    },
    "late": {
      "mdi": 49.520507,
      "aei_text": 2.953901,
      "aei_vision": 0.05965,
      "text_ratio": 0.980206,
      "vision_ratio": 0.019794
    },
    "all": {
      "mdi": 49.520507,
      "aei_text": 2.967057,
      "aei_vision": 0.053318,
      "text_ratio": 0.980206,
      "vision_ratio": 0.019794
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980206,
      0.019794
    ],
    "text_vision_ratio": "0.980206:0.019794",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.288007,
      "aei_text": 3.176081,
      "aei_vision": 0.080841,
      "text_ratio": 0.975179,
      "vision_ratio": 0.024821
    },
    "middle": {
      "mdi": 37.853213,
      "aei_text": 3.169254,
      "aei_vision": 0.083725,
      "text_ratio": 0.974262,
      "vision_ratio": 0.025738
    },
    "late": {
      "mdi": 41.735949,
      "aei_text": 3.186704,
      "aei_vision": 0.076354,
      "text_ratio": 0.9766,
      "vision_ratio": 0.0234
    },
    "all": {
      "mdi": 41.735949,
      "aei_text": 3.177347,
      "aei_vision": 0.080306,
      "text_ratio": 0.9766,
      "vision_ratio": 0.0234
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9766,
      0.0234
    ],
    "text_vision_ratio": "0.976600:0.023400",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.293276,
      "aei_text": 3.184871,
      "aei_vision": 0.077128,
      "text_ratio": 0.976356,
      "vision_ratio": 0.023644
    },
    "middle": {
      "mdi": 27.452175,
      "aei_text": 3.100116,
      "aei_vision": 0.112928,
      "text_ratio": 0.964853,
      "vision_ratio": 0.035147
    },
    "late": {
      "mdi": 25.628147,
      "aei_text": 3.082697,
      "aei_vision": 0.120286,
      "text_ratio": 0.962446,
      "vision_ratio": 0.037554
    },
    "all": {
      "mdi": 25.628147,
      "aei_text": 3.122562,
      "aei_vision": 0.103447,
      "text_ratio": 0.962446,
      "vision_ratio": 0.037554
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962446,
      0.037554
    ],
    "text_vision_ratio": "0.962446:0.037554",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.474923,
      "aei_text": 3.009015,
      "aei_vision": 0.062074,
      "text_ratio": 0.979788,
      "vision_ratio": 0.020212
    },
    "middle": {
      "mdi": 49.467823,
      "aei_text": 3.011573,
      "aei_vision": 0.060879,
      "text_ratio": 0.980185,
      "vision_ratio": 0.019815
    },
    "late": {
      "mdi": 36.958948,
      "aei_text": 2.969856,
      "aei_vision": 0.080356,
      "text_ratio": 0.973656,
      "vision_ratio": 0.026344
    },
    "all": {
      "mdi": 36.958948,
      "aei_text": 2.996806,
      "aei_vision": 0.067774,
      "text_ratio": 0.973656,
      "vision_ratio": 0.026344
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973656,
      0.026344
    ],
    "text_vision_ratio": "0.973656:0.026344",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.814677,
      "aei_text": 3.004506,
      "aei_vision": 0.064179,
      "text_ratio": 0.979086,
      "vision_ratio": 0.020914
    },
    "middle": {
      "mdi": 35.853371,
      "aei_text": 2.964847,
      "aei_vision": 0.082694,
      "text_ratio": 0.972865,
      "vision_ratio": 0.027135
    },
    "late": {
      "mdi": 28.926027,
      "aei_text": 2.925353,
      "aei_vision": 0.101132,
      "text_ratio": 0.966584,
      "vision_ratio": 0.033416
    },
    "all": {
      "mdi": 28.926027,
      "aei_text": 2.964911,
      "aei_vision": 0.082664,
      "text_ratio": 0.966584,
      "vision_ratio": 0.033416
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966584,
      0.033416
    ],
    "text_vision_ratio": "0.966584:0.033416",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.040879,
      "aei_text": 2.955975,
      "aei_vision": 0.086836,
      "text_ratio": 0.971462,
      "vision_ratio": 0.028538
    },
    "middle": {
      "mdi": 29.524874,
      "aei_text": 2.929449,
      "aei_vision": 0.09922,
      "text_ratio": 0.96724,
      "vision_ratio": 0.03276
    },
    "late": {
      "mdi": 22.567727,
      "aei_text": 2.869611,
      "aei_vision": 0.127156,
      "text_ratio": 0.957569,
      "vision_ratio": 0.042431
    },
    "all": {
      "mdi": 22.567727,
      "aei_text": 2.918344,
      "aei_vision": 0.104404,
      "text_ratio": 0.957569,
      "vision_ratio": 0.042431
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957569,
      0.042431
    ],
    "text_vision_ratio": "0.957569:0.042431",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.105716,
      "aei_text": 2.961292,
      "aei_vision": 0.084354,
      "text_ratio": 0.972304,
      "vision_ratio": 0.027696
    },
    "middle": {
      "mdi": 23.899935,
      "aei_text": 2.883544,
      "aei_vision": 0.120651,
      "text_ratio": 0.959839,
      "vision_ratio": 0.040161
    },
    "late": {
      "mdi": 20.961365,
      "aei_text": 2.850674,
      "aei_vision": 0.135997,
      "text_ratio": 0.954465,
      "vision_ratio": 0.045535
    },
    "all": {
      "mdi": 20.961365,
      "aei_text": 2.898485,
      "aei_vision": 0.113676,
      "text_ratio": 0.954465,
      "vision_ratio": 0.045535
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954465,
      0.045535
    ],
    "text_vision_ratio": "0.954465:0.045535",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 170.0,
    "total_tokens": 517.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.329395,
      "aei_text": 2.910134,
      "aei_vision": 0.0642,
      "text_ratio": 0.978415,
      "vision_ratio": 0.021585
    },
    "middle": {
      "mdi": 27.846869,
      "aei_text": 2.833482,
      "aei_vision": 0.101752,
      "text_ratio": 0.965334,
      "vision_ratio": 0.034666
    },
    "late": {
      "mdi": 24.863243,
      "aei_text": 2.810449,
      "aei_vision": 0.113036,
      "text_ratio": 0.961335,
      "vision_ratio": 0.038665
    },
    "all": {
      "mdi": 24.863243,
      "aei_text": 2.851358,
      "aei_vision": 0.092995,
      "text_ratio": 0.961335,
      "vision_ratio": 0.038665
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961335,
      0.038665
    ],
    "text_vision_ratio": "0.961335:0.038665",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 170.0,
    "total_tokens": 517.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.65617,
      "aei_text": 2.892304,
      "aei_vision": 0.072935,
      "text_ratio": 0.975403,
      "vision_ratio": 0.024597
    },
    "middle": {
      "mdi": 34.923861,
      "aei_text": 2.873245,
      "aei_vision": 0.082272,
      "text_ratio": 0.972163,
      "vision_ratio": 0.027837
    },
    "late": {
      "mdi": 38.626427,
      "aei_text": 2.888535,
      "aei_vision": 0.074781,
      "text_ratio": 0.974764,
      "vision_ratio": 0.025236
    },
    "all": {
      "mdi": 38.626427,
      "aei_text": 2.884696,
      "aei_vision": 0.076662,
      "text_ratio": 0.974764,
      "vision_ratio": 0.025236
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974764,
      0.025236
    ],
    "text_vision_ratio": "0.974764:0.025236",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.027469,
      "aei_text": 3.2644,
      "aei_vision": 0.066583,
      "text_ratio": 0.980011,
      "vision_ratio": 0.019989
    },
    "middle": {
      "mdi": 27.011648,
      "aei_text": 3.143598,
      "aei_vision": 0.116379,
      "text_ratio": 0.964301,
      "vision_ratio": 0.035699
    },
    "late": {
      "mdi": 27.061949,
      "aei_text": 3.14408,
      "aei_vision": 0.116181,
      "text_ratio": 0.964365,
      "vision_ratio": 0.035635
    },
    "all": {
      "mdi": 27.061949,
      "aei_text": 3.184011,
      "aei_vision": 0.099721,
      "text_ratio": 0.964365,
      "vision_ratio": 0.035635
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964365,
      0.035635
    ],
    "text_vision_ratio": "0.964365:0.035635",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.754262,
      "aei_text": 3.241973,
      "aei_vision": 0.075828,
      "text_ratio": 0.977145,
      "vision_ratio": 0.022855
    },
    "middle": {
      "mdi": 33.196651,
      "aei_text": 3.192618,
      "aei_vision": 0.096173,
      "text_ratio": 0.970757,
      "vision_ratio": 0.029243
    },
    "late": {
      "mdi": 35.443648,
      "aei_text": 3.206461,
      "aei_vision": 0.090466,
      "text_ratio": 0.97256,
      "vision_ratio": 0.02744
    },
    "all": {
      "mdi": 35.443648,
      "aei_text": 3.213682,
      "aei_vision": 0.08749,
      "text_ratio": 0.97256,
      "vision_ratio": 0.02744
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97256,
      0.02744
    ],
    "text_vision_ratio": "0.972560:0.027440",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 165.0,
    "total_tokens": 581.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.264636,
      "aei_text": 2.826872,
      "aei_vision": 0.275399,
      "text_ratio": 0.911227,
      "vision_ratio": 0.088773
    },
    "middle": {
      "mdi": 8.783578,
      "aei_text": 2.735906,
      "aei_vision": 0.31148,
      "text_ratio": 0.897788,
      "vision_ratio": 0.102212
    },
    "late": {
      "mdi": 10.383815,
      "aei_text": 2.833285,
      "aei_vision": 0.272856,
      "text_ratio": 0.912156,
      "vision_ratio": 0.087844
    },
    "all": {
      "mdi": 10.383815,
      "aei_text": 2.798713,
      "aei_vision": 0.286568,
      "text_ratio": 0.912156,
      "vision_ratio": 0.087844
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.912156,
      0.087844
    ],
    "text_vision_ratio": "0.912156:0.087844",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 165.0,
    "total_tokens": 581.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 8.73824,
      "aei_text": 2.732744,
      "aei_vision": 0.312734,
      "text_ratio": 0.897312,
      "vision_ratio": 0.102688
    },
    "middle": {
      "mdi": 7.637521,
      "aei_text": 2.647312,
      "aei_vision": 0.346619,
      "text_ratio": 0.884226,
      "vision_ratio": 0.115774
    },
    "late": {
      "mdi": 10.417944,
      "aei_text": 2.835099,
      "aei_vision": 0.272136,
      "text_ratio": 0.912419,
      "vision_ratio": 0.087581
    },
    "all": {
      "mdi": 10.417944,
      "aei_text": 2.738382,
      "aei_vision": 0.310497,
      "text_ratio": 0.912419,
      "vision_ratio": 0.087581
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.912419,
      0.087581
    ],
    "text_vision_ratio": "0.912419:0.087581",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.459206,
      "aei_text": 3.232346,
      "aei_vision": 0.091157,
      "text_ratio": 0.972572,
      "vision_ratio": 0.027428
    },
    "middle": {
      "mdi": 32.92734,
      "aei_text": 3.216325,
      "aei_vision": 0.097679,
      "text_ratio": 0.970525,
      "vision_ratio": 0.029475
    },
    "late": {
      "mdi": 26.347473,
      "aei_text": 3.161517,
      "aei_vision": 0.119993,
      "text_ratio": 0.963434,
      "vision_ratio": 0.036566
    },
    "all": {
      "mdi": 26.347473,
      "aei_text": 3.203396,
      "aei_vision": 0.102943,
      "text_ratio": 0.963434,
      "vision_ratio": 0.036566
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963434,
      0.036566
    ],
    "text_vision_ratio": "0.963434:0.036566",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.139664,
      "aei_text": 3.241849,
      "aei_vision": 0.087288,
      "text_ratio": 0.973781,
      "vision_ratio": 0.026219
    },
    "middle": {
      "mdi": 34.948274,
      "aei_text": 3.229288,
      "aei_vision": 0.092402,
      "text_ratio": 0.972182,
      "vision_ratio": 0.027818
    },
    "late": {
      "mdi": 38.78786,
      "aei_text": 3.250417,
      "aei_vision": 0.0838,
      "text_ratio": 0.974867,
      "vision_ratio": 0.025133
    },
    "all": {
      "mdi": 38.78786,
      "aei_text": 3.240518,
      "aei_vision": 0.08783,
      "text_ratio": 0.974867,
      "vision_ratio": 0.025133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974867,
      0.025133
    ],
    "text_vision_ratio": "0.974867:0.025133",
    "skip_reason": null
  }
}
```


## === Rollout Step 9 ===
Step: 8/43 | 2025-10-22 18:28:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 39.384 | 35.735 | 36.738 | 36.738 |
| MDI Std | 11.639 | 13.350 | 11.459 | 11.459 |
| Vision Tokens | 351.0 ± 54.1 |
| Text Tokens | 164.6 ± 4.8 |
| Total Tokens | 515.6 ± 53.1 |
| Vision Ratio | 0.676 |
| Text Ratio | 0.324 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.222479,
      "aei_text": 2.970443,
      "aei_vision": 0.068724,
      "text_ratio": 0.977387,
      "vision_ratio": 0.022613
    },
    "middle": {
      "mdi": 25.06823,
      "aei_text": 2.873333,
      "aei_vision": 0.114621,
      "text_ratio": 0.961639,
      "vision_ratio": 0.038361
    },
    "late": {
      "mdi": 30.641736,
      "aei_text": 2.914597,
      "aei_vision": 0.095119,
      "text_ratio": 0.968396,
      "vision_ratio": 0.031604
    },
    "all": {
      "mdi": 30.641736,
      "aei_text": 2.919462,
      "aei_vision": 0.092819,
      "text_ratio": 0.968396,
      "vision_ratio": 0.031604
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968396,
      0.031604
    ],
    "text_vision_ratio": "0.968396:0.031604",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.81651,
      "aei_text": 2.986414,
      "aei_vision": 0.061176,
      "text_ratio": 0.979926,
      "vision_ratio": 0.020074
    },
    "middle": {
      "mdi": 33.178777,
      "aei_text": 2.929063,
      "aei_vision": 0.088281,
      "text_ratio": 0.970742,
      "vision_ratio": 0.029258
    },
    "late": {
      "mdi": 34.078403,
      "aei_text": 2.933706,
      "aei_vision": 0.086087,
      "text_ratio": 0.971492,
      "vision_ratio": 0.028508
    },
    "all": {
      "mdi": 34.078403,
      "aei_text": 2.94973,
      "aei_vision": 0.078514,
      "text_ratio": 0.971492,
      "vision_ratio": 0.028508
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971492,
      0.028508
    ],
    "text_vision_ratio": "0.971492:0.028508",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 169.0,
    "total_tokens": 387.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.268009,
      "aei_text": 2.215268,
      "aei_vision": 0.057888,
      "text_ratio": 0.974534,
      "vision_ratio": 0.025466
    },
    "middle": {
      "mdi": 38.103858,
      "aei_text": 2.214957,
      "aei_vision": 0.058129,
      "text_ratio": 0.974427,
      "vision_ratio": 0.025573
    },
    "late": {
      "mdi": 44.214331,
      "aei_text": 2.225026,
      "aei_vision": 0.050324,
      "text_ratio": 0.977883,
      "vision_ratio": 0.022117
    },
    "all": {
      "mdi": 44.214331,
      "aei_text": 2.218419,
      "aei_vision": 0.055446,
      "text_ratio": 0.977883,
      "vision_ratio": 0.022117
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977883,
      0.022117
    ],
    "text_vision_ratio": "0.977883:0.022117",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 169.0,
    "total_tokens": 387.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.16797,
      "aei_text": 2.218691,
      "aei_vision": 0.055235,
      "text_ratio": 0.975709,
      "vision_ratio": 0.024291
    },
    "middle": {
      "mdi": 35.023488,
      "aei_text": 2.208597,
      "aei_vision": 0.06306,
      "text_ratio": 0.97224,
      "vision_ratio": 0.02776
    },
    "late": {
      "mdi": 34.936283,
      "aei_text": 2.208401,
      "aei_vision": 0.063212,
      "text_ratio": 0.972173,
      "vision_ratio": 0.027827
    },
    "all": {
      "mdi": 34.936283,
      "aei_text": 2.211898,
      "aei_vision": 0.060501,
      "text_ratio": 0.972173,
      "vision_ratio": 0.027827
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972173,
      0.027827
    ],
    "text_vision_ratio": "0.972173:0.027827",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.81506,
      "aei_text": 2.796328,
      "aei_vision": 0.236675,
      "text_ratio": 0.921967,
      "vision_ratio": 0.078033
    },
    "middle": {
      "mdi": 11.974868,
      "aei_text": 2.80254,
      "aei_vision": 0.234035,
      "text_ratio": 0.922928,
      "vision_ratio": 0.077072
    },
    "late": {
      "mdi": 18.807326,
      "aei_text": 2.98037,
      "aei_vision": 0.158469,
      "text_ratio": 0.949514,
      "vision_ratio": 0.050486
    },
    "all": {
      "mdi": 18.807326,
      "aei_text": 2.859729,
      "aei_vision": 0.209734,
      "text_ratio": 0.949514,
      "vision_ratio": 0.050486
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.949514,
      0.050486
    ],
    "text_vision_ratio": "0.949514:0.050486",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.363974,
      "aei_text": 2.778012,
      "aei_vision": 0.244458,
      "text_ratio": 0.91912,
      "vision_ratio": 0.08088
    },
    "middle": {
      "mdi": 8.541254,
      "aei_text": 2.62896,
      "aei_vision": 0.307796,
      "text_ratio": 0.895192,
      "vision_ratio": 0.104808
    },
    "late": {
      "mdi": 12.45413,
      "aei_text": 2.820366,
      "aei_vision": 0.22646,
      "text_ratio": 0.925673,
      "vision_ratio": 0.074327
    },
    "all": {
      "mdi": 12.45413,
      "aei_text": 2.742429,
      "aei_vision": 0.259579,
      "text_ratio": 0.925673,
      "vision_ratio": 0.074327
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.925673,
      0.074327
    ],
    "text_vision_ratio": "0.925673:0.074327",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.597956,
      "aei_text": 3.320803,
      "aei_vision": 0.066954,
      "text_ratio": 0.980236,
      "vision_ratio": 0.019764
    },
    "middle": {
      "mdi": 62.801045,
      "aei_text": 3.354482,
      "aei_vision": 0.053414,
      "text_ratio": 0.984326,
      "vision_ratio": 0.015674
    },
    "late": {
      "mdi": 57.813757,
      "aei_text": 3.343493,
      "aei_vision": 0.057832,
      "text_ratio": 0.982997,
      "vision_ratio": 0.017003
    },
    "all": {
      "mdi": 57.813757,
      "aei_text": 3.339589,
      "aei_vision": 0.059402,
      "text_ratio": 0.982997,
      "vision_ratio": 0.017003
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982997,
      0.017003
    ],
    "text_vision_ratio": "0.982997:0.017003",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.53473,
      "aei_text": 3.313934,
      "aei_vision": 0.069716,
      "text_ratio": 0.979396,
      "vision_ratio": 0.020604
    },
    "middle": {
      "mdi": 37.54725,
      "aei_text": 3.270674,
      "aei_vision": 0.087108,
      "text_ratio": 0.974058,
      "vision_ratio": 0.025942
    },
    "late": {
      "mdi": 30.076761,
      "aei_text": 3.220968,
      "aei_vision": 0.107092,
      "text_ratio": 0.967822,
      "vision_ratio": 0.032178
    },
    "all": {
      "mdi": 30.076761,
      "aei_text": 3.268522,
      "aei_vision": 0.087973,
      "text_ratio": 0.967822,
      "vision_ratio": 0.032178
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967822,
      0.032178
    ],
    "text_vision_ratio": "0.967822:0.032178",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 159.0,
    "total_tokens": 506.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.942691,
      "aei_text": 3.041012,
      "aei_vision": 0.064781,
      "text_ratio": 0.979142,
      "vision_ratio": 0.020858
    },
    "middle": {
      "mdi": 52.668568,
      "aei_text": 3.05577,
      "aei_vision": 0.058019,
      "text_ratio": 0.981367,
      "vision_ratio": 0.018633
    },
    "late": {
      "mdi": 44.064302,
      "aei_text": 3.032212,
      "aei_vision": 0.068813,
      "text_ratio": 0.977809,
      "vision_ratio": 0.022191
    },
    "all": {
      "mdi": 44.064302,
      "aei_text": 3.042998,
      "aei_vision": 0.063871,
      "text_ratio": 0.977809,
      "vision_ratio": 0.022191
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977809,
      0.022191
    ],
    "text_vision_ratio": "0.977809:0.022191",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 159.0,
    "total_tokens": 506.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.661411,
      "aei_text": 3.037226,
      "aei_vision": 0.066516,
      "text_ratio": 0.978569,
      "vision_ratio": 0.021431
    },
    "middle": {
      "mdi": 52.390737,
      "aei_text": 3.055126,
      "aei_vision": 0.058314,
      "text_ratio": 0.98127,
      "vision_ratio": 0.01873
    },
    "late": {
      "mdi": 43.472686,
      "aei_text": 3.030266,
      "aei_vision": 0.069705,
      "text_ratio": 0.977514,
      "vision_ratio": 0.022486
    },
    "all": {
      "mdi": 43.472686,
      "aei_text": 3.040867,
      "aei_vision": 0.064848,
      "text_ratio": 0.977514,
      "vision_ratio": 0.022486
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977514,
      0.022486
    ],
    "text_vision_ratio": "0.977514:0.022486",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.75987,
      "aei_text": 3.146795,
      "aei_vision": 0.093211,
      "text_ratio": 0.971231,
      "vision_ratio": 0.028769
    },
    "middle": {
      "mdi": 40.634392,
      "aei_text": 3.182074,
      "aei_vision": 0.07831,
      "text_ratio": 0.975981,
      "vision_ratio": 0.024019
    },
    "late": {
      "mdi": 50.071908,
      "aei_text": 3.215439,
      "aei_vision": 0.064216,
      "text_ratio": 0.98042,
      "vision_ratio": 0.01958
    },
    "all": {
      "mdi": 50.071908,
      "aei_text": 3.181435,
      "aei_vision": 0.07858,
      "text_ratio": 0.98042,
      "vision_ratio": 0.01958
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98042,
      0.01958
    ],
    "text_vision_ratio": "0.980420:0.019580",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.869788,
      "aei_text": 3.17414,
      "aei_vision": 0.081661,
      "text_ratio": 0.974918,
      "vision_ratio": 0.025082
    },
    "middle": {
      "mdi": 39.051608,
      "aei_text": 3.174989,
      "aei_vision": 0.081302,
      "text_ratio": 0.975032,
      "vision_ratio": 0.024968
    },
    "late": {
      "mdi": 43.712347,
      "aei_text": 3.194457,
      "aei_vision": 0.073079,
      "text_ratio": 0.977635,
      "vision_ratio": 0.022365
    },
    "all": {
      "mdi": 43.712347,
      "aei_text": 3.181199,
      "aei_vision": 0.078679,
      "text_ratio": 0.977635,
      "vision_ratio": 0.022365
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977635,
      0.022365
    ],
    "text_vision_ratio": "0.977635:0.022365",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.522229,
      "aei_text": 3.030905,
      "aei_vision": 0.057707,
      "text_ratio": 0.981316,
      "vision_ratio": 0.018684
    },
    "middle": {
      "mdi": 28.029737,
      "aei_text": 2.929985,
      "aei_vision": 0.104531,
      "text_ratio": 0.965553,
      "vision_ratio": 0.034447
    },
    "late": {
      "mdi": 23.988827,
      "aei_text": 2.895163,
      "aei_vision": 0.120688,
      "text_ratio": 0.959982,
      "vision_ratio": 0.040018
    },
    "all": {
      "mdi": 23.988827,
      "aei_text": 2.952001,
      "aei_vision": 0.094317,
      "text_ratio": 0.959982,
      "vision_ratio": 0.040018
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959982,
      0.040018
    ],
    "text_vision_ratio": "0.959982:0.040018",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.993475,
      "aei_text": 3.011044,
      "aei_vision": 0.066922,
      "text_ratio": 0.978258,
      "vision_ratio": 0.021742
    },
    "middle": {
      "mdi": 39.570557,
      "aei_text": 2.992299,
      "aei_vision": 0.075619,
      "text_ratio": 0.975352,
      "vision_ratio": 0.024648
    },
    "late": {
      "mdi": 34.93311,
      "aei_text": 2.97192,
      "aei_vision": 0.085075,
      "text_ratio": 0.972171,
      "vision_ratio": 0.027829
    },
    "all": {
      "mdi": 34.93311,
      "aei_text": 2.991759,
      "aei_vision": 0.07587,
      "text_ratio": 0.972171,
      "vision_ratio": 0.027829
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972171,
      0.027829
    ],
    "text_vision_ratio": "0.972171:0.027829",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 173.0,
    "total_tokens": 543.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.961745,
      "aei_text": 2.962539,
      "aei_vision": 0.08238,
      "text_ratio": 0.972945,
      "vision_ratio": 0.027055
    },
    "middle": {
      "mdi": 34.792695,
      "aei_text": 2.956962,
      "aei_vision": 0.084988,
      "text_ratio": 0.972061,
      "vision_ratio": 0.027939
    },
    "late": {
      "mdi": 47.024893,
      "aei_text": 3.002187,
      "aei_vision": 0.063842,
      "text_ratio": 0.979177,
      "vision_ratio": 0.020823
    },
    "all": {
      "mdi": 47.024893,
      "aei_text": 2.973885,
      "aei_vision": 0.077075,
      "text_ratio": 0.979177,
      "vision_ratio": 0.020823
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979177,
      0.020823
    ],
    "text_vision_ratio": "0.979177:0.020823",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 173.0,
    "total_tokens": 543.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.649817,
      "aei_text": 2.981843,
      "aei_vision": 0.073354,
      "text_ratio": 0.97599,
      "vision_ratio": 0.02401
    },
    "middle": {
      "mdi": 32.386558,
      "aei_text": 2.944294,
      "aei_vision": 0.090911,
      "text_ratio": 0.970048,
      "vision_ratio": 0.029952
    },
    "late": {
      "mdi": 37.520355,
      "aei_text": 2.969464,
      "aei_vision": 0.079143,
      "text_ratio": 0.97404,
      "vision_ratio": 0.02596
    },
    "all": {
      "mdi": 37.520355,
      "aei_text": 2.9652,
      "aei_vision": 0.081136,
      "text_ratio": 0.97404,
      "vision_ratio": 0.02596
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97404,
      0.02596
    ],
    "text_vision_ratio": "0.974040:0.025960",
    "skip_reason": null
  }
}
```


## === Rollout Step 10 ===
Step: 9/43 | 2025-10-22 18:29:29

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 45.108 | 38.864 | 44.286 | 44.286 |
| MDI Std | 16.703 | 20.499 | 23.482 | 23.482 |
| Vision Tokens | 367.6 ± 53.2 |
| Text Tokens | 164.8 ± 2.4 |
| Total Tokens | 532.4 ± 53.9 |
| Vision Ratio | 0.687 |
| Text Ratio | 0.313 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 166.0,
    "total_tokens": 582.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.945635,
      "aei_text": 2.971964,
      "aei_vision": 0.213111,
      "text_ratio": 0.933091,
      "vision_ratio": 0.066909
    },
    "middle": {
      "mdi": 12.67272,
      "aei_text": 2.927176,
      "aei_vision": 0.230982,
      "text_ratio": 0.926862,
      "vision_ratio": 0.073138
    },
    "late": {
      "mdi": 35.668966,
      "aei_text": 3.275869,
      "aei_vision": 0.091841,
      "text_ratio": 0.972729,
      "vision_ratio": 0.027271
    },
    "all": {
      "mdi": 35.668966,
      "aei_text": 3.058281,
      "aei_vision": 0.178667,
      "text_ratio": 0.972729,
      "vision_ratio": 0.027271
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972729,
      0.027271
    ],
    "text_vision_ratio": "0.972729:0.027271",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 166.0,
    "total_tokens": 582.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.98197,
      "aei_text": 2.973141,
      "aei_vision": 0.212641,
      "text_ratio": 0.933253,
      "vision_ratio": 0.066747
    },
    "middle": {
      "mdi": 13.199463,
      "aei_text": 2.94659,
      "aei_vision": 0.223236,
      "text_ratio": 0.929575,
      "vision_ratio": 0.070425
    },
    "late": {
      "mdi": 36.870683,
      "aei_text": 3.282893,
      "aei_vision": 0.089038,
      "text_ratio": 0.973594,
      "vision_ratio": 0.026406
    },
    "all": {
      "mdi": 36.870683,
      "aei_text": 3.06767,
      "aei_vision": 0.17492,
      "text_ratio": 0.973594,
      "vision_ratio": 0.026406
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973594,
      0.026406
    ],
    "text_vision_ratio": "0.973594:0.026406",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.331467,
      "aei_text": 3.271039,
      "aei_vision": 0.058068,
      "text_ratio": 0.982558,
      "vision_ratio": 0.017442
    },
    "middle": {
      "mdi": 41.588357,
      "aei_text": 3.224127,
      "aei_vision": 0.077525,
      "text_ratio": 0.976519,
      "vision_ratio": 0.023481
    },
    "late": {
      "mdi": 44.048611,
      "aei_text": 3.234025,
      "aei_vision": 0.073419,
      "text_ratio": 0.977802,
      "vision_ratio": 0.022198
    },
    "all": {
      "mdi": 44.048611,
      "aei_text": 3.24306,
      "aei_vision": 0.069672,
      "text_ratio": 0.977802,
      "vision_ratio": 0.022198
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977802,
      0.022198
    ],
    "text_vision_ratio": "0.977802:0.022198",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.080082,
      "aei_text": 3.272801,
      "aei_vision": 0.057337,
      "text_ratio": 0.982782,
      "vision_ratio": 0.017218
    },
    "middle": {
      "mdi": 27.441853,
      "aei_text": 3.135553,
      "aei_vision": 0.114262,
      "text_ratio": 0.964841,
      "vision_ratio": 0.035159
    },
    "late": {
      "mdi": 22.808054,
      "aei_text": 3.084934,
      "aei_vision": 0.135256,
      "text_ratio": 0.957997,
      "vision_ratio": 0.042003
    },
    "all": {
      "mdi": 22.808054,
      "aei_text": 3.164437,
      "aei_vision": 0.102282,
      "text_ratio": 0.957997,
      "vision_ratio": 0.042003
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957997,
      0.042003
    ],
    "text_vision_ratio": "0.957997:0.042003",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 72.620277,
      "aei_text": 3.31518,
      "aei_vision": 0.045651,
      "text_ratio": 0.986417,
      "vision_ratio": 0.013583
    },
    "middle": {
      "mdi": 59.585657,
      "aei_text": 3.291902,
      "aei_vision": 0.055247,
      "text_ratio": 0.983494,
      "vision_ratio": 0.016506
    },
    "late": {
      "mdi": 44.504383,
      "aei_text": 3.248833,
      "aei_vision": 0.073,
      "text_ratio": 0.978024,
      "vision_ratio": 0.021976
    },
    "all": {
      "mdi": 44.504383,
      "aei_text": 3.285303,
      "aei_vision": 0.057967,
      "text_ratio": 0.978024,
      "vision_ratio": 0.021976
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978024,
      0.021976
    ],
    "text_vision_ratio": "0.978024:0.021976",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 73.545166,
      "aei_text": 3.316528,
      "aei_vision": 0.045095,
      "text_ratio": 0.986585,
      "vision_ratio": 0.013415
    },
    "middle": {
      "mdi": 29.549815,
      "aei_text": 3.166009,
      "aei_vision": 0.107141,
      "text_ratio": 0.967267,
      "vision_ratio": 0.032733
    },
    "late": {
      "mdi": 34.004635,
      "aei_text": 3.197792,
      "aei_vision": 0.09404,
      "text_ratio": 0.971432,
      "vision_ratio": 0.028568
    },
    "all": {
      "mdi": 34.004635,
      "aei_text": 3.226766,
      "aei_vision": 0.082096,
      "text_ratio": 0.971432,
      "vision_ratio": 0.028568
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971432,
      0.028568
    ],
    "text_vision_ratio": "0.971432:0.028568",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.451034,
      "aei_text": 3.181011,
      "aei_vision": 0.073209,
      "text_ratio": 0.977503,
      "vision_ratio": 0.022497
    },
    "middle": {
      "mdi": 64.516276,
      "aei_text": 3.235283,
      "aei_vision": 0.050147,
      "text_ratio": 0.984737,
      "vision_ratio": 0.015263
    },
    "late": {
      "mdi": 87.035792,
      "aei_text": 3.265013,
      "aei_vision": 0.037513,
      "text_ratio": 0.988641,
      "vision_ratio": 0.011359
    },
    "all": {
      "mdi": 87.035792,
      "aei_text": 3.227112,
      "aei_vision": 0.053619,
      "text_ratio": 0.988641,
      "vision_ratio": 0.011359
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988641,
      0.011359
    ],
    "text_vision_ratio": "0.988641:0.011359",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.142087,
      "aei_text": 3.179841,
      "aei_vision": 0.073706,
      "text_ratio": 0.977346,
      "vision_ratio": 0.022654
    },
    "middle": {
      "mdi": 68.427921,
      "aei_text": 3.241805,
      "aei_vision": 0.047375,
      "text_ratio": 0.985597,
      "vision_ratio": 0.014403
    },
    "late": {
      "mdi": 98.841425,
      "aei_text": 3.275312,
      "aei_vision": 0.033137,
      "text_ratio": 0.989984,
      "vision_ratio": 0.010016
    },
    "all": {
      "mdi": 98.841425,
      "aei_text": 3.232316,
      "aei_vision": 0.051408,
      "text_ratio": 0.989984,
      "vision_ratio": 0.010016
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989984,
      0.010016
    ],
    "text_vision_ratio": "0.989984:0.010016",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 168.0,
    "total_tokens": 538.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.896039,
      "aei_text": 3.049385,
      "aei_vision": 0.069468,
      "text_ratio": 0.977726,
      "vision_ratio": 0.022274
    },
    "middle": {
      "mdi": 63.053153,
      "aei_text": 3.0943,
      "aei_vision": 0.049074,
      "text_ratio": 0.984388,
      "vision_ratio": 0.015612
    },
    "late": {
      "mdi": 54.993493,
      "aei_text": 3.07907,
      "aei_vision": 0.05599,
      "text_ratio": 0.982141,
      "vision_ratio": 0.017859
    },
    "all": {
      "mdi": 54.993493,
      "aei_text": 3.074249,
      "aei_vision": 0.058179,
      "text_ratio": 0.982141,
      "vision_ratio": 0.017859
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982141,
      0.017859
    ],
    "text_vision_ratio": "0.982141:0.017859",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 168.0,
    "total_tokens": 538.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.474212,
      "aei_text": 3.068491,
      "aei_vision": 0.060793,
      "text_ratio": 0.980573,
      "vision_ratio": 0.019427
    },
    "middle": {
      "mdi": 54.070981,
      "aei_text": 3.077049,
      "aei_vision": 0.056908,
      "text_ratio": 0.981842,
      "vision_ratio": 0.018158
    },
    "late": {
      "mdi": 50.708268,
      "aei_text": 3.069083,
      "aei_vision": 0.060524,
      "text_ratio": 0.980661,
      "vision_ratio": 0.019339
    },
    "all": {
      "mdi": 50.708268,
      "aei_text": 3.071541,
      "aei_vision": 0.059408,
      "text_ratio": 0.980661,
      "vision_ratio": 0.019339
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980661,
      0.019339
    ],
    "text_vision_ratio": "0.980661:0.019339",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.186406,
      "aei_text": 3.036683,
      "aei_vision": 0.055026,
      "text_ratio": 0.982202,
      "vision_ratio": 0.017798
    },
    "middle": {
      "mdi": 29.718834,
      "aei_text": 2.941924,
      "aei_vision": 0.098992,
      "text_ratio": 0.967447,
      "vision_ratio": 0.032553
    },
    "late": {
      "mdi": 22.775071,
      "aei_text": 2.882499,
      "aei_vision": 0.126564,
      "text_ratio": 0.957939,
      "vision_ratio": 0.042061
    },
    "all": {
      "mdi": 22.775071,
      "aei_text": 2.953688,
      "aei_vision": 0.093534,
      "text_ratio": 0.957939,
      "vision_ratio": 0.042061
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957939,
      0.042061
    ],
    "text_vision_ratio": "0.957939:0.042061",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.008667,
      "aei_text": 3.032001,
      "aei_vision": 0.057198,
      "text_ratio": 0.981484,
      "vision_ratio": 0.018516
    },
    "middle": {
      "mdi": 19.355755,
      "aei_text": 2.839139,
      "aei_vision": 0.146682,
      "text_ratio": 0.950874,
      "vision_ratio": 0.049126
    },
    "late": {
      "mdi": 14.695682,
      "aei_text": 2.751711,
      "aei_vision": 0.187246,
      "text_ratio": 0.936288,
      "vision_ratio": 0.063712
    },
    "all": {
      "mdi": 14.695682,
      "aei_text": 2.874294,
      "aei_vision": 0.130371,
      "text_ratio": 0.936288,
      "vision_ratio": 0.063712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936288,
      0.063712
    ],
    "text_vision_ratio": "0.936288:0.063712",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 164.0,
    "total_tokens": 400.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.294561,
      "aei_text": 2.331801,
      "aei_vision": 0.074511,
      "text_ratio": 0.969035,
      "vision_ratio": 0.030965
    },
    "middle": {
      "mdi": 17.830209,
      "aei_text": 2.256878,
      "aei_vision": 0.126576,
      "text_ratio": 0.946894,
      "vision_ratio": 0.053106
    },
    "late": {
      "mdi": 17.300467,
      "aei_text": 2.251729,
      "aei_vision": 0.130154,
      "text_ratio": 0.945357,
      "vision_ratio": 0.054643
    },
    "all": {
      "mdi": 17.300467,
      "aei_text": 2.280145,
      "aei_vision": 0.110408,
      "text_ratio": 0.945357,
      "vision_ratio": 0.054643
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945357,
      0.054643
    ],
    "text_vision_ratio": "0.945357:0.054643",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 164.0,
    "total_tokens": 400.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 29.392624,
      "aei_text": 2.325186,
      "aei_vision": 0.079108,
      "text_ratio": 0.967097,
      "vision_ratio": 0.032903
    },
    "middle": {
      "mdi": 40.728568,
      "aei_text": 2.355789,
      "aei_vision": 0.057841,
      "text_ratio": 0.976036,
      "vision_ratio": 0.023964
    },
    "late": {
      "mdi": 54.810355,
      "aei_text": 2.376627,
      "aei_vision": 0.043361,
      "text_ratio": 0.982082,
      "vision_ratio": 0.017918
    },
    "all": {
      "mdi": 54.810355,
      "aei_text": 2.352541,
      "aei_vision": 0.060099,
      "text_ratio": 0.982082,
      "vision_ratio": 0.017918
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982082,
      0.017918
    ],
    "text_vision_ratio": "0.982082:0.017918",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.09186,
      "aei_text": 3.158183,
      "aei_vision": 0.08291,
      "text_ratio": 0.974419,
      "vision_ratio": 0.025581
    },
    "middle": {
      "mdi": 67.089431,
      "aei_text": 3.239656,
      "aei_vision": 0.048289,
      "text_ratio": 0.985313,
      "vision_ratio": 0.014687
    },
    "late": {
      "mdi": 66.990986,
      "aei_text": 3.239495,
      "aei_vision": 0.048357,
      "text_ratio": 0.985292,
      "vision_ratio": 0.014708
    },
    "all": {
      "mdi": 66.990986,
      "aei_text": 3.212433,
      "aei_vision": 0.059857,
      "text_ratio": 0.985292,
      "vision_ratio": 0.014708
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985292,
      0.014708
    ],
    "text_vision_ratio": "0.985292:0.014708",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.285496,
      "aei_text": 3.191051,
      "aei_vision": 0.068943,
      "text_ratio": 0.978852,
      "vision_ratio": 0.021148
    },
    "middle": {
      "mdi": 12.990092,
      "aei_text": 2.838982,
      "aei_vision": 0.21855,
      "text_ratio": 0.928521,
      "vision_ratio": 0.071479
    },
    "late": {
      "mdi": 22.520021,
      "aei_text": 3.036034,
      "aei_vision": 0.134815,
      "text_ratio": 0.957483,
      "vision_ratio": 0.042517
    },
    "all": {
      "mdi": 22.520021,
      "aei_text": 3.022043,
      "aei_vision": 0.14076,
      "text_ratio": 0.957483,
      "vision_ratio": 0.042517
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957483,
      0.042517
    ],
    "text_vision_ratio": "0.957483:0.042517",
    "skip_reason": null
  }
}
```


## === Rollout Step 11 ===
Step: 10/43 | 2025-10-22 18:30:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.489 | 35.949 | 35.330 | 35.330 |
| MDI Std | 12.391 | 11.461 | 11.119 | 11.119 |
| Vision Tokens | 384.4 ± 52.6 |
| Text Tokens | 165.1 ± 4.8 |
| Total Tokens | 549.5 ± 50.9 |
| Vision Ratio | 0.697 |
| Text Ratio | 0.303 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 167.0,
    "total_tokens": 491.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.808565,
      "aei_text": 2.827719,
      "aei_vision": 0.057935,
      "text_ratio": 0.979923,
      "vision_ratio": 0.020077
    },
    "middle": {
      "mdi": 27.593886,
      "aei_text": 2.74698,
      "aei_vision": 0.09955,
      "text_ratio": 0.965027,
      "vision_ratio": 0.034973
    },
    "late": {
      "mdi": 32.583004,
      "aei_text": 2.774892,
      "aei_vision": 0.085164,
      "text_ratio": 0.970223,
      "vision_ratio": 0.029777
    },
    "all": {
      "mdi": 32.583004,
      "aei_text": 2.783201,
      "aei_vision": 0.080881,
      "text_ratio": 0.970223,
      "vision_ratio": 0.029777
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970223,
      0.029777
    ],
    "text_vision_ratio": "0.970223:0.029777",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 167.0,
    "total_tokens": 491.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.774599,
      "aei_text": 2.806578,
      "aei_vision": 0.068832,
      "text_ratio": 0.976062,
      "vision_ratio": 0.023938
    },
    "middle": {
      "mdi": 49.030223,
      "aei_text": 2.828208,
      "aei_vision": 0.057683,
      "text_ratio": 0.980012,
      "vision_ratio": 0.019988
    },
    "late": {
      "mdi": 54.853558,
      "aei_text": 2.839683,
      "aei_vision": 0.051768,
      "text_ratio": 0.982096,
      "vision_ratio": 0.017904
    },
    "all": {
      "mdi": 54.853558,
      "aei_text": 2.824825,
      "aei_vision": 0.059426,
      "text_ratio": 0.982096,
      "vision_ratio": 0.017904
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982096,
      0.017904
    ],
    "text_vision_ratio": "0.982096:0.017904",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.879372,
      "aei_text": 3.198731,
      "aei_vision": 0.071274,
      "text_ratio": 0.978204,
      "vision_ratio": 0.021796
    },
    "middle": {
      "mdi": 50.043766,
      "aei_text": 3.215358,
      "aei_vision": 0.064251,
      "text_ratio": 0.980409,
      "vision_ratio": 0.019591
    },
    "late": {
      "mdi": 58.865872,
      "aei_text": 3.237273,
      "aei_vision": 0.054994,
      "text_ratio": 0.983296,
      "vision_ratio": 0.016704
    },
    "all": {
      "mdi": 58.865872,
      "aei_text": 3.21712,
      "aei_vision": 0.063506,
      "text_ratio": 0.983296,
      "vision_ratio": 0.016704
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983296,
      0.016704
    ],
    "text_vision_ratio": "0.983296:0.016704",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.462437,
      "aei_text": 3.197229,
      "aei_vision": 0.071909,
      "text_ratio": 0.978004,
      "vision_ratio": 0.021996
    },
    "middle": {
      "mdi": 38.446277,
      "aei_text": 3.172134,
      "aei_vision": 0.082508,
      "text_ratio": 0.974649,
      "vision_ratio": 0.025351
    },
    "late": {
      "mdi": 44.317358,
      "aei_text": 3.1967,
      "aei_vision": 0.072132,
      "text_ratio": 0.977933,
      "vision_ratio": 0.022067
    },
    "all": {
      "mdi": 44.317358,
      "aei_text": 3.188687,
      "aei_vision": 0.075516,
      "text_ratio": 0.977933,
      "vision_ratio": 0.022067
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977933,
      0.022067
    ],
    "text_vision_ratio": "0.977933:0.022067",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.246956,
      "aei_text": 3.243957,
      "aei_vision": 0.07501,
      "text_ratio": 0.9774,
      "vision_ratio": 0.0226
    },
    "middle": {
      "mdi": 42.495404,
      "aei_text": 3.240913,
      "aei_vision": 0.076265,
      "text_ratio": 0.977009,
      "vision_ratio": 0.022991
    },
    "late": {
      "mdi": 37.713313,
      "aei_text": 3.218871,
      "aei_vision": 0.085351,
      "text_ratio": 0.974169,
      "vision_ratio": 0.025831
    },
    "all": {
      "mdi": 37.713313,
      "aei_text": 3.234581,
      "aei_vision": 0.078875,
      "text_ratio": 0.974169,
      "vision_ratio": 0.025831
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974169,
      0.025831
    ],
    "text_vision_ratio": "0.974169:0.025831",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.365937,
      "aei_text": 3.252025,
      "aei_vision": 0.071684,
      "text_ratio": 0.978432,
      "vision_ratio": 0.021568
    },
    "middle": {
      "mdi": 33.02476,
      "aei_text": 3.191486,
      "aei_vision": 0.096639,
      "text_ratio": 0.97061,
      "vision_ratio": 0.02939
    },
    "late": {
      "mdi": 33.60422,
      "aei_text": 3.195257,
      "aei_vision": 0.095085,
      "text_ratio": 0.971102,
      "vision_ratio": 0.028898
    },
    "all": {
      "mdi": 33.60422,
      "aei_text": 3.212922,
      "aei_vision": 0.087803,
      "text_ratio": 0.971102,
      "vision_ratio": 0.028898
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971102,
      0.028898
    ],
    "text_vision_ratio": "0.971102:0.028898",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 176.0,
    "total_tokens": 523.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.04694,
      "aei_text": 2.82519,
      "aei_vision": 0.074255,
      "text_ratio": 0.97439,
      "vision_ratio": 0.02561
    },
    "middle": {
      "mdi": 46.749329,
      "aei_text": 2.851339,
      "aei_vision": 0.060992,
      "text_ratio": 0.979057,
      "vision_ratio": 0.020943
    },
    "late": {
      "mdi": 38.475545,
      "aei_text": 2.826741,
      "aei_vision": 0.073469,
      "text_ratio": 0.974668,
      "vision_ratio": 0.025332
    },
    "all": {
      "mdi": 38.475545,
      "aei_text": 2.834428,
      "aei_vision": 0.06957,
      "text_ratio": 0.974668,
      "vision_ratio": 0.025332
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974668,
      0.025332
    ],
    "text_vision_ratio": "0.974668:0.025332",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 176.0,
    "total_tokens": 523.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.799336,
      "aei_text": 2.820479,
      "aei_vision": 0.076645,
      "text_ratio": 0.973545,
      "vision_ratio": 0.026455
    },
    "middle": {
      "mdi": 35.733013,
      "aei_text": 2.816205,
      "aei_vision": 0.078812,
      "text_ratio": 0.972777,
      "vision_ratio": 0.027223
    },
    "late": {
      "mdi": 36.424652,
      "aei_text": 2.819004,
      "aei_vision": 0.077393,
      "text_ratio": 0.97328,
      "vision_ratio": 0.02672
    },
    "all": {
      "mdi": 36.424652,
      "aei_text": 2.818564,
      "aei_vision": 0.077616,
      "text_ratio": 0.97328,
      "vision_ratio": 0.02672
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97328,
      0.02672
    ],
    "text_vision_ratio": "0.973280:0.026720",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.81016,
      "aei_text": 2.965893,
      "aei_vision": 0.059544,
      "text_ratio": 0.980319,
      "vision_ratio": 0.019681
    },
    "middle": {
      "mdi": 36.493192,
      "aei_text": 2.922933,
      "aei_vision": 0.080095,
      "text_ratio": 0.973328,
      "vision_ratio": 0.026672
    },
    "late": {
      "mdi": 33.916685,
      "aei_text": 2.910953,
      "aei_vision": 0.085827,
      "text_ratio": 0.97136,
      "vision_ratio": 0.02864
    },
    "all": {
      "mdi": 33.916685,
      "aei_text": 2.933259,
      "aei_vision": 0.075155,
      "text_ratio": 0.97136,
      "vision_ratio": 0.02864
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97136,
      0.02864
    ],
    "text_vision_ratio": "0.971360:0.028640",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.325545,
      "aei_text": 2.97785,
      "aei_vision": 0.053824,
      "text_ratio": 0.982246,
      "vision_ratio": 0.017754
    },
    "middle": {
      "mdi": 37.828154,
      "aei_text": 2.928532,
      "aei_vision": 0.077417,
      "text_ratio": 0.974245,
      "vision_ratio": 0.025755
    },
    "late": {
      "mdi": 36.655515,
      "aei_text": 2.923635,
      "aei_vision": 0.07976,
      "text_ratio": 0.973443,
      "vision_ratio": 0.026557
    },
    "all": {
      "mdi": 36.655515,
      "aei_text": 2.943347,
      "aei_vision": 0.07033,
      "text_ratio": 0.973443,
      "vision_ratio": 0.026557
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973443,
      0.026557
    ],
    "text_vision_ratio": "0.973443:0.026557",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.749804,
      "aei_text": 3.307849,
      "aei_vision": 0.060418,
      "text_ratio": 0.982063,
      "vision_ratio": 0.017937
    },
    "middle": {
      "mdi": 42.314073,
      "aei_text": 3.266629,
      "aei_vision": 0.0772,
      "text_ratio": 0.976913,
      "vision_ratio": 0.023087
    },
    "late": {
      "mdi": 34.041717,
      "aei_text": 3.22365,
      "aei_vision": 0.094697,
      "text_ratio": 0.971463,
      "vision_ratio": 0.028537
    },
    "all": {
      "mdi": 34.041717,
      "aei_text": 3.266035,
      "aei_vision": 0.077441,
      "text_ratio": 0.971463,
      "vision_ratio": 0.028537
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971463,
      0.028537
    ],
    "text_vision_ratio": "0.971463:0.028537",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.053271,
      "aei_text": 3.297598,
      "aei_vision": 0.064591,
      "text_ratio": 0.980789,
      "vision_ratio": 0.019211
    },
    "middle": {
      "mdi": 40.717932,
      "aei_text": 3.259618,
      "aei_vision": 0.080054,
      "text_ratio": 0.976029,
      "vision_ratio": 0.023971
    },
    "late": {
      "mdi": 31.060914,
      "aei_text": 3.202964,
      "aei_vision": 0.103119,
      "text_ratio": 0.968809,
      "vision_ratio": 0.031191
    },
    "all": {
      "mdi": 31.060914,
      "aei_text": 3.253395,
      "aei_vision": 0.082587,
      "text_ratio": 0.968809,
      "vision_ratio": 0.031191
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968809,
      0.031191
    ],
    "text_vision_ratio": "0.968809:0.031191",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 508.0,
    "text_tokens": 163.0,
    "total_tokens": 671.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.260245,
      "aei_text": 3.282221,
      "aei_vision": 0.267713,
      "text_ratio": 0.924587,
      "vision_ratio": 0.075413
    },
    "middle": {
      "mdi": 13.943038,
      "aei_text": 3.364522,
      "aei_vision": 0.241305,
      "text_ratio": 0.933079,
      "vision_ratio": 0.066921
    },
    "late": {
      "mdi": 17.936814,
      "aei_text": 3.507183,
      "aei_vision": 0.19553,
      "text_ratio": 0.947193,
      "vision_ratio": 0.052807
    },
    "all": {
      "mdi": 17.936814,
      "aei_text": 3.384605,
      "aei_vision": 0.234861,
      "text_ratio": 0.947193,
      "vision_ratio": 0.052807
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947193,
      0.052807
    ],
    "text_vision_ratio": "0.947193:0.052807",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 508.0,
    "text_tokens": 163.0,
    "total_tokens": 671.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.866848,
      "aei_text": 3.199082,
      "aei_vision": 0.294389,
      "text_ratio": 0.915732,
      "vision_ratio": 0.084268
    },
    "middle": {
      "mdi": 5.595585,
      "aei_text": 2.643961,
      "aei_vision": 0.472508,
      "text_ratio": 0.848383,
      "vision_ratio": 0.151617
    },
    "late": {
      "mdi": 11.203837,
      "aei_text": 3.220672,
      "aei_vision": 0.287462,
      "text_ratio": 0.918059,
      "vision_ratio": 0.081941
    },
    "all": {
      "mdi": 11.203837,
      "aei_text": 3.021196,
      "aei_vision": 0.351467,
      "text_ratio": 0.918059,
      "vision_ratio": 0.081941
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.918059,
      0.081941
    ],
    "text_vision_ratio": "0.918059:0.081941",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 161.0,
    "total_tokens": 531.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.23824,
      "aei_text": 3.135263,
      "aei_vision": 0.070872,
      "text_ratio": 0.977895,
      "vision_ratio": 0.022105
    },
    "middle": {
      "mdi": 39.796539,
      "aei_text": 3.118077,
      "aei_vision": 0.07835,
      "text_ratio": 0.975488,
      "vision_ratio": 0.024512
    },
    "late": {
      "mdi": 32.759727,
      "aei_text": 3.081935,
      "aei_vision": 0.094077,
      "text_ratio": 0.970379,
      "vision_ratio": 0.029621
    },
    "all": {
      "mdi": 32.759727,
      "aei_text": 3.111763,
      "aei_vision": 0.081098,
      "text_ratio": 0.970379,
      "vision_ratio": 0.029621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970379,
      0.029621
    ],
    "text_vision_ratio": "0.970379:0.029621",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 161.0,
    "total_tokens": 531.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.141111,
      "aei_text": 3.13133,
      "aei_vision": 0.072583,
      "text_ratio": 0.977345,
      "vision_ratio": 0.022655
    },
    "middle": {
      "mdi": 35.378216,
      "aei_text": 3.096961,
      "aei_vision": 0.087539,
      "text_ratio": 0.972511,
      "vision_ratio": 0.027489
    },
    "late": {
      "mdi": 30.859434,
      "aei_text": 3.069544,
      "aei_vision": 0.099469,
      "text_ratio": 0.968612,
      "vision_ratio": 0.031388
    },
    "all": {
      "mdi": 30.859434,
      "aei_text": 3.099278,
      "aei_vision": 0.086531,
      "text_ratio": 0.968612,
      "vision_ratio": 0.031388
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968612,
      0.031388
    ],
    "text_vision_ratio": "0.968612:0.031388",
    "skip_reason": null
  }
}
```


## === Rollout Step 12 ===
Step: 11/43 | 2025-10-22 18:32:05

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 43.835 | 43.775 | 38.930 | 38.930 |
| MDI Std | 12.036 | 21.163 | 15.604 | 15.604 |
| Vision Tokens | 364.6 ± 87.6 |
| Text Tokens | 164.2 ± 4.1 |
| Total Tokens | 528.9 ± 87.9 |
| Vision Ratio | 0.681 |
| Text Ratio | 0.319 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 254.0,
    "text_tokens": 162.0,
    "total_tokens": 416.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.349017,
      "aei_text": 2.494587,
      "aei_vision": 0.04676,
      "text_ratio": 0.9816,
      "vision_ratio": 0.0184
    },
    "middle": {
      "mdi": 49.995908,
      "aei_text": 2.489819,
      "aei_vision": 0.0498,
      "text_ratio": 0.980391,
      "vision_ratio": 0.019609
    },
    "late": {
      "mdi": 36.49499,
      "aei_text": 2.462123,
      "aei_vision": 0.067465,
      "text_ratio": 0.97333,
      "vision_ratio": 0.02667
    },
    "all": {
      "mdi": 36.49499,
      "aei_text": 2.482174,
      "aei_vision": 0.054676,
      "text_ratio": 0.97333,
      "vision_ratio": 0.02667
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97333,
      0.02667
    ],
    "text_vision_ratio": "0.973330:0.026670",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 254.0,
    "text_tokens": 162.0,
    "total_tokens": 416.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.757612,
      "aei_text": 2.492399,
      "aei_vision": 0.048155,
      "text_ratio": 0.981045,
      "vision_ratio": 0.018955
    },
    "middle": {
      "mdi": 40.481921,
      "aei_text": 2.472153,
      "aei_vision": 0.061068,
      "text_ratio": 0.975893,
      "vision_ratio": 0.024107
    },
    "late": {
      "mdi": 29.78404,
      "aei_text": 2.439481,
      "aei_vision": 0.081906,
      "text_ratio": 0.967516,
      "vision_ratio": 0.032484
    },
    "all": {
      "mdi": 29.78404,
      "aei_text": 2.468016,
      "aei_vision": 0.063707,
      "text_ratio": 0.967516,
      "vision_ratio": 0.032484
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967516,
      0.032484
    ],
    "text_vision_ratio": "0.967516:0.032484",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 159.0,
    "total_tokens": 575.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.179744,
      "aei_text": 3.452645,
      "aei_vision": 0.062571,
      "text_ratio": 0.9822,
      "vision_ratio": 0.0178
    },
    "middle": {
      "mdi": 18.374094,
      "aei_text": 3.165592,
      "aei_vision": 0.172286,
      "text_ratio": 0.948385,
      "vision_ratio": 0.051615
    },
    "late": {
      "mdi": 21.031372,
      "aei_text": 3.216244,
      "aei_vision": 0.152926,
      "text_ratio": 0.95461,
      "vision_ratio": 0.04539
    },
    "all": {
      "mdi": 21.031372,
      "aei_text": 3.278212,
      "aei_vision": 0.129241,
      "text_ratio": 0.95461,
      "vision_ratio": 0.04539
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95461,
      0.04539
    ],
    "text_vision_ratio": "0.954610:0.045390",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 159.0,
    "total_tokens": 575.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.657726,
      "aei_text": 3.464417,
      "aei_vision": 0.058072,
      "text_ratio": 0.983514,
      "vision_ratio": 0.016486
    },
    "middle": {
      "mdi": 93.40598,
      "aei_text": 3.517816,
      "aei_vision": 0.037662,
      "text_ratio": 0.989407,
      "vision_ratio": 0.010593
    },
    "late": {
      "mdi": 65.957,
      "aei_text": 3.478374,
      "aei_vision": 0.052737,
      "text_ratio": 0.985065,
      "vision_ratio": 0.014935
    },
    "all": {
      "mdi": 65.957,
      "aei_text": 3.486865,
      "aei_vision": 0.049492,
      "text_ratio": 0.985065,
      "vision_ratio": 0.014935
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985065,
      0.014935
    ],
    "text_vision_ratio": "0.985065:0.014935",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.803369,
      "aei_text": 3.002998,
      "aei_vision": 0.05911,
      "text_ratio": 0.980696,
      "vision_ratio": 0.019304
    },
    "middle": {
      "mdi": 69.278905,
      "aei_text": 3.035556,
      "aei_vision": 0.043816,
      "text_ratio": 0.985771,
      "vision_ratio": 0.014229
    },
    "late": {
      "mdi": 63.508213,
      "aei_text": 3.027356,
      "aei_vision": 0.047669,
      "text_ratio": 0.984498,
      "vision_ratio": 0.015502
    },
    "all": {
      "mdi": 63.508213,
      "aei_text": 3.021965,
      "aei_vision": 0.050201,
      "text_ratio": 0.984498,
      "vision_ratio": 0.015502
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984498,
      0.015502
    ],
    "text_vision_ratio": "0.984498:0.015502",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 61.872719,
      "aei_text": 3.024762,
      "aei_vision": 0.048887,
      "text_ratio": 0.984095,
      "vision_ratio": 0.015905
    },
    "middle": {
      "mdi": 49.096536,
      "aei_text": 2.998806,
      "aei_vision": 0.06108,
      "text_ratio": 0.980039,
      "vision_ratio": 0.019961
    },
    "late": {
      "mdi": 40.478302,
      "aei_text": 2.972504,
      "aei_vision": 0.073435,
      "text_ratio": 0.975891,
      "vision_ratio": 0.024109
    },
    "all": {
      "mdi": 40.478302,
      "aei_text": 2.998693,
      "aei_vision": 0.061133,
      "text_ratio": 0.975891,
      "vision_ratio": 0.024109
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975891,
      0.024109
    ],
    "text_vision_ratio": "0.975891:0.024109",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.321817,
      "aei_text": 3.1514,
      "aei_vision": 0.063895,
      "text_ratio": 0.980128,
      "vision_ratio": 0.019872
    },
    "middle": {
      "mdi": 57.179185,
      "aei_text": 3.170799,
      "aei_vision": 0.055454,
      "text_ratio": 0.982812,
      "vision_ratio": 0.017188
    },
    "late": {
      "mdi": 58.799149,
      "aei_text": 3.174178,
      "aei_vision": 0.053983,
      "text_ratio": 0.983277,
      "vision_ratio": 0.016723
    },
    "all": {
      "mdi": 58.799149,
      "aei_text": 3.165462,
      "aei_vision": 0.057776,
      "text_ratio": 0.983277,
      "vision_ratio": 0.016723
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983277,
      0.016723
    ],
    "text_vision_ratio": "0.983277:0.016723",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.395628,
      "aei_text": 3.154392,
      "aei_vision": 0.062593,
      "text_ratio": 0.980543,
      "vision_ratio": 0.019457
    },
    "middle": {
      "mdi": 32.868828,
      "aei_text": 3.082698,
      "aei_vision": 0.093788,
      "text_ratio": 0.970474,
      "vision_ratio": 0.029526
    },
    "late": {
      "mdi": 35.648602,
      "aei_text": 3.098488,
      "aei_vision": 0.086918,
      "text_ratio": 0.972714,
      "vision_ratio": 0.027286
    },
    "all": {
      "mdi": 35.648602,
      "aei_text": 3.111864,
      "aei_vision": 0.081097,
      "text_ratio": 0.972714,
      "vision_ratio": 0.027286
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972714,
      0.027286
    ],
    "text_vision_ratio": "0.972714:0.027286",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.410739,
      "aei_text": 2.894398,
      "aei_vision": 0.077368,
      "text_ratio": 0.973966,
      "vision_ratio": 0.026034
    },
    "middle": {
      "mdi": 67.708984,
      "aei_text": 2.963391,
      "aei_vision": 0.043767,
      "text_ratio": 0.985446,
      "vision_ratio": 0.014554
    },
    "late": {
      "mdi": 51.720052,
      "aei_text": 2.93667,
      "aei_vision": 0.05678,
      "text_ratio": 0.981032,
      "vision_ratio": 0.018968
    },
    "all": {
      "mdi": 51.720052,
      "aei_text": 2.931493,
      "aei_vision": 0.059302,
      "text_ratio": 0.981032,
      "vision_ratio": 0.018968
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981032,
      0.018968
    ],
    "text_vision_ratio": "0.981032:0.018968",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.087861,
      "aei_text": 2.90449,
      "aei_vision": 0.072453,
      "text_ratio": 0.975662,
      "vision_ratio": 0.024338
    },
    "middle": {
      "mdi": 26.563833,
      "aei_text": 2.834186,
      "aei_vision": 0.106693,
      "text_ratio": 0.963721,
      "vision_ratio": 0.036279
    },
    "late": {
      "mdi": 37.669509,
      "aei_text": 2.895433,
      "aei_vision": 0.076864,
      "text_ratio": 0.97414,
      "vision_ratio": 0.02586
    },
    "all": {
      "mdi": 37.669509,
      "aei_text": 2.878019,
      "aei_vision": 0.085345,
      "text_ratio": 0.97414,
      "vision_ratio": 0.02586
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97414,
      0.02586
    ],
    "text_vision_ratio": "0.974140:0.025860",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.954182,
      "aei_text": 2.329209,
      "aei_vision": 0.07068,
      "text_ratio": 0.970549,
      "vision_ratio": 0.029451
    },
    "middle": {
      "mdi": 31.998912,
      "aei_text": 2.32632,
      "aei_vision": 0.0727,
      "text_ratio": 0.969696,
      "vision_ratio": 0.030304
    },
    "late": {
      "mdi": 19.410435,
      "aei_text": 2.263511,
      "aei_vision": 0.116613,
      "text_ratio": 0.951005,
      "vision_ratio": 0.048995
    },
    "all": {
      "mdi": 19.410435,
      "aei_text": 2.30634,
      "aei_vision": 0.086669,
      "text_ratio": 0.951005,
      "vision_ratio": 0.048995
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951005,
      0.048995
    ],
    "text_vision_ratio": "0.951005:0.048995",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.080856,
      "aei_text": 2.332416,
      "aei_vision": 0.068438,
      "text_ratio": 0.971494,
      "vision_ratio": 0.028506
    },
    "middle": {
      "mdi": 46.56194,
      "aei_text": 2.357873,
      "aei_vision": 0.050639,
      "text_ratio": 0.978975,
      "vision_ratio": 0.021025
    },
    "late": {
      "mdi": 52.845291,
      "aei_text": 2.366258,
      "aei_vision": 0.044777,
      "text_ratio": 0.981428,
      "vision_ratio": 0.018572
    },
    "all": {
      "mdi": 52.845291,
      "aei_text": 2.352178,
      "aei_vision": 0.054621,
      "text_ratio": 0.981428,
      "vision_ratio": 0.018572
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981428,
      0.018572
    ],
    "text_vision_ratio": "0.981428:0.018572",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.011145,
      "aei_text": 3.278793,
      "aei_vision": 0.078046,
      "text_ratio": 0.97675,
      "vision_ratio": 0.02325
    },
    "middle": {
      "mdi": 38.384804,
      "aei_text": 3.261671,
      "aei_vision": 0.084973,
      "text_ratio": 0.974609,
      "vision_ratio": 0.025391
    },
    "late": {
      "mdi": 35.298504,
      "aei_text": 3.244509,
      "aei_vision": 0.091916,
      "text_ratio": 0.972451,
      "vision_ratio": 0.027549
    },
    "all": {
      "mdi": 35.298504,
      "aei_text": 3.261661,
      "aei_vision": 0.084977,
      "text_ratio": 0.972451,
      "vision_ratio": 0.027549
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972451,
      0.027549
    ],
    "text_vision_ratio": "0.972451:0.027549",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.735948,
      "aei_text": 3.273099,
      "aei_vision": 0.080349,
      "text_ratio": 0.97604,
      "vision_ratio": 0.02396
    },
    "middle": {
      "mdi": 52.519935,
      "aei_text": 3.315656,
      "aei_vision": 0.063131,
      "text_ratio": 0.981315,
      "vision_ratio": 0.018685
    },
    "late": {
      "mdi": 40.459365,
      "aei_text": 3.27182,
      "aei_vision": 0.080867,
      "text_ratio": 0.97588,
      "vision_ratio": 0.02412
    },
    "all": {
      "mdi": 40.459365,
      "aei_text": 3.286858,
      "aei_vision": 0.074782,
      "text_ratio": 0.97588,
      "vision_ratio": 0.02412
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97588,
      0.02412
    ],
    "text_vision_ratio": "0.975880:0.024120",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 166.0,
    "total_tokens": 697.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 21.778336,
      "aei_text": 3.66106,
      "aei_vision": 0.168106,
      "text_ratio": 0.956099,
      "vision_ratio": 0.043901
    },
    "middle": {
      "mdi": 15.599983,
      "aei_text": 3.484329,
      "aei_vision": 0.223355,
      "text_ratio": 0.939759,
      "vision_ratio": 0.060241
    },
    "late": {
      "mdi": 19.742527,
      "aei_text": 3.613341,
      "aei_vision": 0.183023,
      "text_ratio": 0.95179,
      "vision_ratio": 0.04821
    },
    "all": {
      "mdi": 19.742527,
      "aei_text": 3.586252,
      "aei_vision": 0.191492,
      "text_ratio": 0.95179,
      "vision_ratio": 0.04821
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95179,
      0.04821
    ],
    "text_vision_ratio": "0.951790:0.048210",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 166.0,
    "total_tokens": 697.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 19.955786,
      "aei_text": 3.618733,
      "aei_vision": 0.181338,
      "text_ratio": 0.95228,
      "vision_ratio": 0.04772
    },
    "middle": {
      "mdi": 10.37639,
      "aei_text": 3.20941,
      "aei_vision": 0.309299,
      "text_ratio": 0.912099,
      "vision_ratio": 0.087901
    },
    "late": {
      "mdi": 14.034151,
      "aei_text": 3.419411,
      "aei_vision": 0.243649,
      "text_ratio": 0.933485,
      "vision_ratio": 0.066515
    },
    "all": {
      "mdi": 14.034151,
      "aei_text": 3.415822,
      "aei_vision": 0.244771,
      "text_ratio": 0.933485,
      "vision_ratio": 0.066515
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.933485,
      0.066515
    ],
    "text_vision_ratio": "0.933485:0.066515",
    "skip_reason": null
  }
}
```


## === Rollout Step 13 ===
Step: 12/43 | 2025-10-22 18:33:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 40.079 | 43.354 | 38.577 | 38.577 |
| MDI Std | 13.663 | 21.316 | 18.492 | 18.492 |
| Vision Tokens | 357.2 ± 79.3 |
| Text Tokens | 167.9 ± 9.8 |
| Total Tokens | 525.1 ± 75.3 |
| Vision Ratio | 0.672 |
| Text Ratio | 0.328 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.347375,
      "aei_text": 3.315165,
      "aei_vision": 0.06333,
      "text_ratio": 0.981255,
      "vision_ratio": 0.018745
    },
    "middle": {
      "mdi": 64.407576,
      "aei_text": 3.343392,
      "aei_vision": 0.05191,
      "text_ratio": 0.984711,
      "vision_ratio": 0.015289
    },
    "late": {
      "mdi": 37.433464,
      "aei_text": 3.256664,
      "aei_vision": 0.086999,
      "text_ratio": 0.973981,
      "vision_ratio": 0.026019
    },
    "all": {
      "mdi": 37.433464,
      "aei_text": 3.305082,
      "aei_vision": 0.067409,
      "text_ratio": 0.973981,
      "vision_ratio": 0.026019
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973981,
      0.026019
    ],
    "text_vision_ratio": "0.973981:0.026019",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.507856,
      "aei_text": 3.315622,
      "aei_vision": 0.063145,
      "text_ratio": 0.981311,
      "vision_ratio": 0.018689
    },
    "middle": {
      "mdi": 20.241028,
      "aei_text": 3.093893,
      "aei_vision": 0.152853,
      "text_ratio": 0.952921,
      "vision_ratio": 0.047079
    },
    "late": {
      "mdi": 30.213055,
      "aei_text": 3.20916,
      "aei_vision": 0.106218,
      "text_ratio": 0.967962,
      "vision_ratio": 0.032038
    },
    "all": {
      "mdi": 30.213055,
      "aei_text": 3.206193,
      "aei_vision": 0.107418,
      "text_ratio": 0.967962,
      "vision_ratio": 0.032038
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967962,
      0.032038
    ],
    "text_vision_ratio": "0.967962:0.032038",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.709423,
      "aei_text": 3.233252,
      "aei_vision": 0.079423,
      "text_ratio": 0.976025,
      "vision_ratio": 0.023975
    },
    "middle": {
      "mdi": 27.326019,
      "aei_text": 3.146581,
      "aei_vision": 0.11515,
      "text_ratio": 0.964697,
      "vision_ratio": 0.035303
    },
    "late": {
      "mdi": 28.393717,
      "aei_text": 3.156259,
      "aei_vision": 0.11116,
      "text_ratio": 0.965979,
      "vision_ratio": 0.034021
    },
    "all": {
      "mdi": 28.393717,
      "aei_text": 3.178714,
      "aei_vision": 0.101904,
      "text_ratio": 0.965979,
      "vision_ratio": 0.034021
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965979,
      0.034021
    ],
    "text_vision_ratio": "0.965979:0.034021",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.976303,
      "aei_text": 3.214998,
      "aei_vision": 0.086948,
      "text_ratio": 0.973668,
      "vision_ratio": 0.026332
    },
    "middle": {
      "mdi": 48.920745,
      "aei_text": 3.264065,
      "aei_vision": 0.066721,
      "text_ratio": 0.979968,
      "vision_ratio": 0.020032
    },
    "late": {
      "mdi": 41.745052,
      "aei_text": 3.23777,
      "aei_vision": 0.077561,
      "text_ratio": 0.976605,
      "vision_ratio": 0.023395
    },
    "all": {
      "mdi": 41.745052,
      "aei_text": 3.238956,
      "aei_vision": 0.077072,
      "text_ratio": 0.976605,
      "vision_ratio": 0.023395
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976605,
      0.023395
    ],
    "text_vision_ratio": "0.976605:0.023395",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 168.0,
    "total_tokens": 386.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.565611,
      "aei_text": 2.206897,
      "aei_vision": 0.069915,
      "text_ratio": 0.969293,
      "vision_ratio": 0.030707
    },
    "middle": {
      "mdi": 38.77038,
      "aei_text": 2.22321,
      "aei_vision": 0.057343,
      "text_ratio": 0.974856,
      "vision_ratio": 0.025144
    },
    "late": {
      "mdi": 34.747416,
      "aei_text": 2.214905,
      "aei_vision": 0.063743,
      "text_ratio": 0.972026,
      "vision_ratio": 0.027974
    },
    "all": {
      "mdi": 34.747416,
      "aei_text": 2.215006,
      "aei_vision": 0.063665,
      "text_ratio": 0.972026,
      "vision_ratio": 0.027974
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972026,
      0.027974
    ],
    "text_vision_ratio": "0.972026:0.027974",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 168.0,
    "total_tokens": 386.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.136229,
      "aei_text": 2.205696,
      "aei_vision": 0.07084,
      "text_ratio": 0.968882,
      "vision_ratio": 0.031118
    },
    "middle": {
      "mdi": 19.591595,
      "aei_text": 2.154893,
      "aei_vision": 0.109991,
      "text_ratio": 0.951436,
      "vision_ratio": 0.048564
    },
    "late": {
      "mdi": 18.150784,
      "aei_text": 2.144319,
      "aei_vision": 0.118139,
      "text_ratio": 0.947783,
      "vision_ratio": 0.052217
    },
    "all": {
      "mdi": 18.150784,
      "aei_text": 2.168291,
      "aei_vision": 0.099666,
      "text_ratio": 0.947783,
      "vision_ratio": 0.052217
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947783,
      0.052217
    ],
    "text_vision_ratio": "0.947783:0.052217",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 190.0,
    "total_tokens": 426.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.939362,
      "aei_text": 2.165134,
      "aei_vision": 0.061968,
      "text_ratio": 0.972175,
      "vision_ratio": 0.027825
    },
    "middle": {
      "mdi": 48.805387,
      "aei_text": 2.18646,
      "aei_vision": 0.0448,
      "text_ratio": 0.979922,
      "vision_ratio": 0.020078
    },
    "late": {
      "mdi": 47.99925,
      "aei_text": 2.185549,
      "aei_vision": 0.045533,
      "text_ratio": 0.979592,
      "vision_ratio": 0.020408
    },
    "all": {
      "mdi": 47.99925,
      "aei_text": 2.179051,
      "aei_vision": 0.050764,
      "text_ratio": 0.979592,
      "vision_ratio": 0.020408
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979592,
      0.020408
    ],
    "text_vision_ratio": "0.979592:0.020408",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 190.0,
    "total_tokens": 426.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.929048,
      "aei_text": 2.174462,
      "aei_vision": 0.054458,
      "text_ratio": 0.975567,
      "vision_ratio": 0.024433
    },
    "middle": {
      "mdi": 50.911402,
      "aei_text": 2.188707,
      "aei_vision": 0.04299,
      "text_ratio": 0.980736,
      "vision_ratio": 0.019264
    },
    "late": {
      "mdi": 45.661973,
      "aei_text": 2.18273,
      "aei_vision": 0.047802,
      "text_ratio": 0.978569,
      "vision_ratio": 0.021431
    },
    "all": {
      "mdi": 45.661973,
      "aei_text": 2.181967,
      "aei_vision": 0.048416,
      "text_ratio": 0.978569,
      "vision_ratio": 0.021431
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978569,
      0.021431
    ],
    "text_vision_ratio": "0.978569:0.021431",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.673685,
      "aei_text": 3.282856,
      "aei_vision": 0.064784,
      "text_ratio": 0.980648,
      "vision_ratio": 0.019352
    },
    "middle": {
      "mdi": 46.687144,
      "aei_text": 3.270024,
      "aei_vision": 0.070041,
      "text_ratio": 0.97903,
      "vision_ratio": 0.02097
    },
    "late": {
      "mdi": 38.044638,
      "aei_text": 3.233526,
      "aei_vision": 0.084993,
      "text_ratio": 0.974388,
      "vision_ratio": 0.025612
    },
    "all": {
      "mdi": 38.044638,
      "aei_text": 3.262122,
      "aei_vision": 0.073278,
      "text_ratio": 0.974388,
      "vision_ratio": 0.025612
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974388,
      0.025612
    ],
    "text_vision_ratio": "0.974388:0.025612",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.94254,
      "aei_text": 3.267392,
      "aei_vision": 0.071119,
      "text_ratio": 0.978697,
      "vision_ratio": 0.021303
    },
    "middle": {
      "mdi": 57.389458,
      "aei_text": 3.300606,
      "aei_vision": 0.057512,
      "text_ratio": 0.982874,
      "vision_ratio": 0.017126
    },
    "late": {
      "mdi": 47.769633,
      "aei_text": 3.27371,
      "aei_vision": 0.068531,
      "text_ratio": 0.979495,
      "vision_ratio": 0.020505
    },
    "all": {
      "mdi": 47.769633,
      "aei_text": 3.280572,
      "aei_vision": 0.06572,
      "text_ratio": 0.979495,
      "vision_ratio": 0.020505
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979495,
      0.020505
    ],
    "text_vision_ratio": "0.979495:0.020505",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 176.0,
    "total_tokens": 638.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.625167,
      "aei_text": 2.848225,
      "aei_vision": 0.295914,
      "text_ratio": 0.905884,
      "vision_ratio": 0.094116
    },
    "middle": {
      "mdi": 7.148936,
      "aei_text": 2.651429,
      "aei_vision": 0.370884,
      "text_ratio": 0.877285,
      "vision_ratio": 0.122715
    },
    "late": {
      "mdi": 10.034849,
      "aei_text": 2.873362,
      "aei_vision": 0.286338,
      "text_ratio": 0.909378,
      "vision_ratio": 0.090622
    },
    "all": {
      "mdi": 10.034849,
      "aei_text": 2.790982,
      "aei_vision": 0.317721,
      "text_ratio": 0.909378,
      "vision_ratio": 0.090622
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.909378,
      0.090622
    ],
    "text_vision_ratio": "0.909378:0.090622",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 176.0,
    "total_tokens": 638.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.262081,
      "aei_text": 2.886615,
      "aei_vision": 0.281289,
      "text_ratio": 0.911206,
      "vision_ratio": 0.088794
    },
    "middle": {
      "mdi": 8.597242,
      "aei_text": 2.777074,
      "aei_vision": 0.323019,
      "text_ratio": 0.895803,
      "vision_ratio": 0.104197
    },
    "late": {
      "mdi": 12.202768,
      "aei_text": 2.983256,
      "aei_vision": 0.244474,
      "text_ratio": 0.924258,
      "vision_ratio": 0.075742
    },
    "all": {
      "mdi": 12.202768,
      "aei_text": 2.882314,
      "aei_vision": 0.282928,
      "text_ratio": 0.924258,
      "vision_ratio": 0.075742
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.924258,
      0.075742
    ],
    "text_vision_ratio": "0.924258:0.075742",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.327414,
      "aei_text": 3.281818,
      "aei_vision": 0.065209,
      "text_ratio": 0.980517,
      "vision_ratio": 0.019483
    },
    "middle": {
      "mdi": 88.746461,
      "aei_text": 3.348882,
      "aei_vision": 0.037735,
      "text_ratio": 0.988857,
      "vision_ratio": 0.011143
    },
    "late": {
      "mdi": 90.772403,
      "aei_text": 3.350884,
      "aei_vision": 0.036915,
      "text_ratio": 0.989103,
      "vision_ratio": 0.010897
    },
    "all": {
      "mdi": 90.772403,
      "aei_text": 3.327182,
      "aei_vision": 0.046625,
      "text_ratio": 0.989103,
      "vision_ratio": 0.010897
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989103,
      0.010897
    ],
    "text_vision_ratio": "0.989103:0.010897",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.160814,
      "aei_text": 3.297663,
      "aei_vision": 0.058718,
      "text_ratio": 0.982505,
      "vision_ratio": 0.017495
    },
    "middle": {
      "mdi": 59.830749,
      "aei_text": 3.30611,
      "aei_vision": 0.055258,
      "text_ratio": 0.983561,
      "vision_ratio": 0.016439
    },
    "late": {
      "mdi": 35.360421,
      "aei_text": 3.218795,
      "aei_vision": 0.091028,
      "text_ratio": 0.972498,
      "vision_ratio": 0.027502
    },
    "all": {
      "mdi": 35.360421,
      "aei_text": 3.274193,
      "aei_vision": 0.068333,
      "text_ratio": 0.972498,
      "vision_ratio": 0.027502
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972498,
      0.027502
    ],
    "text_vision_ratio": "0.972498:0.027502",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.626238,
      "aei_text": 3.084558,
      "aei_vision": 0.064766,
      "text_ratio": 0.979435,
      "vision_ratio": 0.020565
    },
    "middle": {
      "mdi": 46.76072,
      "aei_text": 3.082007,
      "aei_vision": 0.06591,
      "text_ratio": 0.979062,
      "vision_ratio": 0.020938
    },
    "late": {
      "mdi": 40.593454,
      "aei_text": 3.06085,
      "aei_vision": 0.075403,
      "text_ratio": 0.975958,
      "vision_ratio": 0.024042
    },
    "all": {
      "mdi": 40.593454,
      "aei_text": 3.075803,
      "aei_vision": 0.068694,
      "text_ratio": 0.975958,
      "vision_ratio": 0.024042
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975958,
      0.024042
    ],
    "text_vision_ratio": "0.975958:0.024042",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.527837,
      "aei_text": 3.092497,
      "aei_vision": 0.061204,
      "text_ratio": 0.980593,
      "vision_ratio": 0.019407
    },
    "middle": {
      "mdi": 59.53199,
      "aei_text": 3.112386,
      "aei_vision": 0.052281,
      "text_ratio": 0.98348,
      "vision_ratio": 0.01652
    },
    "late": {
      "mdi": 58.116912,
      "aei_text": 3.109653,
      "aei_vision": 0.053507,
      "text_ratio": 0.983084,
      "vision_ratio": 0.016916
    },
    "all": {
      "mdi": 58.116912,
      "aei_text": 3.104846,
      "aei_vision": 0.055664,
      "text_ratio": 0.983084,
      "vision_ratio": 0.016916
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983084,
      0.016916
    ],
    "text_vision_ratio": "0.983084:0.016916",
    "skip_reason": null
  }
}
```


## === Rollout Step 14 ===
Step: 13/43 | 2025-10-22 18:34:38

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.758 | 33.866 | 34.258 | 34.258 |
| MDI Std | 11.776 | 14.835 | 13.151 | 13.151 |
| Vision Tokens | 372.9 ± 40.6 |
| Text Tokens | 163.5 ± 2.8 |
| Total Tokens | 536.4 ± 39.8 |
| Vision Ratio | 0.694 |
| Text Ratio | 0.306 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.769736,
      "aei_text": 2.92485,
      "aei_vision": 0.062537,
      "text_ratio": 0.979066,
      "vision_ratio": 0.020934
    },
    "middle": {
      "mdi": 32.362749,
      "aei_text": 2.871098,
      "aei_vision": 0.088716,
      "text_ratio": 0.970026,
      "vision_ratio": 0.029974
    },
    "late": {
      "mdi": 28.852864,
      "aei_text": 2.850411,
      "aei_vision": 0.098791,
      "text_ratio": 0.966502,
      "vision_ratio": 0.033498
    },
    "all": {
      "mdi": 28.852864,
      "aei_text": 2.882122,
      "aei_vision": 0.083347,
      "text_ratio": 0.966502,
      "vision_ratio": 0.033498
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966502,
      0.033498
    ],
    "text_vision_ratio": "0.966502:0.033498",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.182074,
      "aei_text": 2.914666,
      "aei_vision": 0.067497,
      "text_ratio": 0.977366,
      "vision_ratio": 0.022634
    },
    "middle": {
      "mdi": 13.704242,
      "aei_text": 2.655405,
      "aei_vision": 0.193765,
      "text_ratio": 0.931992,
      "vision_ratio": 0.068008
    },
    "late": {
      "mdi": 25.023831,
      "aei_text": 2.821726,
      "aei_vision": 0.112762,
      "text_ratio": 0.961574,
      "vision_ratio": 0.038426
    },
    "all": {
      "mdi": 25.023831,
      "aei_text": 2.797286,
      "aei_vision": 0.124665,
      "text_ratio": 0.961574,
      "vision_ratio": 0.038426
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961574,
      0.038426
    ],
    "text_vision_ratio": "0.961574:0.038426",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.881733,
      "aei_text": 3.277334,
      "aei_vision": 0.067046,
      "text_ratio": 0.979953,
      "vision_ratio": 0.020047
    },
    "middle": {
      "mdi": 36.827987,
      "aei_text": 3.227099,
      "aei_vision": 0.087626,
      "text_ratio": 0.973565,
      "vision_ratio": 0.026435
    },
    "late": {
      "mdi": 28.880986,
      "aei_text": 3.172829,
      "aei_vision": 0.109859,
      "text_ratio": 0.966534,
      "vision_ratio": 0.033466
    },
    "all": {
      "mdi": 28.880986,
      "aei_text": 3.225761,
      "aei_vision": 0.088174,
      "text_ratio": 0.966534,
      "vision_ratio": 0.033466
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966534,
      0.033466
    ],
    "text_vision_ratio": "0.966534:0.033466",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.270116,
      "aei_text": 3.248836,
      "aei_vision": 0.078721,
      "text_ratio": 0.976343,
      "vision_ratio": 0.023657
    },
    "middle": {
      "mdi": 53.147299,
      "aei_text": 3.289893,
      "aei_vision": 0.061901,
      "text_ratio": 0.981532,
      "vision_ratio": 0.018468
    },
    "late": {
      "mdi": 41.098737,
      "aei_text": 3.248079,
      "aei_vision": 0.079031,
      "text_ratio": 0.976246,
      "vision_ratio": 0.023754
    },
    "all": {
      "mdi": 41.098737,
      "aei_text": 3.262264,
      "aei_vision": 0.07322,
      "text_ratio": 0.976246,
      "vision_ratio": 0.023754
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976246,
      0.023754
    ],
    "text_vision_ratio": "0.976246:0.023754",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.563842,
      "aei_text": 3.04319,
      "aei_vision": 0.057895,
      "text_ratio": 0.981331,
      "vision_ratio": 0.018669
    },
    "middle": {
      "mdi": 25.662642,
      "aei_text": 2.921826,
      "aei_vision": 0.113855,
      "text_ratio": 0.962494,
      "vision_ratio": 0.037506
    },
    "late": {
      "mdi": 24.339336,
      "aei_text": 2.9095,
      "aei_vision": 0.119539,
      "text_ratio": 0.960536,
      "vision_ratio": 0.039464
    },
    "all": {
      "mdi": 24.339336,
      "aei_text": 2.95817,
      "aei_vision": 0.097098,
      "text_ratio": 0.960536,
      "vision_ratio": 0.039464
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960536,
      0.039464
    ],
    "text_vision_ratio": "0.960536:0.039464",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.066988,
      "aei_text": 3.03462,
      "aei_vision": 0.061846,
      "text_ratio": 0.980027,
      "vision_ratio": 0.019973
    },
    "middle": {
      "mdi": 25.273869,
      "aei_text": 2.918328,
      "aei_vision": 0.115468,
      "text_ratio": 0.961939,
      "vision_ratio": 0.038061
    },
    "late": {
      "mdi": 28.749985,
      "aei_text": 2.946483,
      "aei_vision": 0.102486,
      "text_ratio": 0.966387,
      "vision_ratio": 0.033613
    },
    "all": {
      "mdi": 28.749985,
      "aei_text": 2.966488,
      "aei_vision": 0.093262,
      "text_ratio": 0.966387,
      "vision_ratio": 0.033613
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966387,
      0.033613
    ],
    "text_vision_ratio": "0.966387:0.033613",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 163.0,
    "total_tokens": 487.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.2917,
      "aei_text": 2.832587,
      "aei_vision": 0.078051,
      "text_ratio": 0.973184,
      "vision_ratio": 0.026816
    },
    "middle": {
      "mdi": 27.844069,
      "aei_text": 2.788654,
      "aei_vision": 0.100153,
      "text_ratio": 0.965331,
      "vision_ratio": 0.034669
    },
    "late": {
      "mdi": 24.427851,
      "aei_text": 2.762908,
      "aei_vision": 0.113105,
      "text_ratio": 0.960673,
      "vision_ratio": 0.039327
    },
    "all": {
      "mdi": 24.427851,
      "aei_text": 2.794724,
      "aei_vision": 0.097099,
      "text_ratio": 0.960673,
      "vision_ratio": 0.039327
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960673,
      0.039327
    ],
    "text_vision_ratio": "0.960673:0.039327",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 163.0,
    "total_tokens": 487.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.564786,
      "aei_text": 2.833686,
      "aei_vision": 0.077498,
      "text_ratio": 0.973379,
      "vision_ratio": 0.026621
    },
    "middle": {
      "mdi": 38.503374,
      "aei_text": 2.841061,
      "aei_vision": 0.073787,
      "text_ratio": 0.974686,
      "vision_ratio": 0.025314
    },
    "late": {
      "mdi": 32.687117,
      "aei_text": 2.816459,
      "aei_vision": 0.086164,
      "text_ratio": 0.970315,
      "vision_ratio": 0.029685
    },
    "all": {
      "mdi": 32.687117,
      "aei_text": 2.830398,
      "aei_vision": 0.079152,
      "text_ratio": 0.970315,
      "vision_ratio": 0.029685
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970315,
      0.029685
    ],
    "text_vision_ratio": "0.970315:0.029685",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.00997,
      "aei_text": 3.230955,
      "aei_vision": 0.06334,
      "text_ratio": 0.980773,
      "vision_ratio": 0.019227
    },
    "middle": {
      "mdi": 30.716565,
      "aei_text": 3.138457,
      "aei_vision": 0.102175,
      "text_ratio": 0.968471,
      "vision_ratio": 0.031529
    },
    "late": {
      "mdi": 48.933917,
      "aei_text": 3.224851,
      "aei_vision": 0.065902,
      "text_ratio": 0.979974,
      "vision_ratio": 0.020026
    },
    "all": {
      "mdi": 48.933917,
      "aei_text": 3.198081,
      "aei_vision": 0.077142,
      "text_ratio": 0.979974,
      "vision_ratio": 0.020026
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979974,
      0.020026
    ],
    "text_vision_ratio": "0.979974:0.020026",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.74981,
      "aei_text": 3.233017,
      "aei_vision": 0.062474,
      "text_ratio": 0.981043,
      "vision_ratio": 0.018957
    },
    "middle": {
      "mdi": 38.6315,
      "aei_text": 3.185422,
      "aei_vision": 0.082457,
      "text_ratio": 0.974768,
      "vision_ratio": 0.025232
    },
    "late": {
      "mdi": 34.16389,
      "aei_text": 3.161413,
      "aei_vision": 0.092537,
      "text_ratio": 0.971562,
      "vision_ratio": 0.028438
    },
    "all": {
      "mdi": 34.16389,
      "aei_text": 3.193275,
      "aei_vision": 0.079159,
      "text_ratio": 0.971562,
      "vision_ratio": 0.028438
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971562,
      0.028438
    ],
    "text_vision_ratio": "0.971562:0.028438",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 161.0,
    "total_tokens": 623.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.423118,
      "aei_text": 3.143468,
      "aei_vision": 0.253034,
      "text_ratio": 0.925502,
      "vision_ratio": 0.074498
    },
    "middle": {
      "mdi": 8.462346,
      "aei_text": 2.88968,
      "aei_vision": 0.341475,
      "text_ratio": 0.894318,
      "vision_ratio": 0.105682
    },
    "late": {
      "mdi": 18.485288,
      "aei_text": 3.349591,
      "aei_vision": 0.181203,
      "text_ratio": 0.948679,
      "vision_ratio": 0.051321
    },
    "all": {
      "mdi": 18.485288,
      "aei_text": 3.127594,
      "aei_vision": 0.258566,
      "text_ratio": 0.948679,
      "vision_ratio": 0.051321
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948679,
      0.051321
    ],
    "text_vision_ratio": "0.948679:0.051321",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 161.0,
    "total_tokens": 623.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.028986,
      "aei_text": 3.212469,
      "aei_vision": 0.228988,
      "text_ratio": 0.933462,
      "vision_ratio": 0.066538
    },
    "middle": {
      "mdi": 11.16841,
      "aei_text": 3.07857,
      "aei_vision": 0.27565,
      "text_ratio": 0.91782,
      "vision_ratio": 0.08218
    },
    "late": {
      "mdi": 15.157134,
      "aei_text": 3.253592,
      "aei_vision": 0.214657,
      "text_ratio": 0.938108,
      "vision_ratio": 0.061892
    },
    "all": {
      "mdi": 15.157134,
      "aei_text": 3.181578,
      "aei_vision": 0.239753,
      "text_ratio": 0.938108,
      "vision_ratio": 0.061892
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.938108,
      0.061892
    ],
    "text_vision_ratio": "0.938108:0.061892",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.26413,
      "aei_text": 3.001703,
      "aei_vision": 0.059719,
      "text_ratio": 0.980493,
      "vision_ratio": 0.019507
    },
    "middle": {
      "mdi": 45.368601,
      "aei_text": 2.9886,
      "aei_vision": 0.065874,
      "text_ratio": 0.978434,
      "vision_ratio": 0.021566
    },
    "late": {
      "mdi": 46.866368,
      "aei_text": 2.992887,
      "aei_vision": 0.06386,
      "text_ratio": 0.979109,
      "vision_ratio": 0.020891
    },
    "all": {
      "mdi": 46.866368,
      "aei_text": 2.994396,
      "aei_vision": 0.063151,
      "text_ratio": 0.979109,
      "vision_ratio": 0.020891
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979109,
      0.020891
    ],
    "text_vision_ratio": "0.979109:0.020891",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.786284,
      "aei_text": 2.986859,
      "aei_vision": 0.066691,
      "text_ratio": 0.978159,
      "vision_ratio": 0.021841
    },
    "middle": {
      "mdi": 63.00685,
      "aei_text": 3.026574,
      "aei_vision": 0.048036,
      "text_ratio": 0.984377,
      "vision_ratio": 0.015623
    },
    "late": {
      "mdi": 68.934512,
      "aei_text": 3.035104,
      "aei_vision": 0.044029,
      "text_ratio": 0.985701,
      "vision_ratio": 0.014299
    },
    "all": {
      "mdi": 68.934512,
      "aei_text": 3.016193,
      "aei_vision": 0.052912,
      "text_ratio": 0.985701,
      "vision_ratio": 0.014299
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985701,
      0.014299
    ],
    "text_vision_ratio": "0.985701:0.014299",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.988973,
      "aei_text": 3.073197,
      "aei_vision": 0.069863,
      "text_ratio": 0.977772,
      "vision_ratio": 0.022228
    },
    "middle": {
      "mdi": 52.0633,
      "aei_text": 3.096356,
      "aei_vision": 0.059473,
      "text_ratio": 0.981155,
      "vision_ratio": 0.018845
    },
    "late": {
      "mdi": 46.854866,
      "aei_text": 3.082289,
      "aei_vision": 0.065784,
      "text_ratio": 0.979103,
      "vision_ratio": 0.020897
    },
    "all": {
      "mdi": 46.854866,
      "aei_text": 3.083949,
      "aei_vision": 0.065039,
      "text_ratio": 0.979103,
      "vision_ratio": 0.020897
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979103,
      0.020897
    ],
    "text_vision_ratio": "0.979103:0.020897",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.27876,
      "aei_text": 3.077425,
      "aei_vision": 0.067966,
      "text_ratio": 0.978392,
      "vision_ratio": 0.021608
    },
    "middle": {
      "mdi": 39.106034,
      "aei_text": 3.054802,
      "aei_vision": 0.078116,
      "text_ratio": 0.975066,
      "vision_ratio": 0.024934
    },
    "late": {
      "mdi": 34.679228,
      "aei_text": 3.033919,
      "aei_vision": 0.087485,
      "text_ratio": 0.971972,
      "vision_ratio": 0.028028
    },
    "all": {
      "mdi": 34.679228,
      "aei_text": 3.055386,
      "aei_vision": 0.077854,
      "text_ratio": 0.971972,
      "vision_ratio": 0.028028
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971972,
      0.028028
    ],
    "text_vision_ratio": "0.971972:0.028028",
    "skip_reason": null
  }
}
```


## === Rollout Step 15 ===
Step: 14/43 | 2025-10-22 18:35:57

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 43.231 | 40.800 | 37.829 | 37.829 |
| MDI Std | 15.314 | 17.559 | 13.686 | 13.686 |
| Vision Tokens | 359.6 ± 56.9 |
| Text Tokens | 166.1 ± 4.2 |
| Total Tokens | 525.8 ± 58.8 |
| Vision Ratio | 0.679 |
| Text Ratio | 0.321 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 65.078466,
      "aei_text": 3.316593,
      "aei_vision": 0.050963,
      "text_ratio": 0.984866,
      "vision_ratio": 0.015134
    },
    "middle": {
      "mdi": 46.661692,
      "aei_text": 3.269935,
      "aei_vision": 0.070078,
      "text_ratio": 0.979019,
      "vision_ratio": 0.020981
    },
    "late": {
      "mdi": 41.995436,
      "aei_text": 3.251972,
      "aei_vision": 0.077436,
      "text_ratio": 0.976742,
      "vision_ratio": 0.023258
    },
    "all": {
      "mdi": 41.995436,
      "aei_text": 3.279503,
      "aei_vision": 0.066158,
      "text_ratio": 0.976742,
      "vision_ratio": 0.023258
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976742,
      0.023258
    ],
    "text_vision_ratio": "0.976742:0.023258",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 68.303057,
      "aei_text": 3.322264,
      "aei_vision": 0.04864,
      "text_ratio": 0.985571,
      "vision_ratio": 0.014429
    },
    "middle": {
      "mdi": 37.110538,
      "aei_text": 3.228627,
      "aei_vision": 0.087,
      "text_ratio": 0.973761,
      "vision_ratio": 0.026239
    },
    "late": {
      "mdi": 34.930621,
      "aei_text": 3.216239,
      "aei_vision": 0.092075,
      "text_ratio": 0.972169,
      "vision_ratio": 0.027831
    },
    "all": {
      "mdi": 34.930621,
      "aei_text": 3.255714,
      "aei_vision": 0.075904,
      "text_ratio": 0.972169,
      "vision_ratio": 0.027831
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972169,
      0.027831
    ],
    "text_vision_ratio": "0.972169:0.027831",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.454033,
      "aei_text": 2.89409,
      "aei_vision": 0.066601,
      "text_ratio": 0.977505,
      "vision_ratio": 0.022495
    },
    "middle": {
      "mdi": 48.567487,
      "aei_text": 2.907749,
      "aei_vision": 0.05987,
      "text_ratio": 0.979825,
      "vision_ratio": 0.020175
    },
    "late": {
      "mdi": 41.171138,
      "aei_text": 2.886948,
      "aei_vision": 0.070121,
      "text_ratio": 0.976287,
      "vision_ratio": 0.023713
    },
    "all": {
      "mdi": 41.171138,
      "aei_text": 2.896267,
      "aei_vision": 0.065528,
      "text_ratio": 0.976287,
      "vision_ratio": 0.023713
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976287,
      0.023713
    ],
    "text_vision_ratio": "0.976287:0.023713",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.82111,
      "aei_text": 2.885786,
      "aei_vision": 0.070693,
      "text_ratio": 0.976089,
      "vision_ratio": 0.023911
    },
    "middle": {
      "mdi": 39.233936,
      "aei_text": 2.880268,
      "aei_vision": 0.073413,
      "text_ratio": 0.975145,
      "vision_ratio": 0.024855
    },
    "late": {
      "mdi": 32.71187,
      "aei_text": 2.852301,
      "aei_vision": 0.087195,
      "text_ratio": 0.970337,
      "vision_ratio": 0.029663
    },
    "all": {
      "mdi": 32.71187,
      "aei_text": 2.872782,
      "aei_vision": 0.077102,
      "text_ratio": 0.970337,
      "vision_ratio": 0.029663
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970337,
      0.029663
    ],
    "text_vision_ratio": "0.970337:0.029663",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.351054,
      "aei_text": 2.930586,
      "aei_vision": 0.070871,
      "text_ratio": 0.976388,
      "vision_ratio": 0.023612
    },
    "middle": {
      "mdi": 37.587515,
      "aei_text": 2.916613,
      "aei_vision": 0.077595,
      "text_ratio": 0.974085,
      "vision_ratio": 0.025915
    },
    "late": {
      "mdi": 33.951608,
      "aei_text": 2.900343,
      "aei_vision": 0.085426,
      "text_ratio": 0.971389,
      "vision_ratio": 0.028611
    },
    "all": {
      "mdi": 33.951608,
      "aei_text": 2.915844,
      "aei_vision": 0.077966,
      "text_ratio": 0.971389,
      "vision_ratio": 0.028611
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971389,
      0.028611
    ],
    "text_vision_ratio": "0.971389:0.028611",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.822653,
      "aei_text": 2.928772,
      "aei_vision": 0.071744,
      "text_ratio": 0.97609,
      "vision_ratio": 0.02391
    },
    "middle": {
      "mdi": 42.21238,
      "aei_text": 2.933449,
      "aei_vision": 0.069493,
      "text_ratio": 0.976858,
      "vision_ratio": 0.023142
    },
    "late": {
      "mdi": 49.840697,
      "aei_text": 2.954665,
      "aei_vision": 0.059282,
      "text_ratio": 0.980331,
      "vision_ratio": 0.019669
    },
    "all": {
      "mdi": 49.840697,
      "aei_text": 2.938964,
      "aei_vision": 0.066839,
      "text_ratio": 0.980331,
      "vision_ratio": 0.019669
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980331,
      0.019669
    ],
    "text_vision_ratio": "0.980331:0.019669",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 160.0,
    "total_tokens": 378.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.131488,
      "aei_text": 2.269182,
      "aei_vision": 0.06849,
      "text_ratio": 0.970702,
      "vision_ratio": 0.029298
    },
    "middle": {
      "mdi": 18.157097,
      "aei_text": 2.197594,
      "aei_vision": 0.121032,
      "text_ratio": 0.9478,
      "vision_ratio": 0.0522
    },
    "late": {
      "mdi": 16.516568,
      "aei_text": 2.182462,
      "aei_vision": 0.132138,
      "text_ratio": 0.942911,
      "vision_ratio": 0.057089
    },
    "all": {
      "mdi": 16.516568,
      "aei_text": 2.216404,
      "aei_vision": 0.107226,
      "text_ratio": 0.942911,
      "vision_ratio": 0.057089
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942911,
      0.057089
    ],
    "text_vision_ratio": "0.942911:0.057089",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 160.0,
    "total_tokens": 378.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.942508,
      "aei_text": 2.265851,
      "aei_vision": 0.070935,
      "text_ratio": 0.969644,
      "vision_ratio": 0.030356
    },
    "middle": {
      "mdi": 34.794904,
      "aei_text": 2.273475,
      "aei_vision": 0.065339,
      "text_ratio": 0.972063,
      "vision_ratio": 0.027937
    },
    "late": {
      "mdi": 40.893984,
      "aei_text": 2.286325,
      "aei_vision": 0.055909,
      "text_ratio": 0.97613,
      "vision_ratio": 0.02387
    },
    "all": {
      "mdi": 40.893984,
      "aei_text": 2.275217,
      "aei_vision": 0.064061,
      "text_ratio": 0.97613,
      "vision_ratio": 0.02387
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97613,
      0.02387
    ],
    "text_vision_ratio": "0.976130:0.023870",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.862212,
      "aei_text": 2.76294,
      "aei_vision": 0.232919,
      "text_ratio": 0.922253,
      "vision_ratio": 0.077747
    },
    "middle": {
      "mdi": 11.778796,
      "aei_text": 2.759768,
      "aei_vision": 0.2343,
      "text_ratio": 0.921745,
      "vision_ratio": 0.078255
    },
    "late": {
      "mdi": 17.337263,
      "aei_text": 2.912201,
      "aei_vision": 0.167974,
      "text_ratio": 0.945466,
      "vision_ratio": 0.054534
    },
    "all": {
      "mdi": 17.337263,
      "aei_text": 2.811662,
      "aei_vision": 0.21172,
      "text_ratio": 0.945466,
      "vision_ratio": 0.054534
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945466,
      0.054534
    ],
    "text_vision_ratio": "0.945466:0.054534",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.513804,
      "aei_text": 2.749437,
      "aei_vision": 0.238795,
      "text_ratio": 0.920088,
      "vision_ratio": 0.079912
    },
    "middle": {
      "mdi": 8.72127,
      "aei_text": 2.610359,
      "aei_vision": 0.299309,
      "text_ratio": 0.897133,
      "vision_ratio": 0.102867
    },
    "late": {
      "mdi": 12.871662,
      "aei_text": 2.79856,
      "aei_vision": 0.21742,
      "text_ratio": 0.927911,
      "vision_ratio": 0.072089
    },
    "all": {
      "mdi": 12.871662,
      "aei_text": 2.719462,
      "aei_vision": 0.251837,
      "text_ratio": 0.927911,
      "vision_ratio": 0.072089
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927911,
      0.072089
    ],
    "text_vision_ratio": "0.927911:0.072089",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.386256,
      "aei_text": 3.284611,
      "aei_vision": 0.058252,
      "text_ratio": 0.982574,
      "vision_ratio": 0.017426
    },
    "middle": {
      "mdi": 65.946091,
      "aei_text": 3.30437,
      "aei_vision": 0.050107,
      "text_ratio": 0.985063,
      "vision_ratio": 0.014937
    },
    "late": {
      "mdi": 50.967361,
      "aei_text": 3.270269,
      "aei_vision": 0.064164,
      "text_ratio": 0.980757,
      "vision_ratio": 0.019243
    },
    "all": {
      "mdi": 50.967361,
      "aei_text": 3.286421,
      "aei_vision": 0.057506,
      "text_ratio": 0.980757,
      "vision_ratio": 0.019243
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980757,
      0.019243
    ],
    "text_vision_ratio": "0.980757:0.019243",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.124745,
      "aei_text": 3.281513,
      "aei_vision": 0.059529,
      "text_ratio": 0.982183,
      "vision_ratio": 0.017817
    },
    "middle": {
      "mdi": 69.560853,
      "aei_text": 3.310474,
      "aei_vision": 0.047591,
      "text_ratio": 0.985828,
      "vision_ratio": 0.014172
    },
    "late": {
      "mdi": 44.407882,
      "aei_text": 3.248468,
      "aei_vision": 0.073151,
      "text_ratio": 0.977977,
      "vision_ratio": 0.022023
    },
    "all": {
      "mdi": 44.407882,
      "aei_text": 3.28015,
      "aei_vision": 0.060091,
      "text_ratio": 0.977977,
      "vision_ratio": 0.022023
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977977,
      0.022023
    ],
    "text_vision_ratio": "0.977977:0.022023",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.008532,
      "aei_text": 3.177679,
      "aei_vision": 0.063543,
      "text_ratio": 0.980395,
      "vision_ratio": 0.019605
    },
    "middle": {
      "mdi": 55.479963,
      "aei_text": 3.191665,
      "aei_vision": 0.057528,
      "text_ratio": 0.982295,
      "vision_ratio": 0.017705
    },
    "late": {
      "mdi": 55.569415,
      "aei_text": 3.191872,
      "aei_vision": 0.057439,
      "text_ratio": 0.982323,
      "vision_ratio": 0.017677
    },
    "all": {
      "mdi": 55.569415,
      "aei_text": 3.187071,
      "aei_vision": 0.059504,
      "text_ratio": 0.982323,
      "vision_ratio": 0.017677
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982323,
      0.017677
    ],
    "text_vision_ratio": "0.982323:0.017677",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.160914,
      "aei_text": 3.169176,
      "aei_vision": 0.067199,
      "text_ratio": 0.979236,
      "vision_ratio": 0.020764
    },
    "middle": {
      "mdi": 63.241895,
      "aei_text": 3.207502,
      "aei_vision": 0.050718,
      "text_ratio": 0.984434,
      "vision_ratio": 0.015566
    },
    "late": {
      "mdi": 60.521906,
      "aei_text": 3.202398,
      "aei_vision": 0.052913,
      "text_ratio": 0.983746,
      "vision_ratio": 0.016254
    },
    "all": {
      "mdi": 60.521906,
      "aei_text": 3.193019,
      "aei_vision": 0.056946,
      "text_ratio": 0.983746,
      "vision_ratio": 0.016254
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983746,
      0.016254
    ],
    "text_vision_ratio": "0.983746:0.016254",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.420684,
      "aei_text": 3.179082,
      "aei_vision": 0.068484,
      "text_ratio": 0.978912,
      "vision_ratio": 0.021088
    },
    "middle": {
      "mdi": 27.372555,
      "aei_text": 3.076376,
      "aei_vision": 0.112389,
      "text_ratio": 0.964755,
      "vision_ratio": 0.035245
    },
    "late": {
      "mdi": 25.433631,
      "aei_text": 3.058021,
      "aei_vision": 0.120235,
      "text_ratio": 0.962169,
      "vision_ratio": 0.037831
    },
    "all": {
      "mdi": 25.433631,
      "aei_text": 3.104461,
      "aei_vision": 0.100383,
      "text_ratio": 0.962169,
      "vision_ratio": 0.037831
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962169,
      0.037831
    ],
    "text_vision_ratio": "0.962169:0.037831",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.308826,
      "aei_text": 3.185054,
      "aei_vision": 0.065931,
      "text_ratio": 0.97972,
      "vision_ratio": 0.02028
    },
    "middle": {
      "mdi": 46.365906,
      "aei_text": 3.178902,
      "aei_vision": 0.068561,
      "text_ratio": 0.978888,
      "vision_ratio": 0.021112
    },
    "late": {
      "mdi": 46.137866,
      "aei_text": 3.178147,
      "aei_vision": 0.068884,
      "text_ratio": 0.978786,
      "vision_ratio": 0.021214
    },
    "all": {
      "mdi": 46.137866,
      "aei_text": 3.1807,
      "aei_vision": 0.067792,
      "text_ratio": 0.978786,
      "vision_ratio": 0.021214
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978786,
      0.021214
    ],
    "text_vision_ratio": "0.978786:0.021214",
    "skip_reason": null
  }
}
```


## === Rollout Step 16 ===
Step: 15/43 | 2025-10-22 18:37:14

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 43.490 | 52.896 | 44.536 | 44.536 |
| MDI Std | 12.475 | 23.737 | 19.161 | 19.161 |
| Vision Tokens | 356.1 ± 51.5 |
| Text Tokens | 163.5 ± 3.2 |
| Total Tokens | 519.6 ± 52.7 |
| Vision Ratio | 0.682 |
| Text Ratio | 0.318 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.204322,
      "aei_text": 2.369732,
      "aei_vision": 0.071368,
      "text_ratio": 0.970764,
      "vision_ratio": 0.029236
    },
    "middle": {
      "mdi": 45.959934,
      "aei_text": 2.398039,
      "aei_vision": 0.052177,
      "text_ratio": 0.978705,
      "vision_ratio": 0.021295
    },
    "late": {
      "mdi": 45.510446,
      "aei_text": 2.397303,
      "aei_vision": 0.052676,
      "text_ratio": 0.978499,
      "vision_ratio": 0.021501
    },
    "all": {
      "mdi": 45.510446,
      "aei_text": 2.388357,
      "aei_vision": 0.058741,
      "text_ratio": 0.978499,
      "vision_ratio": 0.021501
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978499,
      0.021501
    ],
    "text_vision_ratio": "0.978499:0.021501",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.201285,
      "aei_text": 2.380611,
      "aei_vision": 0.063993,
      "text_ratio": 0.973823,
      "vision_ratio": 0.026177
    },
    "middle": {
      "mdi": 32.066171,
      "aei_text": 2.36616,
      "aei_vision": 0.07379,
      "text_ratio": 0.969758,
      "vision_ratio": 0.030242
    },
    "late": {
      "mdi": 28.948273,
      "aei_text": 2.355006,
      "aei_vision": 0.081352,
      "text_ratio": 0.966609,
      "vision_ratio": 0.033391
    },
    "all": {
      "mdi": 28.948273,
      "aei_text": 2.367258,
      "aei_vision": 0.073045,
      "text_ratio": 0.966609,
      "vision_ratio": 0.033391
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966609,
      0.033391
    ],
    "text_vision_ratio": "0.966609:0.033391",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.265388,
      "aei_text": 3.248755,
      "aei_vision": 0.06731,
      "text_ratio": 0.979702,
      "vision_ratio": 0.020298
    },
    "middle": {
      "mdi": 44.805697,
      "aei_text": 3.236864,
      "aei_vision": 0.072242,
      "text_ratio": 0.978169,
      "vision_ratio": 0.021831
    },
    "late": {
      "mdi": 38.231541,
      "aei_text": 3.208689,
      "aei_vision": 0.083928,
      "text_ratio": 0.97451,
      "vision_ratio": 0.02549
    },
    "all": {
      "mdi": 38.231541,
      "aei_text": 3.231431,
      "aei_vision": 0.074496,
      "text_ratio": 0.97451,
      "vision_ratio": 0.02549
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97451,
      0.02549
    ],
    "text_vision_ratio": "0.974510:0.025490",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.871879,
      "aei_text": 3.247485,
      "aei_vision": 0.067837,
      "text_ratio": 0.979538,
      "vision_ratio": 0.020462
    },
    "middle": {
      "mdi": 64.634313,
      "aei_text": 3.288377,
      "aei_vision": 0.050877,
      "text_ratio": 0.984764,
      "vision_ratio": 0.015236
    },
    "late": {
      "mdi": 50.89544,
      "aei_text": 3.256762,
      "aei_vision": 0.063989,
      "text_ratio": 0.98073,
      "vision_ratio": 0.01927
    },
    "all": {
      "mdi": 50.89544,
      "aei_text": 3.2642,
      "aei_vision": 0.060904,
      "text_ratio": 0.98073,
      "vision_ratio": 0.01927
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98073,
      0.01927
    ],
    "text_vision_ratio": "0.980730:0.019270",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.219335,
      "aei_text": 2.985071,
      "aei_vision": 0.05609,
      "text_ratio": 0.981556,
      "vision_ratio": 0.018444
    },
    "middle": {
      "mdi": 71.915626,
      "aei_text": 3.014866,
      "aei_vision": 0.041922,
      "text_ratio": 0.986286,
      "vision_ratio": 0.013714
    },
    "late": {
      "mdi": 59.810536,
      "aei_text": 2.997629,
      "aei_vision": 0.050119,
      "text_ratio": 0.983555,
      "vision_ratio": 0.016445
    },
    "all": {
      "mdi": 59.810536,
      "aei_text": 2.99919,
      "aei_vision": 0.049376,
      "text_ratio": 0.983555,
      "vision_ratio": 0.016445
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983555,
      0.016445
    ],
    "text_vision_ratio": "0.983555:0.016445",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.639279,
      "aei_text": 2.97691,
      "aei_vision": 0.059971,
      "text_ratio": 0.980252,
      "vision_ratio": 0.019748
    },
    "middle": {
      "mdi": 66.083107,
      "aei_text": 3.007325,
      "aei_vision": 0.045508,
      "text_ratio": 0.985093,
      "vision_ratio": 0.014907
    },
    "late": {
      "mdi": 75.783844,
      "aei_text": 3.019245,
      "aei_vision": 0.03984,
      "text_ratio": 0.986976,
      "vision_ratio": 0.013024
    },
    "all": {
      "mdi": 75.783844,
      "aei_text": 3.001158,
      "aei_vision": 0.048441,
      "text_ratio": 0.986976,
      "vision_ratio": 0.013024
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986976,
      0.013024
    ],
    "text_vision_ratio": "0.986976:0.013024",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.374132,
      "aei_text": 2.972761,
      "aei_vision": 0.222277,
      "text_ratio": 0.930431,
      "vision_ratio": 0.069569
    },
    "middle": {
      "mdi": 8.777714,
      "aei_text": 2.743708,
      "aei_vision": 0.312577,
      "text_ratio": 0.897727,
      "vision_ratio": 0.102273
    },
    "late": {
      "mdi": 12.824092,
      "aei_text": 2.952571,
      "aei_vision": 0.230236,
      "text_ratio": 0.927663,
      "vision_ratio": 0.072337
    },
    "all": {
      "mdi": 12.824092,
      "aei_text": 2.88969,
      "aei_vision": 0.255026,
      "text_ratio": 0.927663,
      "vision_ratio": 0.072337
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927663,
      0.072337
    ],
    "text_vision_ratio": "0.927663:0.072337",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.308378,
      "aei_text": 3.004031,
      "aei_vision": 0.209949,
      "text_ratio": 0.934676,
      "vision_ratio": 0.065324
    },
    "middle": {
      "mdi": 9.460513,
      "aei_text": 2.788834,
      "aei_vision": 0.294787,
      "text_ratio": 0.904402,
      "vision_ratio": 0.095598
    },
    "late": {
      "mdi": 11.650104,
      "aei_text": 2.904243,
      "aei_vision": 0.249289,
      "text_ratio": 0.920949,
      "vision_ratio": 0.079051
    },
    "all": {
      "mdi": 11.650104,
      "aei_text": 2.899019,
      "aei_vision": 0.251348,
      "text_ratio": 0.920949,
      "vision_ratio": 0.079051
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.920949,
      0.079051
    ],
    "text_vision_ratio": "0.920949:0.079051",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.727977,
      "aei_text": 2.938815,
      "aei_vision": 0.055735,
      "text_ratio": 0.981388,
      "vision_ratio": 0.018612
    },
    "middle": {
      "mdi": 44.282169,
      "aei_text": 2.917956,
      "aei_vision": 0.065895,
      "text_ratio": 0.977916,
      "vision_ratio": 0.022084
    },
    "late": {
      "mdi": 32.279657,
      "aei_text": 2.870657,
      "aei_vision": 0.088931,
      "text_ratio": 0.969952,
      "vision_ratio": 0.030048
    },
    "all": {
      "mdi": 32.279657,
      "aei_text": 2.90915,
      "aei_vision": 0.070183,
      "text_ratio": 0.969952,
      "vision_ratio": 0.030048
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969952,
      0.030048
    ],
    "text_vision_ratio": "0.969952:0.030048",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 169.0,
    "total_tokens": 516.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.266075,
      "aei_text": 2.923511,
      "aei_vision": 0.063189,
      "text_ratio": 0.978843,
      "vision_ratio": 0.021157
    },
    "middle": {
      "mdi": 58.254782,
      "aei_text": 2.949303,
      "aei_vision": 0.050628,
      "text_ratio": 0.983124,
      "vision_ratio": 0.016876
    },
    "late": {
      "mdi": 54.551375,
      "aei_text": 2.942502,
      "aei_vision": 0.05394,
      "text_ratio": 0.981999,
      "vision_ratio": 0.018001
    },
    "all": {
      "mdi": 54.551375,
      "aei_text": 2.938438,
      "aei_vision": 0.055919,
      "text_ratio": 0.981999,
      "vision_ratio": 0.018001
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981999,
      0.018001
    ],
    "text_vision_ratio": "0.981999:0.018001",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 160.0,
    "total_tokens": 530.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.52521,
      "aei_text": 3.167525,
      "aei_vision": 0.062692,
      "text_ratio": 0.980592,
      "vision_ratio": 0.019408
    },
    "middle": {
      "mdi": 50.71365,
      "aei_text": 3.16804,
      "aei_vision": 0.062469,
      "text_ratio": 0.980663,
      "vision_ratio": 0.019337
    },
    "late": {
      "mdi": 42.899621,
      "aei_text": 3.143073,
      "aei_vision": 0.073266,
      "text_ratio": 0.977221,
      "vision_ratio": 0.022779
    },
    "all": {
      "mdi": 42.899621,
      "aei_text": 3.159543,
      "aei_vision": 0.066144,
      "text_ratio": 0.977221,
      "vision_ratio": 0.022779
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977221,
      0.022779
    ],
    "text_vision_ratio": "0.977221:0.022779",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 160.0,
    "total_tokens": 530.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.35016,
      "aei_text": 3.169754,
      "aei_vision": 0.061728,
      "text_ratio": 0.980898,
      "vision_ratio": 0.019102
    },
    "middle": {
      "mdi": 107.3564,
      "aei_text": 3.242652,
      "aei_vision": 0.030205,
      "text_ratio": 0.990771,
      "vision_ratio": 0.009229
    },
    "late": {
      "mdi": 84.758462,
      "aei_text": 3.224524,
      "aei_vision": 0.038044,
      "text_ratio": 0.988339,
      "vision_ratio": 0.011661
    },
    "all": {
      "mdi": 84.758462,
      "aei_text": 3.212318,
      "aei_vision": 0.043322,
      "text_ratio": 0.988339,
      "vision_ratio": 0.011661
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988339,
      0.011661
    ],
    "text_vision_ratio": "0.988339:0.011661",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.28619,
      "aei_text": 3.211465,
      "aei_vision": 0.060268,
      "text_ratio": 0.981579,
      "vision_ratio": 0.018421
    },
    "middle": {
      "mdi": 70.248628,
      "aei_text": 3.244601,
      "aei_vision": 0.046187,
      "text_ratio": 0.985965,
      "vision_ratio": 0.014035
    },
    "late": {
      "mdi": 54.866156,
      "aei_text": 3.215381,
      "aei_vision": 0.058604,
      "text_ratio": 0.9821,
      "vision_ratio": 0.0179
    },
    "all": {
      "mdi": 54.866156,
      "aei_text": 3.223812,
      "aei_vision": 0.055021,
      "text_ratio": 0.9821,
      "vision_ratio": 0.0179
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9821,
      0.0179
    ],
    "text_vision_ratio": "0.982100:0.017900",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.517792,
      "aei_text": 3.206809,
      "aei_vision": 0.062247,
      "text_ratio": 0.980959,
      "vision_ratio": 0.019041
    },
    "middle": {
      "mdi": 74.452213,
      "aei_text": 3.25055,
      "aei_vision": 0.04366,
      "text_ratio": 0.986747,
      "vision_ratio": 0.013253
    },
    "late": {
      "mdi": 51.248285,
      "aei_text": 3.206072,
      "aei_vision": 0.06256,
      "text_ratio": 0.980861,
      "vision_ratio": 0.019139
    },
    "all": {
      "mdi": 51.248285,
      "aei_text": 3.221143,
      "aei_vision": 0.056156,
      "text_ratio": 0.980861,
      "vision_ratio": 0.019139
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980861,
      0.019139
    ],
    "text_vision_ratio": "0.980861:0.019139",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.307498,
      "aei_text": 3.037791,
      "aei_vision": 0.060384,
      "text_ratio": 0.98051,
      "vision_ratio": 0.01949
    },
    "middle": {
      "mdi": 42.117623,
      "aei_text": 3.013573,
      "aei_vision": 0.071551,
      "text_ratio": 0.976808,
      "vision_ratio": 0.023192
    },
    "late": {
      "mdi": 31.37696,
      "aei_text": 2.963888,
      "aei_vision": 0.094461,
      "text_ratio": 0.969114,
      "vision_ratio": 0.030886
    },
    "all": {
      "mdi": 31.37696,
      "aei_text": 3.005091,
      "aei_vision": 0.075462,
      "text_ratio": 0.969114,
      "vision_ratio": 0.030886
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969114,
      0.030886
    ],
    "text_vision_ratio": "0.969114:0.030886",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.781124,
      "aei_text": 3.015864,
      "aei_vision": 0.070495,
      "text_ratio": 0.977159,
      "vision_ratio": 0.022841
    },
    "middle": {
      "mdi": 55.204972,
      "aei_text": 3.04897,
      "aei_vision": 0.05523,
      "text_ratio": 0.982208,
      "vision_ratio": 0.017792
    },
    "late": {
      "mdi": 36.943452,
      "aei_text": 2.993045,
      "aei_vision": 0.081017,
      "text_ratio": 0.973645,
      "vision_ratio": 0.026355
    },
    "all": {
      "mdi": 36.943452,
      "aei_text": 3.019292,
      "aei_vision": 0.068914,
      "text_ratio": 0.973645,
      "vision_ratio": 0.026355
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973645,
      0.026355
    ],
    "text_vision_ratio": "0.973645:0.026355",
    "skip_reason": null
  }
}
```


## === Rollout Step 17 ===
Step: 16/43 | 2025-10-22 18:38:31

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 47.349 | 52.101 | 43.976 | 43.976 |
| MDI Std | 15.645 | 27.510 | 21.986 | 21.986 |
| Vision Tokens | 384.4 ± 22.8 |
| Text Tokens | 162.1 ± 2.0 |
| Total Tokens | 546.5 ± 23.4 |
| Vision Ratio | 0.703 |
| Text Ratio | 0.297 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.565909,
      "aei_text": 3.21121,
      "aei_vision": 0.077256,
      "text_ratio": 0.976507,
      "vision_ratio": 0.023493
    },
    "middle": {
      "mdi": 50.866632,
      "aei_text": 3.243537,
      "aei_vision": 0.063766,
      "text_ratio": 0.98072,
      "vision_ratio": 0.01928
    },
    "late": {
      "mdi": 37.089655,
      "aei_text": 3.190223,
      "aei_vision": 0.086014,
      "text_ratio": 0.973746,
      "vision_ratio": 0.026254
    },
    "all": {
      "mdi": 37.089655,
      "aei_text": 3.21499,
      "aei_vision": 0.075679,
      "text_ratio": 0.973746,
      "vision_ratio": 0.026254
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973746,
      0.026254
    ],
    "text_vision_ratio": "0.973746:0.026254",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.490689,
      "aei_text": 3.218976,
      "aei_vision": 0.074015,
      "text_ratio": 0.977523,
      "vision_ratio": 0.022477
    },
    "middle": {
      "mdi": 52.090215,
      "aei_text": 3.246969,
      "aei_vision": 0.062334,
      "text_ratio": 0.981164,
      "vision_ratio": 0.018836
    },
    "late": {
      "mdi": 40.813739,
      "aei_text": 3.207987,
      "aei_vision": 0.078601,
      "text_ratio": 0.976084,
      "vision_ratio": 0.023916
    },
    "all": {
      "mdi": 40.813739,
      "aei_text": 3.224642,
      "aei_vision": 0.07165,
      "text_ratio": 0.976084,
      "vision_ratio": 0.023916
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976084,
      0.023916
    ],
    "text_vision_ratio": "0.976084:0.023916",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.682179,
      "aei_text": 2.85794,
      "aei_vision": 0.267543,
      "text_ratio": 0.9144,
      "vision_ratio": 0.0856
    },
    "middle": {
      "mdi": 7.543871,
      "aei_text": 2.64666,
      "aei_vision": 0.350836,
      "text_ratio": 0.882957,
      "vision_ratio": 0.117043
    },
    "late": {
      "mdi": 13.405201,
      "aei_text": 2.97386,
      "aei_vision": 0.221844,
      "text_ratio": 0.930581,
      "vision_ratio": 0.069419
    },
    "all": {
      "mdi": 13.405201,
      "aei_text": 2.826167,
      "aei_vision": 0.280069,
      "text_ratio": 0.930581,
      "vision_ratio": 0.069419
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.930581,
      0.069419
    ],
    "text_vision_ratio": "0.930581:0.069419",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.692259,
      "aei_text": 2.947516,
      "aei_vision": 0.232229,
      "text_ratio": 0.926966,
      "vision_ratio": 0.073034
    },
    "middle": {
      "mdi": 10.133917,
      "aei_text": 2.828575,
      "aei_vision": 0.27912,
      "text_ratio": 0.910184,
      "vision_ratio": 0.089816
    },
    "late": {
      "mdi": 13.081023,
      "aei_text": 2.962179,
      "aei_vision": 0.226449,
      "text_ratio": 0.928982,
      "vision_ratio": 0.071018
    },
    "all": {
      "mdi": 13.081023,
      "aei_text": 2.91276,
      "aei_vision": 0.245931,
      "text_ratio": 0.928982,
      "vision_ratio": 0.071018
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928982,
      0.071018
    ],
    "text_vision_ratio": "0.928982:0.071018",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.833458,
      "aei_text": 3.319297,
      "aei_vision": 0.061659,
      "text_ratio": 0.981763,
      "vision_ratio": 0.018237
    },
    "middle": {
      "mdi": 91.066284,
      "aei_text": 3.37996,
      "aei_vision": 0.037115,
      "text_ratio": 0.989138,
      "vision_ratio": 0.010862
    },
    "late": {
      "mdi": 72.212327,
      "aei_text": 3.356801,
      "aei_vision": 0.046485,
      "text_ratio": 0.986341,
      "vision_ratio": 0.013659
    },
    "all": {
      "mdi": 72.212327,
      "aei_text": 3.352015,
      "aei_vision": 0.048422,
      "text_ratio": 0.986341,
      "vision_ratio": 0.013659
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986341,
      0.013659
    ],
    "text_vision_ratio": "0.986341:0.013659",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.423851,
      "aei_text": 3.31818,
      "aei_vision": 0.06211,
      "text_ratio": 0.981626,
      "vision_ratio": 0.018374
    },
    "middle": {
      "mdi": 65.53404,
      "aei_text": 3.345518,
      "aei_vision": 0.05105,
      "text_ratio": 0.98497,
      "vision_ratio": 0.01503
    },
    "late": {
      "mdi": 50.246546,
      "aei_text": 3.308927,
      "aei_vision": 0.065854,
      "text_ratio": 0.980486,
      "vision_ratio": 0.019514
    },
    "all": {
      "mdi": 50.246546,
      "aei_text": 3.324211,
      "aei_vision": 0.05967,
      "text_ratio": 0.980486,
      "vision_ratio": 0.019514
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980486,
      0.019514
    ],
    "text_vision_ratio": "0.980486:0.019514",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.722783,
      "aei_text": 3.024193,
      "aei_vision": 0.060821,
      "text_ratio": 0.980285,
      "vision_ratio": 0.019715
    },
    "middle": {
      "mdi": 73.813665,
      "aei_text": 3.065763,
      "aei_vision": 0.041534,
      "text_ratio": 0.986633,
      "vision_ratio": 0.013367
    },
    "late": {
      "mdi": 63.914534,
      "aei_text": 3.05235,
      "aei_vision": 0.047757,
      "text_ratio": 0.984595,
      "vision_ratio": 0.015405
    },
    "all": {
      "mdi": 63.914534,
      "aei_text": 3.047435,
      "aei_vision": 0.050037,
      "text_ratio": 0.984595,
      "vision_ratio": 0.015405
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984595,
      0.015405
    ],
    "text_vision_ratio": "0.984595:0.015405",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.444569,
      "aei_text": 3.032968,
      "aei_vision": 0.05675,
      "text_ratio": 0.981633,
      "vision_ratio": 0.018367
    },
    "middle": {
      "mdi": 50.107979,
      "aei_text": 3.025159,
      "aei_vision": 0.060373,
      "text_ratio": 0.980434,
      "vision_ratio": 0.019566
    },
    "late": {
      "mdi": 40.174202,
      "aei_text": 2.994623,
      "aei_vision": 0.074541,
      "text_ratio": 0.975713,
      "vision_ratio": 0.024287
    },
    "all": {
      "mdi": 40.174202,
      "aei_text": 3.017586,
      "aei_vision": 0.063887,
      "text_ratio": 0.975713,
      "vision_ratio": 0.024287
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975713,
      0.024287
    ],
    "text_vision_ratio": "0.975713:0.024287",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 69.534849,
      "aei_text": 3.269815,
      "aei_vision": 0.047024,
      "text_ratio": 0.985823,
      "vision_ratio": 0.014177
    },
    "middle": {
      "mdi": 77.884511,
      "aei_text": 3.281466,
      "aei_vision": 0.042132,
      "text_ratio": 0.987323,
      "vision_ratio": 0.012677
    },
    "late": {
      "mdi": 67.98956,
      "aei_text": 3.267356,
      "aei_vision": 0.048057,
      "text_ratio": 0.985505,
      "vision_ratio": 0.014495
    },
    "all": {
      "mdi": 67.98956,
      "aei_text": 3.272877,
      "aei_vision": 0.045739,
      "text_ratio": 0.985505,
      "vision_ratio": 0.014495
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985505,
      0.014495
    ],
    "text_vision_ratio": "0.985505:0.014495",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 71.490396,
      "aei_text": 3.27278,
      "aei_vision": 0.045779,
      "text_ratio": 0.986205,
      "vision_ratio": 0.013795
    },
    "middle": {
      "mdi": 97.195887,
      "aei_text": 3.300928,
      "aei_vision": 0.033962,
      "text_ratio": 0.989816,
      "vision_ratio": 0.010184
    },
    "late": {
      "mdi": 87.374565,
      "aei_text": 3.292077,
      "aei_vision": 0.037678,
      "text_ratio": 0.988685,
      "vision_ratio": 0.011315
    },
    "all": {
      "mdi": 87.374565,
      "aei_text": 3.288595,
      "aei_vision": 0.039139,
      "text_ratio": 0.988685,
      "vision_ratio": 0.011315
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988685,
      0.011315
    ],
    "text_vision_ratio": "0.988685:0.011315",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.890144,
      "aei_text": 3.250276,
      "aei_vision": 0.072405,
      "text_ratio": 0.978209,
      "vision_ratio": 0.021791
    },
    "middle": {
      "mdi": 41.605799,
      "aei_text": 3.237175,
      "aei_vision": 0.077806,
      "text_ratio": 0.976529,
      "vision_ratio": 0.023471
    },
    "late": {
      "mdi": 39.850797,
      "aei_text": 3.229339,
      "aei_vision": 0.081036,
      "text_ratio": 0.975521,
      "vision_ratio": 0.024479
    },
    "all": {
      "mdi": 39.850797,
      "aei_text": 3.238928,
      "aei_vision": 0.077083,
      "text_ratio": 0.975521,
      "vision_ratio": 0.024479
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975521,
      0.024479
    ],
    "text_vision_ratio": "0.975521:0.024479",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.08404,
      "aei_text": 3.25806,
      "aei_vision": 0.069197,
      "text_ratio": 0.979203,
      "vision_ratio": 0.020797
    },
    "middle": {
      "mdi": 32.62462,
      "aei_text": 3.18881,
      "aei_vision": 0.097742,
      "text_ratio": 0.97026,
      "vision_ratio": 0.02974
    },
    "late": {
      "mdi": 26.315129,
      "aei_text": 3.136756,
      "aei_vision": 0.1192,
      "text_ratio": 0.96339,
      "vision_ratio": 0.03661
    },
    "all": {
      "mdi": 26.315129,
      "aei_text": 3.194562,
      "aei_vision": 0.095371,
      "text_ratio": 0.96339,
      "vision_ratio": 0.03661
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96339,
      0.03661
    ],
    "text_vision_ratio": "0.963390:0.036610",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.704452,
      "aei_text": 3.023586,
      "aei_vision": 0.055271,
      "text_ratio": 0.982048,
      "vision_ratio": 0.017952
    },
    "middle": {
      "mdi": 90.104316,
      "aei_text": 3.069018,
      "aei_vision": 0.034061,
      "text_ratio": 0.989024,
      "vision_ratio": 0.010976
    },
    "late": {
      "mdi": 70.33047,
      "aei_text": 3.049112,
      "aei_vision": 0.043354,
      "text_ratio": 0.985981,
      "vision_ratio": 0.014019
    },
    "all": {
      "mdi": 70.33047,
      "aei_text": 3.047241,
      "aei_vision": 0.044228,
      "text_ratio": 0.985981,
      "vision_ratio": 0.014019
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985981,
      0.014019
    ],
    "text_vision_ratio": "0.985981:0.014019",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.398323,
      "aei_text": 3.025013,
      "aei_vision": 0.054605,
      "text_ratio": 0.982269,
      "vision_ratio": 0.017731
    },
    "middle": {
      "mdi": 23.123011,
      "aei_text": 2.875597,
      "aei_vision": 0.124361,
      "text_ratio": 0.958546,
      "vision_ratio": 0.041454
    },
    "late": {
      "mdi": 17.511461,
      "aei_text": 2.79954,
      "aei_vision": 0.159869,
      "text_ratio": 0.945979,
      "vision_ratio": 0.054021
    },
    "all": {
      "mdi": 17.511461,
      "aei_text": 2.900073,
      "aei_vision": 0.112934,
      "text_ratio": 0.945979,
      "vision_ratio": 0.054021
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945979,
      0.054021
    ],
    "text_vision_ratio": "0.945979:0.054021",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.25443,
      "aei_text": 3.288841,
      "aei_vision": 0.068156,
      "text_ratio": 0.979697,
      "vision_ratio": 0.020303
    },
    "middle": {
      "mdi": 42.932026,
      "aei_text": 3.26921,
      "aei_vision": 0.076149,
      "text_ratio": 0.977238,
      "vision_ratio": 0.022762
    },
    "late": {
      "mdi": 36.708158,
      "aei_text": 3.239487,
      "aei_vision": 0.08825,
      "text_ratio": 0.973481,
      "vision_ratio": 0.026519
    },
    "all": {
      "mdi": 36.708158,
      "aei_text": 3.265842,
      "aei_vision": 0.07752,
      "text_ratio": 0.973481,
      "vision_ratio": 0.026519
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973481,
      0.026519
    ],
    "text_vision_ratio": "0.973481:0.026519",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.366864,
      "aei_text": 3.285859,
      "aei_vision": 0.06937,
      "text_ratio": 0.979325,
      "vision_ratio": 0.020675
    },
    "middle": {
      "mdi": 26.9953,
      "aei_text": 3.168,
      "aei_vision": 0.117354,
      "text_ratio": 0.96428,
      "vision_ratio": 0.03572
    },
    "late": {
      "mdi": 26.595627,
      "aei_text": 3.164034,
      "aei_vision": 0.118968,
      "text_ratio": 0.963762,
      "vision_ratio": 0.036238
    },
    "all": {
      "mdi": 26.595627,
      "aei_text": 3.20595,
      "aei_vision": 0.101903,
      "text_ratio": 0.963762,
      "vision_ratio": 0.036238
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963762,
      0.036238
    ],
    "text_vision_ratio": "0.963762:0.036238",
    "skip_reason": null
  }
}
```


## === Rollout Step 18 ===
Step: 17/43 | 2025-10-22 18:39:46

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 31.773 | 39.065 | 37.820 | 37.820 |
| MDI Std | 12.338 | 23.362 | 21.282 | 21.282 |
| Vision Tokens | 266.8 ± 116.4 |
| Text Tokens | 165.1 ± 8.9 |
| Total Tokens | 431.9 ± 118.7 |
| Vision Ratio | 0.577 |
| Text Ratio | 0.423 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 163.0,
    "total_tokens": 464.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.865814,
      "aei_text": 2.738714,
      "aei_vision": 0.058437,
      "text_ratio": 0.979108,
      "vision_ratio": 0.020892
    },
    "middle": {
      "mdi": 34.995664,
      "aei_text": 2.703946,
      "aei_vision": 0.077265,
      "text_ratio": 0.972219,
      "vision_ratio": 0.027781
    },
    "late": {
      "mdi": 30.514127,
      "aei_text": 2.684187,
      "aei_vision": 0.087965,
      "text_ratio": 0.968268,
      "vision_ratio": 0.031732
    },
    "all": {
      "mdi": 30.514127,
      "aei_text": 2.708945,
      "aei_vision": 0.074558,
      "text_ratio": 0.968268,
      "vision_ratio": 0.031732
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968268,
      0.031732
    ],
    "text_vision_ratio": "0.968268:0.031732",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 163.0,
    "total_tokens": 464.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.78329,
      "aei_text": 2.736261,
      "aei_vision": 0.059766,
      "text_ratio": 0.978625,
      "vision_ratio": 0.021375
    },
    "middle": {
      "mdi": 88.25155,
      "aei_text": 2.788282,
      "aei_vision": 0.031595,
      "text_ratio": 0.988796,
      "vision_ratio": 0.011204
    },
    "late": {
      "mdi": 82.82015,
      "aei_text": 2.784539,
      "aei_vision": 0.033622,
      "text_ratio": 0.98807,
      "vision_ratio": 0.01193
    },
    "all": {
      "mdi": 82.82015,
      "aei_text": 2.769687,
      "aei_vision": 0.041664,
      "text_ratio": 0.98807,
      "vision_ratio": 0.01193
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98807,
      0.01193
    ],
    "text_vision_ratio": "0.988070:0.011930",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 37.0,
    "text_tokens": 161.0,
    "total_tokens": 198.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.576541,
      "aei_text": 1.205875,
      "aei_vision": 0.104165,
      "text_ratio": 0.920487,
      "vision_ratio": 0.079513
    },
    "middle": {
      "mdi": 5.260827,
      "aei_text": 1.178339,
      "aei_vision": 0.223984,
      "text_ratio": 0.840277,
      "vision_ratio": 0.159723
    },
    "late": {
      "mdi": 5.188377,
      "aei_text": 1.177651,
      "aei_vision": 0.226979,
      "text_ratio": 0.838407,
      "vision_ratio": 0.161593
    },
    "all": {
      "mdi": 5.188377,
      "aei_text": 1.187285,
      "aei_vision": 0.185059,
      "text_ratio": 0.838407,
      "vision_ratio": 0.161593
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.838407,
      0.161593
    ],
    "text_vision_ratio": "0.838407:0.161593",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 37.0,
    "text_tokens": 161.0,
    "total_tokens": 198.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.663784,
      "aei_text": 1.206051,
      "aei_vision": 0.103401,
      "text_ratio": 0.921035,
      "vision_ratio": 0.078965
    },
    "middle": {
      "mdi": 9.572583,
      "aei_text": 1.200981,
      "aei_vision": 0.125461,
      "text_ratio": 0.905416,
      "vision_ratio": 0.094584
    },
    "late": {
      "mdi": 9.533129,
      "aei_text": 1.200865,
      "aei_vision": 0.125968,
      "text_ratio": 0.905061,
      "vision_ratio": 0.094939
    },
    "all": {
      "mdi": 9.533129,
      "aei_text": 1.202631,
      "aei_vision": 0.118279,
      "text_ratio": 0.905061,
      "vision_ratio": 0.094939
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.905061,
      0.094939
    ],
    "text_vision_ratio": "0.905061:0.094939",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 161.0,
    "total_tokens": 577.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.005893,
      "aei_text": 2.989862,
      "aei_vision": 0.229885,
      "text_ratio": 0.928601,
      "vision_ratio": 0.071399
    },
    "middle": {
      "mdi": 7.515457,
      "aei_text": 2.666943,
      "aei_vision": 0.354861,
      "text_ratio": 0.882566,
      "vision_ratio": 0.117434
    },
    "late": {
      "mdi": 12.720112,
      "aei_text": 2.97877,
      "aei_vision": 0.234178,
      "text_ratio": 0.927114,
      "vision_ratio": 0.072886
    },
    "all": {
      "mdi": 12.720112,
      "aei_text": 2.878543,
      "aei_vision": 0.272968,
      "text_ratio": 0.927114,
      "vision_ratio": 0.072886
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.927114,
      0.072886
    ],
    "text_vision_ratio": "0.927114:0.072886",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 161.0,
    "total_tokens": 577.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.823435,
      "aei_text": 3.019459,
      "aei_vision": 0.21843,
      "text_ratio": 0.932539,
      "vision_ratio": 0.067461
    },
    "middle": {
      "mdi": 14.860881,
      "aei_text": 3.053024,
      "aei_vision": 0.20544,
      "text_ratio": 0.936952,
      "vision_ratio": 0.063048
    },
    "late": {
      "mdi": 25.829232,
      "aei_text": 3.25794,
      "aei_vision": 0.126134,
      "text_ratio": 0.962727,
      "vision_ratio": 0.037273
    },
    "all": {
      "mdi": 25.829232,
      "aei_text": 3.110166,
      "aei_vision": 0.183325,
      "text_ratio": 0.962727,
      "vision_ratio": 0.037273
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962727,
      0.037273
    ],
    "text_vision_ratio": "0.962727:0.037273",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.272653,
      "aei_text": 3.274576,
      "aei_vision": 0.073964,
      "text_ratio": 0.977912,
      "vision_ratio": 0.022088
    },
    "middle": {
      "mdi": 61.395171,
      "aei_text": 3.323294,
      "aei_vision": 0.05413,
      "text_ratio": 0.983973,
      "vision_ratio": 0.016027
    },
    "late": {
      "mdi": 43.919514,
      "aei_text": 3.273193,
      "aei_vision": 0.074527,
      "text_ratio": 0.977738,
      "vision_ratio": 0.022262
    },
    "all": {
      "mdi": 43.919514,
      "aei_text": 3.290369,
      "aei_vision": 0.067534,
      "text_ratio": 0.977738,
      "vision_ratio": 0.022262
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977738,
      0.022262
    ],
    "text_vision_ratio": "0.977738:0.022262",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.677554,
      "aei_text": 3.263894,
      "aei_vision": 0.078313,
      "text_ratio": 0.976568,
      "vision_ratio": 0.023432
    },
    "middle": {
      "mdi": 73.458408,
      "aei_text": 3.344422,
      "aei_vision": 0.045528,
      "text_ratio": 0.98657,
      "vision_ratio": 0.01343
    },
    "late": {
      "mdi": 59.151126,
      "aei_text": 3.318451,
      "aei_vision": 0.056101,
      "text_ratio": 0.983375,
      "vision_ratio": 0.016625
    },
    "all": {
      "mdi": 59.151126,
      "aei_text": 3.308934,
      "aei_vision": 0.059976,
      "text_ratio": 0.983375,
      "vision_ratio": 0.016625
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983375,
      0.016625
    ],
    "text_vision_ratio": "0.983375:0.016625",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 164.0,
    "total_tokens": 400.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.064914,
      "aei_text": 2.342875,
      "aei_vision": 0.066815,
      "text_ratio": 0.972272,
      "vision_ratio": 0.027728
    },
    "middle": {
      "mdi": 58.530939,
      "aei_text": 2.380498,
      "aei_vision": 0.040671,
      "text_ratio": 0.983202,
      "vision_ratio": 0.016798
    },
    "late": {
      "mdi": 66.896847,
      "aei_text": 2.387663,
      "aei_vision": 0.035692,
      "text_ratio": 0.985272,
      "vision_ratio": 0.014728
    },
    "all": {
      "mdi": 66.896847,
      "aei_text": 2.370344,
      "aei_vision": 0.047727,
      "text_ratio": 0.985272,
      "vision_ratio": 0.014728
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985272,
      0.014728
    ],
    "text_vision_ratio": "0.985272:0.014728",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 164.0,
    "total_tokens": 400.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.810591,
      "aei_text": 2.339454,
      "aei_vision": 0.069193,
      "text_ratio": 0.971273,
      "vision_ratio": 0.028727
    },
    "middle": {
      "mdi": 45.64849,
      "aei_text": 2.364486,
      "aei_vision": 0.051798,
      "text_ratio": 0.978563,
      "vision_ratio": 0.021437
    },
    "late": {
      "mdi": 49.290018,
      "aei_text": 2.369837,
      "aei_vision": 0.048079,
      "text_ratio": 0.980115,
      "vision_ratio": 0.019885
    },
    "all": {
      "mdi": 49.290018,
      "aei_text": 2.357927,
      "aei_vision": 0.056356,
      "text_ratio": 0.980115,
      "vision_ratio": 0.019885
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980115,
      0.019885
    ],
    "text_vision_ratio": "0.980115:0.019885",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 188.0,
    "total_tokens": 535.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.192563,
      "aei_text": 2.726473,
      "aei_vision": 0.06462,
      "text_ratio": 0.976848,
      "vision_ratio": 0.023152
    },
    "middle": {
      "mdi": 41.347504,
      "aei_text": 2.72414,
      "aei_vision": 0.065884,
      "text_ratio": 0.976386,
      "vision_ratio": 0.023614
    },
    "late": {
      "mdi": 34.86265,
      "aei_text": 2.702657,
      "aei_vision": 0.077523,
      "text_ratio": 0.972116,
      "vision_ratio": 0.027884
    },
    "all": {
      "mdi": 34.86265,
      "aei_text": 2.717754,
      "aei_vision": 0.069344,
      "text_ratio": 0.972116,
      "vision_ratio": 0.027884
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972116,
      0.027884
    ],
    "text_vision_ratio": "0.972116:0.027884",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 188.0,
    "total_tokens": 535.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.999057,
      "aei_text": 2.723151,
      "aei_vision": 0.06642,
      "text_ratio": 0.97619,
      "vision_ratio": 0.02381
    },
    "middle": {
      "mdi": 55.400377,
      "aei_text": 2.753991,
      "aei_vision": 0.049711,
      "text_ratio": 0.98227,
      "vision_ratio": 0.01773
    },
    "late": {
      "mdi": 39.834062,
      "aei_text": 2.719724,
      "aei_vision": 0.068276,
      "text_ratio": 0.975511,
      "vision_ratio": 0.024489
    },
    "all": {
      "mdi": 39.834062,
      "aei_text": 2.73229,
      "aei_vision": 0.061468,
      "text_ratio": 0.975511,
      "vision_ratio": 0.024489
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975511,
      0.024489
    ],
    "text_vision_ratio": "0.975511:0.024489",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 159.0,
    "total_tokens": 377.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.247935,
      "aei_text": 2.282293,
      "aei_vision": 0.06475,
      "text_ratio": 0.972412,
      "vision_ratio": 0.027588
    },
    "middle": {
      "mdi": 25.036446,
      "aei_text": 2.247964,
      "aei_vision": 0.089788,
      "text_ratio": 0.961592,
      "vision_ratio": 0.038408
    },
    "late": {
      "mdi": 20.881738,
      "aei_text": 2.22498,
      "aei_vision": 0.106551,
      "text_ratio": 0.9543,
      "vision_ratio": 0.0457
    },
    "all": {
      "mdi": 20.881738,
      "aei_text": 2.251742,
      "aei_vision": 0.087032,
      "text_ratio": 0.9543,
      "vision_ratio": 0.0457
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9543,
      0.0457
    ],
    "text_vision_ratio": "0.954300:0.045700",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 159.0,
    "total_tokens": 377.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 36.379884,
      "aei_text": 2.284955,
      "aei_vision": 0.062808,
      "text_ratio": 0.973248,
      "vision_ratio": 0.026752
    },
    "middle": {
      "mdi": 27.937368,
      "aei_text": 2.260149,
      "aei_vision": 0.080901,
      "text_ratio": 0.965443,
      "vision_ratio": 0.034557
    },
    "late": {
      "mdi": 24.388604,
      "aei_text": 2.244868,
      "aei_vision": 0.092046,
      "text_ratio": 0.960612,
      "vision_ratio": 0.039388
    },
    "all": {
      "mdi": 24.388604,
      "aei_text": 2.263329,
      "aei_vision": 0.078581,
      "text_ratio": 0.960612,
      "vision_ratio": 0.039388
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.960612,
      0.039388
    ],
    "text_vision_ratio": "0.960612:0.039388",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 186.0,
    "text_tokens": 165.0,
    "total_tokens": 351.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 28.279711,
      "aei_text": 2.045727,
      "aei_vision": 0.072339,
      "text_ratio": 0.965847,
      "vision_ratio": 0.034153
    },
    "middle": {
      "mdi": 36.49089,
      "aei_text": 2.063526,
      "aei_vision": 0.056549,
      "text_ratio": 0.973327,
      "vision_ratio": 0.026673
    },
    "late": {
      "mdi": 37.381717,
      "aei_text": 2.065001,
      "aei_vision": 0.055241,
      "text_ratio": 0.973946,
      "vision_ratio": 0.026054
    },
    "all": {
      "mdi": 37.381717,
      "aei_text": 2.058083,
      "aei_vision": 0.061378,
      "text_ratio": 0.973946,
      "vision_ratio": 0.026054
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973946,
      0.026054
    ],
    "text_vision_ratio": "0.973946:0.026054",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 186.0,
    "text_tokens": 165.0,
    "total_tokens": 351.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 27.722493,
      "aei_text": 2.044152,
      "aei_vision": 0.073736,
      "text_ratio": 0.965184,
      "vision_ratio": 0.034816
    },
    "middle": {
      "mdi": 39.338843,
      "aei_text": 2.068013,
      "aei_vision": 0.052569,
      "text_ratio": 0.97521,
      "vision_ratio": 0.02479
    },
    "late": {
      "mdi": 61.903726,
      "aei_text": 2.089228,
      "aei_vision": 0.03375,
      "text_ratio": 0.984103,
      "vision_ratio": 0.015897
    },
    "all": {
      "mdi": 61.903726,
      "aei_text": 2.067131,
      "aei_vision": 0.053351,
      "text_ratio": 0.984103,
      "vision_ratio": 0.015897
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984103,
      0.015897
    ],
    "text_vision_ratio": "0.984103:0.015897",
    "skip_reason": null
  }
}
```


## === Rollout Step 19 ===
Step: 18/43 | 2025-10-22 18:41:03

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.757 | 46.015 | 41.876 | 41.876 |
| MDI Std | 13.307 | 22.190 | 20.197 | 20.197 |
| Vision Tokens | 336.0 ± 60.0 |
| Text Tokens | 164.6 ± 6.0 |
| Total Tokens | 500.6 ± 55.9 |
| Vision Ratio | 0.666 |
| Text Ratio | 0.334 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.504838,
      "aei_text": 2.695959,
      "aei_vision": 0.283641,
      "text_ratio": 0.904806,
      "vision_ratio": 0.095194
    },
    "middle": {
      "mdi": 6.146383,
      "aei_text": 2.431068,
      "aei_vision": 0.395528,
      "text_ratio": 0.860069,
      "vision_ratio": 0.139931
    },
    "late": {
      "mdi": 7.537053,
      "aei_text": 2.562546,
      "aei_vision": 0.339993,
      "text_ratio": 0.882864,
      "vision_ratio": 0.117136
    },
    "all": {
      "mdi": 7.537053,
      "aei_text": 2.563123,
      "aei_vision": 0.33975,
      "text_ratio": 0.882864,
      "vision_ratio": 0.117136
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.882864,
      0.117136
    ],
    "text_vision_ratio": "0.882864:0.117136",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.44866,
      "aei_text": 2.692766,
      "aei_vision": 0.284989,
      "text_ratio": 0.904294,
      "vision_ratio": 0.095706
    },
    "middle": {
      "mdi": 7.965919,
      "aei_text": 2.595953,
      "aei_vision": 0.325882,
      "text_ratio": 0.888467,
      "vision_ratio": 0.111533
    },
    "late": {
      "mdi": 10.942005,
      "aei_text": 2.768469,
      "aei_vision": 0.253013,
      "text_ratio": 0.916262,
      "vision_ratio": 0.083738
    },
    "all": {
      "mdi": 10.942005,
      "aei_text": 2.685759,
      "aei_vision": 0.287949,
      "text_ratio": 0.916262,
      "vision_ratio": 0.083738
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.916262,
      0.083738
    ],
    "text_vision_ratio": "0.916262:0.083738",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 167.0,
    "total_tokens": 422.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.69837,
      "aei_text": 2.431024,
      "aei_vision": 0.06282,
      "text_ratio": 0.97481,
      "vision_ratio": 0.02519
    },
    "middle": {
      "mdi": 27.467857,
      "aei_text": 2.39387,
      "aei_vision": 0.087152,
      "text_ratio": 0.964873,
      "vision_ratio": 0.035127
    },
    "late": {
      "mdi": 24.831789,
      "aei_text": 2.380562,
      "aei_vision": 0.095868,
      "text_ratio": 0.961288,
      "vision_ratio": 0.038712
    },
    "all": {
      "mdi": 24.831789,
      "aei_text": 2.401827,
      "aei_vision": 0.081941,
      "text_ratio": 0.961288,
      "vision_ratio": 0.038712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961288,
      0.038712
    ],
    "text_vision_ratio": "0.961288:0.038712",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 167.0,
    "total_tokens": 422.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.408567,
      "aei_text": 2.430328,
      "aei_vision": 0.063276,
      "text_ratio": 0.974625,
      "vision_ratio": 0.025375
    },
    "middle": {
      "mdi": 46.914751,
      "aei_text": 2.447293,
      "aei_vision": 0.052165,
      "text_ratio": 0.97913,
      "vision_ratio": 0.02087
    },
    "late": {
      "mdi": 41.894115,
      "aei_text": 2.438083,
      "aei_vision": 0.058196,
      "text_ratio": 0.976687,
      "vision_ratio": 0.023313
    },
    "all": {
      "mdi": 41.894115,
      "aei_text": 2.438568,
      "aei_vision": 0.057879,
      "text_ratio": 0.976687,
      "vision_ratio": 0.023313
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976687,
      0.023313
    ],
    "text_vision_ratio": "0.976687:0.023313",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.732798,
      "aei_text": 3.293583,
      "aei_vision": 0.066226,
      "text_ratio": 0.980289,
      "vision_ratio": 0.019711
    },
    "middle": {
      "mdi": 47.850628,
      "aei_text": 3.287497,
      "aei_vision": 0.068703,
      "text_ratio": 0.979529,
      "vision_ratio": 0.020471
    },
    "late": {
      "mdi": 44.80617,
      "aei_text": 3.276627,
      "aei_vision": 0.073129,
      "text_ratio": 0.978169,
      "vision_ratio": 0.021831
    },
    "all": {
      "mdi": 44.80617,
      "aei_text": 3.285902,
      "aei_vision": 0.069353,
      "text_ratio": 0.978169,
      "vision_ratio": 0.021831
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978169,
      0.021831
    ],
    "text_vision_ratio": "0.978169:0.021831",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.668865,
      "aei_text": 3.299402,
      "aei_vision": 0.063857,
      "text_ratio": 0.981013,
      "vision_ratio": 0.018987
    },
    "middle": {
      "mdi": 31.804697,
      "aei_text": 3.208463,
      "aei_vision": 0.10088,
      "text_ratio": 0.969517,
      "vision_ratio": 0.030483
    },
    "late": {
      "mdi": 28.048629,
      "aei_text": 3.177953,
      "aei_vision": 0.113302,
      "text_ratio": 0.965575,
      "vision_ratio": 0.034425
    },
    "all": {
      "mdi": 28.048629,
      "aei_text": 3.228609,
      "aei_vision": 0.092678,
      "text_ratio": 0.965575,
      "vision_ratio": 0.034425
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965575,
      0.034425
    ],
    "text_vision_ratio": "0.965575:0.034425",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 161.0,
    "total_tokens": 462.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.696754,
      "aei_text": 2.746423,
      "aei_vision": 0.065867,
      "text_ratio": 0.976579,
      "vision_ratio": 0.023421
    },
    "middle": {
      "mdi": 33.512778,
      "aei_text": 2.71794,
      "aei_vision": 0.081102,
      "text_ratio": 0.971025,
      "vision_ratio": 0.028975
    },
    "late": {
      "mdi": 30.419329,
      "aei_text": 2.703414,
      "aei_vision": 0.088872,
      "text_ratio": 0.968172,
      "vision_ratio": 0.031828
    },
    "all": {
      "mdi": 30.419329,
      "aei_text": 2.72259,
      "aei_vision": 0.078615,
      "text_ratio": 0.968172,
      "vision_ratio": 0.031828
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968172,
      0.031828
    ],
    "text_vision_ratio": "0.968172:0.031828",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 161.0,
    "total_tokens": 462.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.283641,
      "aei_text": 2.74806,
      "aei_vision": 0.064991,
      "text_ratio": 0.976897,
      "vision_ratio": 0.023103
    },
    "middle": {
      "mdi": 37.716165,
      "aei_text": 2.734041,
      "aei_vision": 0.07249,
      "text_ratio": 0.974171,
      "vision_ratio": 0.025829
    },
    "late": {
      "mdi": 31.579432,
      "aei_text": 2.709177,
      "aei_vision": 0.085789,
      "text_ratio": 0.969306,
      "vision_ratio": 0.030694
    },
    "all": {
      "mdi": 31.579432,
      "aei_text": 2.730425,
      "aei_vision": 0.074424,
      "text_ratio": 0.969306,
      "vision_ratio": 0.030694
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969306,
      0.030694
    ],
    "text_vision_ratio": "0.969306:0.030694",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 162.0,
    "total_tokens": 532.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.084672,
      "aei_text": 3.12561,
      "aei_vision": 0.069328,
      "text_ratio": 0.978301,
      "vision_ratio": 0.021699
    },
    "middle": {
      "mdi": 52.997599,
      "aei_text": 3.148275,
      "aei_vision": 0.059404,
      "text_ratio": 0.981481,
      "vision_ratio": 0.018519
    },
    "late": {
      "mdi": 51.641163,
      "aei_text": 3.144862,
      "aei_vision": 0.060898,
      "text_ratio": 0.981003,
      "vision_ratio": 0.018997
    },
    "all": {
      "mdi": 51.641163,
      "aei_text": 3.139583,
      "aei_vision": 0.063209,
      "text_ratio": 0.981003,
      "vision_ratio": 0.018997
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981003,
      0.018997
    ],
    "text_vision_ratio": "0.981003:0.018997",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 162.0,
    "total_tokens": 532.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.391584,
      "aei_text": 3.116065,
      "aei_vision": 0.073507,
      "text_ratio": 0.976954,
      "vision_ratio": 0.023046
    },
    "middle": {
      "mdi": 49.195371,
      "aei_text": 3.138254,
      "aei_vision": 0.063792,
      "text_ratio": 0.980078,
      "vision_ratio": 0.019922
    },
    "late": {
      "mdi": 54.402813,
      "aei_text": 3.151638,
      "aei_vision": 0.057932,
      "text_ratio": 0.98195,
      "vision_ratio": 0.01805
    },
    "all": {
      "mdi": 54.402813,
      "aei_text": 3.135322,
      "aei_vision": 0.065075,
      "text_ratio": 0.98195,
      "vision_ratio": 0.01805
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98195,
      0.01805
    ],
    "text_vision_ratio": "0.981950:0.018050",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.55376,
      "aei_text": 3.317102,
      "aei_vision": 0.056651,
      "text_ratio": 0.983208,
      "vision_ratio": 0.016792
    },
    "middle": {
      "mdi": 100.967778,
      "aei_text": 3.374166,
      "aei_vision": 0.033418,
      "text_ratio": 0.990193,
      "vision_ratio": 0.009807
    },
    "late": {
      "mdi": 95.719045,
      "aei_text": 3.369778,
      "aei_vision": 0.035205,
      "text_ratio": 0.989661,
      "vision_ratio": 0.010339
    },
    "all": {
      "mdi": 95.719045,
      "aei_text": 3.353678,
      "aei_vision": 0.04176,
      "text_ratio": 0.989661,
      "vision_ratio": 0.010339
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989661,
      0.010339
    ],
    "text_vision_ratio": "0.989661:0.010339",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.509834,
      "aei_text": 3.304561,
      "aei_vision": 0.061756,
      "text_ratio": 0.981655,
      "vision_ratio": 0.018345
    },
    "middle": {
      "mdi": 47.114651,
      "aei_text": 3.284992,
      "aei_vision": 0.069723,
      "text_ratio": 0.979216,
      "vision_ratio": 0.020784
    },
    "late": {
      "mdi": 44.812809,
      "aei_text": 3.276652,
      "aei_vision": 0.073119,
      "text_ratio": 0.978172,
      "vision_ratio": 0.021828
    },
    "all": {
      "mdi": 44.812809,
      "aei_text": 3.288732,
      "aei_vision": 0.068201,
      "text_ratio": 0.978172,
      "vision_ratio": 0.021828
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978172,
      0.021828
    ],
    "text_vision_ratio": "0.978172:0.021828",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 179.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.561319,
      "aei_text": 2.250327,
      "aei_vision": 0.051659,
      "text_ratio": 0.977559,
      "vision_ratio": 0.022441
    },
    "middle": {
      "mdi": 59.293441,
      "aei_text": 2.268005,
      "aei_vision": 0.038251,
      "text_ratio": 0.983414,
      "vision_ratio": 0.016586
    },
    "late": {
      "mdi": 50.087445,
      "aei_text": 2.258974,
      "aei_vision": 0.045101,
      "text_ratio": 0.980426,
      "vision_ratio": 0.019574
    },
    "all": {
      "mdi": 50.087445,
      "aei_text": 2.259105,
      "aei_vision": 0.045001,
      "text_ratio": 0.980426,
      "vision_ratio": 0.019574
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980426,
      0.019574
    ],
    "text_vision_ratio": "0.980426:0.019574",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 179.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.214585,
      "aei_text": 2.251304,
      "aei_vision": 0.050918,
      "text_ratio": 0.977883,
      "vision_ratio": 0.022117
    },
    "middle": {
      "mdi": 63.085014,
      "aei_text": 2.270974,
      "aei_vision": 0.035999,
      "text_ratio": 0.984396,
      "vision_ratio": 0.015604
    },
    "late": {
      "mdi": 61.348589,
      "aei_text": 2.269659,
      "aei_vision": 0.036996,
      "text_ratio": 0.983961,
      "vision_ratio": 0.016039
    },
    "all": {
      "mdi": 61.348589,
      "aei_text": 2.263983,
      "aei_vision": 0.041301,
      "text_ratio": 0.983961,
      "vision_ratio": 0.016039
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983961,
      0.016039
    ],
    "text_vision_ratio": "0.983961:0.016039",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.611423,
      "aei_text": 3.011935,
      "aei_vision": 0.060711,
      "text_ratio": 0.980242,
      "vision_ratio": 0.019758
    },
    "middle": {
      "mdi": 61.51207,
      "aei_text": 3.036247,
      "aei_vision": 0.04936,
      "text_ratio": 0.984003,
      "vision_ratio": 0.015997
    },
    "late": {
      "mdi": 49.334291,
      "aei_text": 3.011235,
      "aei_vision": 0.061037,
      "text_ratio": 0.980133,
      "vision_ratio": 0.019867
    },
    "all": {
      "mdi": 49.334291,
      "aei_text": 3.019804,
      "aei_vision": 0.057037,
      "text_ratio": 0.980133,
      "vision_ratio": 0.019867
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980133,
      0.019867
    ],
    "text_vision_ratio": "0.980133:0.019867",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.743295,
      "aei_text": 3.012265,
      "aei_vision": 0.060556,
      "text_ratio": 0.980293,
      "vision_ratio": 0.019707
    },
    "middle": {
      "mdi": 62.689249,
      "aei_text": 3.038167,
      "aei_vision": 0.048464,
      "text_ratio": 0.984299,
      "vision_ratio": 0.015701
    },
    "late": {
      "mdi": 42.611102,
      "aei_text": 2.991594,
      "aei_vision": 0.070207,
      "text_ratio": 0.97707,
      "vision_ratio": 0.02293
    },
    "all": {
      "mdi": 42.611102,
      "aei_text": 3.01401,
      "aei_vision": 0.059742,
      "text_ratio": 0.97707,
      "vision_ratio": 0.02293
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97707,
      0.02293
    ],
    "text_vision_ratio": "0.977070:0.022930",
    "skip_reason": null
  }
}
```


## === Rollout Step 20 ===
Step: 19/43 | 2025-10-22 18:42:22

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 40.860 | 47.131 | 39.838 | 39.838 |
| MDI Std | 13.557 | 26.502 | 19.736 | 19.736 |
| Vision Tokens | 356.5 ± 111.2 |
| Text Tokens | 166.0 ± 3.6 |
| Total Tokens | 522.5 ± 113.9 |
| Vision Ratio | 0.660 |
| Text Ratio | 0.340 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 171.0,
    "total_tokens": 541.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.887592,
      "aei_text": 3.011793,
      "aei_vision": 0.070225,
      "text_ratio": 0.977215,
      "vision_ratio": 0.022785
    },
    "middle": {
      "mdi": 35.907631,
      "aei_text": 2.983935,
      "aei_vision": 0.0831,
      "text_ratio": 0.972905,
      "vision_ratio": 0.027095
    },
    "late": {
      "mdi": 42.222908,
      "aei_text": 3.009518,
      "aei_vision": 0.071277,
      "text_ratio": 0.976864,
      "vision_ratio": 0.023136
    },
    "all": {
      "mdi": 42.222908,
      "aei_text": 3.001749,
      "aei_vision": 0.074867,
      "text_ratio": 0.976864,
      "vision_ratio": 0.023136
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976864,
      0.023136
    ],
    "text_vision_ratio": "0.976864:0.023136",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 171.0,
    "total_tokens": 541.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.338247,
      "aei_text": 3.009918,
      "aei_vision": 0.071092,
      "text_ratio": 0.976926,
      "vision_ratio": 0.023074
    },
    "middle": {
      "mdi": 48.697195,
      "aei_text": 3.02915,
      "aei_vision": 0.062204,
      "text_ratio": 0.979878,
      "vision_ratio": 0.020122
    },
    "late": {
      "mdi": 41.080188,
      "aei_text": 3.005442,
      "aei_vision": 0.07316,
      "text_ratio": 0.976236,
      "vision_ratio": 0.023764
    },
    "all": {
      "mdi": 41.080188,
      "aei_text": 3.014839,
      "aei_vision": 0.068818,
      "text_ratio": 0.976236,
      "vision_ratio": 0.023764
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976236,
      0.023764
    ],
    "text_vision_ratio": "0.976236:0.023764",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 167.0,
    "total_tokens": 698.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.951354,
      "aei_text": 3.484969,
      "aei_vision": 0.218475,
      "text_ratio": 0.941008,
      "vision_ratio": 0.058992
    },
    "middle": {
      "mdi": 10.076982,
      "aei_text": 3.177141,
      "aei_vision": 0.315287,
      "text_ratio": 0.909723,
      "vision_ratio": 0.090277
    },
    "late": {
      "mdi": 10.867548,
      "aei_text": 3.233561,
      "aei_vision": 0.297543,
      "text_ratio": 0.915737,
      "vision_ratio": 0.084263
    },
    "all": {
      "mdi": 10.867548,
      "aei_text": 3.298516,
      "aei_vision": 0.277115,
      "text_ratio": 0.915737,
      "vision_ratio": 0.084263
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.915737,
      0.084263
    ],
    "text_vision_ratio": "0.915737:0.084263",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 167.0,
    "total_tokens": 698.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.603524,
      "aei_text": 3.540193,
      "aei_vision": 0.201107,
      "text_ratio": 0.946247,
      "vision_ratio": 0.053753
    },
    "middle": {
      "mdi": 11.98499,
      "aei_text": 3.303275,
      "aei_vision": 0.275618,
      "text_ratio": 0.922988,
      "vision_ratio": 0.077012
    },
    "late": {
      "mdi": 13.572672,
      "aei_text": 3.386332,
      "aei_vision": 0.249496,
      "text_ratio": 0.931378,
      "vision_ratio": 0.068622
    },
    "all": {
      "mdi": 13.572672,
      "aei_text": 3.409926,
      "aei_vision": 0.242076,
      "text_ratio": 0.931378,
      "vision_ratio": 0.068622
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931378,
      0.068622
    ],
    "text_vision_ratio": "0.931378:0.068622",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.775501,
      "aei_text": 2.973587,
      "aei_vision": 0.072926,
      "text_ratio": 0.976063,
      "vision_ratio": 0.023937
    },
    "middle": {
      "mdi": 57.700943,
      "aei_text": 3.017506,
      "aei_vision": 0.052296,
      "text_ratio": 0.982964,
      "vision_ratio": 0.017036
    },
    "late": {
      "mdi": 53.193182,
      "aei_text": 3.008434,
      "aei_vision": 0.056557,
      "text_ratio": 0.981547,
      "vision_ratio": 0.018453
    },
    "all": {
      "mdi": 53.193182,
      "aei_text": 2.99984,
      "aei_vision": 0.060594,
      "text_ratio": 0.981547,
      "vision_ratio": 0.018453
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981547,
      0.018453
    ],
    "text_vision_ratio": "0.981547:0.018453",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.247568,
      "aei_text": 2.991148,
      "aei_vision": 0.064677,
      "text_ratio": 0.978835,
      "vision_ratio": 0.021165
    },
    "middle": {
      "mdi": 42.137454,
      "aei_text": 2.978364,
      "aei_vision": 0.070682,
      "text_ratio": 0.976818,
      "vision_ratio": 0.023182
    },
    "late": {
      "mdi": 36.530845,
      "aei_text": 2.956542,
      "aei_vision": 0.080933,
      "text_ratio": 0.973355,
      "vision_ratio": 0.026645
    },
    "all": {
      "mdi": 36.530845,
      "aei_text": 2.975352,
      "aei_vision": 0.072097,
      "text_ratio": 0.973355,
      "vision_ratio": 0.026645
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973355,
      0.026645
    ],
    "text_vision_ratio": "0.973355:0.026645",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 101.0,
    "text_tokens": 158.0,
    "total_tokens": 259.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.324232,
      "aei_text": 1.595513,
      "aei_vision": 0.068406,
      "text_ratio": 0.958889,
      "vision_ratio": 0.041111
    },
    "middle": {
      "mdi": 13.850063,
      "aei_text": 1.56692,
      "aei_vision": 0.113135,
      "text_ratio": 0.93266,
      "vision_ratio": 0.06734
    },
    "late": {
      "mdi": 13.217944,
      "aei_text": 1.563621,
      "aei_vision": 0.118295,
      "text_ratio": 0.929666,
      "vision_ratio": 0.070334
    },
    "all": {
      "mdi": 13.217944,
      "aei_text": 1.575344,
      "aei_vision": 0.099956,
      "text_ratio": 0.929666,
      "vision_ratio": 0.070334
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.929666,
      0.070334
    ],
    "text_vision_ratio": "0.929666:0.070334",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 101.0,
    "text_tokens": 158.0,
    "total_tokens": 259.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 22.603231,
      "aei_text": 1.594156,
      "aei_vision": 0.070528,
      "text_ratio": 0.957633,
      "vision_ratio": 0.042367
    },
    "middle": {
      "mdi": 12.575825,
      "aei_text": 1.559947,
      "aei_vision": 0.124043,
      "text_ratio": 0.92634,
      "vision_ratio": 0.07366
    },
    "late": {
      "mdi": 11.287244,
      "aei_text": 1.55138,
      "aei_vision": 0.137445,
      "text_ratio": 0.918615,
      "vision_ratio": 0.081385
    },
    "all": {
      "mdi": 11.287244,
      "aei_text": 1.568492,
      "aei_vision": 0.110676,
      "text_ratio": 0.918615,
      "vision_ratio": 0.081385
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.918615,
      0.081385
    ],
    "text_vision_ratio": "0.918615:0.081385",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.508647,
      "aei_text": 3.209454,
      "aei_vision": 0.061122,
      "text_ratio": 0.981311,
      "vision_ratio": 0.018689
    },
    "middle": {
      "mdi": 74.266953,
      "aei_text": 3.250301,
      "aei_vision": 0.043765,
      "text_ratio": 0.986714,
      "vision_ratio": 0.013286
    },
    "late": {
      "mdi": 60.236122,
      "aei_text": 3.227213,
      "aei_vision": 0.053576,
      "text_ratio": 0.98367,
      "vision_ratio": 0.01633
    },
    "all": {
      "mdi": 60.236122,
      "aei_text": 3.22899,
      "aei_vision": 0.052821,
      "text_ratio": 0.98367,
      "vision_ratio": 0.01633
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98367,
      0.01633
    ],
    "text_vision_ratio": "0.983670:0.016330",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.664534,
      "aei_text": 3.22807,
      "aei_vision": 0.053212,
      "text_ratio": 0.983783,
      "vision_ratio": 0.016217
    },
    "middle": {
      "mdi": 51.415646,
      "aei_text": 3.206531,
      "aei_vision": 0.062365,
      "text_ratio": 0.980922,
      "vision_ratio": 0.019078
    },
    "late": {
      "mdi": 47.637849,
      "aei_text": 3.19544,
      "aei_vision": 0.067078,
      "text_ratio": 0.97944,
      "vision_ratio": 0.02056
    },
    "all": {
      "mdi": 47.637849,
      "aei_text": 3.210013,
      "aei_vision": 0.060885,
      "text_ratio": 0.97944,
      "vision_ratio": 0.02056
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97944,
      0.02056
    ],
    "text_vision_ratio": "0.979440:0.020560",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.989177,
      "aei_text": 2.941968,
      "aei_vision": 0.065393,
      "text_ratio": 0.978256,
      "vision_ratio": 0.021744
    },
    "middle": {
      "mdi": 56.205956,
      "aei_text": 2.968118,
      "aei_vision": 0.052808,
      "text_ratio": 0.982519,
      "vision_ratio": 0.017481
    },
    "late": {
      "mdi": 45.371436,
      "aei_text": 2.943063,
      "aei_vision": 0.064866,
      "text_ratio": 0.978435,
      "vision_ratio": 0.021565
    },
    "all": {
      "mdi": 45.371436,
      "aei_text": 2.951052,
      "aei_vision": 0.061021,
      "text_ratio": 0.978435,
      "vision_ratio": 0.021565
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978435,
      0.021565
    ],
    "text_vision_ratio": "0.978435:0.021565",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.547248,
      "aei_text": 2.934533,
      "aei_vision": 0.068971,
      "text_ratio": 0.977036,
      "vision_ratio": 0.022964
    },
    "middle": {
      "mdi": 82.912327,
      "aei_text": 3.002597,
      "aei_vision": 0.036214,
      "text_ratio": 0.988083,
      "vision_ratio": 0.011917
    },
    "late": {
      "mdi": 62.843026,
      "aei_text": 2.979335,
      "aei_vision": 0.047409,
      "text_ratio": 0.984337,
      "vision_ratio": 0.015663
    },
    "all": {
      "mdi": 62.843026,
      "aei_text": 2.972158,
      "aei_vision": 0.050863,
      "text_ratio": 0.984337,
      "vision_ratio": 0.015663
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984337,
      0.015663
    ],
    "text_vision_ratio": "0.984337:0.015663",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 168.0,
    "total_tokens": 538.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.819471,
      "aei_text": 3.049131,
      "aei_vision": 0.069584,
      "text_ratio": 0.977688,
      "vision_ratio": 0.022312
    },
    "middle": {
      "mdi": 72.340769,
      "aei_text": 3.107766,
      "aei_vision": 0.04296,
      "text_ratio": 0.986365,
      "vision_ratio": 0.013635
    },
    "late": {
      "mdi": 56.07619,
      "aei_text": 3.081361,
      "aei_vision": 0.05495,
      "text_ratio": 0.98248,
      "vision_ratio": 0.01752
    },
    "all": {
      "mdi": 56.07619,
      "aei_text": 3.079402,
      "aei_vision": 0.055839,
      "text_ratio": 0.98248,
      "vision_ratio": 0.01752
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98248,
      0.01752
    ],
    "text_vision_ratio": "0.982480:0.017520",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 168.0,
    "total_tokens": 538.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.983381,
      "aei_text": 3.046295,
      "aei_vision": 0.070871,
      "text_ratio": 0.977264,
      "vision_ratio": 0.022736
    },
    "middle": {
      "mdi": 41.762604,
      "aei_text": 3.041961,
      "aei_vision": 0.072839,
      "text_ratio": 0.976615,
      "vision_ratio": 0.023385
    },
    "late": {
      "mdi": 33.599114,
      "aei_text": 3.005382,
      "aei_vision": 0.089448,
      "text_ratio": 0.971098,
      "vision_ratio": 0.028902
    },
    "all": {
      "mdi": 33.599114,
      "aei_text": 3.031212,
      "aei_vision": 0.07772,
      "text_ratio": 0.971098,
      "vision_ratio": 0.028902
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971098,
      0.028902
    ],
    "text_vision_ratio": "0.971098:0.028902",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.696107,
      "aei_text": 3.224033,
      "aei_vision": 0.054928,
      "text_ratio": 0.983248,
      "vision_ratio": 0.016752
    },
    "middle": {
      "mdi": 38.499497,
      "aei_text": 3.16013,
      "aei_vision": 0.082082,
      "text_ratio": 0.974683,
      "vision_ratio": 0.025317
    },
    "late": {
      "mdi": 30.404792,
      "aei_text": 3.112398,
      "aei_vision": 0.102365,
      "text_ratio": 0.968158,
      "vision_ratio": 0.031842
    },
    "all": {
      "mdi": 30.404792,
      "aei_text": 3.165519,
      "aei_vision": 0.079792,
      "text_ratio": 0.968158,
      "vision_ratio": 0.031842
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968158,
      0.031842
    ],
    "text_vision_ratio": "0.968158:0.031842",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.821908,
      "aei_text": 3.217647,
      "aei_vision": 0.057641,
      "text_ratio": 0.982401,
      "vision_ratio": 0.017599
    },
    "middle": {
      "mdi": 103.757172,
      "aei_text": 3.278925,
      "aei_vision": 0.031602,
      "text_ratio": 0.990454,
      "vision_ratio": 0.009546
    },
    "late": {
      "mdi": 79.266023,
      "aei_text": 3.256609,
      "aei_vision": 0.041085,
      "text_ratio": 0.987541,
      "vision_ratio": 0.012459
    },
    "all": {
      "mdi": 79.266023,
      "aei_text": 3.251067,
      "aei_vision": 0.04344,
      "text_ratio": 0.987541,
      "vision_ratio": 0.012459
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987541,
      0.012459
    ],
    "text_vision_ratio": "0.987541:0.012459",
    "skip_reason": null
  }
}
```


## === Rollout Step 21 ===
Step: 20/43 | 2025-10-22 18:43:40

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 47.948 | 58.890 | 49.770 | 49.770 |
| MDI Std | 13.770 | 22.192 | 14.923 | 14.923 |
| Vision Tokens | 372.9 ± 26.8 |
| Text Tokens | 165.5 ± 3.2 |
| Total Tokens | 538.4 ± 25.9 |
| Vision Ratio | 0.692 |
| Text Ratio | 0.308 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 161.0,
    "total_tokens": 577.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.508082,
      "aei_text": 3.042067,
      "aei_vision": 0.209681,
      "text_ratio": 0.935517,
      "vision_ratio": 0.064483
    },
    "middle": {
      "mdi": 16.554164,
      "aei_text": 3.09999,
      "aei_vision": 0.187263,
      "text_ratio": 0.943033,
      "vision_ratio": 0.056967
    },
    "late": {
      "mdi": 22.07789,
      "aei_text": 3.208365,
      "aei_vision": 0.14532,
      "text_ratio": 0.956668,
      "vision_ratio": 0.043332
    },
    "all": {
      "mdi": 22.07789,
      "aei_text": 3.116778,
      "aei_vision": 0.180766,
      "text_ratio": 0.956668,
      "vision_ratio": 0.043332
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956668,
      0.043332
    ],
    "text_vision_ratio": "0.956668:0.043332",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 161.0,
    "total_tokens": 577.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.511522,
      "aei_text": 3.042176,
      "aei_vision": 0.209639,
      "text_ratio": 0.935532,
      "vision_ratio": 0.064468
    },
    "middle": {
      "mdi": 18.811344,
      "aei_text": 3.151037,
      "aei_vision": 0.167507,
      "text_ratio": 0.949524,
      "vision_ratio": 0.050476
    },
    "late": {
      "mdi": 33.622226,
      "aei_text": 3.328089,
      "aei_vision": 0.098985,
      "text_ratio": 0.971117,
      "vision_ratio": 0.028883
    },
    "all": {
      "mdi": 33.622226,
      "aei_text": 3.173832,
      "aei_vision": 0.158685,
      "text_ratio": 0.971117,
      "vision_ratio": 0.028883
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971117,
      0.028883
    ],
    "text_vision_ratio": "0.971117:0.028883",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.763741,
      "aei_text": 2.970408,
      "aei_vision": 0.057384,
      "text_ratio": 0.981048,
      "vision_ratio": 0.018952
    },
    "middle": {
      "mdi": 55.101461,
      "aei_text": 2.977409,
      "aei_vision": 0.054035,
      "text_ratio": 0.982175,
      "vision_ratio": 0.017825
    },
    "late": {
      "mdi": 46.467024,
      "aei_text": 2.957324,
      "aei_vision": 0.063643,
      "text_ratio": 0.978933,
      "vision_ratio": 0.021067
    },
    "all": {
      "mdi": 46.467024,
      "aei_text": 2.968381,
      "aei_vision": 0.058354,
      "text_ratio": 0.978933,
      "vision_ratio": 0.021067
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978933,
      0.021067
    ],
    "text_vision_ratio": "0.978933:0.021067",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.394832,
      "aei_text": 2.971798,
      "aei_vision": 0.056719,
      "text_ratio": 0.981272,
      "vision_ratio": 0.018728
    },
    "middle": {
      "mdi": 51.556221,
      "aei_text": 2.969944,
      "aei_vision": 0.057606,
      "text_ratio": 0.980973,
      "vision_ratio": 0.019027
    },
    "late": {
      "mdi": 44.701428,
      "aei_text": 2.952304,
      "aei_vision": 0.066045,
      "text_ratio": 0.978119,
      "vision_ratio": 0.021881
    },
    "all": {
      "mdi": 44.701428,
      "aei_text": 2.964681,
      "aei_vision": 0.060124,
      "text_ratio": 0.978119,
      "vision_ratio": 0.021881
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978119,
      0.021881
    ],
    "text_vision_ratio": "0.978119:0.021881",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.608131,
      "aei_text": 2.905401,
      "aei_vision": 0.061027,
      "text_ratio": 0.979427,
      "vision_ratio": 0.020573
    },
    "middle": {
      "mdi": 51.225195,
      "aei_text": 2.913812,
      "aei_vision": 0.056882,
      "text_ratio": 0.980852,
      "vision_ratio": 0.019148
    },
    "late": {
      "mdi": 41.013483,
      "aei_text": 2.886427,
      "aei_vision": 0.070378,
      "text_ratio": 0.976198,
      "vision_ratio": 0.023802
    },
    "all": {
      "mdi": 41.013483,
      "aei_text": 2.901878,
      "aei_vision": 0.062763,
      "text_ratio": 0.976198,
      "vision_ratio": 0.023802
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976198,
      0.023802
    ],
    "text_vision_ratio": "0.976198:0.023802",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.607328,
      "aei_text": 2.910195,
      "aei_vision": 0.058665,
      "text_ratio": 0.98024,
      "vision_ratio": 0.01976
    },
    "middle": {
      "mdi": 64.092913,
      "aei_text": 2.936275,
      "aei_vision": 0.045813,
      "text_ratio": 0.984637,
      "vision_ratio": 0.015363
    },
    "late": {
      "mdi": 57.582075,
      "aei_text": 2.926121,
      "aei_vision": 0.050817,
      "text_ratio": 0.98293,
      "vision_ratio": 0.01707
    },
    "all": {
      "mdi": 57.582075,
      "aei_text": 2.924195,
      "aei_vision": 0.051766,
      "text_ratio": 0.98293,
      "vision_ratio": 0.01707
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98293,
      0.01707
    ],
    "text_vision_ratio": "0.982930:0.017070",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 61.935199,
      "aei_text": 3.269828,
      "aei_vision": 0.052794,
      "text_ratio": 0.984111,
      "vision_ratio": 0.015889
    },
    "middle": {
      "mdi": 93.501626,
      "aei_text": 3.311472,
      "aei_vision": 0.035416,
      "text_ratio": 0.989418,
      "vision_ratio": 0.010582
    },
    "late": {
      "mdi": 71.461397,
      "aei_text": 3.286146,
      "aei_vision": 0.045985,
      "text_ratio": 0.9862,
      "vision_ratio": 0.0138
    },
    "all": {
      "mdi": 71.461397,
      "aei_text": 3.289151,
      "aei_vision": 0.044731,
      "text_ratio": 0.9862,
      "vision_ratio": 0.0138
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9862,
      0.0138
    ],
    "text_vision_ratio": "0.986200:0.013800",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.760204,
      "aei_text": 3.267474,
      "aei_vision": 0.053777,
      "text_ratio": 0.983808,
      "vision_ratio": 0.016192
    },
    "middle": {
      "mdi": 73.626543,
      "aei_text": 3.289284,
      "aei_vision": 0.044675,
      "text_ratio": 0.9866,
      "vision_ratio": 0.0134
    },
    "late": {
      "mdi": 63.436521,
      "aei_text": 3.272713,
      "aei_vision": 0.05159,
      "text_ratio": 0.984481,
      "vision_ratio": 0.015519
    },
    "all": {
      "mdi": 63.436521,
      "aei_text": 3.276489,
      "aei_vision": 0.050015,
      "text_ratio": 0.984481,
      "vision_ratio": 0.015519
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984481,
      0.015519
    ],
    "text_vision_ratio": "0.984481:0.015519",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.192415,
      "aei_text": 3.266305,
      "aei_vision": 0.054264,
      "text_ratio": 0.983658,
      "vision_ratio": 0.016342
    },
    "middle": {
      "mdi": 65.170563,
      "aei_text": 3.275886,
      "aei_vision": 0.050266,
      "text_ratio": 0.984888,
      "vision_ratio": 0.015112
    },
    "late": {
      "mdi": 50.340937,
      "aei_text": 3.242014,
      "aei_vision": 0.064401,
      "text_ratio": 0.980522,
      "vision_ratio": 0.019478
    },
    "all": {
      "mdi": 50.340937,
      "aei_text": 3.261405,
      "aei_vision": 0.056309,
      "text_ratio": 0.980522,
      "vision_ratio": 0.019478
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980522,
      0.019478
    ],
    "text_vision_ratio": "0.980522:0.019478",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.991496,
      "aei_text": 3.263762,
      "aei_vision": 0.055326,
      "text_ratio": 0.983331,
      "vision_ratio": 0.016669
    },
    "middle": {
      "mdi": 51.191981,
      "aei_text": 3.244465,
      "aei_vision": 0.063378,
      "text_ratio": 0.98084,
      "vision_ratio": 0.01916
    },
    "late": {
      "mdi": 36.144588,
      "aei_text": 3.185169,
      "aei_vision": 0.088123,
      "text_ratio": 0.973078,
      "vision_ratio": 0.026922
    },
    "all": {
      "mdi": 36.144588,
      "aei_text": 3.231128,
      "aei_vision": 0.068944,
      "text_ratio": 0.973078,
      "vision_ratio": 0.026922
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973078,
      0.026922
    ],
    "text_vision_ratio": "0.973078:0.026922",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.219939,
      "aei_text": 2.980648,
      "aei_vision": 0.058193,
      "text_ratio": 0.98085,
      "vision_ratio": 0.01915
    },
    "middle": {
      "mdi": 86.91555,
      "aei_text": 3.029722,
      "aei_vision": 0.034858,
      "text_ratio": 0.988625,
      "vision_ratio": 0.011375
    },
    "late": {
      "mdi": 74.587892,
      "aei_text": 3.017939,
      "aei_vision": 0.040462,
      "text_ratio": 0.98677,
      "vision_ratio": 0.01323
    },
    "all": {
      "mdi": 74.587892,
      "aei_text": 3.009434,
      "aei_vision": 0.044505,
      "text_ratio": 0.98677,
      "vision_ratio": 0.01323
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98677,
      0.01323
    ],
    "text_vision_ratio": "0.986770:0.013230",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.147959,
      "aei_text": 2.980483,
      "aei_vision": 0.058272,
      "text_ratio": 0.980824,
      "vision_ratio": 0.019176
    },
    "middle": {
      "mdi": 86.95496,
      "aei_text": 3.029755,
      "aei_vision": 0.034843,
      "text_ratio": 0.988631,
      "vision_ratio": 0.011369
    },
    "late": {
      "mdi": 60.76977,
      "aei_text": 2.999237,
      "aei_vision": 0.049354,
      "text_ratio": 0.983811,
      "vision_ratio": 0.016189
    },
    "all": {
      "mdi": 60.76977,
      "aei_text": 3.003158,
      "aei_vision": 0.04749,
      "text_ratio": 0.983811,
      "vision_ratio": 0.016189
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983811,
      0.016189
    ],
    "text_vision_ratio": "0.983811:0.016189",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 170.0,
    "total_tokens": 563.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.451497,
      "aei_text": 3.17447,
      "aei_vision": 0.05939,
      "text_ratio": 0.981635,
      "vision_ratio": 0.018365
    },
    "middle": {
      "mdi": 77.61851,
      "aei_text": 3.215981,
      "aei_vision": 0.041433,
      "text_ratio": 0.98728,
      "vision_ratio": 0.01272
    },
    "late": {
      "mdi": 67.566545,
      "aei_text": 3.202203,
      "aei_vision": 0.047393,
      "text_ratio": 0.985416,
      "vision_ratio": 0.014584
    },
    "all": {
      "mdi": 67.566545,
      "aei_text": 3.197556,
      "aei_vision": 0.049403,
      "text_ratio": 0.985416,
      "vision_ratio": 0.014584
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985416,
      0.014584
    ],
    "text_vision_ratio": "0.985416:0.014584",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 170.0,
    "total_tokens": 563.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.07047,
      "aei_text": 3.173525,
      "aei_vision": 0.059798,
      "text_ratio": 0.981506,
      "vision_ratio": 0.018494
    },
    "middle": {
      "mdi": 69.317826,
      "aei_text": 3.204881,
      "aei_vision": 0.046235,
      "text_ratio": 0.985779,
      "vision_ratio": 0.014221
    },
    "late": {
      "mdi": 50.33912,
      "aei_text": 3.166354,
      "aei_vision": 0.0629,
      "text_ratio": 0.980522,
      "vision_ratio": 0.019478
    },
    "all": {
      "mdi": 50.33912,
      "aei_text": 3.181589,
      "aei_vision": 0.05631,
      "text_ratio": 0.980522,
      "vision_ratio": 0.019478
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980522,
      0.019478
    ],
    "text_vision_ratio": "0.980522:0.019478",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.092264,
      "aei_text": 2.984728,
      "aei_vision": 0.067693,
      "text_ratio": 0.977823,
      "vision_ratio": 0.022177
    },
    "middle": {
      "mdi": 33.594436,
      "aei_text": 2.94238,
      "aei_vision": 0.087585,
      "text_ratio": 0.971094,
      "vision_ratio": 0.028906
    },
    "late": {
      "mdi": 28.314864,
      "aei_text": 2.910045,
      "aei_vision": 0.102774,
      "text_ratio": 0.965888,
      "vision_ratio": 0.034112
    },
    "all": {
      "mdi": 28.314864,
      "aei_text": 2.945722,
      "aei_vision": 0.086015,
      "text_ratio": 0.965888,
      "vision_ratio": 0.034112
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965888,
      0.034112
    ],
    "text_vision_ratio": "0.965888:0.034112",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.908377,
      "aei_text": 2.977581,
      "aei_vision": 0.07105,
      "text_ratio": 0.976695,
      "vision_ratio": 0.023305
    },
    "middle": {
      "mdi": 47.013805,
      "aei_text": 2.993295,
      "aei_vision": 0.063668,
      "text_ratio": 0.979173,
      "vision_ratio": 0.020827
    },
    "late": {
      "mdi": 47.888558,
      "aei_text": 2.995665,
      "aei_vision": 0.062555,
      "text_ratio": 0.979545,
      "vision_ratio": 0.020455
    },
    "all": {
      "mdi": 47.888558,
      "aei_text": 2.988849,
      "aei_vision": 0.065757,
      "text_ratio": 0.979545,
      "vision_ratio": 0.020455
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979545,
      0.020455
    ],
    "text_vision_ratio": "0.979545:0.020455",
    "skip_reason": null
  }
}
```


## === Rollout Step 22 ===
Step: 21/43 | 2025-10-22 18:44:57

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.148 | 58.324 | 49.608 | 49.608 |
| MDI Std | 13.013 | 25.543 | 19.050 | 19.050 |
| Vision Tokens | 365.4 ± 57.7 |
| Text Tokens | 166.8 ± 3.9 |
| Total Tokens | 532.1 ± 59.4 |
| Vision Ratio | 0.682 |
| Text Ratio | 0.318 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.017683,
      "aei_text": 3.24677,
      "aei_vision": 0.062417,
      "text_ratio": 0.981138,
      "vision_ratio": 0.018862
    },
    "middle": {
      "mdi": 71.198702,
      "aei_text": 3.285753,
      "aei_vision": 0.046149,
      "text_ratio": 0.986149,
      "vision_ratio": 0.013851
    },
    "late": {
      "mdi": 50.826348,
      "aei_text": 3.243422,
      "aei_vision": 0.063814,
      "text_ratio": 0.980705,
      "vision_ratio": 0.019295
    },
    "all": {
      "mdi": 50.826348,
      "aei_text": 3.258649,
      "aei_vision": 0.05746,
      "text_ratio": 0.980705,
      "vision_ratio": 0.019295
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980705,
      0.019295
    ],
    "text_vision_ratio": "0.980705:0.019295",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.4616,
      "aei_text": 3.24798,
      "aei_vision": 0.061912,
      "text_ratio": 0.981295,
      "vision_ratio": 0.018705
    },
    "middle": {
      "mdi": 40.039215,
      "aei_text": 3.20455,
      "aei_vision": 0.080035,
      "text_ratio": 0.975633,
      "vision_ratio": 0.024367
    },
    "late": {
      "mdi": 26.969117,
      "aei_text": 3.119186,
      "aei_vision": 0.115658,
      "text_ratio": 0.964246,
      "vision_ratio": 0.035754
    },
    "all": {
      "mdi": 26.969117,
      "aei_text": 3.190571,
      "aei_vision": 0.085869,
      "text_ratio": 0.964246,
      "vision_ratio": 0.035754
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964246,
      0.035754
    ],
    "text_vision_ratio": "0.964246:0.035754",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.841675,
      "aei_text": 3.231047,
      "aei_vision": 0.068978,
      "text_ratio": 0.979098,
      "vision_ratio": 0.020902
    },
    "middle": {
      "mdi": 58.210123,
      "aei_text": 3.262052,
      "aei_vision": 0.056039,
      "text_ratio": 0.983111,
      "vision_ratio": 0.016889
    },
    "late": {
      "mdi": 51.699135,
      "aei_text": 3.245889,
      "aei_vision": 0.062784,
      "text_ratio": 0.981024,
      "vision_ratio": 0.018976
    },
    "all": {
      "mdi": 51.699135,
      "aei_text": 3.246331,
      "aei_vision": 0.0626,
      "text_ratio": 0.981024,
      "vision_ratio": 0.018976
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981024,
      0.018976
    ],
    "text_vision_ratio": "0.981024:0.018976",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.711694,
      "aei_text": 3.237095,
      "aei_vision": 0.066454,
      "text_ratio": 0.979884,
      "vision_ratio": 0.020116
    },
    "middle": {
      "mdi": 47.889852,
      "aei_text": 3.234492,
      "aei_vision": 0.06754,
      "text_ratio": 0.979546,
      "vision_ratio": 0.020454
    },
    "late": {
      "mdi": 44.519636,
      "aei_text": 3.222866,
      "aei_vision": 0.072392,
      "text_ratio": 0.978031,
      "vision_ratio": 0.021969
    },
    "all": {
      "mdi": 44.519636,
      "aei_text": 3.231484,
      "aei_vision": 0.068795,
      "text_ratio": 0.978031,
      "vision_ratio": 0.021969
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978031,
      0.021969
    ],
    "text_vision_ratio": "0.978031:0.021969",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.254347,
      "aei_text": 3.190759,
      "aei_vision": 0.063492,
      "text_ratio": 0.980489,
      "vision_ratio": 0.019511
    },
    "middle": {
      "mdi": 54.471939,
      "aei_text": 3.201786,
      "aei_vision": 0.058779,
      "text_ratio": 0.981973,
      "vision_ratio": 0.018027
    },
    "late": {
      "mdi": 72.426637,
      "aei_text": 3.234806,
      "aei_vision": 0.044663,
      "text_ratio": 0.986381,
      "vision_ratio": 0.013619
    },
    "all": {
      "mdi": 72.426637,
      "aei_text": 3.209121,
      "aei_vision": 0.055643,
      "text_ratio": 0.986381,
      "vision_ratio": 0.013619
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986381,
      0.013619
    ],
    "text_vision_ratio": "0.986381:0.013619",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.810806,
      "aei_text": 3.180353,
      "aei_vision": 0.067941,
      "text_ratio": 0.979084,
      "vision_ratio": 0.020916
    },
    "middle": {
      "mdi": 74.033714,
      "aei_text": 3.237004,
      "aei_vision": 0.043723,
      "text_ratio": 0.986673,
      "vision_ratio": 0.013327
    },
    "late": {
      "mdi": 68.352347,
      "aei_text": 3.228784,
      "aei_vision": 0.047237,
      "text_ratio": 0.985581,
      "vision_ratio": 0.014419
    },
    "all": {
      "mdi": 68.352347,
      "aei_text": 3.215379,
      "aei_vision": 0.052968,
      "text_ratio": 0.985581,
      "vision_ratio": 0.014419
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985581,
      0.014419
    ],
    "text_vision_ratio": "0.985581:0.014419",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.739421,
      "aei_text": 2.263487,
      "aei_vision": 0.049487,
      "text_ratio": 0.978605,
      "vision_ratio": 0.021395
    },
    "middle": {
      "mdi": 76.476838,
      "aei_text": 2.289474,
      "aei_vision": 0.029937,
      "text_ratio": 0.987093,
      "vision_ratio": 0.012907
    },
    "late": {
      "mdi": 50.231434,
      "aei_text": 2.269218,
      "aei_vision": 0.045175,
      "text_ratio": 0.980481,
      "vision_ratio": 0.019519
    },
    "all": {
      "mdi": 50.231434,
      "aei_text": 2.274059,
      "aei_vision": 0.041534,
      "text_ratio": 0.980481,
      "vision_ratio": 0.019519
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980481,
      0.019519
    ],
    "text_vision_ratio": "0.980481:0.019519",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.859295,
      "aei_text": 2.246011,
      "aei_vision": 0.062634,
      "text_ratio": 0.97287,
      "vision_ratio": 0.02713
    },
    "middle": {
      "mdi": 42.94914,
      "aei_text": 2.259342,
      "aei_vision": 0.052605,
      "text_ratio": 0.977246,
      "vision_ratio": 0.022754
    },
    "late": {
      "mdi": 48.429768,
      "aei_text": 2.267044,
      "aei_vision": 0.046811,
      "text_ratio": 0.979769,
      "vision_ratio": 0.020231
    },
    "all": {
      "mdi": 48.429768,
      "aei_text": 2.257466,
      "aei_vision": 0.054017,
      "text_ratio": 0.979769,
      "vision_ratio": 0.020231
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979769,
      0.020231
    ],
    "text_vision_ratio": "0.979769:0.020231",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.052601,
      "aei_text": 3.162222,
      "aei_vision": 0.07019,
      "text_ratio": 0.978286,
      "vision_ratio": 0.021714
    },
    "middle": {
      "mdi": 95.778433,
      "aei_text": 3.246618,
      "aei_vision": 0.033897,
      "text_ratio": 0.989667,
      "vision_ratio": 0.010333
    },
    "late": {
      "mdi": 83.934262,
      "aei_text": 3.235794,
      "aei_vision": 0.038552,
      "text_ratio": 0.988226,
      "vision_ratio": 0.011774
    },
    "all": {
      "mdi": 83.934262,
      "aei_text": 3.214885,
      "aei_vision": 0.047543,
      "text_ratio": 0.988226,
      "vision_ratio": 0.011774
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988226,
      0.011774
    ],
    "text_vision_ratio": "0.988226:0.011774",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 169.0,
    "total_tokens": 562.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.550754,
      "aei_text": 3.156879,
      "aei_vision": 0.072487,
      "text_ratio": 0.977554,
      "vision_ratio": 0.022446
    },
    "middle": {
      "mdi": 61.597144,
      "aei_text": 3.204467,
      "aei_vision": 0.052023,
      "text_ratio": 0.984025,
      "vision_ratio": 0.015975
    },
    "late": {
      "mdi": 63.054558,
      "aei_text": 3.207164,
      "aei_vision": 0.050863,
      "text_ratio": 0.984388,
      "vision_ratio": 0.015612
    },
    "all": {
      "mdi": 63.054558,
      "aei_text": 3.189506,
      "aei_vision": 0.058457,
      "text_ratio": 0.984388,
      "vision_ratio": 0.015612
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984388,
      0.015612
    ],
    "text_vision_ratio": "0.984388:0.015612",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.157204,
      "aei_text": 3.163977,
      "aei_vision": 0.058422,
      "text_ratio": 0.98187,
      "vision_ratio": 0.01813
    },
    "middle": {
      "mdi": 98.387645,
      "aei_text": 3.22296,
      "aei_vision": 0.032758,
      "text_ratio": 0.989938,
      "vision_ratio": 0.010062
    },
    "late": {
      "mdi": 64.389022,
      "aei_text": 3.184578,
      "aei_vision": 0.049458,
      "text_ratio": 0.984707,
      "vision_ratio": 0.015293
    },
    "all": {
      "mdi": 64.389022,
      "aei_text": 3.1905,
      "aei_vision": 0.046882,
      "text_ratio": 0.984707,
      "vision_ratio": 0.015293
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984707,
      0.015293
    ],
    "text_vision_ratio": "0.984707:0.015293",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 171.0,
    "total_tokens": 564.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.762334,
      "aei_text": 3.155387,
      "aei_vision": 0.06216,
      "text_ratio": 0.980681,
      "vision_ratio": 0.019319
    },
    "middle": {
      "mdi": 76.759386,
      "aei_text": 3.202364,
      "aei_vision": 0.04172,
      "text_ratio": 0.98714,
      "vision_ratio": 0.01286
    },
    "late": {
      "mdi": 62.757994,
      "aei_text": 3.181728,
      "aei_vision": 0.050698,
      "text_ratio": 0.984316,
      "vision_ratio": 0.015684
    },
    "all": {
      "mdi": 62.757994,
      "aei_text": 3.179824,
      "aei_vision": 0.051527,
      "text_ratio": 0.984316,
      "vision_ratio": 0.015684
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984316,
      0.015684
    ],
    "text_vision_ratio": "0.984316:0.015684",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.235298,
      "aei_text": 3.034683,
      "aei_vision": 0.055954,
      "text_ratio": 0.981896,
      "vision_ratio": 0.018104
    },
    "middle": {
      "mdi": 81.888595,
      "aei_text": 3.074363,
      "aei_vision": 0.037543,
      "text_ratio": 0.987936,
      "vision_ratio": 0.012064
    },
    "late": {
      "mdi": 45.713429,
      "aei_text": 3.013214,
      "aei_vision": 0.065915,
      "text_ratio": 0.978593,
      "vision_ratio": 0.021407
    },
    "all": {
      "mdi": 45.713429,
      "aei_text": 3.040741,
      "aei_vision": 0.053143,
      "text_ratio": 0.978593,
      "vision_ratio": 0.021407
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978593,
      0.021407
    ],
    "text_vision_ratio": "0.978593:0.021407",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.704776,
      "aei_text": 3.037746,
      "aei_vision": 0.054533,
      "text_ratio": 0.982365,
      "vision_ratio": 0.017635
    },
    "middle": {
      "mdi": 28.232611,
      "aei_text": 2.931489,
      "aei_vision": 0.103833,
      "text_ratio": 0.965792,
      "vision_ratio": 0.034208
    },
    "late": {
      "mdi": 23.166025,
      "aei_text": 2.886711,
      "aei_vision": 0.12461,
      "text_ratio": 0.95862,
      "vision_ratio": 0.04138
    },
    "all": {
      "mdi": 23.166025,
      "aei_text": 2.951948,
      "aei_vision": 0.094341,
      "text_ratio": 0.95862,
      "vision_ratio": 0.04138
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95862,
      0.04138
    ],
    "text_vision_ratio": "0.958620:0.041380",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 173.0,
    "total_tokens": 566.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.474633,
      "aei_text": 2.731008,
      "aei_vision": 0.238004,
      "text_ratio": 0.919837,
      "vision_ratio": 0.080163
    },
    "middle": {
      "mdi": 10.667369,
      "aei_text": 2.697276,
      "aei_vision": 0.252853,
      "text_ratio": 0.914291,
      "vision_ratio": 0.085709
    },
    "late": {
      "mdi": 17.148797,
      "aei_text": 2.888978,
      "aei_vision": 0.168465,
      "text_ratio": 0.9449,
      "vision_ratio": 0.0551
    },
    "all": {
      "mdi": 17.148797,
      "aei_text": 2.772424,
      "aei_vision": 0.219773,
      "text_ratio": 0.9449,
      "vision_ratio": 0.0551
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9449,
      0.0551
    ],
    "text_vision_ratio": "0.944900:0.055100",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 173.0,
    "total_tokens": 566.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.736585,
      "aei_text": 2.77647,
      "aei_vision": 0.217992,
      "text_ratio": 0.927202,
      "vision_ratio": 0.072798
    },
    "middle": {
      "mdi": 14.596054,
      "aei_text": 2.83106,
      "aei_vision": 0.193961,
      "text_ratio": 0.935881,
      "vision_ratio": 0.064119
    },
    "late": {
      "mdi": 20.1122,
      "aei_text": 2.939643,
      "aei_vision": 0.146162,
      "text_ratio": 0.952634,
      "vision_ratio": 0.047366
    },
    "all": {
      "mdi": 20.1122,
      "aei_text": 2.849042,
      "aei_vision": 0.186045,
      "text_ratio": 0.952634,
      "vision_ratio": 0.047366
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952634,
      0.047366
    ],
    "text_vision_ratio": "0.952634:0.047366",
    "skip_reason": null
  }
}
```


## === Rollout Step 23 ===
Step: 22/43 | 2025-10-22 18:46:15

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 45.422 | 61.435 | 51.257 | 51.257 |
| MDI Std | 12.297 | 28.835 | 21.051 | 21.051 |
| Vision Tokens | 368.8 ± 96.1 |
| Text Tokens | 166.0 ± 4.6 |
| Total Tokens | 534.8 ± 94.0 |
| Vision Ratio | 0.678 |
| Text Ratio | 0.322 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.801483,
      "aei_text": 3.217526,
      "aei_vision": 0.063335,
      "text_ratio": 0.980696,
      "vision_ratio": 0.019304
    },
    "middle": {
      "mdi": 54.490733,
      "aei_text": 3.227255,
      "aei_vision": 0.059226,
      "text_ratio": 0.981979,
      "vision_ratio": 0.018021
    },
    "late": {
      "mdi": 43.805732,
      "aei_text": 3.194807,
      "aei_vision": 0.072931,
      "text_ratio": 0.977681,
      "vision_ratio": 0.022319
    },
    "all": {
      "mdi": 43.805732,
      "aei_text": 3.213189,
      "aei_vision": 0.065167,
      "text_ratio": 0.977681,
      "vision_ratio": 0.022319
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977681,
      0.022319
    ],
    "text_vision_ratio": "0.977681:0.022319",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.83647,
      "aei_text": 3.217624,
      "aei_vision": 0.063294,
      "text_ratio": 0.980709,
      "vision_ratio": 0.019291
    },
    "middle": {
      "mdi": 46.197629,
      "aei_text": 3.203311,
      "aei_vision": 0.069339,
      "text_ratio": 0.978812,
      "vision_ratio": 0.021188
    },
    "late": {
      "mdi": 33.101085,
      "aei_text": 3.142697,
      "aei_vision": 0.094942,
      "text_ratio": 0.970675,
      "vision_ratio": 0.029325
    },
    "all": {
      "mdi": 33.101085,
      "aei_text": 3.187888,
      "aei_vision": 0.075854,
      "text_ratio": 0.970675,
      "vision_ratio": 0.029325
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970675,
      0.029325
    ],
    "text_vision_ratio": "0.970675:0.029325",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 172.0,
    "total_tokens": 519.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.399682,
      "aei_text": 2.883406,
      "aei_vision": 0.066438,
      "text_ratio": 0.977477,
      "vision_ratio": 0.022523
    },
    "middle": {
      "mdi": 75.141441,
      "aei_text": 2.938546,
      "aei_vision": 0.039107,
      "text_ratio": 0.986867,
      "vision_ratio": 0.013133
    },
    "late": {
      "mdi": 50.540193,
      "aei_text": 2.901616,
      "aei_vision": 0.057412,
      "text_ratio": 0.980598,
      "vision_ratio": 0.019402
    },
    "all": {
      "mdi": 50.540193,
      "aei_text": 2.907858,
      "aei_vision": 0.054318,
      "text_ratio": 0.980598,
      "vision_ratio": 0.019402
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980598,
      0.019402
    ],
    "text_vision_ratio": "0.980598:0.019402",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 172.0,
    "total_tokens": 519.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.670804,
      "aei_text": 2.884202,
      "aei_vision": 0.066044,
      "text_ratio": 0.977614,
      "vision_ratio": 0.022386
    },
    "middle": {
      "mdi": 40.673022,
      "aei_text": 2.874845,
      "aei_vision": 0.070682,
      "text_ratio": 0.976004,
      "vision_ratio": 0.023996
    },
    "late": {
      "mdi": 36.089793,
      "aei_text": 2.857695,
      "aei_vision": 0.079183,
      "text_ratio": 0.973038,
      "vision_ratio": 0.026962
    },
    "all": {
      "mdi": 36.089793,
      "aei_text": 2.872248,
      "aei_vision": 0.071969,
      "text_ratio": 0.973038,
      "vision_ratio": 0.026962
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973038,
      0.026962
    ],
    "text_vision_ratio": "0.973038:0.026962",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.560005,
      "aei_text": 3.279469,
      "aei_vision": 0.066172,
      "text_ratio": 0.980222,
      "vision_ratio": 0.019778
    },
    "middle": {
      "mdi": 60.561365,
      "aei_text": 3.307674,
      "aei_vision": 0.054617,
      "text_ratio": 0.983756,
      "vision_ratio": 0.016244
    },
    "late": {
      "mdi": 46.228461,
      "aei_text": 3.268412,
      "aei_vision": 0.070701,
      "text_ratio": 0.978826,
      "vision_ratio": 0.021174
    },
    "all": {
      "mdi": 46.228461,
      "aei_text": 3.285174,
      "aei_vision": 0.063834,
      "text_ratio": 0.978826,
      "vision_ratio": 0.021174
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978826,
      0.021174
    ],
    "text_vision_ratio": "0.978826:0.021174",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.089246,
      "aei_text": 3.284084,
      "aei_vision": 0.064281,
      "text_ratio": 0.980802,
      "vision_ratio": 0.019198
    },
    "middle": {
      "mdi": 92.824907,
      "aei_text": 3.352825,
      "aei_vision": 0.03612,
      "text_ratio": 0.989342,
      "vision_ratio": 0.010658
    },
    "late": {
      "mdi": 91.818328,
      "aei_text": 3.351884,
      "aei_vision": 0.036506,
      "text_ratio": 0.989226,
      "vision_ratio": 0.010774
    },
    "all": {
      "mdi": 91.818328,
      "aei_text": 3.329594,
      "aei_vision": 0.045637,
      "text_ratio": 0.989226,
      "vision_ratio": 0.010774
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989226,
      0.010774
    ],
    "text_vision_ratio": "0.989226:0.010774",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.532299,
      "aei_text": 2.251594,
      "aei_vision": 0.058434,
      "text_ratio": 0.974704,
      "vision_ratio": 0.025296
    },
    "middle": {
      "mdi": 68.222161,
      "aei_text": 2.284751,
      "aei_vision": 0.03349,
      "text_ratio": 0.985554,
      "vision_ratio": 0.014446
    },
    "late": {
      "mdi": 45.076196,
      "aei_text": 2.262547,
      "aei_vision": 0.050194,
      "text_ratio": 0.978297,
      "vision_ratio": 0.021703
    },
    "all": {
      "mdi": 45.076196,
      "aei_text": 2.266296,
      "aei_vision": 0.047373,
      "text_ratio": 0.978297,
      "vision_ratio": 0.021703
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978297,
      0.021703
    ],
    "text_vision_ratio": "0.978297:0.021703",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.196429,
      "aei_text": 2.254707,
      "aei_vision": 0.056092,
      "text_ratio": 0.975726,
      "vision_ratio": 0.024274
    },
    "middle": {
      "mdi": 33.150367,
      "aei_text": 2.23947,
      "aei_vision": 0.067555,
      "text_ratio": 0.970718,
      "vision_ratio": 0.029282
    },
    "late": {
      "mdi": 27.727622,
      "aei_text": 2.222711,
      "aei_vision": 0.080162,
      "text_ratio": 0.96519,
      "vision_ratio": 0.03481
    },
    "all": {
      "mdi": 27.727622,
      "aei_text": 2.238966,
      "aei_vision": 0.067934,
      "text_ratio": 0.96519,
      "vision_ratio": 0.03481
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96519,
      0.03481
    ],
    "text_vision_ratio": "0.965190:0.034810",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 159.0,
    "total_tokens": 690.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.623065,
      "aei_text": 3.802113,
      "aei_vision": 0.160949,
      "text_ratio": 0.959388,
      "vision_ratio": 0.040612
    },
    "middle": {
      "mdi": 20.062594,
      "aei_text": 3.720335,
      "aei_vision": 0.185436,
      "text_ratio": 0.952522,
      "vision_ratio": 0.047478
    },
    "late": {
      "mdi": 28.081034,
      "aei_text": 3.878375,
      "aei_vision": 0.138114,
      "text_ratio": 0.965613,
      "vision_ratio": 0.034387
    },
    "all": {
      "mdi": 28.081034,
      "aei_text": 3.800308,
      "aei_vision": 0.16149,
      "text_ratio": 0.965613,
      "vision_ratio": 0.034387
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965613,
      0.034387
    ],
    "text_vision_ratio": "0.965613:0.034387",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 159.0,
    "total_tokens": 690.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 22.308847,
      "aei_text": 3.774571,
      "aei_vision": 0.169196,
      "text_ratio": 0.957098,
      "vision_ratio": 0.042902
    },
    "middle": {
      "mdi": 17.63773,
      "aei_text": 3.648749,
      "aei_vision": 0.206872,
      "text_ratio": 0.946345,
      "vision_ratio": 0.053655
    },
    "late": {
      "mdi": 38.371583,
      "aei_text": 3.992169,
      "aei_vision": 0.10404,
      "text_ratio": 0.974601,
      "vision_ratio": 0.025399
    },
    "all": {
      "mdi": 38.371583,
      "aei_text": 3.805138,
      "aei_vision": 0.160043,
      "text_ratio": 0.974601,
      "vision_ratio": 0.025399
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974601,
      0.025399
    ],
    "text_vision_ratio": "0.974601:0.025399",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.026235,
      "aei_text": 3.263837,
      "aei_vision": 0.055295,
      "text_ratio": 0.983341,
      "vision_ratio": 0.016659
    },
    "middle": {
      "mdi": 112.99056,
      "aei_text": 3.325807,
      "aei_vision": 0.029434,
      "text_ratio": 0.991227,
      "vision_ratio": 0.008773
    },
    "late": {
      "mdi": 91.571773,
      "aei_text": 3.309729,
      "aei_vision": 0.036144,
      "text_ratio": 0.989198,
      "vision_ratio": 0.010802
    },
    "all": {
      "mdi": 91.571773,
      "aei_text": 3.299804,
      "aei_vision": 0.040285,
      "text_ratio": 0.989198,
      "vision_ratio": 0.010802
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989198,
      0.010802
    ],
    "text_vision_ratio": "0.989198:0.010802",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.662243,
      "aei_text": 3.267274,
      "aei_vision": 0.05386,
      "text_ratio": 0.983783,
      "vision_ratio": 0.016217
    },
    "middle": {
      "mdi": 70.338229,
      "aei_text": 3.284444,
      "aei_vision": 0.046695,
      "text_ratio": 0.985982,
      "vision_ratio": 0.014018
    },
    "late": {
      "mdi": 51.13361,
      "aei_text": 3.2443,
      "aei_vision": 0.063447,
      "text_ratio": 0.980819,
      "vision_ratio": 0.019181
    },
    "all": {
      "mdi": 51.13361,
      "aei_text": 3.265339,
      "aei_vision": 0.054668,
      "text_ratio": 0.980819,
      "vision_ratio": 0.019181
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980819,
      0.019181
    ],
    "text_vision_ratio": "0.980819:0.019181",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 172.0,
    "total_tokens": 408.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.157608,
      "aei_text": 2.280487,
      "aei_vision": 0.066764,
      "text_ratio": 0.971557,
      "vision_ratio": 0.028443
    },
    "middle": {
      "mdi": 39.766331,
      "aei_text": 2.292976,
      "aei_vision": 0.057661,
      "text_ratio": 0.97547,
      "vision_ratio": 0.02453
    },
    "late": {
      "mdi": 37.381376,
      "aei_text": 2.288107,
      "aei_vision": 0.06121,
      "text_ratio": 0.973946,
      "vision_ratio": 0.026054
    },
    "all": {
      "mdi": 37.381376,
      "aei_text": 2.28719,
      "aei_vision": 0.061879,
      "text_ratio": 0.973946,
      "vision_ratio": 0.026054
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973946,
      0.026054
    ],
    "text_vision_ratio": "0.973946:0.026054",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 172.0,
    "total_tokens": 408.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.659531,
      "aei_text": 2.281763,
      "aei_vision": 0.065834,
      "text_ratio": 0.971957,
      "vision_ratio": 0.028043
    },
    "middle": {
      "mdi": 56.420796,
      "aei_text": 2.315776,
      "aei_vision": 0.041045,
      "text_ratio": 0.982585,
      "vision_ratio": 0.017415
    },
    "late": {
      "mdi": 47.431656,
      "aei_text": 2.305403,
      "aei_vision": 0.048605,
      "text_ratio": 0.979352,
      "vision_ratio": 0.020648
    },
    "all": {
      "mdi": 47.431656,
      "aei_text": 2.300977,
      "aei_vision": 0.051831,
      "text_ratio": 0.979352,
      "vision_ratio": 0.020648
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979352,
      0.020648
    ],
    "text_vision_ratio": "0.979352:0.020648",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 170.0,
    "total_tokens": 609.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.779664,
      "aei_text": 3.436352,
      "aei_vision": 0.056538,
      "text_ratio": 0.983813,
      "vision_ratio": 0.016187
    },
    "middle": {
      "mdi": 73.296501,
      "aei_text": 3.460436,
      "aei_vision": 0.047211,
      "text_ratio": 0.98654,
      "vision_ratio": 0.01346
    },
    "late": {
      "mdi": 60.629493,
      "aei_text": 3.436005,
      "aei_vision": 0.056672,
      "text_ratio": 0.983774,
      "vision_ratio": 0.016226
    },
    "all": {
      "mdi": 60.629493,
      "aei_text": 3.444261,
      "aei_vision": 0.053475,
      "text_ratio": 0.983774,
      "vision_ratio": 0.016226
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983774,
      0.016226
    ],
    "text_vision_ratio": "0.983774:0.016226",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 170.0,
    "total_tokens": 609.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 63.441989,
      "aei_text": 3.442239,
      "aei_vision": 0.054258,
      "text_ratio": 0.984482,
      "vision_ratio": 0.015518
    },
    "middle": {
      "mdi": 121.182252,
      "aei_text": 3.507607,
      "aei_vision": 0.028945,
      "text_ratio": 0.991816,
      "vision_ratio": 0.008184
    },
    "late": {
      "mdi": 91.119348,
      "aei_text": 3.483626,
      "aei_vision": 0.038231,
      "text_ratio": 0.989145,
      "vision_ratio": 0.010855
    },
    "all": {
      "mdi": 91.119348,
      "aei_text": 3.47782,
      "aei_vision": 0.04048,
      "text_ratio": 0.989145,
      "vision_ratio": 0.010855
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989145,
      0.010855
    ],
    "text_vision_ratio": "0.989145:0.010855",
    "skip_reason": null
  }
}
```


## === Rollout Step 24 ===
Step: 23/43 | 2025-10-22 18:47:32

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 40.326 | 42.906 | 37.745 | 37.745 |
| MDI Std | 12.754 | 19.623 | 17.446 | 17.446 |
| Vision Tokens | 329.1 ± 92.5 |
| Text Tokens | 162.6 ± 2.3 |
| Total Tokens | 491.8 ± 93.8 |
| Vision Ratio | 0.655 |
| Text Ratio | 0.345 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 165.0,
    "total_tokens": 651.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.440731,
      "aei_text": 3.313395,
      "aei_vision": 0.214588,
      "text_ratio": 0.939175,
      "vision_ratio": 0.060825
    },
    "middle": {
      "mdi": 14.607504,
      "aei_text": 3.283392,
      "aei_vision": 0.224774,
      "text_ratio": 0.935928,
      "vision_ratio": 0.064072
    },
    "late": {
      "mdi": 26.333859,
      "aei_text": 3.548548,
      "aei_vision": 0.134752,
      "text_ratio": 0.963415,
      "vision_ratio": 0.036585
    },
    "all": {
      "mdi": 26.333859,
      "aei_text": 3.38178,
      "aei_vision": 0.191371,
      "text_ratio": 0.963415,
      "vision_ratio": 0.036585
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963415,
      0.036585
    ],
    "text_vision_ratio": "0.963415:0.036585",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 165.0,
    "total_tokens": 651.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.375916,
      "aei_text": 3.311159,
      "aei_vision": 0.215347,
      "text_ratio": 0.938935,
      "vision_ratio": 0.061065
    },
    "middle": {
      "mdi": 16.868171,
      "aei_text": 3.358931,
      "aei_vision": 0.199128,
      "text_ratio": 0.944035,
      "vision_ratio": 0.055965
    },
    "late": {
      "mdi": 20.277628,
      "aei_text": 3.44504,
      "aei_vision": 0.169894,
      "text_ratio": 0.953002,
      "vision_ratio": 0.046998
    },
    "all": {
      "mdi": 20.277628,
      "aei_text": 3.371704,
      "aei_vision": 0.194792,
      "text_ratio": 0.953002,
      "vision_ratio": 0.046998
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953002,
      0.046998
    ],
    "text_vision_ratio": "0.953002:0.046998",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 162.0,
    "total_tokens": 486.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.159956,
      "aei_text": 2.889217,
      "aei_vision": 0.055391,
      "text_ratio": 0.981189,
      "vision_ratio": 0.018811
    },
    "middle": {
      "mdi": 43.646538,
      "aei_text": 2.868555,
      "aei_vision": 0.065722,
      "text_ratio": 0.977602,
      "vision_ratio": 0.022398
    },
    "late": {
      "mdi": 30.042525,
      "aei_text": 2.812749,
      "aei_vision": 0.093626,
      "text_ratio": 0.967786,
      "vision_ratio": 0.032214
    },
    "all": {
      "mdi": 30.042525,
      "aei_text": 2.856827,
      "aei_vision": 0.071587,
      "text_ratio": 0.967786,
      "vision_ratio": 0.032214
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967786,
      0.032214
    ],
    "text_vision_ratio": "0.967786:0.032214",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 162.0,
    "total_tokens": 486.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.157374,
      "aei_text": 2.893157,
      "aei_vision": 0.053421,
      "text_ratio": 0.98187,
      "vision_ratio": 0.01813
    },
    "middle": {
      "mdi": 70.997015,
      "aei_text": 2.917805,
      "aei_vision": 0.041098,
      "text_ratio": 0.986111,
      "vision_ratio": 0.013889
    },
    "late": {
      "mdi": 77.16202,
      "aei_text": 2.924206,
      "aei_vision": 0.037897,
      "text_ratio": 0.987206,
      "vision_ratio": 0.012794
    },
    "all": {
      "mdi": 77.16202,
      "aei_text": 2.91172,
      "aei_vision": 0.04414,
      "text_ratio": 0.987206,
      "vision_ratio": 0.012794
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987206,
      0.012794
    ],
    "text_vision_ratio": "0.987206:0.012794",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.614634,
      "aei_text": 3.256453,
      "aei_vision": 0.069859,
      "text_ratio": 0.978998,
      "vision_ratio": 0.021002
    },
    "middle": {
      "mdi": 58.086299,
      "aei_text": 3.288581,
      "aei_vision": 0.056615,
      "text_ratio": 0.983076,
      "vision_ratio": 0.016924
    },
    "late": {
      "mdi": 41.644387,
      "aei_text": 3.23734,
      "aei_vision": 0.077738,
      "text_ratio": 0.97655,
      "vision_ratio": 0.02345
    },
    "all": {
      "mdi": 41.644387,
      "aei_text": 3.260792,
      "aei_vision": 0.06807,
      "text_ratio": 0.97655,
      "vision_ratio": 0.02345
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97655,
      0.02345
    ],
    "text_vision_ratio": "0.976550:0.023450",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.162663,
      "aei_text": 3.254877,
      "aei_vision": 0.070509,
      "text_ratio": 0.978797,
      "vision_ratio": 0.021203
    },
    "middle": {
      "mdi": 74.545592,
      "aei_text": 3.31795,
      "aei_vision": 0.044509,
      "text_ratio": 0.986763,
      "vision_ratio": 0.013237
    },
    "late": {
      "mdi": 59.532918,
      "aei_text": 3.291788,
      "aei_vision": 0.055294,
      "text_ratio": 0.98348,
      "vision_ratio": 0.01652
    },
    "all": {
      "mdi": 59.532918,
      "aei_text": 3.288194,
      "aei_vision": 0.056775,
      "text_ratio": 0.98348,
      "vision_ratio": 0.01652
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98348,
      0.01652
    ],
    "text_vision_ratio": "0.983480:0.016520",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 140.0,
    "text_tokens": 161.0,
    "total_tokens": 301.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 22.391601,
      "aei_text": 1.799676,
      "aei_vision": 0.080373,
      "text_ratio": 0.95725,
      "vision_ratio": 0.04275
    },
    "middle": {
      "mdi": 20.089579,
      "aei_text": 1.792,
      "aei_vision": 0.0892,
      "text_ratio": 0.952583,
      "vision_ratio": 0.047417
    },
    "late": {
      "mdi": 16.501517,
      "aei_text": 1.775978,
      "aei_vision": 0.107625,
      "text_ratio": 0.942862,
      "vision_ratio": 0.057138
    },
    "all": {
      "mdi": 16.501517,
      "aei_text": 1.789218,
      "aei_vision": 0.092399,
      "text_ratio": 0.942862,
      "vision_ratio": 0.057138
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942862,
      0.057138
    ],
    "text_vision_ratio": "0.942862:0.057138",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 140.0,
    "text_tokens": 161.0,
    "total_tokens": 301.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 24.053473,
      "aei_text": 1.804336,
      "aei_vision": 0.075014,
      "text_ratio": 0.960085,
      "vision_ratio": 0.039915
    },
    "middle": {
      "mdi": 17.286712,
      "aei_text": 1.780025,
      "aei_vision": 0.102971,
      "text_ratio": 0.945315,
      "vision_ratio": 0.054685
    },
    "late": {
      "mdi": 12.95329,
      "aei_text": 1.751955,
      "aei_vision": 0.135252,
      "text_ratio": 0.928332,
      "vision_ratio": 0.071668
    },
    "all": {
      "mdi": 12.95329,
      "aei_text": 1.778767,
      "aei_vision": 0.104418,
      "text_ratio": 0.928332,
      "vision_ratio": 0.071668
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.928332,
      0.071668
    ],
    "text_vision_ratio": "0.928332:0.071668",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.340009,
      "aei_text": 2.985191,
      "aei_vision": 0.061754,
      "text_ratio": 0.979732,
      "vision_ratio": 0.020268
    },
    "middle": {
      "mdi": 40.026405,
      "aei_text": 2.959415,
      "aei_vision": 0.073937,
      "text_ratio": 0.975625,
      "vision_ratio": 0.024375
    },
    "late": {
      "mdi": 34.640394,
      "aei_text": 2.936491,
      "aei_vision": 0.084771,
      "text_ratio": 0.971942,
      "vision_ratio": 0.028058
    },
    "all": {
      "mdi": 34.640394,
      "aei_text": 2.960372,
      "aei_vision": 0.073484,
      "text_ratio": 0.971942,
      "vision_ratio": 0.028058
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971942,
      0.028058
    ],
    "text_vision_ratio": "0.971942:0.028058",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.232833,
      "aei_text": 2.996742,
      "aei_vision": 0.056295,
      "text_ratio": 0.981561,
      "vision_ratio": 0.018439
    },
    "middle": {
      "mdi": 79.4628,
      "aei_text": 3.03504,
      "aei_vision": 0.038194,
      "text_ratio": 0.987572,
      "vision_ratio": 0.012428
    },
    "late": {
      "mdi": 70.97924,
      "aei_text": 3.02566,
      "aei_vision": 0.042627,
      "text_ratio": 0.986107,
      "vision_ratio": 0.013893
    },
    "all": {
      "mdi": 70.97924,
      "aei_text": 3.019146,
      "aei_vision": 0.045706,
      "text_ratio": 0.986107,
      "vision_ratio": 0.013893
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986107,
      0.013893
    ],
    "text_vision_ratio": "0.986107:0.013893",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 163.0,
    "total_tokens": 487.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.087433,
      "aei_text": 2.855977,
      "aei_vision": 0.066283,
      "text_ratio": 0.977318,
      "vision_ratio": 0.022682
    },
    "middle": {
      "mdi": 41.770932,
      "aei_text": 2.852013,
      "aei_vision": 0.068277,
      "text_ratio": 0.97662,
      "vision_ratio": 0.02338
    },
    "late": {
      "mdi": 35.201017,
      "aei_text": 2.828037,
      "aei_vision": 0.08034,
      "text_ratio": 0.972376,
      "vision_ratio": 0.027624
    },
    "all": {
      "mdi": 35.201017,
      "aei_text": 2.845343,
      "aei_vision": 0.071633,
      "text_ratio": 0.972376,
      "vision_ratio": 0.027624
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972376,
      0.027624
    ],
    "text_vision_ratio": "0.972376:0.027624",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 163.0,
    "total_tokens": 487.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.232245,
      "aei_text": 2.861961,
      "aei_vision": 0.063273,
      "text_ratio": 0.97837,
      "vision_ratio": 0.02163
    },
    "middle": {
      "mdi": 49.178108,
      "aei_text": 2.87166,
      "aei_vision": 0.058393,
      "text_ratio": 0.980071,
      "vision_ratio": 0.019929
    },
    "late": {
      "mdi": 41.691021,
      "aei_text": 2.851765,
      "aei_vision": 0.068402,
      "text_ratio": 0.976576,
      "vision_ratio": 0.023424
    },
    "all": {
      "mdi": 41.691021,
      "aei_text": 2.861798,
      "aei_vision": 0.063355,
      "text_ratio": 0.976576,
      "vision_ratio": 0.023424
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976576,
      0.023424
    ],
    "text_vision_ratio": "0.976576:0.023424",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 272.0,
    "text_tokens": 158.0,
    "total_tokens": 430.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.86666,
      "aei_text": 2.628906,
      "aei_vision": 0.053798,
      "text_ratio": 0.979947,
      "vision_ratio": 0.020053
    },
    "middle": {
      "mdi": 34.080736,
      "aei_text": 2.590657,
      "aei_vision": 0.076015,
      "text_ratio": 0.971494,
      "vision_ratio": 0.028506
    },
    "late": {
      "mdi": 32.926394,
      "aei_text": 2.586297,
      "aei_vision": 0.078548,
      "text_ratio": 0.970524,
      "vision_ratio": 0.029476
    },
    "all": {
      "mdi": 32.926394,
      "aei_text": 2.601956,
      "aei_vision": 0.069452,
      "text_ratio": 0.970524,
      "vision_ratio": 0.029476
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970524,
      0.029476
    ],
    "text_vision_ratio": "0.970524:0.029476",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 272.0,
    "text_tokens": 158.0,
    "total_tokens": 430.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.15535,
      "aei_text": 2.621573,
      "aei_vision": 0.058057,
      "text_ratio": 0.978334,
      "vision_ratio": 0.021666
    },
    "middle": {
      "mdi": 38.468744,
      "aei_text": 2.604945,
      "aei_vision": 0.067716,
      "text_ratio": 0.974663,
      "vision_ratio": 0.025337
    },
    "late": {
      "mdi": 28.910758,
      "aei_text": 2.568571,
      "aei_vision": 0.088845,
      "text_ratio": 0.966567,
      "vision_ratio": 0.033433
    },
    "all": {
      "mdi": 28.910758,
      "aei_text": 2.598363,
      "aei_vision": 0.071539,
      "text_ratio": 0.966567,
      "vision_ratio": 0.033433
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966567,
      0.033433
    ],
    "text_vision_ratio": "0.966567:0.033433",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.327323,
      "aei_text": 2.948127,
      "aei_vision": 0.068043,
      "text_ratio": 0.977441,
      "vision_ratio": 0.022559
    },
    "middle": {
      "mdi": 43.814126,
      "aei_text": 2.949635,
      "aei_vision": 0.067322,
      "text_ratio": 0.977686,
      "vision_ratio": 0.022314
    },
    "late": {
      "mdi": 41.30246,
      "aei_text": 2.94149,
      "aei_vision": 0.071218,
      "text_ratio": 0.976361,
      "vision_ratio": 0.023639
    },
    "all": {
      "mdi": 41.30246,
      "aei_text": 2.946415,
      "aei_vision": 0.068862,
      "text_ratio": 0.976361,
      "vision_ratio": 0.023639
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976361,
      0.023639
    ],
    "text_vision_ratio": "0.976361:0.023639",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.622372,
      "aei_text": 2.942579,
      "aei_vision": 0.070697,
      "text_ratio": 0.976538,
      "vision_ratio": 0.023462
    },
    "middle": {
      "mdi": 43.560074,
      "aei_text": 2.948852,
      "aei_vision": 0.067696,
      "text_ratio": 0.977558,
      "vision_ratio": 0.022442
    },
    "late": {
      "mdi": 33.821183,
      "aei_text": 2.910476,
      "aei_vision": 0.086055,
      "text_ratio": 0.971282,
      "vision_ratio": 0.028718
    },
    "all": {
      "mdi": 33.821183,
      "aei_text": 2.933965,
      "aei_vision": 0.074818,
      "text_ratio": 0.971282,
      "vision_ratio": 0.028718
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971282,
      0.028718
    ],
    "text_vision_ratio": "0.971282:0.028718",
    "skip_reason": null
  }
}
```


## === Rollout Step 25 ===
Step: 24/43 | 2025-10-22 18:48:50

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.468 | 55.462 | 48.503 | 48.503 |
| MDI Std | 12.287 | 19.927 | 14.930 | 14.930 |
| Vision Tokens | 368.6 ± 70.5 |
| Text Tokens | 164.5 ± 4.7 |
| Total Tokens | 533.1 ± 73.5 |
| Vision Ratio | 0.687 |
| Text Ratio | 0.313 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 290.0,
    "text_tokens": 159.0,
    "total_tokens": 449.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.035882,
      "aei_text": 2.711589,
      "aei_vision": 0.061577,
      "text_ratio": 0.977795,
      "vision_ratio": 0.022205
    },
    "middle": {
      "mdi": 51.160107,
      "aei_text": 2.726691,
      "aei_vision": 0.053297,
      "text_ratio": 0.980828,
      "vision_ratio": 0.019172
    },
    "late": {
      "mdi": 46.783962,
      "aei_text": 2.717939,
      "aei_vision": 0.058096,
      "text_ratio": 0.979072,
      "vision_ratio": 0.020928
    },
    "all": {
      "mdi": 46.783962,
      "aei_text": 2.718739,
      "aei_vision": 0.057657,
      "text_ratio": 0.979072,
      "vision_ratio": 0.020928
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979072,
      0.020928
    ],
    "text_vision_ratio": "0.979072:0.020928",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 290.0,
    "text_tokens": 159.0,
    "total_tokens": 449.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.05071,
      "aei_text": 2.716316,
      "aei_vision": 0.058985,
      "text_ratio": 0.978746,
      "vision_ratio": 0.021254
    },
    "middle": {
      "mdi": 59.651499,
      "aei_text": 2.740118,
      "aei_vision": 0.045935,
      "text_ratio": 0.983512,
      "vision_ratio": 0.016488
    },
    "late": {
      "mdi": 42.637222,
      "aei_text": 2.708056,
      "aei_vision": 0.063514,
      "text_ratio": 0.977084,
      "vision_ratio": 0.022916
    },
    "all": {
      "mdi": 42.637222,
      "aei_text": 2.721489,
      "aei_vision": 0.056149,
      "text_ratio": 0.977084,
      "vision_ratio": 0.022916
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977084,
      0.022916
    ],
    "text_vision_ratio": "0.977084:0.022916",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.798203,
      "aei_text": 3.215563,
      "aei_vision": 0.052889,
      "text_ratio": 0.983818,
      "vision_ratio": 0.016182
    },
    "middle": {
      "mdi": 77.101949,
      "aei_text": 3.240955,
      "aei_vision": 0.042035,
      "text_ratio": 0.987196,
      "vision_ratio": 0.012804
    },
    "late": {
      "mdi": 64.799414,
      "aei_text": 3.222936,
      "aei_vision": 0.049737,
      "text_ratio": 0.984802,
      "vision_ratio": 0.015198
    },
    "all": {
      "mdi": 64.799414,
      "aei_text": 3.226488,
      "aei_vision": 0.048219,
      "text_ratio": 0.984802,
      "vision_ratio": 0.015198
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984802,
      0.015198
    ],
    "text_vision_ratio": "0.984802:0.015198",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.27445,
      "aei_text": 3.214528,
      "aei_vision": 0.053332,
      "text_ratio": 0.98368,
      "vision_ratio": 0.01632
    },
    "middle": {
      "mdi": 61.77023,
      "aei_text": 3.217439,
      "aei_vision": 0.052087,
      "text_ratio": 0.984069,
      "vision_ratio": 0.015931
    },
    "late": {
      "mdi": 55.615194,
      "aei_text": 3.204498,
      "aei_vision": 0.057619,
      "text_ratio": 0.982337,
      "vision_ratio": 0.017663
    },
    "all": {
      "mdi": 55.615194,
      "aei_text": 3.212155,
      "aei_vision": 0.054346,
      "text_ratio": 0.982337,
      "vision_ratio": 0.017663
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982337,
      0.017663
    ],
    "text_vision_ratio": "0.982337:0.017663",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.144237,
      "aei_text": 3.027689,
      "aei_vision": 0.059199,
      "text_ratio": 0.980822,
      "vision_ratio": 0.019178
    },
    "middle": {
      "mdi": 77.098166,
      "aei_text": 3.069472,
      "aei_vision": 0.039813,
      "text_ratio": 0.987196,
      "vision_ratio": 0.012804
    },
    "late": {
      "mdi": 64.99714,
      "aei_text": 3.05401,
      "aei_vision": 0.046987,
      "text_ratio": 0.984848,
      "vision_ratio": 0.015152
    },
    "all": {
      "mdi": 64.99714,
      "aei_text": 3.050394,
      "aei_vision": 0.048665,
      "text_ratio": 0.984848,
      "vision_ratio": 0.015152
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984848,
      0.015152
    ],
    "text_vision_ratio": "0.984848:0.015152",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.884487,
      "aei_text": 3.027064,
      "aei_vision": 0.059489,
      "text_ratio": 0.980726,
      "vision_ratio": 0.019274
    },
    "middle": {
      "mdi": 78.942751,
      "aei_text": 3.071424,
      "aei_vision": 0.038907,
      "text_ratio": 0.987491,
      "vision_ratio": 0.012509
    },
    "late": {
      "mdi": 62.867191,
      "aei_text": 3.050692,
      "aei_vision": 0.048526,
      "text_ratio": 0.984343,
      "vision_ratio": 0.015657
    },
    "all": {
      "mdi": 62.867191,
      "aei_text": 3.049734,
      "aei_vision": 0.048971,
      "text_ratio": 0.984343,
      "vision_ratio": 0.015657
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984343,
      0.015657
    ],
    "text_vision_ratio": "0.984343:0.015657",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 162.0,
    "total_tokens": 463.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.35997,
      "aei_text": 2.732242,
      "aei_vision": 0.067697,
      "text_ratio": 0.975822,
      "vision_ratio": 0.024178
    },
    "middle": {
      "mdi": 38.105626,
      "aei_text": 2.725147,
      "aei_vision": 0.071516,
      "text_ratio": 0.974428,
      "vision_ratio": 0.025572
    },
    "late": {
      "mdi": 29.640974,
      "aei_text": 2.689439,
      "aei_vision": 0.090734,
      "text_ratio": 0.967364,
      "vision_ratio": 0.032636
    },
    "all": {
      "mdi": 29.640974,
      "aei_text": 2.715602,
      "aei_vision": 0.076653,
      "text_ratio": 0.967364,
      "vision_ratio": 0.032636
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967364,
      0.032636
    ],
    "text_vision_ratio": "0.967364:0.032636",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 162.0,
    "total_tokens": 463.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.930041,
      "aei_text": 2.73946,
      "aei_vision": 0.063812,
      "text_ratio": 0.977237,
      "vision_ratio": 0.022763
    },
    "middle": {
      "mdi": 71.264532,
      "aei_text": 2.785403,
      "aei_vision": 0.039085,
      "text_ratio": 0.986162,
      "vision_ratio": 0.013838
    },
    "late": {
      "mdi": 63.356644,
      "aei_text": 2.776597,
      "aei_vision": 0.043825,
      "text_ratio": 0.984462,
      "vision_ratio": 0.015538
    },
    "all": {
      "mdi": 63.356644,
      "aei_text": 2.767152,
      "aei_vision": 0.048908,
      "text_ratio": 0.984462,
      "vision_ratio": 0.015538
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984462,
      0.015538
    ],
    "text_vision_ratio": "0.984462:0.015538",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 174.0,
    "total_tokens": 567.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.877163,
      "aei_text": 3.117451,
      "aei_vision": 0.062503,
      "text_ratio": 0.980345,
      "vision_ratio": 0.019655
    },
    "middle": {
      "mdi": 54.862127,
      "aei_text": 3.129771,
      "aei_vision": 0.057048,
      "text_ratio": 0.982099,
      "vision_ratio": 0.017901
    },
    "late": {
      "mdi": 50.05817,
      "aei_text": 3.11794,
      "aei_vision": 0.062286,
      "text_ratio": 0.980414,
      "vision_ratio": 0.019586
    },
    "all": {
      "mdi": 50.05817,
      "aei_text": 3.121723,
      "aei_vision": 0.060611,
      "text_ratio": 0.980414,
      "vision_ratio": 0.019586
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980414,
      0.019586
    ],
    "text_vision_ratio": "0.980414:0.019586",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 174.0,
    "total_tokens": 567.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.306063,
      "aei_text": 3.10707,
      "aei_vision": 0.067099,
      "text_ratio": 0.978861,
      "vision_ratio": 0.021139
    },
    "middle": {
      "mdi": 53.658244,
      "aei_text": 3.126997,
      "aei_vision": 0.058276,
      "text_ratio": 0.981704,
      "vision_ratio": 0.018296
    },
    "late": {
      "mdi": 51.100272,
      "aei_text": 3.120687,
      "aei_vision": 0.06107,
      "text_ratio": 0.980806,
      "vision_ratio": 0.019194
    },
    "all": {
      "mdi": 51.100272,
      "aei_text": 3.118249,
      "aei_vision": 0.062149,
      "text_ratio": 0.980806,
      "vision_ratio": 0.019194
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980806,
      0.019194
    ],
    "text_vision_ratio": "0.980806:0.019194",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.624928,
      "aei_text": 3.016805,
      "aei_vision": 0.058437,
      "text_ratio": 0.980998,
      "vision_ratio": 0.019002
    },
    "middle": {
      "mdi": 76.576119,
      "aei_text": 3.05648,
      "aei_vision": 0.039914,
      "text_ratio": 0.987109,
      "vision_ratio": 0.012891
    },
    "late": {
      "mdi": 63.183601,
      "aei_text": 3.038952,
      "aei_vision": 0.048097,
      "text_ratio": 0.98442,
      "vision_ratio": 0.01558
    },
    "all": {
      "mdi": 63.183601,
      "aei_text": 3.03742,
      "aei_vision": 0.048813,
      "text_ratio": 0.98442,
      "vision_ratio": 0.01558
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98442,
      0.01558
    ],
    "text_vision_ratio": "0.984420:0.015580",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.964168,
      "aei_text": 3.012815,
      "aei_vision": 0.0603,
      "text_ratio": 0.980378,
      "vision_ratio": 0.019622
    },
    "middle": {
      "mdi": 64.826353,
      "aei_text": 3.04148,
      "aei_vision": 0.046917,
      "text_ratio": 0.984809,
      "vision_ratio": 0.015191
    },
    "late": {
      "mdi": 52.747613,
      "aei_text": 3.019365,
      "aei_vision": 0.057242,
      "text_ratio": 0.981395,
      "vision_ratio": 0.018605
    },
    "all": {
      "mdi": 52.747613,
      "aei_text": 3.024558,
      "aei_vision": 0.054817,
      "text_ratio": 0.981395,
      "vision_ratio": 0.018605
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981395,
      0.018605
    ],
    "text_vision_ratio": "0.981395:0.018605",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.277207,
      "aei_text": 2.996991,
      "aei_vision": 0.067687,
      "text_ratio": 0.977914,
      "vision_ratio": 0.022086
    },
    "middle": {
      "mdi": 52.353092,
      "aei_text": 3.018477,
      "aei_vision": 0.057656,
      "text_ratio": 0.981257,
      "vision_ratio": 0.018743
    },
    "late": {
      "mdi": 41.077865,
      "aei_text": 2.986259,
      "aei_vision": 0.072698,
      "text_ratio": 0.976235,
      "vision_ratio": 0.023765
    },
    "all": {
      "mdi": 41.077865,
      "aei_text": 3.000582,
      "aei_vision": 0.066011,
      "text_ratio": 0.976235,
      "vision_ratio": 0.023765
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976235,
      0.023765
    ],
    "text_vision_ratio": "0.976235:0.023765",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.829301,
      "aei_text": 2.98892,
      "aei_vision": 0.071455,
      "text_ratio": 0.976651,
      "vision_ratio": 0.023349
    },
    "middle": {
      "mdi": 43.24909,
      "aei_text": 2.993708,
      "aei_vision": 0.06922,
      "text_ratio": 0.977401,
      "vision_ratio": 0.022599
    },
    "late": {
      "mdi": 50.840684,
      "aei_text": 3.014952,
      "aei_vision": 0.059302,
      "text_ratio": 0.98071,
      "vision_ratio": 0.01929
    },
    "all": {
      "mdi": 50.840684,
      "aei_text": 2.999192,
      "aei_vision": 0.06666,
      "text_ratio": 0.98071,
      "vision_ratio": 0.01929
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98071,
      0.01929
    ],
    "text_vision_ratio": "0.980710:0.019290",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 168.0,
    "total_tokens": 699.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.580705,
      "aei_text": 3.459016,
      "aei_vision": 0.222006,
      "text_ratio": 0.939689,
      "vision_ratio": 0.060311
    },
    "middle": {
      "mdi": 12.408824,
      "aei_text": 3.316063,
      "aei_vision": 0.267234,
      "text_ratio": 0.925422,
      "vision_ratio": 0.074578
    },
    "late": {
      "mdi": 15.424043,
      "aei_text": 3.453101,
      "aei_vision": 0.223878,
      "text_ratio": 0.939114,
      "vision_ratio": 0.060886
    },
    "all": {
      "mdi": 15.424043,
      "aei_text": 3.409387,
      "aei_vision": 0.237708,
      "text_ratio": 0.939114,
      "vision_ratio": 0.060886
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939114,
      0.060886
    ],
    "text_vision_ratio": "0.939114:0.060886",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 168.0,
    "total_tokens": 699.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.558086,
      "aei_text": 3.458168,
      "aei_vision": 0.222275,
      "text_ratio": 0.939607,
      "vision_ratio": 0.060393
    },
    "middle": {
      "mdi": 14.360637,
      "aei_text": 3.410154,
      "aei_vision": 0.237465,
      "text_ratio": 0.934899,
      "vision_ratio": 0.065101
    },
    "late": {
      "mdi": 20.919326,
      "aei_text": 3.614584,
      "aei_vision": 0.172787,
      "text_ratio": 0.954378,
      "vision_ratio": 0.045622
    },
    "all": {
      "mdi": 20.919326,
      "aei_text": 3.494313,
      "aei_vision": 0.210839,
      "text_ratio": 0.954378,
      "vision_ratio": 0.045622
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954378,
      0.045622
    ],
    "text_vision_ratio": "0.954378:0.045622",
    "skip_reason": null
  }
}
```


## === Rollout Step 26 ===
Step: 25/43 | 2025-10-22 18:50:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.443 | 48.934 | 42.197 | 42.197 |
| MDI Std | 12.006 | 21.952 | 17.333 | 17.333 |
| Vision Tokens | 335.2 ± 62.7 |
| Text Tokens | 164.6 ± 4.4 |
| Total Tokens | 499.9 ± 63.4 |
| Vision Ratio | 0.665 |
| Text Ratio | 0.335 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 162.0,
    "total_tokens": 398.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.350387,
      "aei_text": 2.378658,
      "aei_vision": 0.053633,
      "text_ratio": 0.977949,
      "vision_ratio": 0.022051
    },
    "middle": {
      "mdi": 21.182278,
      "aei_text": 2.298699,
      "aei_vision": 0.10852,
      "text_ratio": 0.954919,
      "vision_ratio": 0.045081
    },
    "late": {
      "mdi": 18.338893,
      "aei_text": 2.275992,
      "aei_vision": 0.124107,
      "text_ratio": 0.948291,
      "vision_ratio": 0.051709
    },
    "all": {
      "mdi": 18.338893,
      "aei_text": 2.317794,
      "aei_vision": 0.095413,
      "text_ratio": 0.948291,
      "vision_ratio": 0.051709
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948291,
      0.051709
    ],
    "text_vision_ratio": "0.948291:0.051709",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 162.0,
    "total_tokens": 398.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.083828,
      "aei_text": 2.372658,
      "aei_vision": 0.057752,
      "text_ratio": 0.976238,
      "vision_ratio": 0.023762
    },
    "middle": {
      "mdi": 24.24871,
      "aei_text": 2.317558,
      "aei_vision": 0.095574,
      "text_ratio": 0.960394,
      "vision_ratio": 0.039606
    },
    "late": {
      "mdi": 22.457506,
      "aei_text": 2.30713,
      "aei_vision": 0.102733,
      "text_ratio": 0.95737,
      "vision_ratio": 0.04263
    },
    "all": {
      "mdi": 22.457506,
      "aei_text": 2.332436,
      "aei_vision": 0.085361,
      "text_ratio": 0.95737,
      "vision_ratio": 0.04263
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95737,
      0.04263
    ],
    "text_vision_ratio": "0.957370:0.042630",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.324568,
      "aei_text": 2.889392,
      "aei_vision": 0.255144,
      "text_ratio": 0.918861,
      "vision_ratio": 0.081139
    },
    "middle": {
      "mdi": 7.798121,
      "aei_text": 2.668554,
      "aei_vision": 0.342205,
      "text_ratio": 0.886339,
      "vision_ratio": 0.113661
    },
    "late": {
      "mdi": 9.417556,
      "aei_text": 2.786147,
      "aei_vision": 0.295846,
      "text_ratio": 0.904008,
      "vision_ratio": 0.095992
    },
    "all": {
      "mdi": 9.417556,
      "aei_text": 2.781364,
      "aei_vision": 0.297731,
      "text_ratio": 0.904008,
      "vision_ratio": 0.095992
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.904008,
      0.095992
    ],
    "text_vision_ratio": "0.904008:0.095992",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.134309,
      "aei_text": 3.028923,
      "aei_vision": 0.200136,
      "text_ratio": 0.93802,
      "vision_ratio": 0.06198
    },
    "middle": {
      "mdi": 14.106951,
      "aei_text": 2.997586,
      "aei_vision": 0.21249,
      "text_ratio": 0.933805,
      "vision_ratio": 0.066195
    },
    "late": {
      "mdi": 19.172903,
      "aei_text": 3.123363,
      "aei_vision": 0.162905,
      "text_ratio": 0.950429,
      "vision_ratio": 0.049571
    },
    "all": {
      "mdi": 19.172903,
      "aei_text": 3.04995,
      "aei_vision": 0.191846,
      "text_ratio": 0.950429,
      "vision_ratio": 0.049571
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950429,
      0.049571
    ],
    "text_vision_ratio": "0.950429:0.049571",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.926544,
      "aei_text": 3.192634,
      "aei_vision": 0.062691,
      "text_ratio": 0.980742,
      "vision_ratio": 0.019258
    },
    "middle": {
      "mdi": 90.361535,
      "aei_text": 3.25502,
      "aei_vision": 0.036022,
      "text_ratio": 0.989054,
      "vision_ratio": 0.010946
    },
    "late": {
      "mdi": 43.346988,
      "aei_text": 3.168303,
      "aei_vision": 0.073092,
      "text_ratio": 0.977451,
      "vision_ratio": 0.022549
    },
    "all": {
      "mdi": 43.346988,
      "aei_text": 3.205325,
      "aei_vision": 0.057266,
      "text_ratio": 0.977451,
      "vision_ratio": 0.022549
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977451,
      0.022549
    ],
    "text_vision_ratio": "0.977451:0.022549",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.416366,
      "aei_text": 3.179068,
      "aei_vision": 0.06849,
      "text_ratio": 0.97891,
      "vision_ratio": 0.02109
    },
    "middle": {
      "mdi": 44.09248,
      "aei_text": 3.171049,
      "aei_vision": 0.071918,
      "text_ratio": 0.977823,
      "vision_ratio": 0.022177
    },
    "late": {
      "mdi": 34.903314,
      "aei_text": 3.129538,
      "aei_vision": 0.089663,
      "text_ratio": 0.972147,
      "vision_ratio": 0.027853
    },
    "all": {
      "mdi": 34.903314,
      "aei_text": 3.159889,
      "aei_vision": 0.076689,
      "text_ratio": 0.972147,
      "vision_ratio": 0.027853
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972147,
      0.027853
    ],
    "text_vision_ratio": "0.972147:0.027853",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.61532,
      "aei_text": 3.015298,
      "aei_vision": 0.070756,
      "text_ratio": 0.977072,
      "vision_ratio": 0.022928
    },
    "middle": {
      "mdi": 63.537933,
      "aei_text": 3.064161,
      "aei_vision": 0.048226,
      "text_ratio": 0.984505,
      "vision_ratio": 0.015495
    },
    "late": {
      "mdi": 66.472345,
      "aei_text": 3.068632,
      "aei_vision": 0.046164,
      "text_ratio": 0.985179,
      "vision_ratio": 0.014821
    },
    "all": {
      "mdi": 66.472345,
      "aei_text": 3.04937,
      "aei_vision": 0.055046,
      "text_ratio": 0.985179,
      "vision_ratio": 0.014821
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985179,
      0.014821
    ],
    "text_vision_ratio": "0.985179:0.014821",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.952774,
      "aei_text": 3.016445,
      "aei_vision": 0.070227,
      "text_ratio": 0.977248,
      "vision_ratio": 0.022752
    },
    "middle": {
      "mdi": 49.821287,
      "aei_text": 3.036566,
      "aei_vision": 0.060949,
      "text_ratio": 0.980323,
      "vision_ratio": 0.019677
    },
    "late": {
      "mdi": 43.537481,
      "aei_text": 3.018394,
      "aei_vision": 0.069329,
      "text_ratio": 0.977547,
      "vision_ratio": 0.022453
    },
    "all": {
      "mdi": 43.537481,
      "aei_text": 3.023805,
      "aei_vision": 0.066833,
      "text_ratio": 0.977547,
      "vision_ratio": 0.022453
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977547,
      0.022453
    ],
    "text_vision_ratio": "0.977547:0.022453",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.008557,
      "aei_text": 3.30038,
      "aei_vision": 0.063458,
      "text_ratio": 0.981135,
      "vision_ratio": 0.018865
    },
    "middle": {
      "mdi": 60.366771,
      "aei_text": 3.321118,
      "aei_vision": 0.055016,
      "text_ratio": 0.983705,
      "vision_ratio": 0.016295
    },
    "late": {
      "mdi": 56.241474,
      "aei_text": 3.311621,
      "aei_vision": 0.058882,
      "text_ratio": 0.98253,
      "vision_ratio": 0.01747
    },
    "all": {
      "mdi": 56.241474,
      "aei_text": 3.311038,
      "aei_vision": 0.059119,
      "text_ratio": 0.98253,
      "vision_ratio": 0.01747
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98253,
      0.01747
    ],
    "text_vision_ratio": "0.982530:0.017470",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.567017,
      "aei_text": 3.286541,
      "aei_vision": 0.069093,
      "text_ratio": 0.97941,
      "vision_ratio": 0.02059
    },
    "middle": {
      "mdi": 44.528228,
      "aei_text": 3.275564,
      "aei_vision": 0.073562,
      "text_ratio": 0.978036,
      "vision_ratio": 0.021964
    },
    "late": {
      "mdi": 35.868451,
      "aei_text": 3.234737,
      "aei_vision": 0.090183,
      "text_ratio": 0.972877,
      "vision_ratio": 0.027123
    },
    "all": {
      "mdi": 35.868451,
      "aei_text": 3.265614,
      "aei_vision": 0.077613,
      "text_ratio": 0.972877,
      "vision_ratio": 0.027123
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972877,
      0.027123
    ],
    "text_vision_ratio": "0.972877:0.027123",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 172.0,
    "total_tokens": 519.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 37.984603,
      "aei_text": 2.865262,
      "aei_vision": 0.075432,
      "text_ratio": 0.974349,
      "vision_ratio": 0.025651
    },
    "middle": {
      "mdi": 61.92482,
      "aei_text": 2.922239,
      "aei_vision": 0.04719,
      "text_ratio": 0.984108,
      "vision_ratio": 0.015892
    },
    "late": {
      "mdi": 46.530105,
      "aei_text": 2.892049,
      "aei_vision": 0.062154,
      "text_ratio": 0.978961,
      "vision_ratio": 0.021039
    },
    "all": {
      "mdi": 46.530105,
      "aei_text": 2.893181,
      "aei_vision": 0.061593,
      "text_ratio": 0.978961,
      "vision_ratio": 0.021039
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978961,
      0.021039
    ],
    "text_vision_ratio": "0.978961:0.021039",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 172.0,
    "total_tokens": 519.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.285932,
      "aei_text": 2.8664,
      "aei_vision": 0.074868,
      "text_ratio": 0.974546,
      "vision_ratio": 0.025454
    },
    "middle": {
      "mdi": 42.975093,
      "aei_text": 2.882141,
      "aei_vision": 0.067065,
      "text_ratio": 0.97726,
      "vision_ratio": 0.02274
    },
    "late": {
      "mdi": 43.924763,
      "aei_text": 2.884938,
      "aei_vision": 0.065679,
      "text_ratio": 0.977741,
      "vision_ratio": 0.022259
    },
    "all": {
      "mdi": 43.924763,
      "aei_text": 2.877825,
      "aei_vision": 0.069205,
      "text_ratio": 0.977741,
      "vision_ratio": 0.022259
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977741,
      0.022259
    ],
    "text_vision_ratio": "0.977741:0.022259",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 254.0,
    "text_tokens": 161.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.62775,
      "aei_text": 2.506552,
      "aei_vision": 0.045059,
      "text_ratio": 0.982341,
      "vision_ratio": 0.017659
    },
    "middle": {
      "mdi": 66.969198,
      "aei_text": 2.518314,
      "aei_vision": 0.037604,
      "text_ratio": 0.985287,
      "vision_ratio": 0.014713
    },
    "late": {
      "mdi": 59.778433,
      "aei_text": 2.511361,
      "aei_vision": 0.042011,
      "text_ratio": 0.983547,
      "vision_ratio": 0.016453
    },
    "all": {
      "mdi": 59.778433,
      "aei_text": 2.512076,
      "aei_vision": 0.041558,
      "text_ratio": 0.983547,
      "vision_ratio": 0.016453
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983547,
      0.016453
    ],
    "text_vision_ratio": "0.983547:0.016453",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 254.0,
    "text_tokens": 161.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.801339,
      "aei_text": 2.506767,
      "aei_vision": 0.044923,
      "text_ratio": 0.982395,
      "vision_ratio": 0.017605
    },
    "middle": {
      "mdi": 66.983838,
      "aei_text": 2.518327,
      "aei_vision": 0.037596,
      "text_ratio": 0.985291,
      "vision_ratio": 0.014709
    },
    "late": {
      "mdi": 53.646527,
      "aei_text": 2.504002,
      "aei_vision": 0.046676,
      "text_ratio": 0.981701,
      "vision_ratio": 0.018299
    },
    "all": {
      "mdi": 53.646527,
      "aei_text": 2.509699,
      "aei_vision": 0.043065,
      "text_ratio": 0.981701,
      "vision_ratio": 0.018299
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981701,
      0.018299
    ],
    "text_vision_ratio": "0.981701:0.018299",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 296.0,
    "text_tokens": 170.0,
    "total_tokens": 466.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.466718,
      "aei_text": 2.628096,
      "aei_vision": 0.064945,
      "text_ratio": 0.975884,
      "vision_ratio": 0.024116
    },
    "middle": {
      "mdi": 54.145561,
      "aei_text": 2.655774,
      "aei_vision": 0.049049,
      "text_ratio": 0.981866,
      "vision_ratio": 0.018134
    },
    "late": {
      "mdi": 50.520297,
      "aei_text": 2.64985,
      "aei_vision": 0.052451,
      "text_ratio": 0.98059,
      "vision_ratio": 0.01941
    },
    "all": {
      "mdi": 50.520297,
      "aei_text": 2.644571,
      "aei_vision": 0.055483,
      "text_ratio": 0.98059,
      "vision_ratio": 0.01941
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98059,
      0.01941
    ],
    "text_vision_ratio": "0.980590:0.019410",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 296.0,
    "text_tokens": 170.0,
    "total_tokens": 466.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.535727,
      "aei_text": 2.628281,
      "aei_vision": 0.064839,
      "text_ratio": 0.975924,
      "vision_ratio": 0.024076
    },
    "middle": {
      "mdi": 69.899042,
      "aei_text": 2.674554,
      "aei_vision": 0.038263,
      "text_ratio": 0.985895,
      "vision_ratio": 0.014105
    },
    "late": {
      "mdi": 70.99545,
      "aei_text": 2.675558,
      "aei_vision": 0.037686,
      "text_ratio": 0.98611,
      "vision_ratio": 0.01389
    },
    "all": {
      "mdi": 70.99545,
      "aei_text": 2.65945,
      "aei_vision": 0.046938,
      "text_ratio": 0.98611,
      "vision_ratio": 0.01389
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98611,
      0.01389
    ],
    "text_vision_ratio": "0.986110:0.013890",
    "skip_reason": null
  }
}
```


## === Rollout Step 27 ===
Step: 26/43 | 2025-10-22 18:51:25

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 36.262 | 54.055 | 43.223 | 43.223 |
| MDI Std | 14.152 | 29.123 | 20.517 | 20.517 |
| Vision Tokens | 344.6 ± 49.6 |
| Text Tokens | 164.0 ± 2.6 |
| Total Tokens | 508.6 ± 49.3 |
| Vision Ratio | 0.674 |
| Text Ratio | 0.326 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 167.0,
    "total_tokens": 491.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.523906,
      "aei_text": 2.80255,
      "aei_vision": 0.070908,
      "text_ratio": 0.975323,
      "vision_ratio": 0.024677
    },
    "middle": {
      "mdi": 83.363745,
      "aei_text": 2.873251,
      "aei_vision": 0.034466,
      "text_ratio": 0.988147,
      "vision_ratio": 0.011853
    },
    "late": {
      "mdi": 54.67001,
      "aei_text": 2.839357,
      "aei_vision": 0.051936,
      "text_ratio": 0.982037,
      "vision_ratio": 0.017963
    },
    "all": {
      "mdi": 54.67001,
      "aei_text": 2.838388,
      "aei_vision": 0.052436,
      "text_ratio": 0.982037,
      "vision_ratio": 0.017963
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982037,
      0.017963
    ],
    "text_vision_ratio": "0.982037:0.017963",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 167.0,
    "total_tokens": 491.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.201217,
      "aei_text": 2.807899,
      "aei_vision": 0.068151,
      "text_ratio": 0.976304,
      "vision_ratio": 0.023696
    },
    "middle": {
      "mdi": 60.591039,
      "aei_text": 2.848898,
      "aei_vision": 0.047018,
      "text_ratio": 0.983764,
      "vision_ratio": 0.016236
    },
    "late": {
      "mdi": 40.945332,
      "aei_text": 2.80711,
      "aei_vision": 0.068558,
      "text_ratio": 0.976159,
      "vision_ratio": 0.023841
    },
    "all": {
      "mdi": 40.945332,
      "aei_text": 2.821298,
      "aei_vision": 0.061245,
      "text_ratio": 0.976159,
      "vision_ratio": 0.023841
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976159,
      0.023841
    ],
    "text_vision_ratio": "0.976159:0.023841",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.273912,
      "aei_text": 2.925826,
      "aei_vision": 0.067612,
      "text_ratio": 0.977413,
      "vision_ratio": 0.022587
    },
    "middle": {
      "mdi": 95.812477,
      "aei_text": 3.000787,
      "aei_vision": 0.031319,
      "text_ratio": 0.989671,
      "vision_ratio": 0.010329
    },
    "late": {
      "mdi": 79.725878,
      "aei_text": 2.988064,
      "aei_vision": 0.037479,
      "text_ratio": 0.987612,
      "vision_ratio": 0.012388
    },
    "all": {
      "mdi": 79.725878,
      "aei_text": 2.971536,
      "aei_vision": 0.045481,
      "text_ratio": 0.987612,
      "vision_ratio": 0.012388
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987612,
      0.012388
    ],
    "text_vision_ratio": "0.987612:0.012388",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.263684,
      "aei_text": 2.925794,
      "aei_vision": 0.067627,
      "text_ratio": 0.977408,
      "vision_ratio": 0.022592
    },
    "middle": {
      "mdi": 69.572702,
      "aei_text": 2.977092,
      "aei_vision": 0.042791,
      "text_ratio": 0.98583,
      "vision_ratio": 0.01417
    },
    "late": {
      "mdi": 51.010543,
      "aei_text": 2.946182,
      "aei_vision": 0.057756,
      "text_ratio": 0.980773,
      "vision_ratio": 0.019227
    },
    "all": {
      "mdi": 51.010543,
      "aei_text": 2.949685,
      "aei_vision": 0.05606,
      "text_ratio": 0.980773,
      "vision_ratio": 0.019227
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980773,
      0.019227
    ],
    "text_vision_ratio": "0.980773:0.019227",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.353415,
      "aei_text": 2.910436,
      "aei_vision": 0.20277,
      "text_ratio": 0.934868,
      "vision_ratio": 0.065132
    },
    "middle": {
      "mdi": 9.565828,
      "aei_text": 2.715964,
      "aei_vision": 0.283924,
      "text_ratio": 0.905355,
      "vision_ratio": 0.094645
    },
    "late": {
      "mdi": 11.530651,
      "aei_text": 2.811952,
      "aei_vision": 0.243868,
      "text_ratio": 0.920196,
      "vision_ratio": 0.079804
    },
    "all": {
      "mdi": 11.530651,
      "aei_text": 2.812768,
      "aei_vision": 0.243527,
      "text_ratio": 0.920196,
      "vision_ratio": 0.079804
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.920196,
      0.079804
    ],
    "text_vision_ratio": "0.920196:0.079804",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.020584,
      "aei_text": 2.868429,
      "aei_vision": 0.2203,
      "text_ratio": 0.928676,
      "vision_ratio": 0.071324
    },
    "middle": {
      "mdi": 10.66036,
      "aei_text": 2.772999,
      "aei_vision": 0.260122,
      "text_ratio": 0.914239,
      "vision_ratio": 0.085761
    },
    "late": {
      "mdi": 13.506003,
      "aei_text": 2.884543,
      "aei_vision": 0.213575,
      "text_ratio": 0.931063,
      "vision_ratio": 0.068937
    },
    "all": {
      "mdi": 13.506003,
      "aei_text": 2.841993,
      "aei_vision": 0.231331,
      "text_ratio": 0.931063,
      "vision_ratio": 0.068937
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931063,
      0.068937
    ],
    "text_vision_ratio": "0.931063:0.068937",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 162.0,
    "total_tokens": 486.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.283023,
      "aei_text": 2.8675,
      "aei_vision": 0.06625,
      "text_ratio": 0.977418,
      "vision_ratio": 0.022582
    },
    "middle": {
      "mdi": 63.305857,
      "aei_text": 2.908125,
      "aei_vision": 0.045938,
      "text_ratio": 0.984449,
      "vision_ratio": 0.015551
    },
    "late": {
      "mdi": 59.570934,
      "aei_text": 2.902551,
      "aei_vision": 0.048724,
      "text_ratio": 0.98349,
      "vision_ratio": 0.01651
    },
    "all": {
      "mdi": 59.570934,
      "aei_text": 2.892716,
      "aei_vision": 0.053642,
      "text_ratio": 0.98349,
      "vision_ratio": 0.01651
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98349,
      0.01651
    ],
    "text_vision_ratio": "0.983490:0.016510",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 162.0,
    "total_tokens": 486.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.138423,
      "aei_text": 2.872715,
      "aei_vision": 0.063642,
      "text_ratio": 0.978326,
      "vision_ratio": 0.021674
    },
    "middle": {
      "mdi": 92.512251,
      "aei_text": 2.936516,
      "aei_vision": 0.031742,
      "text_ratio": 0.989306,
      "vision_ratio": 0.010694
    },
    "late": {
      "mdi": 67.629511,
      "aei_text": 2.91383,
      "aei_vision": 0.043085,
      "text_ratio": 0.985429,
      "vision_ratio": 0.014571
    },
    "all": {
      "mdi": 67.629511,
      "aei_text": 2.90768,
      "aei_vision": 0.04616,
      "text_ratio": 0.985429,
      "vision_ratio": 0.014571
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985429,
      0.014571
    ],
    "text_vision_ratio": "0.985429:0.014571",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.99038,
      "aei_text": 2.350589,
      "aei_vision": 0.067178,
      "text_ratio": 0.972215,
      "vision_ratio": 0.027785
    },
    "middle": {
      "mdi": 52.639553,
      "aei_text": 2.382327,
      "aei_vision": 0.045257,
      "text_ratio": 0.981357,
      "vision_ratio": 0.018643
    },
    "late": {
      "mdi": 48.485473,
      "aei_text": 2.376876,
      "aei_vision": 0.049022,
      "text_ratio": 0.979792,
      "vision_ratio": 0.020208
    },
    "all": {
      "mdi": 48.485473,
      "aei_text": 2.369932,
      "aei_vision": 0.053818,
      "text_ratio": 0.979792,
      "vision_ratio": 0.020208
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979792,
      0.020208
    ],
    "text_vision_ratio": "0.979792:0.020208",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.182761,
      "aei_text": 2.345512,
      "aei_vision": 0.070685,
      "text_ratio": 0.970745,
      "vision_ratio": 0.029255
    },
    "middle": {
      "mdi": 47.613815,
      "aei_text": 2.375614,
      "aei_vision": 0.049893,
      "text_ratio": 0.97943,
      "vision_ratio": 0.02057
    },
    "late": {
      "mdi": 46.661776,
      "aei_text": 2.374185,
      "aei_vision": 0.050881,
      "text_ratio": 0.979019,
      "vision_ratio": 0.020981
    },
    "all": {
      "mdi": 46.661776,
      "aei_text": 2.365106,
      "aei_vision": 0.057152,
      "text_ratio": 0.979019,
      "vision_ratio": 0.020981
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979019,
      0.020981
    ],
    "text_vision_ratio": "0.979019:0.020981",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.313118,
      "aei_text": 2.952723,
      "aei_vision": 0.071472,
      "text_ratio": 0.976367,
      "vision_ratio": 0.023633
    },
    "middle": {
      "mdi": 83.57872,
      "aei_text": 3.026867,
      "aei_vision": 0.036216,
      "text_ratio": 0.988177,
      "vision_ratio": 0.011823
    },
    "late": {
      "mdi": 65.273001,
      "aei_text": 3.006174,
      "aei_vision": 0.046055,
      "text_ratio": 0.984911,
      "vision_ratio": 0.015089
    },
    "all": {
      "mdi": 65.273001,
      "aei_text": 2.995257,
      "aei_vision": 0.051247,
      "text_ratio": 0.984911,
      "vision_ratio": 0.015089
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984911,
      0.015089
    ],
    "text_vision_ratio": "0.984911:0.015089",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.328436,
      "aei_text": 2.962484,
      "aei_vision": 0.06683,
      "text_ratio": 0.977939,
      "vision_ratio": 0.022061
    },
    "middle": {
      "mdi": 41.823544,
      "aei_text": 2.95447,
      "aei_vision": 0.070641,
      "text_ratio": 0.976648,
      "vision_ratio": 0.023352
    },
    "late": {
      "mdi": 32.616462,
      "aei_text": 2.915073,
      "aei_vision": 0.089374,
      "text_ratio": 0.970253,
      "vision_ratio": 0.029747
    },
    "all": {
      "mdi": 32.616462,
      "aei_text": 2.944001,
      "aei_vision": 0.075619,
      "text_ratio": 0.970253,
      "vision_ratio": 0.029747
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970253,
      0.029747
    ],
    "text_vision_ratio": "0.970253:0.029747",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.416414,
      "aei_text": 3.328414,
      "aei_vision": 0.05797,
      "text_ratio": 0.982882,
      "vision_ratio": 0.017118
    },
    "middle": {
      "mdi": 44.51263,
      "aei_text": 3.289063,
      "aei_vision": 0.073891,
      "text_ratio": 0.978028,
      "vision_ratio": 0.021972
    },
    "late": {
      "mdi": 38.088843,
      "aei_text": 3.260138,
      "aei_vision": 0.085593,
      "text_ratio": 0.974417,
      "vision_ratio": 0.025583
    },
    "all": {
      "mdi": 38.088843,
      "aei_text": 3.292541,
      "aei_vision": 0.072483,
      "text_ratio": 0.974417,
      "vision_ratio": 0.025583
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974417,
      0.025583
    ],
    "text_vision_ratio": "0.974417:0.025583",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.911057,
      "aei_text": 3.327195,
      "aei_vision": 0.058463,
      "text_ratio": 0.982732,
      "vision_ratio": 0.017268
    },
    "middle": {
      "mdi": 82.366826,
      "aei_text": 3.370553,
      "aei_vision": 0.040921,
      "text_ratio": 0.988005,
      "vision_ratio": 0.011995
    },
    "late": {
      "mdi": 53.393246,
      "aei_text": 3.318096,
      "aei_vision": 0.062144,
      "text_ratio": 0.981615,
      "vision_ratio": 0.018385
    },
    "all": {
      "mdi": 53.393246,
      "aei_text": 3.338615,
      "aei_vision": 0.053843,
      "text_ratio": 0.981615,
      "vision_ratio": 0.018385
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981615,
      0.018385
    ],
    "text_vision_ratio": "0.981615:0.018385",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.409661,
      "aei_text": 2.912062,
      "aei_vision": 0.202091,
      "text_ratio": 0.935106,
      "vision_ratio": 0.064894
    },
    "middle": {
      "mdi": 15.502728,
      "aei_text": 2.941637,
      "aei_vision": 0.18975,
      "text_ratio": 0.939404,
      "vision_ratio": 0.060596
    },
    "late": {
      "mdi": 16.058052,
      "aei_text": 2.955319,
      "aei_vision": 0.18404,
      "text_ratio": 0.941377,
      "vision_ratio": 0.058623
    },
    "all": {
      "mdi": 16.058052,
      "aei_text": 2.936346,
      "aei_vision": 0.191957,
      "text_ratio": 0.941377,
      "vision_ratio": 0.058623
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.941377,
      0.058623
    ],
    "text_vision_ratio": "0.941377:0.058623",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.586185,
      "aei_text": 2.917096,
      "aei_vision": 0.19999,
      "text_ratio": 0.935841,
      "vision_ratio": 0.064159
    },
    "middle": {
      "mdi": 11.464405,
      "aei_text": 2.809159,
      "aei_vision": 0.245033,
      "text_ratio": 0.919772,
      "vision_ratio": 0.080228
    },
    "late": {
      "mdi": 12.40644,
      "aei_text": 2.846526,
      "aei_vision": 0.229439,
      "text_ratio": 0.925409,
      "vision_ratio": 0.074591
    },
    "all": {
      "mdi": 12.40644,
      "aei_text": 2.857585,
      "aei_vision": 0.224825,
      "text_ratio": 0.925409,
      "vision_ratio": 0.074591
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.925409,
      0.074591
    ],
    "text_vision_ratio": "0.925409:0.074591",
    "skip_reason": null
  }
}
```


## === Rollout Step 28 ===
Step: 27/43 | 2025-10-22 18:52:41

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 42.349 | 60.925 | 48.441 | 48.441 |
| MDI Std | 12.637 | 26.973 | 18.667 | 18.667 |
| Vision Tokens | 375.8 ± 22.3 |
| Text Tokens | 167.0 ± 9.7 |
| Total Tokens | 542.8 ± 18.0 |
| Vision Ratio | 0.692 |
| Text Ratio | 0.308 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.963748,
      "aei_text": 3.041798,
      "aei_vision": 0.058537,
      "text_ratio": 0.981119,
      "vision_ratio": 0.018881
    },
    "middle": {
      "mdi": 97.518404,
      "aei_text": 3.099812,
      "aei_vision": 0.031787,
      "text_ratio": 0.98985,
      "vision_ratio": 0.01015
    },
    "late": {
      "mdi": 67.912203,
      "aei_text": 3.070689,
      "aei_vision": 0.045216,
      "text_ratio": 0.985489,
      "vision_ratio": 0.014511
    },
    "all": {
      "mdi": 67.912203,
      "aei_text": 3.070766,
      "aei_vision": 0.04518,
      "text_ratio": 0.985489,
      "vision_ratio": 0.014511
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985489,
      0.014511
    ],
    "text_vision_ratio": "0.985489:0.014511",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.069015,
      "aei_text": 3.034626,
      "aei_vision": 0.061844,
      "text_ratio": 0.980028,
      "vision_ratio": 0.019972
    },
    "middle": {
      "mdi": 64.156541,
      "aei_text": 3.065136,
      "aei_vision": 0.047776,
      "text_ratio": 0.984652,
      "vision_ratio": 0.015348
    },
    "late": {
      "mdi": 51.994696,
      "aei_text": 3.041871,
      "aei_vision": 0.058503,
      "text_ratio": 0.98113,
      "vision_ratio": 0.01887
    },
    "all": {
      "mdi": 51.994696,
      "aei_text": 3.047213,
      "aei_vision": 0.05604,
      "text_ratio": 0.98113,
      "vision_ratio": 0.01887
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98113,
      0.01887
    ],
    "text_vision_ratio": "0.981130:0.018870",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.331482,
      "aei_text": 3.222167,
      "aei_vision": 0.072683,
      "text_ratio": 0.97794,
      "vision_ratio": 0.02206
    },
    "middle": {
      "mdi": 60.491569,
      "aei_text": 3.266924,
      "aei_vision": 0.054006,
      "text_ratio": 0.983738,
      "vision_ratio": 0.016262
    },
    "late": {
      "mdi": 56.022835,
      "aei_text": 3.257024,
      "aei_vision": 0.058137,
      "text_ratio": 0.982463,
      "vision_ratio": 0.017537
    },
    "all": {
      "mdi": 56.022835,
      "aei_text": 3.248706,
      "aei_vision": 0.061609,
      "text_ratio": 0.982463,
      "vision_ratio": 0.017537
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982463,
      0.017537
    ],
    "text_vision_ratio": "0.982463:0.017537",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.694932,
      "aei_text": 3.215845,
      "aei_vision": 0.075321,
      "text_ratio": 0.977114,
      "vision_ratio": 0.022886
    },
    "middle": {
      "mdi": 42.601626,
      "aei_text": 3.215471,
      "aei_vision": 0.075478,
      "text_ratio": 0.977065,
      "vision_ratio": 0.022935
    },
    "late": {
      "mdi": 44.453427,
      "aei_text": 3.22262,
      "aei_vision": 0.072494,
      "text_ratio": 0.977999,
      "vision_ratio": 0.022001
    },
    "all": {
      "mdi": 44.453427,
      "aei_text": 3.217979,
      "aei_vision": 0.074431,
      "text_ratio": 0.977999,
      "vision_ratio": 0.022001
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977999,
      0.022001
    ],
    "text_vision_ratio": "0.977999:0.022001",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 181.0,
    "total_tokens": 528.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.469915,
      "aei_text": 2.782,
      "aei_vision": 0.070484,
      "text_ratio": 0.97529,
      "vision_ratio": 0.02471
    },
    "middle": {
      "mdi": 23.537829,
      "aei_text": 2.697425,
      "aei_vision": 0.1146,
      "text_ratio": 0.959247,
      "vision_ratio": 0.040753
    },
    "late": {
      "mdi": 20.917167,
      "aei_text": 2.67221,
      "aei_vision": 0.127752,
      "text_ratio": 0.954374,
      "vision_ratio": 0.045626
    },
    "all": {
      "mdi": 20.917167,
      "aei_text": 2.717222,
      "aei_vision": 0.104273,
      "text_ratio": 0.954374,
      "vision_ratio": 0.045626
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954374,
      0.045626
    ],
    "text_vision_ratio": "0.954374:0.045626",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 181.0,
    "total_tokens": 528.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.587275,
      "aei_text": 2.782382,
      "aei_vision": 0.070285,
      "text_ratio": 0.975362,
      "vision_ratio": 0.024638
    },
    "middle": {
      "mdi": 47.330709,
      "aei_text": 2.803569,
      "aei_vision": 0.059234,
      "text_ratio": 0.979309,
      "vision_ratio": 0.020691
    },
    "late": {
      "mdi": 27.8846,
      "aei_text": 2.72947,
      "aei_vision": 0.097884,
      "text_ratio": 0.965379,
      "vision_ratio": 0.034621
    },
    "all": {
      "mdi": 27.8846,
      "aei_text": 2.771802,
      "aei_vision": 0.075803,
      "text_ratio": 0.965379,
      "vision_ratio": 0.034621
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965379,
      0.034621
    ],
    "text_vision_ratio": "0.965379:0.034621",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 183.0,
    "total_tokens": 530.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.285716,
      "aei_text": 2.762824,
      "aei_vision": 0.070326,
      "text_ratio": 0.975177,
      "vision_ratio": 0.024823
    },
    "middle": {
      "mdi": 56.469572,
      "aei_text": 2.802085,
      "aei_vision": 0.049621,
      "text_ratio": 0.982599,
      "vision_ratio": 0.017401
    },
    "late": {
      "mdi": 59.123803,
      "aei_text": 2.806177,
      "aei_vision": 0.047463,
      "text_ratio": 0.983368,
      "vision_ratio": 0.016632
    },
    "all": {
      "mdi": 59.123803,
      "aei_text": 2.790362,
      "aei_vision": 0.055803,
      "text_ratio": 0.983368,
      "vision_ratio": 0.016632
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983368,
      0.016632
    ],
    "text_vision_ratio": "0.983368:0.016632",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 183.0,
    "total_tokens": 530.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.089343,
      "aei_text": 2.762185,
      "aei_vision": 0.070663,
      "text_ratio": 0.975056,
      "vision_ratio": 0.024944
    },
    "middle": {
      "mdi": 45.028759,
      "aei_text": 2.779144,
      "aei_vision": 0.061719,
      "text_ratio": 0.978274,
      "vision_ratio": 0.021726
    },
    "late": {
      "mdi": 44.704999,
      "aei_text": 2.778331,
      "aei_vision": 0.062148,
      "text_ratio": 0.978121,
      "vision_ratio": 0.021879
    },
    "all": {
      "mdi": 44.704999,
      "aei_text": 2.773221,
      "aei_vision": 0.064843,
      "text_ratio": 0.978121,
      "vision_ratio": 0.021879
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978121,
      0.021879
    ],
    "text_vision_ratio": "0.978121:0.021879",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.880605,
      "aei_text": 3.294043,
      "aei_vision": 0.066039,
      "text_ratio": 0.980346,
      "vision_ratio": 0.019654
    },
    "middle": {
      "mdi": 81.701636,
      "aei_text": 3.355375,
      "aei_vision": 0.041069,
      "text_ratio": 0.987908,
      "vision_ratio": 0.012092
    },
    "late": {
      "mdi": 53.053186,
      "aei_text": 3.303314,
      "aei_vision": 0.062264,
      "text_ratio": 0.9815,
      "vision_ratio": 0.0185
    },
    "all": {
      "mdi": 53.053186,
      "aei_text": 3.317574,
      "aei_vision": 0.056459,
      "text_ratio": 0.9815,
      "vision_ratio": 0.0185
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9815,
      0.0185
    ],
    "text_vision_ratio": "0.981500:0.018500",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.64196,
      "aei_text": 3.296369,
      "aei_vision": 0.065092,
      "text_ratio": 0.980636,
      "vision_ratio": 0.019364
    },
    "middle": {
      "mdi": 98.08991,
      "aei_text": 3.371817,
      "aei_vision": 0.034375,
      "text_ratio": 0.989908,
      "vision_ratio": 0.010092
    },
    "late": {
      "mdi": 77.117962,
      "aei_text": 3.349565,
      "aei_vision": 0.043434,
      "text_ratio": 0.987199,
      "vision_ratio": 0.012801
    },
    "all": {
      "mdi": 77.117962,
      "aei_text": 3.339254,
      "aei_vision": 0.047632,
      "text_ratio": 0.987199,
      "vision_ratio": 0.012801
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987199,
      0.012801
    ],
    "text_vision_ratio": "0.987199:0.012801",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 172.0,
    "total_tokens": 565.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.661504,
      "aei_text": 2.782717,
      "aei_vision": 0.219778,
      "text_ratio": 0.926802,
      "vision_ratio": 0.073198
    },
    "middle": {
      "mdi": 17.293779,
      "aei_text": 2.901529,
      "aei_vision": 0.167779,
      "text_ratio": 0.945337,
      "vision_ratio": 0.054663
    },
    "late": {
      "mdi": 17.206078,
      "aei_text": 2.899804,
      "aei_vision": 0.168534,
      "text_ratio": 0.945073,
      "vision_ratio": 0.054927
    },
    "all": {
      "mdi": 17.206078,
      "aei_text": 2.861356,
      "aei_vision": 0.185361,
      "text_ratio": 0.945073,
      "vision_ratio": 0.054927
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.945073,
      0.054927
    ],
    "text_vision_ratio": "0.945073:0.054927",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 172.0,
    "total_tokens": 565.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.427777,
      "aei_text": 2.737537,
      "aei_vision": 0.239551,
      "text_ratio": 0.919535,
      "vision_ratio": 0.080465
    },
    "middle": {
      "mdi": 13.16396,
      "aei_text": 2.799049,
      "aei_vision": 0.21263,
      "text_ratio": 0.929398,
      "vision_ratio": 0.070602
    },
    "late": {
      "mdi": 13.743346,
      "aei_text": 2.816611,
      "aei_vision": 0.204944,
      "text_ratio": 0.932173,
      "vision_ratio": 0.067827
    },
    "all": {
      "mdi": 13.743346,
      "aei_text": 2.784388,
      "aei_vision": 0.219047,
      "text_ratio": 0.932173,
      "vision_ratio": 0.067827
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.932173,
      0.067827
    ],
    "text_vision_ratio": "0.932173:0.067827",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.88902,
      "aei_text": 3.343673,
      "aei_vision": 0.05776,
      "text_ratio": 0.983019,
      "vision_ratio": 0.016981
    },
    "middle": {
      "mdi": 97.208473,
      "aei_text": 3.400335,
      "aei_vision": 0.03498,
      "text_ratio": 0.989818,
      "vision_ratio": 0.010182
    },
    "late": {
      "mdi": 73.027861,
      "aei_text": 3.372475,
      "aei_vision": 0.046181,
      "text_ratio": 0.986492,
      "vision_ratio": 0.013508
    },
    "all": {
      "mdi": 73.027861,
      "aei_text": 3.372155,
      "aei_vision": 0.046309,
      "text_ratio": 0.986492,
      "vision_ratio": 0.013508
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986492,
      0.013508
    ],
    "text_vision_ratio": "0.986492:0.013508",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.195852,
      "aei_text": 3.319508,
      "aei_vision": 0.067475,
      "text_ratio": 0.980078,
      "vision_ratio": 0.019922
    },
    "middle": {
      "mdi": 81.587215,
      "aei_text": 3.384169,
      "aei_vision": 0.041479,
      "text_ratio": 0.987892,
      "vision_ratio": 0.012108
    },
    "late": {
      "mdi": 57.380349,
      "aei_text": 3.342452,
      "aei_vision": 0.058251,
      "text_ratio": 0.982871,
      "vision_ratio": 0.017129
    },
    "all": {
      "mdi": 57.380349,
      "aei_text": 3.348707,
      "aei_vision": 0.055736,
      "text_ratio": 0.982871,
      "vision_ratio": 0.017129
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982871,
      0.017129
    ],
    "text_vision_ratio": "0.982871:0.017129",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.376554,
      "aei_text": 3.326302,
      "aei_vision": 0.064744,
      "text_ratio": 0.980907,
      "vision_ratio": 0.019093
    },
    "middle": {
      "mdi": 73.560126,
      "aei_text": 3.373279,
      "aei_vision": 0.045857,
      "text_ratio": 0.986588,
      "vision_ratio": 0.013412
    },
    "late": {
      "mdi": 56.096756,
      "aei_text": 3.339278,
      "aei_vision": 0.059527,
      "text_ratio": 0.982486,
      "vision_ratio": 0.017514
    },
    "all": {
      "mdi": 56.096756,
      "aei_text": 3.346293,
      "aei_vision": 0.056706,
      "text_ratio": 0.982486,
      "vision_ratio": 0.017514
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982486,
      0.017514
    ],
    "text_vision_ratio": "0.982486:0.017514",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 158.0,
    "total_tokens": 551.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.019038,
      "aei_text": 3.318931,
      "aei_vision": 0.067707,
      "text_ratio": 0.980008,
      "vision_ratio": 0.019992
    },
    "middle": {
      "mdi": 75.057518,
      "aei_text": 3.375481,
      "aei_vision": 0.044972,
      "text_ratio": 0.986852,
      "vision_ratio": 0.013148
    },
    "late": {
      "mdi": 54.414669,
      "aei_text": 3.334901,
      "aei_vision": 0.061287,
      "text_ratio": 0.981954,
      "vision_ratio": 0.018046
    },
    "all": {
      "mdi": 54.414669,
      "aei_text": 3.343099,
      "aei_vision": 0.057991,
      "text_ratio": 0.981954,
      "vision_ratio": 0.018046
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981954,
      0.018046
    ],
    "text_vision_ratio": "0.981954:0.018046",
    "skip_reason": null
  }
}
```


## === Rollout Step 29 ===
Step: 28/43 | 2025-10-22 18:53:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.747 | 53.219 | 44.280 | 44.280 |
| MDI Std | 13.318 | 21.587 | 15.877 | 15.877 |
| Vision Tokens | 359.8 ± 69.7 |
| Text Tokens | 165.4 ± 3.2 |
| Total Tokens | 525.1 ± 67.5 |
| Vision Ratio | 0.679 |
| Text Ratio | 0.321 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.298144,
      "aei_text": 2.967052,
      "aei_vision": 0.058989,
      "text_ratio": 0.980506,
      "vision_ratio": 0.019494
    },
    "middle": {
      "mdi": 79.180484,
      "aei_text": 3.010874,
      "aei_vision": 0.038025,
      "text_ratio": 0.987528,
      "vision_ratio": 0.012472
    },
    "late": {
      "mdi": 51.634671,
      "aei_text": 2.97012,
      "aei_vision": 0.057522,
      "text_ratio": 0.981001,
      "vision_ratio": 0.018999
    },
    "all": {
      "mdi": 51.634671,
      "aei_text": 2.982678,
      "aei_vision": 0.051514,
      "text_ratio": 0.981001,
      "vision_ratio": 0.018999
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981001,
      0.018999
    ],
    "text_vision_ratio": "0.981001:0.018999",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.198575,
      "aei_text": 2.966818,
      "aei_vision": 0.059102,
      "text_ratio": 0.980468,
      "vision_ratio": 0.019532
    },
    "middle": {
      "mdi": 64.898399,
      "aei_text": 2.993928,
      "aei_vision": 0.046133,
      "text_ratio": 0.984825,
      "vision_ratio": 0.015175
    },
    "late": {
      "mdi": 44.747412,
      "aei_text": 2.952439,
      "aei_vision": 0.06598,
      "text_ratio": 0.978141,
      "vision_ratio": 0.021859
    },
    "all": {
      "mdi": 44.747412,
      "aei_text": 2.971056,
      "aei_vision": 0.057074,
      "text_ratio": 0.978141,
      "vision_ratio": 0.021859
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978141,
      0.021859
    ],
    "text_vision_ratio": "0.978141:0.021859",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 170.0,
    "total_tokens": 517.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.172222,
      "aei_text": 2.897527,
      "aei_vision": 0.070376,
      "text_ratio": 0.976288,
      "vision_ratio": 0.023712
    },
    "middle": {
      "mdi": 53.665801,
      "aei_text": 2.929744,
      "aei_vision": 0.054592,
      "text_ratio": 0.981707,
      "vision_ratio": 0.018293
    },
    "late": {
      "mdi": 37.779862,
      "aei_text": 2.88529,
      "aei_vision": 0.076371,
      "text_ratio": 0.974213,
      "vision_ratio": 0.025787
    },
    "all": {
      "mdi": 37.779862,
      "aei_text": 2.904194,
      "aei_vision": 0.06711,
      "text_ratio": 0.974213,
      "vision_ratio": 0.025787
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974213,
      0.025787
    ],
    "text_vision_ratio": "0.974213:0.025787",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 170.0,
    "total_tokens": 517.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.678744,
      "aei_text": 2.899191,
      "aei_vision": 0.06956,
      "text_ratio": 0.976569,
      "vision_ratio": 0.023431
    },
    "middle": {
      "mdi": 41.371151,
      "aei_text": 2.898185,
      "aei_vision": 0.070053,
      "text_ratio": 0.976399,
      "vision_ratio": 0.023601
    },
    "late": {
      "mdi": 32.271831,
      "aei_text": 2.860266,
      "aei_vision": 0.08863,
      "text_ratio": 0.969945,
      "vision_ratio": 0.030055
    },
    "all": {
      "mdi": 32.271831,
      "aei_text": 2.885888,
      "aei_vision": 0.076078,
      "text_ratio": 0.969945,
      "vision_ratio": 0.030055
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969945,
      0.030055
    ],
    "text_vision_ratio": "0.969945:0.030055",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 65.468341,
      "aei_text": 2.994741,
      "aei_vision": 0.045743,
      "text_ratio": 0.984955,
      "vision_ratio": 0.015045
    },
    "middle": {
      "mdi": 53.090837,
      "aei_text": 2.973293,
      "aei_vision": 0.056004,
      "text_ratio": 0.981513,
      "vision_ratio": 0.018487
    },
    "late": {
      "mdi": 44.9531,
      "aei_text": 2.953042,
      "aei_vision": 0.065692,
      "text_ratio": 0.978239,
      "vision_ratio": 0.021761
    },
    "all": {
      "mdi": 44.9531,
      "aei_text": 2.973696,
      "aei_vision": 0.055811,
      "text_ratio": 0.978239,
      "vision_ratio": 0.021761
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978239,
      0.021761
    ],
    "text_vision_ratio": "0.978239:0.021761",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.700544,
      "aei_text": 2.996454,
      "aei_vision": 0.044924,
      "text_ratio": 0.985229,
      "vision_ratio": 0.014771
    },
    "middle": {
      "mdi": 37.410206,
      "aei_text": 2.92682,
      "aei_vision": 0.078236,
      "text_ratio": 0.973965,
      "vision_ratio": 0.026035
    },
    "late": {
      "mdi": 27.620683,
      "aei_text": 2.872935,
      "aei_vision": 0.104014,
      "text_ratio": 0.96506,
      "vision_ratio": 0.03494
    },
    "all": {
      "mdi": 27.620683,
      "aei_text": 2.932075,
      "aei_vision": 0.075722,
      "text_ratio": 0.96506,
      "vision_ratio": 0.03494
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96506,
      0.03494
    ],
    "text_vision_ratio": "0.965060:0.034940",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.744283,
      "aei_text": 3.250274,
      "aei_vision": 0.06668,
      "text_ratio": 0.979897,
      "vision_ratio": 0.020103
    },
    "middle": {
      "mdi": 91.601399,
      "aei_text": 3.323563,
      "aei_vision": 0.036283,
      "text_ratio": 0.989201,
      "vision_ratio": 0.010799
    },
    "late": {
      "mdi": 64.865985,
      "aei_text": 3.2888,
      "aei_vision": 0.050701,
      "text_ratio": 0.984818,
      "vision_ratio": 0.015182
    },
    "all": {
      "mdi": 64.865985,
      "aei_text": 3.287551,
      "aei_vision": 0.051219,
      "text_ratio": 0.984818,
      "vision_ratio": 0.015182
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984818,
      0.015182
    ],
    "text_vision_ratio": "0.984818:0.015182",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.785182,
      "aei_text": 3.25348,
      "aei_vision": 0.06535,
      "text_ratio": 0.980309,
      "vision_ratio": 0.019691
    },
    "middle": {
      "mdi": 59.367395,
      "aei_text": 3.277919,
      "aei_vision": 0.055214,
      "text_ratio": 0.983435,
      "vision_ratio": 0.016565
    },
    "late": {
      "mdi": 41.988626,
      "aei_text": 3.225812,
      "aei_vision": 0.076826,
      "text_ratio": 0.976738,
      "vision_ratio": 0.023262
    },
    "all": {
      "mdi": 41.988626,
      "aei_text": 3.252405,
      "aei_vision": 0.065796,
      "text_ratio": 0.976738,
      "vision_ratio": 0.023262
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976738,
      0.023262
    ],
    "text_vision_ratio": "0.976738:0.023262",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.408322,
      "aei_text": 3.200839,
      "aei_vision": 0.064783,
      "text_ratio": 0.980162,
      "vision_ratio": 0.019838
    },
    "middle": {
      "mdi": 90.755768,
      "aei_text": 3.26854,
      "aei_vision": 0.036015,
      "text_ratio": 0.989102,
      "vision_ratio": 0.010898
    },
    "late": {
      "mdi": 73.304163,
      "aei_text": 3.248991,
      "aei_vision": 0.044322,
      "text_ratio": 0.986542,
      "vision_ratio": 0.013458
    },
    "all": {
      "mdi": 73.304163,
      "aei_text": 3.239467,
      "aei_vision": 0.048369,
      "text_ratio": 0.986542,
      "vision_ratio": 0.013458
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986542,
      0.013458
    ],
    "text_vision_ratio": "0.986542:0.013458",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.680861,
      "aei_text": 3.207251,
      "aei_vision": 0.062059,
      "text_ratio": 0.981018,
      "vision_ratio": 0.018982
    },
    "middle": {
      "mdi": 37.705045,
      "aei_text": 3.156299,
      "aei_vision": 0.08371,
      "text_ratio": 0.974164,
      "vision_ratio": 0.025836
    },
    "late": {
      "mdi": 32.705625,
      "aei_text": 3.128207,
      "aei_vision": 0.095647,
      "text_ratio": 0.970331,
      "vision_ratio": 0.029669
    },
    "all": {
      "mdi": 32.705625,
      "aei_text": 3.163914,
      "aei_vision": 0.080474,
      "text_ratio": 0.970331,
      "vision_ratio": 0.029669
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.970331,
      0.029669
    ],
    "text_vision_ratio": "0.970331:0.029669",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.686307,
      "aei_text": 3.012123,
      "aei_vision": 0.060623,
      "text_ratio": 0.980271,
      "vision_ratio": 0.019729
    },
    "middle": {
      "mdi": 56.465364,
      "aei_text": 3.027143,
      "aei_vision": 0.053611,
      "text_ratio": 0.982598,
      "vision_ratio": 0.017402
    },
    "late": {
      "mdi": 71.178566,
      "aei_text": 3.050186,
      "aei_vision": 0.042853,
      "text_ratio": 0.986145,
      "vision_ratio": 0.013855
    },
    "all": {
      "mdi": 71.178566,
      "aei_text": 3.029821,
      "aei_vision": 0.05236,
      "text_ratio": 0.986145,
      "vision_ratio": 0.013855
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986145,
      0.013855
    ],
    "text_vision_ratio": "0.986145:0.013855",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.91174,
      "aei_text": 3.010153,
      "aei_vision": 0.061543,
      "text_ratio": 0.979965,
      "vision_ratio": 0.020035
    },
    "middle": {
      "mdi": 53.503349,
      "aei_text": 3.02103,
      "aei_vision": 0.056464,
      "text_ratio": 0.981653,
      "vision_ratio": 0.018347
    },
    "late": {
      "mdi": 48.383442,
      "aei_text": 3.008774,
      "aei_vision": 0.062186,
      "text_ratio": 0.97975,
      "vision_ratio": 0.02025
    },
    "all": {
      "mdi": 48.383442,
      "aei_text": 3.013321,
      "aei_vision": 0.060064,
      "text_ratio": 0.97975,
      "vision_ratio": 0.02025
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97975,
      0.02025
    ],
    "text_vision_ratio": "0.979750:0.020250",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 160.0,
    "total_tokens": 646.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 19.066043,
      "aei_text": 3.482661,
      "aei_vision": 0.182663,
      "text_ratio": 0.950165,
      "vision_ratio": 0.049835
    },
    "middle": {
      "mdi": 22.182299,
      "aei_text": 3.551219,
      "aei_vision": 0.160092,
      "text_ratio": 0.956864,
      "vision_ratio": 0.043136
    },
    "late": {
      "mdi": 30.47908,
      "aei_text": 3.671594,
      "aei_vision": 0.120463,
      "text_ratio": 0.968233,
      "vision_ratio": 0.031767
    },
    "all": {
      "mdi": 30.47908,
      "aei_text": 3.568466,
      "aei_vision": 0.154415,
      "text_ratio": 0.968233,
      "vision_ratio": 0.031767
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968233,
      0.031767
    ],
    "text_vision_ratio": "0.968233:0.031767",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 160.0,
    "total_tokens": 646.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.334311,
      "aei_text": 3.435496,
      "aei_vision": 0.198191,
      "text_ratio": 0.945457,
      "vision_ratio": 0.054543
    },
    "middle": {
      "mdi": 10.922681,
      "aei_text": 3.159008,
      "aei_vision": 0.289215,
      "text_ratio": 0.916126,
      "vision_ratio": 0.083874
    },
    "late": {
      "mdi": 14.157684,
      "aei_text": 3.324283,
      "aei_vision": 0.234804,
      "text_ratio": 0.934027,
      "vision_ratio": 0.065973
    },
    "all": {
      "mdi": 14.157684,
      "aei_text": 3.306258,
      "aei_vision": 0.240738,
      "text_ratio": 0.934027,
      "vision_ratio": 0.065973
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.934027,
      0.065973
    ],
    "text_vision_ratio": "0.934027:0.065973",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 169.0,
    "total_tokens": 387.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.704769,
      "aei_text": 2.203048,
      "aei_vision": 0.067362,
      "text_ratio": 0.970331,
      "vision_ratio": 0.029669
    },
    "middle": {
      "mdi": 37.309907,
      "aei_text": 2.213415,
      "aei_vision": 0.059325,
      "text_ratio": 0.973897,
      "vision_ratio": 0.026103
    },
    "late": {
      "mdi": 34.725839,
      "aei_text": 2.207924,
      "aei_vision": 0.063582,
      "text_ratio": 0.972009,
      "vision_ratio": 0.027991
    },
    "all": {
      "mdi": 34.725839,
      "aei_text": 2.208129,
      "aei_vision": 0.063423,
      "text_ratio": 0.972009,
      "vision_ratio": 0.027991
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972009,
      0.027991
    ],
    "text_vision_ratio": "0.972009:0.027991",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 169.0,
    "total_tokens": 387.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.121422,
      "aei_text": 2.2041,
      "aei_vision": 0.066546,
      "text_ratio": 0.970693,
      "vision_ratio": 0.029307
    },
    "middle": {
      "mdi": 62.075145,
      "aei_text": 2.243324,
      "aei_vision": 0.036139,
      "text_ratio": 0.984146,
      "vision_ratio": 0.015854
    },
    "late": {
      "mdi": 57.677578,
      "aei_text": 2.239847,
      "aei_vision": 0.038834,
      "text_ratio": 0.982958,
      "vision_ratio": 0.017042
    },
    "all": {
      "mdi": 57.677578,
      "aei_text": 2.229086,
      "aei_vision": 0.047177,
      "text_ratio": 0.982958,
      "vision_ratio": 0.017042
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982958,
      0.017042
    ],
    "text_vision_ratio": "0.982958:0.017042",
    "skip_reason": null
  }
}
```


## === Rollout Step 30 ===
Step: 29/43 | 2025-10-22 18:55:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 45.336 | 43.482 | 36.695 | 36.695 |
| MDI Std | 15.622 | 18.595 | 12.440 | 12.440 |
| Vision Tokens | 340.8 ± 82.9 |
| Text Tokens | 165.9 ± 4.9 |
| Total Tokens | 506.6 ± 85.3 |
| Vision Ratio | 0.663 |
| Text Ratio | 0.337 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.449402,
      "aei_text": 3.216772,
      "aei_vision": 0.058013,
      "text_ratio": 0.982285,
      "vision_ratio": 0.017715
    },
    "middle": {
      "mdi": 32.028365,
      "aei_text": 3.123773,
      "aei_vision": 0.097531,
      "text_ratio": 0.969723,
      "vision_ratio": 0.030277
    },
    "late": {
      "mdi": 27.152366,
      "aei_text": 3.085844,
      "aei_vision": 0.113649,
      "text_ratio": 0.964479,
      "vision_ratio": 0.035521
    },
    "all": {
      "mdi": 27.152366,
      "aei_text": 3.142121,
      "aei_vision": 0.089735,
      "text_ratio": 0.964479,
      "vision_ratio": 0.035521
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964479,
      0.035521
    ],
    "text_vision_ratio": "0.964479:0.035521",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.575291,
      "aei_text": 3.219381,
      "aei_vision": 0.056904,
      "text_ratio": 0.982631,
      "vision_ratio": 0.017369
    },
    "middle": {
      "mdi": 48.590025,
      "aei_text": 3.19839,
      "aei_vision": 0.065824,
      "text_ratio": 0.979835,
      "vision_ratio": 0.020165
    },
    "late": {
      "mdi": 38.042091,
      "aei_text": 3.157942,
      "aei_vision": 0.083012,
      "text_ratio": 0.974387,
      "vision_ratio": 0.025613
    },
    "all": {
      "mdi": 38.042091,
      "aei_text": 3.191909,
      "aei_vision": 0.068578,
      "text_ratio": 0.974387,
      "vision_ratio": 0.025613
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974387,
      0.025613
    ],
    "text_vision_ratio": "0.974387:0.025613",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 162.0,
    "total_tokens": 532.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.143557,
      "aei_text": 3.15103,
      "aei_vision": 0.058198,
      "text_ratio": 0.981866,
      "vision_ratio": 0.018134
    },
    "middle": {
      "mdi": 70.285446,
      "aei_text": 3.180596,
      "aei_vision": 0.045253,
      "text_ratio": 0.985972,
      "vision_ratio": 0.014028
    },
    "late": {
      "mdi": 57.519911,
      "aei_text": 3.158534,
      "aei_vision": 0.054912,
      "text_ratio": 0.982912,
      "vision_ratio": 0.017088
    },
    "all": {
      "mdi": 57.519911,
      "aei_text": 3.163384,
      "aei_vision": 0.052789,
      "text_ratio": 0.982912,
      "vision_ratio": 0.017088
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982912,
      0.017088
    ],
    "text_vision_ratio": "0.982912:0.017088",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 162.0,
    "total_tokens": 532.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.440651,
      "aei_text": 3.141695,
      "aei_vision": 0.062285,
      "text_ratio": 0.98056,
      "vision_ratio": 0.01944
    },
    "middle": {
      "mdi": 56.782823,
      "aei_text": 3.156969,
      "aei_vision": 0.055597,
      "text_ratio": 0.982694,
      "vision_ratio": 0.017306
    },
    "late": {
      "mdi": 55.237986,
      "aei_text": 3.153559,
      "aei_vision": 0.05709,
      "text_ratio": 0.982218,
      "vision_ratio": 0.017782
    },
    "all": {
      "mdi": 55.237986,
      "aei_text": 3.15074,
      "aei_vision": 0.058325,
      "text_ratio": 0.982218,
      "vision_ratio": 0.017782
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982218,
      0.017782
    ],
    "text_vision_ratio": "0.982218:0.017782",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 162.0,
    "total_tokens": 380.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.121158,
      "aei_text": 2.281868,
      "aei_vision": 0.047419,
      "text_ratio": 0.979642,
      "vision_ratio": 0.020358
    },
    "middle": {
      "mdi": 79.058129,
      "aei_text": 2.306421,
      "aei_vision": 0.029174,
      "text_ratio": 0.987509,
      "vision_ratio": 0.012491
    },
    "late": {
      "mdi": 51.924818,
      "aei_text": 2.286424,
      "aei_vision": 0.044033,
      "text_ratio": 0.981105,
      "vision_ratio": 0.018895
    },
    "all": {
      "mdi": 51.924818,
      "aei_text": 2.291573,
      "aei_vision": 0.040207,
      "text_ratio": 0.981105,
      "vision_ratio": 0.018895
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981105,
      0.018895
    ],
    "text_vision_ratio": "0.981105:0.018895",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 162.0,
    "total_tokens": 380.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.3232,
      "aei_text": 2.276561,
      "aei_vision": 0.051363,
      "text_ratio": 0.977936,
      "vision_ratio": 0.022064
    },
    "middle": {
      "mdi": 39.944443,
      "aei_text": 2.269231,
      "aei_vision": 0.05681,
      "text_ratio": 0.975577,
      "vision_ratio": 0.024423
    },
    "late": {
      "mdi": 36.851262,
      "aei_text": 2.263041,
      "aei_vision": 0.06141,
      "text_ratio": 0.973581,
      "vision_ratio": 0.026419
    },
    "all": {
      "mdi": 36.851262,
      "aei_text": 2.269608,
      "aei_vision": 0.05653,
      "text_ratio": 0.973581,
      "vision_ratio": 0.026419
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973581,
      0.026419
    ],
    "text_vision_ratio": "0.973581:0.026419",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 175.0,
    "total_tokens": 522.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.317517,
      "aei_text": 2.852294,
      "aei_vision": 0.065846,
      "text_ratio": 0.977436,
      "vision_ratio": 0.022564
    },
    "middle": {
      "mdi": 39.732161,
      "aei_text": 2.841072,
      "aei_vision": 0.071506,
      "text_ratio": 0.975449,
      "vision_ratio": 0.024551
    },
    "late": {
      "mdi": 37.738746,
      "aei_text": 2.833956,
      "aei_vision": 0.075094,
      "text_ratio": 0.974186,
      "vision_ratio": 0.025814
    },
    "all": {
      "mdi": 37.738746,
      "aei_text": 2.842439,
      "aei_vision": 0.070816,
      "text_ratio": 0.974186,
      "vision_ratio": 0.025814
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974186,
      0.025814
    ],
    "text_vision_ratio": "0.974186:0.025814",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 175.0,
    "total_tokens": 522.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.03677,
      "aei_text": 2.859687,
      "aei_vision": 0.062117,
      "text_ratio": 0.97874,
      "vision_ratio": 0.02126
    },
    "middle": {
      "mdi": 62.91092,
      "aei_text": 2.891715,
      "aei_vision": 0.045965,
      "text_ratio": 0.984353,
      "vision_ratio": 0.015647
    },
    "late": {
      "mdi": 53.818779,
      "aei_text": 2.876864,
      "aei_vision": 0.053455,
      "text_ratio": 0.981758,
      "vision_ratio": 0.018242
    },
    "all": {
      "mdi": 53.818779,
      "aei_text": 2.876085,
      "aei_vision": 0.053848,
      "text_ratio": 0.981758,
      "vision_ratio": 0.018242
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981758,
      0.018242
    ],
    "text_vision_ratio": "0.981758:0.018242",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 71.695071,
      "aei_text": 3.014603,
      "aei_vision": 0.042048,
      "text_ratio": 0.986244,
      "vision_ratio": 0.013756
    },
    "middle": {
      "mdi": 57.876374,
      "aei_text": 2.99423,
      "aei_vision": 0.051735,
      "text_ratio": 0.983015,
      "vision_ratio": 0.016985
    },
    "late": {
      "mdi": 35.413651,
      "aei_text": 2.929087,
      "aei_vision": 0.082711,
      "text_ratio": 0.972538,
      "vision_ratio": 0.027462
    },
    "all": {
      "mdi": 35.413651,
      "aei_text": 2.979311,
      "aei_vision": 0.058829,
      "text_ratio": 0.972538,
      "vision_ratio": 0.027462
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972538,
      0.027462
    ],
    "text_vision_ratio": "0.972538:0.027462",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 67.547229,
      "aei_text": 3.009337,
      "aei_vision": 0.044552,
      "text_ratio": 0.985412,
      "vision_ratio": 0.014588
    },
    "middle": {
      "mdi": 37.348529,
      "aei_text": 2.937618,
      "aei_vision": 0.078654,
      "text_ratio": 0.973923,
      "vision_ratio": 0.026077
    },
    "late": {
      "mdi": 27.406573,
      "aei_text": 2.88189,
      "aei_vision": 0.105153,
      "text_ratio": 0.964797,
      "vision_ratio": 0.035203
    },
    "all": {
      "mdi": 27.406573,
      "aei_text": 2.942951,
      "aei_vision": 0.076118,
      "text_ratio": 0.964797,
      "vision_ratio": 0.035203
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964797,
      0.035203
    ],
    "text_vision_ratio": "0.964797:0.035203",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.006166,
      "aei_text": 2.241645,
      "aei_vision": 0.065919,
      "text_ratio": 0.971434,
      "vision_ratio": 0.028566
    },
    "middle": {
      "mdi": 40.882002,
      "aei_text": 2.255918,
      "aei_vision": 0.055181,
      "text_ratio": 0.976123,
      "vision_ratio": 0.023877
    },
    "late": {
      "mdi": 38.983096,
      "aei_text": 2.252463,
      "aei_vision": 0.05778,
      "text_ratio": 0.974989,
      "vision_ratio": 0.025011
    },
    "all": {
      "mdi": 38.983096,
      "aei_text": 2.250011,
      "aei_vision": 0.059625,
      "text_ratio": 0.974989,
      "vision_ratio": 0.025011
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974989,
      0.025011
    ],
    "text_vision_ratio": "0.974989:0.025011",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.142846,
      "aei_text": 2.241982,
      "aei_vision": 0.065665,
      "text_ratio": 0.971545,
      "vision_ratio": 0.028455
    },
    "middle": {
      "mdi": 41.276294,
      "aei_text": 2.256597,
      "aei_vision": 0.054671,
      "text_ratio": 0.976346,
      "vision_ratio": 0.023654
    },
    "late": {
      "mdi": 38.908619,
      "aei_text": 2.25232,
      "aei_vision": 0.057887,
      "text_ratio": 0.974943,
      "vision_ratio": 0.025057
    },
    "all": {
      "mdi": 38.908619,
      "aei_text": 2.250299,
      "aei_vision": 0.059408,
      "text_ratio": 0.974943,
      "vision_ratio": 0.025057
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.974943,
      0.025057
    ],
    "text_vision_ratio": "0.974943:0.025057",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.382915,
      "aei_text": 3.027205,
      "aei_vision": 0.065266,
      "text_ratio": 0.978895,
      "vision_ratio": 0.021105
    },
    "middle": {
      "mdi": 28.789422,
      "aei_text": 2.946766,
      "aei_vision": 0.102356,
      "text_ratio": 0.966431,
      "vision_ratio": 0.033569
    },
    "late": {
      "mdi": 26.050332,
      "aei_text": 2.925219,
      "aei_vision": 0.112291,
      "text_ratio": 0.963032,
      "vision_ratio": 0.036968
    },
    "all": {
      "mdi": 26.050332,
      "aei_text": 2.966397,
      "aei_vision": 0.093304,
      "text_ratio": 0.963032,
      "vision_ratio": 0.036968
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963032,
      0.036968
    ],
    "text_vision_ratio": "0.963032:0.036968",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.477383,
      "aei_text": 3.030326,
      "aei_vision": 0.063827,
      "text_ratio": 0.979372,
      "vision_ratio": 0.020628
    },
    "middle": {
      "mdi": 41.279444,
      "aei_text": 3.010579,
      "aei_vision": 0.072932,
      "text_ratio": 0.976348,
      "vision_ratio": 0.023652
    },
    "late": {
      "mdi": 27.678078,
      "aei_text": 2.9385,
      "aei_vision": 0.106167,
      "text_ratio": 0.96513,
      "vision_ratio": 0.03487
    },
    "all": {
      "mdi": 27.678078,
      "aei_text": 2.993141,
      "aei_vision": 0.080972,
      "text_ratio": 0.96513,
      "vision_ratio": 0.03487
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96513,
      0.03487
    ],
    "text_vision_ratio": "0.965130:0.034870",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 172.0,
    "total_tokens": 658.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.994664,
      "aei_text": 3.182934,
      "aei_vision": 0.227439,
      "text_ratio": 0.93331,
      "vision_ratio": 0.06669
    },
    "middle": {
      "mdi": 12.448287,
      "aei_text": 3.11787,
      "aei_vision": 0.250466,
      "text_ratio": 0.925641,
      "vision_ratio": 0.074359
    },
    "late": {
      "mdi": 20.807564,
      "aei_text": 3.368194,
      "aei_vision": 0.161874,
      "text_ratio": 0.954144,
      "vision_ratio": 0.045856
    },
    "all": {
      "mdi": 20.807564,
      "aei_text": 3.222968,
      "aei_vision": 0.21327,
      "text_ratio": 0.954144,
      "vision_ratio": 0.045856
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.954144,
      0.045856
    ],
    "text_vision_ratio": "0.954144:0.045856",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 172.0,
    "total_tokens": 658.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.725687,
      "aei_text": 3.082726,
      "aei_vision": 0.262904,
      "text_ratio": 0.921419,
      "vision_ratio": 0.078581
    },
    "middle": {
      "mdi": 6.471493,
      "aei_text": 2.662905,
      "aei_vision": 0.411482,
      "text_ratio": 0.866158,
      "vision_ratio": 0.133842
    },
    "late": {
      "mdi": 13.58102,
      "aei_text": 3.166731,
      "aei_vision": 0.233173,
      "text_ratio": 0.931418,
      "vision_ratio": 0.068582
    },
    "all": {
      "mdi": 13.58102,
      "aei_text": 2.970775,
      "aei_vision": 0.302524,
      "text_ratio": 0.931418,
      "vision_ratio": 0.068582
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.931418,
      0.068582
    ],
    "text_vision_ratio": "0.931418:0.068582",
    "skip_reason": null
  }
}
```


## === Rollout Step 31 ===
Step: 30/43 | 2025-10-22 18:56:33

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 39.059 | 44.441 | 41.477 | 41.477 |
| MDI Std | 18.439 | 20.762 | 15.316 | 15.316 |
| Vision Tokens | 350.4 ± 53.4 |
| Text Tokens | 163.0 ± 2.2 |
| Total Tokens | 513.4 ± 54.6 |
| Vision Ratio | 0.679 |
| Text Ratio | 0.321 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.634592,
      "aei_text": 3.001695,
      "aei_vision": 0.053954,
      "text_ratio": 0.982343,
      "vision_ratio": 0.017657
    },
    "middle": {
      "mdi": 60.370484,
      "aei_text": 3.010348,
      "aei_vision": 0.049865,
      "text_ratio": 0.983706,
      "vision_ratio": 0.016294
    },
    "late": {
      "mdi": 51.479654,
      "aei_text": 2.992845,
      "aei_vision": 0.058136,
      "text_ratio": 0.980945,
      "vision_ratio": 0.019055
    },
    "all": {
      "mdi": 51.479654,
      "aei_text": 3.00163,
      "aei_vision": 0.053985,
      "text_ratio": 0.980945,
      "vision_ratio": 0.019055
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980945,
      0.019055
    ],
    "text_vision_ratio": "0.980945:0.019055",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 62.917356,
      "aei_text": 3.014479,
      "aei_vision": 0.047912,
      "text_ratio": 0.984355,
      "vision_ratio": 0.015645
    },
    "middle": {
      "mdi": 74.961672,
      "aei_text": 3.03032,
      "aei_vision": 0.040425,
      "text_ratio": 0.986835,
      "vision_ratio": 0.013165
    },
    "late": {
      "mdi": 78.478337,
      "aei_text": 3.034053,
      "aei_vision": 0.038661,
      "text_ratio": 0.987418,
      "vision_ratio": 0.012582
    },
    "all": {
      "mdi": 78.478337,
      "aei_text": 3.026282,
      "aei_vision": 0.042333,
      "text_ratio": 0.987418,
      "vision_ratio": 0.012582
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987418,
      0.012582
    ],
    "text_vision_ratio": "0.987418:0.012582",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 162.0,
    "total_tokens": 398.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 28.627838,
      "aei_text": 2.337825,
      "aei_vision": 0.081663,
      "text_ratio": 0.966248,
      "vision_ratio": 0.033752
    },
    "middle": {
      "mdi": 44.121393,
      "aei_text": 2.378265,
      "aei_vision": 0.053903,
      "text_ratio": 0.977838,
      "vision_ratio": 0.022162
    },
    "late": {
      "mdi": 33.510462,
      "aei_text": 2.354436,
      "aei_vision": 0.07026,
      "text_ratio": 0.971023,
      "vision_ratio": 0.028977
    },
    "all": {
      "mdi": 33.510462,
      "aei_text": 2.356837,
      "aei_vision": 0.068612,
      "text_ratio": 0.971023,
      "vision_ratio": 0.028977
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971023,
      0.028977
    ],
    "text_vision_ratio": "0.971023:0.028977",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 162.0,
    "total_tokens": 398.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 27.732041,
      "aei_text": 2.334174,
      "aei_vision": 0.084169,
      "text_ratio": 0.965196,
      "vision_ratio": 0.034804
    },
    "middle": {
      "mdi": 33.38098,
      "aei_text": 2.354056,
      "aei_vision": 0.070521,
      "text_ratio": 0.970914,
      "vision_ratio": 0.029086
    },
    "late": {
      "mdi": 22.52842,
      "aei_text": 2.307572,
      "aei_vision": 0.102429,
      "text_ratio": 0.957498,
      "vision_ratio": 0.042502
    },
    "all": {
      "mdi": 22.52842,
      "aei_text": 2.33194,
      "aei_vision": 0.085702,
      "text_ratio": 0.957498,
      "vision_ratio": 0.042502
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957498,
      0.042502
    ],
    "text_vision_ratio": "0.957498:0.042502",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.433858,
      "aei_text": 3.00611,
      "aei_vision": 0.069211,
      "text_ratio": 0.977495,
      "vision_ratio": 0.022505
    },
    "middle": {
      "mdi": 58.797766,
      "aei_text": 3.04371,
      "aei_vision": 0.051766,
      "text_ratio": 0.983277,
      "vision_ratio": 0.016723
    },
    "late": {
      "mdi": 48.569912,
      "aei_text": 3.021214,
      "aei_vision": 0.062203,
      "text_ratio": 0.979826,
      "vision_ratio": 0.020174
    },
    "all": {
      "mdi": 48.569912,
      "aei_text": 3.023683,
      "aei_vision": 0.061058,
      "text_ratio": 0.979826,
      "vision_ratio": 0.020174
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979826,
      0.020174
    ],
    "text_vision_ratio": "0.979826:0.020174",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.622575,
      "aei_text": 2.996307,
      "aei_vision": 0.07376,
      "text_ratio": 0.975975,
      "vision_ratio": 0.024025
    },
    "middle": {
      "mdi": 49.446569,
      "aei_text": 3.023491,
      "aei_vision": 0.061147,
      "text_ratio": 0.980177,
      "vision_ratio": 0.019823
    },
    "late": {
      "mdi": 50.103306,
      "aei_text": 3.025148,
      "aei_vision": 0.060378,
      "text_ratio": 0.980432,
      "vision_ratio": 0.019568
    },
    "all": {
      "mdi": 50.103306,
      "aei_text": 3.014978,
      "aei_vision": 0.065097,
      "text_ratio": 0.980432,
      "vision_ratio": 0.019568
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980432,
      0.019568
    ],
    "text_vision_ratio": "0.980432:0.019568",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 160.0,
    "total_tokens": 461.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.786428,
      "aei_text": 2.757123,
      "aei_vision": 0.065981,
      "text_ratio": 0.976628,
      "vision_ratio": 0.023372
    },
    "middle": {
      "mdi": 82.915153,
      "aei_text": 2.817328,
      "aei_vision": 0.033978,
      "text_ratio": 0.988083,
      "vision_ratio": 0.011917
    },
    "late": {
      "mdi": 62.900264,
      "aei_text": 2.797579,
      "aei_vision": 0.044476,
      "text_ratio": 0.984351,
      "vision_ratio": 0.015649
    },
    "all": {
      "mdi": 62.900264,
      "aei_text": 2.790685,
      "aei_vision": 0.048141,
      "text_ratio": 0.984351,
      "vision_ratio": 0.015649
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984351,
      0.015649
    ],
    "text_vision_ratio": "0.984351:0.015649",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 160.0,
    "total_tokens": 461.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.09439,
      "aei_text": 2.760733,
      "aei_vision": 0.064062,
      "text_ratio": 0.977321,
      "vision_ratio": 0.022679
    },
    "middle": {
      "mdi": 36.122483,
      "aei_text": 2.738623,
      "aei_vision": 0.075815,
      "text_ratio": 0.973062,
      "vision_ratio": 0.026938
    },
    "late": {
      "mdi": 31.124176,
      "aei_text": 2.717024,
      "aei_vision": 0.087296,
      "text_ratio": 0.968871,
      "vision_ratio": 0.031129
    },
    "all": {
      "mdi": 31.124176,
      "aei_text": 2.738797,
      "aei_vision": 0.075722,
      "text_ratio": 0.968871,
      "vision_ratio": 0.031129
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.968871,
      0.031129
    ],
    "text_vision_ratio": "0.968871:0.031129",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.141439,
      "aei_text": 3.300022,
      "aei_vision": 0.057752,
      "text_ratio": 0.982801,
      "vision_ratio": 0.017199
    },
    "middle": {
      "mdi": 49.280401,
      "aei_text": 3.278596,
      "aei_vision": 0.066529,
      "text_ratio": 0.980112,
      "vision_ratio": 0.019888
    },
    "late": {
      "mdi": 46.748121,
      "aei_text": 3.270236,
      "aei_vision": 0.069954,
      "text_ratio": 0.979057,
      "vision_ratio": 0.020943
    },
    "all": {
      "mdi": 46.748121,
      "aei_text": 3.28295,
      "aei_vision": 0.064746,
      "text_ratio": 0.979057,
      "vision_ratio": 0.020943
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979057,
      0.020943
    ],
    "text_vision_ratio": "0.979057:0.020943",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.688298,
      "aei_text": 3.301304,
      "aei_vision": 0.057227,
      "text_ratio": 0.982961,
      "vision_ratio": 0.017039
    },
    "middle": {
      "mdi": 34.965029,
      "aei_text": 3.216446,
      "aei_vision": 0.09199,
      "text_ratio": 0.972195,
      "vision_ratio": 0.027805
    },
    "late": {
      "mdi": 34.175408,
      "aei_text": 3.211604,
      "aei_vision": 0.093974,
      "text_ratio": 0.971571,
      "vision_ratio": 0.028429
    },
    "all": {
      "mdi": 34.175408,
      "aei_text": 3.24314,
      "aei_vision": 0.081055,
      "text_ratio": 0.971571,
      "vision_ratio": 0.028429
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971571,
      0.028429
    ],
    "text_vision_ratio": "0.971571:0.028429",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.1255,
      "aei_text": 3.261864,
      "aei_vision": 0.056118,
      "text_ratio": 0.983087,
      "vision_ratio": 0.016913
    },
    "middle": {
      "mdi": 46.856423,
      "aei_text": 3.231096,
      "aei_vision": 0.068957,
      "text_ratio": 0.979104,
      "vision_ratio": 0.020896
    },
    "late": {
      "mdi": 36.9157,
      "aei_text": 3.189311,
      "aei_vision": 0.086394,
      "text_ratio": 0.973626,
      "vision_ratio": 0.026374
    },
    "all": {
      "mdi": 36.9157,
      "aei_text": 3.227418,
      "aei_vision": 0.070492,
      "text_ratio": 0.973626,
      "vision_ratio": 0.026374
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973626,
      0.026374
    ],
    "text_vision_ratio": "0.973626:0.026374",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.092704,
      "aei_text": 3.26398,
      "aei_vision": 0.055235,
      "text_ratio": 0.983359,
      "vision_ratio": 0.016641
    },
    "middle": {
      "mdi": 70.976067,
      "aei_text": 3.285417,
      "aei_vision": 0.046289,
      "text_ratio": 0.986106,
      "vision_ratio": 0.013894
    },
    "late": {
      "mdi": 57.654419,
      "aei_text": 3.26081,
      "aei_vision": 0.056558,
      "text_ratio": 0.982951,
      "vision_ratio": 0.017049
    },
    "all": {
      "mdi": 57.654419,
      "aei_text": 3.270067,
      "aei_vision": 0.052695,
      "text_ratio": 0.982951,
      "vision_ratio": 0.017049
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982951,
      0.017049
    ],
    "text_vision_ratio": "0.982951:0.017049",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.207386,
      "aei_text": 2.855595,
      "aei_vision": 0.216212,
      "text_ratio": 0.929614,
      "vision_ratio": 0.070386
    },
    "middle": {
      "mdi": 19.065837,
      "aei_text": 2.995508,
      "aei_vision": 0.157114,
      "text_ratio": 0.950164,
      "vision_ratio": 0.049836
    },
    "late": {
      "mdi": 27.524774,
      "aei_text": 3.100766,
      "aei_vision": 0.112654,
      "text_ratio": 0.964943,
      "vision_ratio": 0.035057
    },
    "all": {
      "mdi": 27.524774,
      "aei_text": 2.984022,
      "aei_vision": 0.161965,
      "text_ratio": 0.964943,
      "vision_ratio": 0.035057
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964943,
      0.035057
    ],
    "text_vision_ratio": "0.964943:0.035057",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.458454,
      "aei_text": 2.829737,
      "aei_vision": 0.227134,
      "text_ratio": 0.925697,
      "vision_ratio": 0.074303
    },
    "middle": {
      "mdi": 16.71816,
      "aei_text": 2.949753,
      "aei_vision": 0.17644,
      "text_ratio": 0.943561,
      "vision_ratio": 0.056439
    },
    "late": {
      "mdi": 28.468865,
      "aei_text": 3.108931,
      "aei_vision": 0.109205,
      "text_ratio": 0.966066,
      "vision_ratio": 0.033934
    },
    "all": {
      "mdi": 28.468865,
      "aei_text": 2.962815,
      "aei_vision": 0.170923,
      "text_ratio": 0.966066,
      "vision_ratio": 0.033934
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966066,
      0.033934
    ],
    "text_vision_ratio": "0.966066:0.033934",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 11.153512,
      "aei_text": 2.777839,
      "aei_vision": 0.249055,
      "text_ratio": 0.917719,
      "vision_ratio": 0.082281
    },
    "middle": {
      "mdi": 13.739886,
      "aei_text": 2.872517,
      "aei_vision": 0.209064,
      "text_ratio": 0.932157,
      "vision_ratio": 0.067843
    },
    "late": {
      "mdi": 24.754442,
      "aei_text": 3.073524,
      "aei_vision": 0.12416,
      "text_ratio": 0.961172,
      "vision_ratio": 0.038828
    },
    "all": {
      "mdi": 24.754442,
      "aei_text": 2.908055,
      "aei_vision": 0.194053,
      "text_ratio": 0.961172,
      "vision_ratio": 0.038828
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961172,
      0.038828
    ],
    "text_vision_ratio": "0.961172:0.038828",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.22289,
      "aei_text": 2.821055,
      "aei_vision": 0.230801,
      "text_ratio": 0.924374,
      "vision_ratio": 0.075626
    },
    "middle": {
      "mdi": 19.330196,
      "aei_text": 3.000039,
      "aei_vision": 0.1552,
      "text_ratio": 0.950812,
      "vision_ratio": 0.049188
    },
    "late": {
      "mdi": 28.693836,
      "aei_text": 3.110804,
      "aei_vision": 0.108414,
      "text_ratio": 0.966323,
      "vision_ratio": 0.033677
    },
    "all": {
      "mdi": 28.693836,
      "aei_text": 2.977284,
      "aei_vision": 0.164811,
      "text_ratio": 0.966323,
      "vision_ratio": 0.033677
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966323,
      0.033677
    ],
    "text_vision_ratio": "0.966323:0.033677",
    "skip_reason": null
  }
}
```


## === Rollout Step 32 ===
Step: 31/43 | 2025-10-22 18:57:49

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.236 | 49.773 | 41.740 | 41.740 |
| MDI Std | 11.872 | 23.233 | 18.170 | 18.170 |
| Vision Tokens | 356.1 ± 50.1 |
| Text Tokens | 166.6 ± 6.0 |
| Total Tokens | 522.8 ± 51.3 |
| Vision Ratio | 0.678 |
| Text Ratio | 0.322 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 181.0,
    "total_tokens": 574.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.634652,
      "aei_text": 2.588031,
      "aei_vision": 0.268617,
      "text_ratio": 0.905968,
      "vision_ratio": 0.094032
    },
    "middle": {
      "mdi": 5.599593,
      "aei_text": 2.28518,
      "aei_vision": 0.408098,
      "text_ratio": 0.848476,
      "vision_ratio": 0.151524
    },
    "late": {
      "mdi": 10.381084,
      "aei_text": 2.622713,
      "aei_vision": 0.252643,
      "text_ratio": 0.912135,
      "vision_ratio": 0.087865
    },
    "all": {
      "mdi": 10.381084,
      "aei_text": 2.498632,
      "aei_vision": 0.30979,
      "text_ratio": 0.912135,
      "vision_ratio": 0.087865
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.912135,
      0.087865
    ],
    "text_vision_ratio": "0.912135:0.087865",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 181.0,
    "total_tokens": 574.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.718659,
      "aei_text": 2.708832,
      "aei_vision": 0.212981,
      "text_ratio": 0.927107,
      "vision_ratio": 0.072893
    },
    "middle": {
      "mdi": 13.25048,
      "aei_text": 2.724779,
      "aei_vision": 0.205636,
      "text_ratio": 0.929827,
      "vision_ratio": 0.070173
    },
    "late": {
      "mdi": 22.174003,
      "aei_text": 2.888436,
      "aei_vision": 0.130262,
      "text_ratio": 0.956848,
      "vision_ratio": 0.043152
    },
    "all": {
      "mdi": 22.174003,
      "aei_text": 2.774015,
      "aei_vision": 0.18296,
      "text_ratio": 0.956848,
      "vision_ratio": 0.043152
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956848,
      0.043152
    ],
    "text_vision_ratio": "0.956848:0.043152",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.969999,
      "aei_text": 3.187658,
      "aei_vision": 0.075951,
      "text_ratio": 0.976728,
      "vision_ratio": 0.023272
    },
    "middle": {
      "mdi": 44.089026,
      "aei_text": 3.19586,
      "aei_vision": 0.072487,
      "text_ratio": 0.977822,
      "vision_ratio": 0.022178
    },
    "late": {
      "mdi": 32.141222,
      "aei_text": 3.136445,
      "aei_vision": 0.097583,
      "text_ratio": 0.969826,
      "vision_ratio": 0.030174
    },
    "all": {
      "mdi": 32.141222,
      "aei_text": 3.173316,
      "aei_vision": 0.082009,
      "text_ratio": 0.969826,
      "vision_ratio": 0.030174
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.969826,
      0.030174
    ],
    "text_vision_ratio": "0.969826:0.030174",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 43.135812,
      "aei_text": 3.192265,
      "aei_vision": 0.074005,
      "text_ratio": 0.977343,
      "vision_ratio": 0.022657
    },
    "middle": {
      "mdi": 84.469907,
      "aei_text": 3.275662,
      "aei_vision": 0.038779,
      "text_ratio": 0.9883,
      "vision_ratio": 0.0117
    },
    "late": {
      "mdi": 56.207083,
      "aei_text": 3.231363,
      "aei_vision": 0.05749,
      "text_ratio": 0.98252,
      "vision_ratio": 0.01748
    },
    "all": {
      "mdi": 56.207083,
      "aei_text": 3.233097,
      "aei_vision": 0.056758,
      "text_ratio": 0.98252,
      "vision_ratio": 0.01748
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98252,
      0.01748
    ],
    "text_vision_ratio": "0.982520:0.017480",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.434004,
      "aei_text": 2.964471,
      "aei_vision": 0.071547,
      "text_ratio": 0.976434,
      "vision_ratio": 0.023566
    },
    "middle": {
      "mdi": 55.33717,
      "aei_text": 3.001104,
      "aei_vision": 0.054233,
      "text_ratio": 0.98225,
      "vision_ratio": 0.01775
    },
    "late": {
      "mdi": 51.115285,
      "aei_text": 2.992003,
      "aei_vision": 0.058534,
      "text_ratio": 0.980812,
      "vision_ratio": 0.019188
    },
    "all": {
      "mdi": 51.115285,
      "aei_text": 2.98586,
      "aei_vision": 0.061438,
      "text_ratio": 0.980812,
      "vision_ratio": 0.019188
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980812,
      0.019188
    ],
    "text_vision_ratio": "0.980812:0.019188",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.471301,
      "aei_text": 2.961049,
      "aei_vision": 0.073164,
      "text_ratio": 0.975887,
      "vision_ratio": 0.024113
    },
    "middle": {
      "mdi": 45.293113,
      "aei_text": 2.976794,
      "aei_vision": 0.065723,
      "text_ratio": 0.978399,
      "vision_ratio": 0.021601
    },
    "late": {
      "mdi": 35.112905,
      "aei_text": 2.938768,
      "aei_vision": 0.083695,
      "text_ratio": 0.972309,
      "vision_ratio": 0.027691
    },
    "all": {
      "mdi": 35.112905,
      "aei_text": 2.958871,
      "aei_vision": 0.074193,
      "text_ratio": 0.972309,
      "vision_ratio": 0.027691
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972309,
      0.027691
    ],
    "text_vision_ratio": "0.972309:0.027691",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.234921,
      "aei_text": 2.956685,
      "aei_vision": 0.063949,
      "text_ratio": 0.978829,
      "vision_ratio": 0.021171
    },
    "middle": {
      "mdi": 74.224199,
      "aei_text": 3.005712,
      "aei_vision": 0.040495,
      "text_ratio": 0.986706,
      "vision_ratio": 0.013294
    },
    "late": {
      "mdi": 67.379329,
      "aei_text": 2.997372,
      "aei_vision": 0.044485,
      "text_ratio": 0.985376,
      "vision_ratio": 0.014624
    },
    "all": {
      "mdi": 67.379329,
      "aei_text": 2.98658,
      "aei_vision": 0.049648,
      "text_ratio": 0.985376,
      "vision_ratio": 0.014624
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985376,
      0.014624
    ],
    "text_vision_ratio": "0.985376:0.014624",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.72045,
      "aei_text": 2.958014,
      "aei_vision": 0.063313,
      "text_ratio": 0.979045,
      "vision_ratio": 0.020955
    },
    "middle": {
      "mdi": 76.646318,
      "aei_text": 3.008316,
      "aei_vision": 0.039249,
      "text_ratio": 0.987121,
      "vision_ratio": 0.012879
    },
    "late": {
      "mdi": 52.764841,
      "aei_text": 2.972597,
      "aei_vision": 0.056337,
      "text_ratio": 0.9814,
      "vision_ratio": 0.0186
    },
    "all": {
      "mdi": 52.764841,
      "aei_text": 2.979622,
      "aei_vision": 0.052976,
      "text_ratio": 0.9814,
      "vision_ratio": 0.0186
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9814,
      0.0186
    ],
    "text_vision_ratio": "0.981400:0.018600",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.694021,
      "aei_text": 3.303988,
      "aei_vision": 0.067852,
      "text_ratio": 0.979877,
      "vision_ratio": 0.020123
    },
    "middle": {
      "mdi": 43.679864,
      "aei_text": 3.285767,
      "aei_vision": 0.075224,
      "text_ratio": 0.977619,
      "vision_ratio": 0.022381
    },
    "late": {
      "mdi": 36.897831,
      "aei_text": 3.253738,
      "aei_vision": 0.088182,
      "text_ratio": 0.973613,
      "vision_ratio": 0.026387
    },
    "all": {
      "mdi": 36.897831,
      "aei_text": 3.281161,
      "aei_vision": 0.077088,
      "text_ratio": 0.973613,
      "vision_ratio": 0.026387
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973613,
      0.026387
    ],
    "text_vision_ratio": "0.973613:0.026387",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.782333,
      "aei_text": 3.293869,
      "aei_vision": 0.071946,
      "text_ratio": 0.978624,
      "vision_ratio": 0.021376
    },
    "middle": {
      "mdi": 36.059565,
      "aei_text": 3.248996,
      "aei_vision": 0.090101,
      "text_ratio": 0.973016,
      "vision_ratio": 0.026984
    },
    "late": {
      "mdi": 26.396226,
      "aei_text": 3.174448,
      "aei_vision": 0.120261,
      "text_ratio": 0.963499,
      "vision_ratio": 0.036501
    },
    "all": {
      "mdi": 26.396226,
      "aei_text": 3.239109,
      "aei_vision": 0.094101,
      "text_ratio": 0.963499,
      "vision_ratio": 0.036501
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963499,
      0.036501
    ],
    "text_vision_ratio": "0.963499:0.036501",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.367421,
      "aei_text": 2.349082,
      "aei_vision": 0.056786,
      "text_ratio": 0.976397,
      "vision_ratio": 0.023603
    },
    "middle": {
      "mdi": 27.556579,
      "aei_text": 2.310384,
      "aei_vision": 0.083841,
      "text_ratio": 0.964982,
      "vision_ratio": 0.035018
    },
    "late": {
      "mdi": 21.709037,
      "aei_text": 2.28008,
      "aei_vision": 0.105029,
      "text_ratio": 0.955965,
      "vision_ratio": 0.044035
    },
    "all": {
      "mdi": 21.709037,
      "aei_text": 2.313191,
      "aei_vision": 0.081879,
      "text_ratio": 0.955965,
      "vision_ratio": 0.044035
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.955965,
      0.044035
    ],
    "text_vision_ratio": "0.955965:0.044035",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 165.0,
    "total_tokens": 401.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.430831,
      "aei_text": 2.351051,
      "aei_vision": 0.055409,
      "text_ratio": 0.976975,
      "vision_ratio": 0.023025
    },
    "middle": {
      "mdi": 26.388999,
      "aei_text": 2.305351,
      "aei_vision": 0.08736,
      "text_ratio": 0.963489,
      "vision_ratio": 0.036511
    },
    "late": {
      "mdi": 23.149831,
      "aei_text": 2.288885,
      "aei_vision": 0.098873,
      "text_ratio": 0.958592,
      "vision_ratio": 0.041408
    },
    "all": {
      "mdi": 23.149831,
      "aei_text": 2.315093,
      "aei_vision": 0.080549,
      "text_ratio": 0.958592,
      "vision_ratio": 0.041408
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958592,
      0.041408
    ],
    "text_vision_ratio": "0.958592:0.041408",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.003298,
      "aei_text": 2.943874,
      "aei_vision": 0.058874,
      "text_ratio": 0.980393,
      "vision_ratio": 0.019607
    },
    "middle": {
      "mdi": 61.865728,
      "aei_text": 2.966437,
      "aei_vision": 0.04795,
      "text_ratio": 0.984093,
      "vision_ratio": 0.015907
    },
    "late": {
      "mdi": 51.266067,
      "aei_text": 2.946753,
      "aei_vision": 0.05748,
      "text_ratio": 0.980867,
      "vision_ratio": 0.019133
    },
    "all": {
      "mdi": 51.266067,
      "aei_text": 2.952357,
      "aei_vision": 0.054767,
      "text_ratio": 0.980867,
      "vision_ratio": 0.019133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980867,
      0.019133
    ],
    "text_vision_ratio": "0.980867:0.019133",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.47691,
      "aei_text": 2.949389,
      "aei_vision": 0.056204,
      "text_ratio": 0.9813,
      "vision_ratio": 0.0187
    },
    "middle": {
      "mdi": 80.632948,
      "aei_text": 2.988913,
      "aei_vision": 0.037068,
      "text_ratio": 0.98775,
      "vision_ratio": 0.01225
    },
    "late": {
      "mdi": 78.259281,
      "aei_text": 2.98665,
      "aei_vision": 0.038164,
      "text_ratio": 0.987383,
      "vision_ratio": 0.012617
    },
    "all": {
      "mdi": 78.259281,
      "aei_text": 2.974986,
      "aei_vision": 0.043811,
      "text_ratio": 0.987383,
      "vision_ratio": 0.012617
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987383,
      0.012617
    ],
    "text_vision_ratio": "0.987383:0.012617",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.562518,
      "aei_text": 3.233432,
      "aei_vision": 0.067983,
      "text_ratio": 0.979408,
      "vision_ratio": 0.020592
    },
    "middle": {
      "mdi": 69.112766,
      "aei_text": 3.282527,
      "aei_vision": 0.047495,
      "text_ratio": 0.985737,
      "vision_ratio": 0.014263
    },
    "late": {
      "mdi": 57.990847,
      "aei_text": 3.261565,
      "aei_vision": 0.056243,
      "text_ratio": 0.983048,
      "vision_ratio": 0.016952
    },
    "all": {
      "mdi": 57.990847,
      "aei_text": 3.259176,
      "aei_vision": 0.057239,
      "text_ratio": 0.983048,
      "vision_ratio": 0.016952
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983048,
      0.016952
    ],
    "text_vision_ratio": "0.983048:0.016952",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.140393,
      "aei_text": 3.238419,
      "aei_vision": 0.065901,
      "text_ratio": 0.980056,
      "vision_ratio": 0.019944
    },
    "middle": {
      "mdi": 52.168655,
      "aei_text": 3.247184,
      "aei_vision": 0.062244,
      "text_ratio": 0.981192,
      "vision_ratio": 0.018808
    },
    "late": {
      "mdi": 44.903024,
      "aei_text": 3.224272,
      "aei_vision": 0.071805,
      "text_ratio": 0.978215,
      "vision_ratio": 0.021785
    },
    "all": {
      "mdi": 44.903024,
      "aei_text": 3.236623,
      "aei_vision": 0.066651,
      "text_ratio": 0.978215,
      "vision_ratio": 0.021785
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978215,
      0.021785
    ],
    "text_vision_ratio": "0.978215:0.021785",
    "skip_reason": null
  }
}
```


## === Rollout Step 33 ===
Step: 32/43 | 2025-10-22 18:59:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 42.574 | 58.752 | 49.802 | 49.802 |
| MDI Std | 14.966 | 30.161 | 24.840 | 24.840 |
| Vision Tokens | 356.8 ± 60.3 |
| Text Tokens | 165.2 ± 2.9 |
| Total Tokens | 522.0 ± 61.3 |
| Vision Ratio | 0.678 |
| Text Ratio | 0.322 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.993918,
      "aei_text": 2.924958,
      "aei_vision": 0.068032,
      "text_ratio": 0.97727,
      "vision_ratio": 0.02273
    },
    "middle": {
      "mdi": 26.760465,
      "aei_text": 2.845824,
      "aei_vision": 0.106344,
      "text_ratio": 0.963978,
      "vision_ratio": 0.036022
    },
    "late": {
      "mdi": 24.955767,
      "aei_text": 2.831154,
      "aei_vision": 0.113447,
      "text_ratio": 0.961473,
      "vision_ratio": 0.038527
    },
    "all": {
      "mdi": 24.955767,
      "aei_text": 2.86733,
      "aei_vision": 0.095933,
      "text_ratio": 0.961473,
      "vision_ratio": 0.038527
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961473,
      0.038527
    ],
    "text_vision_ratio": "0.961473:0.038527",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.173102,
      "aei_text": 2.915574,
      "aei_vision": 0.072575,
      "text_ratio": 0.975712,
      "vision_ratio": 0.024288
    },
    "middle": {
      "mdi": 63.938787,
      "aei_text": 2.969548,
      "aei_vision": 0.046444,
      "text_ratio": 0.984601,
      "vision_ratio": 0.015399
    },
    "late": {
      "mdi": 54.064584,
      "aei_text": 2.952673,
      "aei_vision": 0.054614,
      "text_ratio": 0.98184,
      "vision_ratio": 0.01816
    },
    "all": {
      "mdi": 54.064584,
      "aei_text": 2.945928,
      "aei_vision": 0.057879,
      "text_ratio": 0.98184,
      "vision_ratio": 0.01816
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98184,
      0.01816
    ],
    "text_vision_ratio": "0.981840:0.018160",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 163.0,
    "total_tokens": 533.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.120899,
      "aei_text": 3.122639,
      "aei_vision": 0.064892,
      "text_ratio": 0.979642,
      "vision_ratio": 0.020358
    },
    "middle": {
      "mdi": 81.18449,
      "aei_text": 3.180997,
      "aei_vision": 0.039182,
      "text_ratio": 0.987832,
      "vision_ratio": 0.012168
    },
    "late": {
      "mdi": 79.331189,
      "aei_text": 3.178977,
      "aei_vision": 0.040072,
      "text_ratio": 0.987552,
      "vision_ratio": 0.012448
    },
    "all": {
      "mdi": 79.331189,
      "aei_text": 3.160866,
      "aei_vision": 0.048051,
      "text_ratio": 0.987552,
      "vision_ratio": 0.012448
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987552,
      0.012448
    ],
    "text_vision_ratio": "0.987552:0.012448",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 163.0,
    "total_tokens": 533.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.118888,
      "aei_text": 3.13091,
      "aei_vision": 0.061248,
      "text_ratio": 0.980813,
      "vision_ratio": 0.019187
    },
    "middle": {
      "mdi": 35.365683,
      "aei_text": 3.072717,
      "aei_vision": 0.086884,
      "text_ratio": 0.972502,
      "vision_ratio": 0.027498
    },
    "late": {
      "mdi": 28.084988,
      "aei_text": 3.025413,
      "aei_vision": 0.107723,
      "text_ratio": 0.965618,
      "vision_ratio": 0.034382
    },
    "all": {
      "mdi": 28.084988,
      "aei_text": 3.076342,
      "aei_vision": 0.085287,
      "text_ratio": 0.965618,
      "vision_ratio": 0.034382
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965618,
      0.034382
    ],
    "text_vision_ratio": "0.965618:0.034382",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 171.0,
    "total_tokens": 610.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.249163,
      "aei_text": 2.988231,
      "aei_vision": 0.225541,
      "text_ratio": 0.92982,
      "vision_ratio": 0.07018
    },
    "middle": {
      "mdi": 17.343788,
      "aei_text": 3.107304,
      "aei_vision": 0.179159,
      "text_ratio": 0.945486,
      "vision_ratio": 0.054514
    },
    "late": {
      "mdi": 19.934818,
      "aei_text": 3.160265,
      "aei_vision": 0.15853,
      "text_ratio": 0.952233,
      "vision_ratio": 0.047767
    },
    "all": {
      "mdi": 19.934818,
      "aei_text": 3.085264,
      "aei_vision": 0.187745,
      "text_ratio": 0.952233,
      "vision_ratio": 0.047767
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952233,
      0.047767
    ],
    "text_vision_ratio": "0.952233:0.047767",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 171.0,
    "total_tokens": 610.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 9.602962,
      "aei_text": 2.814756,
      "aei_vision": 0.293113,
      "text_ratio": 0.905687,
      "vision_ratio": 0.094313
    },
    "middle": {
      "mdi": 7.880865,
      "aei_text": 2.690727,
      "aei_vision": 0.341425,
      "text_ratio": 0.887398,
      "vision_ratio": 0.112602
    },
    "late": {
      "mdi": 10.336454,
      "aei_text": 2.85753,
      "aei_vision": 0.276452,
      "text_ratio": 0.911789,
      "vision_ratio": 0.088211
    },
    "all": {
      "mdi": 10.336454,
      "aei_text": 2.787654,
      "aei_vision": 0.30367,
      "text_ratio": 0.911789,
      "vision_ratio": 0.088211
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.911789,
      0.088211
    ],
    "text_vision_ratio": "0.911789:0.088211",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.567279,
      "aei_text": 3.001562,
      "aei_vision": 0.054017,
      "text_ratio": 0.982322,
      "vision_ratio": 0.017678
    },
    "middle": {
      "mdi": 85.888119,
      "aei_text": 3.04094,
      "aei_vision": 0.035406,
      "text_ratio": 0.988491,
      "vision_ratio": 0.011509
    },
    "late": {
      "mdi": 73.810652,
      "aei_text": 3.029024,
      "aei_vision": 0.041038,
      "text_ratio": 0.986633,
      "vision_ratio": 0.013367
    },
    "all": {
      "mdi": 73.810652,
      "aei_text": 3.02384,
      "aei_vision": 0.043488,
      "text_ratio": 0.986633,
      "vision_ratio": 0.013367
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986633,
      0.013367
    ],
    "text_vision_ratio": "0.986633:0.013367",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.00871,
      "aei_text": 2.996257,
      "aei_vision": 0.056524,
      "text_ratio": 0.981484,
      "vision_ratio": 0.018516
    },
    "middle": {
      "mdi": 72.93445,
      "aei_text": 3.02801,
      "aei_vision": 0.041517,
      "text_ratio": 0.986475,
      "vision_ratio": 0.013525
    },
    "late": {
      "mdi": 60.154877,
      "aei_text": 3.009982,
      "aei_vision": 0.050037,
      "text_ratio": 0.983648,
      "vision_ratio": 0.016352
    },
    "all": {
      "mdi": 60.154877,
      "aei_text": 3.011416,
      "aei_vision": 0.04936,
      "text_ratio": 0.983648,
      "vision_ratio": 0.016352
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983648,
      0.016352
    ],
    "text_vision_ratio": "0.983648:0.016352",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.149913,
      "aei_text": 3.295147,
      "aei_vision": 0.059749,
      "text_ratio": 0.982191,
      "vision_ratio": 0.017809
    },
    "middle": {
      "mdi": 99.70938,
      "aei_text": 3.358768,
      "aei_vision": 0.033686,
      "text_ratio": 0.99007,
      "vision_ratio": 0.00993
    },
    "late": {
      "mdi": 72.662141,
      "aei_text": 3.329155,
      "aei_vision": 0.045817,
      "text_ratio": 0.986425,
      "vision_ratio": 0.013575
    },
    "all": {
      "mdi": 72.662141,
      "aei_text": 3.327684,
      "aei_vision": 0.04642,
      "text_ratio": 0.986425,
      "vision_ratio": 0.013575
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986425,
      0.013575
    ],
    "text_vision_ratio": "0.986425:0.013575",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.897097,
      "aei_text": 3.28921,
      "aei_vision": 0.062181,
      "text_ratio": 0.981446,
      "vision_ratio": 0.018554
    },
    "middle": {
      "mdi": 94.86594,
      "aei_text": 3.354675,
      "aei_vision": 0.035362,
      "text_ratio": 0.989569,
      "vision_ratio": 0.010431
    },
    "late": {
      "mdi": 54.054695,
      "aei_text": 3.29232,
      "aei_vision": 0.060907,
      "text_ratio": 0.981836,
      "vision_ratio": 0.018164
    },
    "all": {
      "mdi": 54.054695,
      "aei_text": 3.312064,
      "aei_vision": 0.052819,
      "text_ratio": 0.981836,
      "vision_ratio": 0.018164
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981836,
      0.018164
    ],
    "text_vision_ratio": "0.981836:0.018164",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 25.730698,
      "aei_text": 2.214848,
      "aei_vision": 0.086078,
      "text_ratio": 0.96259,
      "vision_ratio": 0.03741
    },
    "middle": {
      "mdi": 26.397331,
      "aei_text": 2.217599,
      "aei_vision": 0.084008,
      "text_ratio": 0.9635,
      "vision_ratio": 0.0365
    },
    "late": {
      "mdi": 21.158094,
      "aei_text": 2.191581,
      "aei_vision": 0.103581,
      "text_ratio": 0.95487,
      "vision_ratio": 0.04513
    },
    "all": {
      "mdi": 21.158094,
      "aei_text": 2.208007,
      "aei_vision": 0.091224,
      "text_ratio": 0.95487,
      "vision_ratio": 0.04513
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.95487,
      0.04513
    ],
    "text_vision_ratio": "0.954870:0.045130",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 164.0,
    "total_tokens": 382.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 26.955249,
      "aei_text": 2.219801,
      "aei_vision": 0.082351,
      "text_ratio": 0.964229,
      "vision_ratio": 0.035771
    },
    "middle": {
      "mdi": 21.770277,
      "aei_text": 2.19523,
      "aei_vision": 0.100836,
      "text_ratio": 0.956083,
      "vision_ratio": 0.043917
    },
    "late": {
      "mdi": 19.195791,
      "aei_text": 2.178417,
      "aei_vision": 0.113484,
      "text_ratio": 0.950485,
      "vision_ratio": 0.049515
    },
    "all": {
      "mdi": 19.195791,
      "aei_text": 2.197813,
      "aei_vision": 0.098893,
      "text_ratio": 0.950485,
      "vision_ratio": 0.049515
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950485,
      0.049515
    ],
    "text_vision_ratio": "0.950485:0.049515",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.791534,
      "aei_text": 3.245695,
      "aei_vision": 0.057151,
      "text_ratio": 0.982696,
      "vision_ratio": 0.017304
    },
    "middle": {
      "mdi": 95.248779,
      "aei_text": 3.299315,
      "aei_vision": 0.034639,
      "text_ratio": 0.98961,
      "vision_ratio": 0.01039
    },
    "late": {
      "mdi": 88.645868,
      "aei_text": 3.29333,
      "aei_vision": 0.037152,
      "text_ratio": 0.988845,
      "vision_ratio": 0.011155
    },
    "all": {
      "mdi": 88.645868,
      "aei_text": 3.279434,
      "aei_vision": 0.042986,
      "text_ratio": 0.988845,
      "vision_ratio": 0.011155
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988845,
      0.011155
    ],
    "text_vision_ratio": "0.988845:0.011155",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.723198,
      "aei_text": 3.247805,
      "aei_vision": 0.056265,
      "text_ratio": 0.982971,
      "vision_ratio": 0.017029
    },
    "middle": {
      "mdi": 77.737307,
      "aei_text": 3.281282,
      "aei_vision": 0.04221,
      "text_ratio": 0.9873,
      "vision_ratio": 0.0127
    },
    "late": {
      "mdi": 77.75014,
      "aei_text": 3.281298,
      "aei_vision": 0.042203,
      "text_ratio": 0.987302,
      "vision_ratio": 0.012698
    },
    "all": {
      "mdi": 77.75014,
      "aei_text": 3.270124,
      "aei_vision": 0.046895,
      "text_ratio": 0.987302,
      "vision_ratio": 0.012698
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987302,
      0.012698
    ],
    "text_vision_ratio": "0.987302:0.012698",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.228787,
      "aei_text": 2.953842,
      "aei_vision": 0.065309,
      "text_ratio": 0.978368,
      "vision_ratio": 0.021632
    },
    "middle": {
      "mdi": 64.887776,
      "aei_text": 2.993912,
      "aei_vision": 0.04614,
      "text_ratio": 0.984823,
      "vision_ratio": 0.015177
    },
    "late": {
      "mdi": 49.770309,
      "aei_text": 2.965797,
      "aei_vision": 0.05959,
      "text_ratio": 0.980303,
      "vision_ratio": 0.019697
    },
    "all": {
      "mdi": 49.770309,
      "aei_text": 2.971184,
      "aei_vision": 0.057013,
      "text_ratio": 0.980303,
      "vision_ratio": 0.019697
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980303,
      0.019697
    ],
    "text_vision_ratio": "0.980303:0.019697",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.865684,
      "aei_text": 2.958407,
      "aei_vision": 0.063125,
      "text_ratio": 0.979108,
      "vision_ratio": 0.020892
    },
    "middle": {
      "mdi": 68.118619,
      "aei_text": 2.998351,
      "aei_vision": 0.044017,
      "text_ratio": 0.985532,
      "vision_ratio": 0.014468
    },
    "late": {
      "mdi": 62.920543,
      "aei_text": 2.990994,
      "aei_vision": 0.047536,
      "text_ratio": 0.984356,
      "vision_ratio": 0.015644
    },
    "all": {
      "mdi": 62.920543,
      "aei_text": 2.982585,
      "aei_vision": 0.051559,
      "text_ratio": 0.984356,
      "vision_ratio": 0.015644
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984356,
      0.015644
    ],
    "text_vision_ratio": "0.984356:0.015644",
    "skip_reason": null
  }
}
```


## === Rollout Step 34 ===
Step: 33/43 | 2025-10-22 19:00:23

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 47.245 | 55.775 | 46.560 | 46.560 |
| MDI Std | 17.035 | 26.349 | 20.843 | 20.843 |
| Vision Tokens | 375.2 ± 73.1 |
| Text Tokens | 163.1 ± 1.7 |
| Total Tokens | 538.4 ± 74.5 |
| Vision Ratio | 0.691 |
| Text Ratio | 0.309 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 338.0,
    "text_tokens": 164.0,
    "total_tokens": 502.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.559652,
      "aei_text": 2.912958,
      "aei_vision": 0.071819,
      "text_ratio": 0.975938,
      "vision_ratio": 0.024062
    },
    "middle": {
      "mdi": 44.017659,
      "aei_text": 2.924066,
      "aei_vision": 0.066429,
      "text_ratio": 0.977786,
      "vision_ratio": 0.022214
    },
    "late": {
      "mdi": 41.025993,
      "aei_text": 2.91456,
      "aei_vision": 0.071042,
      "text_ratio": 0.976205,
      "vision_ratio": 0.023795
    },
    "all": {
      "mdi": 41.025993,
      "aei_text": 2.917195,
      "aei_vision": 0.069763,
      "text_ratio": 0.976205,
      "vision_ratio": 0.023795
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976205,
      0.023795
    ],
    "text_vision_ratio": "0.976205:0.023795",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 338.0,
    "text_tokens": 164.0,
    "total_tokens": 502.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.538123,
      "aei_text": 2.909323,
      "aei_vision": 0.073583,
      "text_ratio": 0.975332,
      "vision_ratio": 0.024668
    },
    "middle": {
      "mdi": 39.712709,
      "aei_text": 2.909957,
      "aei_vision": 0.073275,
      "text_ratio": 0.975438,
      "vision_ratio": 0.024562
    },
    "late": {
      "mdi": 34.536196,
      "aei_text": 2.888596,
      "aei_vision": 0.08364,
      "text_ratio": 0.97186,
      "vision_ratio": 0.02814
    },
    "all": {
      "mdi": 34.536196,
      "aei_text": 2.902626,
      "aei_vision": 0.076832,
      "text_ratio": 0.97186,
      "vision_ratio": 0.02814
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97186,
      0.02814
    ],
    "text_vision_ratio": "0.971860:0.028140",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 164.0,
    "total_tokens": 626.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.851702,
      "aei_text": 3.612911,
      "aei_vision": 0.072473,
      "text_ratio": 0.980335,
      "vision_ratio": 0.019665
    },
    "middle": {
      "mdi": 28.539512,
      "aei_text": 3.474148,
      "aei_vision": 0.121731,
      "text_ratio": 0.966147,
      "vision_ratio": 0.033853
    },
    "late": {
      "mdi": 23.087499,
      "aei_text": 3.401974,
      "aei_vision": 0.147351,
      "text_ratio": 0.958485,
      "vision_ratio": 0.041515
    },
    "all": {
      "mdi": 23.087499,
      "aei_text": 3.496361,
      "aei_vision": 0.113846,
      "text_ratio": 0.958485,
      "vision_ratio": 0.041515
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.958485,
      0.041515
    ],
    "text_vision_ratio": "0.958485:0.041515",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 462.0,
    "text_tokens": 164.0,
    "total_tokens": 626.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.373769,
      "aei_text": 3.611041,
      "aei_vision": 0.073137,
      "text_ratio": 0.980148,
      "vision_ratio": 0.019852
    },
    "middle": {
      "mdi": 75.696771,
      "aei_text": 3.680117,
      "aei_vision": 0.048617,
      "text_ratio": 0.986962,
      "vision_ratio": 0.013038
    },
    "late": {
      "mdi": 48.164712,
      "aei_text": 3.606155,
      "aei_vision": 0.074871,
      "text_ratio": 0.97966,
      "vision_ratio": 0.02034
    },
    "all": {
      "mdi": 48.164712,
      "aei_text": 3.632447,
      "aei_vision": 0.065538,
      "text_ratio": 0.97966,
      "vision_ratio": 0.02034
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97966,
      0.02034
    ],
    "text_vision_ratio": "0.979660:0.020340",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.154849,
      "aei_text": 3.028478,
      "aei_vision": 0.052987,
      "text_ratio": 0.982805,
      "vision_ratio": 0.017195
    },
    "middle": {
      "mdi": 86.017266,
      "aei_text": 3.065636,
      "aei_vision": 0.03564,
      "text_ratio": 0.988508,
      "vision_ratio": 0.011492
    },
    "late": {
      "mdi": 91.820877,
      "aei_text": 3.070351,
      "aei_vision": 0.033438,
      "text_ratio": 0.989227,
      "vision_ratio": 0.010773
    },
    "all": {
      "mdi": 91.820877,
      "aei_text": 3.054819,
      "aei_vision": 0.04069,
      "text_ratio": 0.989227,
      "vision_ratio": 0.010773
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989227,
      0.010773
    ],
    "text_vision_ratio": "0.989227:0.010773",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.653932,
      "aei_text": 3.019155,
      "aei_vision": 0.05734,
      "text_ratio": 0.981362,
      "vision_ratio": 0.018638
    },
    "middle": {
      "mdi": 83.978084,
      "aei_text": 3.063828,
      "aei_vision": 0.036484,
      "text_ratio": 0.988232,
      "vision_ratio": 0.011768
    },
    "late": {
      "mdi": 60.330283,
      "aei_text": 3.034247,
      "aei_vision": 0.050294,
      "text_ratio": 0.983695,
      "vision_ratio": 0.016305
    },
    "all": {
      "mdi": 60.330283,
      "aei_text": 3.039085,
      "aei_vision": 0.048035,
      "text_ratio": 0.983695,
      "vision_ratio": 0.016305
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983695,
      0.016305
    ],
    "text_vision_ratio": "0.983695:0.016305",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.279707,
      "aei_text": 2.982386,
      "aei_vision": 0.06308,
      "text_ratio": 0.979287,
      "vision_ratio": 0.020713
    },
    "middle": {
      "mdi": 66.995322,
      "aei_text": 3.020461,
      "aei_vision": 0.045085,
      "text_ratio": 0.985293,
      "vision_ratio": 0.014707
    },
    "late": {
      "mdi": 49.779804,
      "aei_text": 2.988816,
      "aei_vision": 0.060041,
      "text_ratio": 0.980307,
      "vision_ratio": 0.019693
    },
    "all": {
      "mdi": 49.779804,
      "aei_text": 2.997215,
      "aei_vision": 0.056071,
      "text_ratio": 0.980307,
      "vision_ratio": 0.019693
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980307,
      0.019693
    ],
    "text_vision_ratio": "0.980307:0.019693",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.115419,
      "aei_text": 2.981941,
      "aei_vision": 0.06329,
      "text_ratio": 0.979217,
      "vision_ratio": 0.020783
    },
    "middle": {
      "mdi": 47.312769,
      "aei_text": 2.982476,
      "aei_vision": 0.063037,
      "text_ratio": 0.979302,
      "vision_ratio": 0.020698
    },
    "late": {
      "mdi": 33.53335,
      "aei_text": 2.930921,
      "aei_vision": 0.087403,
      "text_ratio": 0.971042,
      "vision_ratio": 0.028958
    },
    "all": {
      "mdi": 33.53335,
      "aei_text": 2.965117,
      "aei_vision": 0.071242,
      "text_ratio": 0.971042,
      "vision_ratio": 0.028958
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971042,
      0.028958
    ],
    "text_vision_ratio": "0.971042:0.028958",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 79.557651,
      "aei_text": 3.324551,
      "aei_vision": 0.041788,
      "text_ratio": 0.987587,
      "vision_ratio": 0.012413
    },
    "middle": {
      "mdi": 87.846386,
      "aei_text": 3.33386,
      "aei_vision": 0.037951,
      "text_ratio": 0.988745,
      "vision_ratio": 0.011255
    },
    "late": {
      "mdi": 73.006617,
      "aei_text": 3.315747,
      "aei_vision": 0.045417,
      "text_ratio": 0.986488,
      "vision_ratio": 0.013512
    },
    "all": {
      "mdi": 73.006617,
      "aei_text": 3.324717,
      "aei_vision": 0.04172,
      "text_ratio": 0.986488,
      "vision_ratio": 0.013512
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986488,
      0.013512
    ],
    "text_vision_ratio": "0.986488:0.013512",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.177915,
      "aei_text": 3.30478,
      "aei_vision": 0.049938,
      "text_ratio": 0.985114,
      "vision_ratio": 0.014886
    },
    "middle": {
      "mdi": 110.561733,
      "aei_text": 3.352369,
      "aei_vision": 0.030321,
      "text_ratio": 0.991036,
      "vision_ratio": 0.008964
    },
    "late": {
      "mdi": 86.306736,
      "aei_text": 3.332262,
      "aei_vision": 0.03861,
      "text_ratio": 0.988546,
      "vision_ratio": 0.011454
    },
    "all": {
      "mdi": 86.306736,
      "aei_text": 3.329796,
      "aei_vision": 0.039626,
      "text_ratio": 0.988546,
      "vision_ratio": 0.011454
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988546,
      0.011454
    ],
    "text_vision_ratio": "0.988546:0.011454",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 166.0,
    "total_tokens": 652.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 16.078336,
      "aei_text": 3.322682,
      "aei_vision": 0.206656,
      "text_ratio": 0.941446,
      "vision_ratio": 0.058554
    },
    "middle": {
      "mdi": 14.680964,
      "aei_text": 3.274669,
      "aei_vision": 0.223055,
      "text_ratio": 0.936228,
      "vision_ratio": 0.063772
    },
    "late": {
      "mdi": 17.956854,
      "aei_text": 3.377103,
      "aei_vision": 0.188068,
      "text_ratio": 0.947249,
      "vision_ratio": 0.052751
    },
    "all": {
      "mdi": 17.956854,
      "aei_text": 3.324813,
      "aei_vision": 0.205928,
      "text_ratio": 0.947249,
      "vision_ratio": 0.052751
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947249,
      0.052751
    ],
    "text_vision_ratio": "0.947249:0.052751",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 166.0,
    "total_tokens": 652.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.472144,
      "aei_text": 3.302749,
      "aei_vision": 0.213464,
      "text_ratio": 0.939291,
      "vision_ratio": 0.060709
    },
    "middle": {
      "mdi": 14.974425,
      "aei_text": 3.285374,
      "aei_vision": 0.219399,
      "text_ratio": 0.9374,
      "vision_ratio": 0.0626
    },
    "late": {
      "mdi": 23.616759,
      "aei_text": 3.494506,
      "aei_vision": 0.147967,
      "text_ratio": 0.959377,
      "vision_ratio": 0.040623
    },
    "all": {
      "mdi": 23.616759,
      "aei_text": 3.360917,
      "aei_vision": 0.193596,
      "text_ratio": 0.959377,
      "vision_ratio": 0.040623
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.959377,
      0.040623
    ],
    "text_vision_ratio": "0.959377:0.040623",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.010116,
      "aei_text": 3.290844,
      "aei_vision": 0.049854,
      "text_ratio": 0.985077,
      "vision_ratio": 0.014923
    },
    "middle": {
      "mdi": 50.069986,
      "aei_text": 3.254335,
      "aei_vision": 0.064996,
      "text_ratio": 0.980419,
      "vision_ratio": 0.019581
    },
    "late": {
      "mdi": 39.825101,
      "aei_text": 3.216324,
      "aei_vision": 0.080761,
      "text_ratio": 0.975505,
      "vision_ratio": 0.024495
    },
    "all": {
      "mdi": 39.825101,
      "aei_text": 3.253831,
      "aei_vision": 0.065205,
      "text_ratio": 0.975505,
      "vision_ratio": 0.024495
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975505,
      0.024495
    ],
    "text_vision_ratio": "0.975505:0.024495",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 63.207408,
      "aei_text": 3.28571,
      "aei_vision": 0.051983,
      "text_ratio": 0.984425,
      "vision_ratio": 0.015575
    },
    "middle": {
      "mdi": 52.106585,
      "aei_text": 3.26019,
      "aei_vision": 0.062568,
      "text_ratio": 0.98117,
      "vision_ratio": 0.01883
    },
    "late": {
      "mdi": 43.587525,
      "aei_text": 3.232251,
      "aei_vision": 0.074155,
      "text_ratio": 0.977572,
      "vision_ratio": 0.022428
    },
    "all": {
      "mdi": 43.587525,
      "aei_text": 3.259374,
      "aei_vision": 0.062906,
      "text_ratio": 0.977572,
      "vision_ratio": 0.022428
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977572,
      0.022428
    ],
    "text_vision_ratio": "0.977572:0.022428",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.522987,
      "aei_text": 2.37069,
      "aei_vision": 0.070718,
      "text_ratio": 0.971034,
      "vision_ratio": 0.028966
    },
    "middle": {
      "mdi": 46.005652,
      "aei_text": 2.398113,
      "aei_vision": 0.052126,
      "text_ratio": 0.978726,
      "vision_ratio": 0.021274
    },
    "late": {
      "mdi": 42.128101,
      "aei_text": 2.391276,
      "aei_vision": 0.056762,
      "text_ratio": 0.976813,
      "vision_ratio": 0.023187
    },
    "all": {
      "mdi": 42.128101,
      "aei_text": 2.386699,
      "aei_vision": 0.059865,
      "text_ratio": 0.976813,
      "vision_ratio": 0.023187
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976813,
      0.023187
    ],
    "text_vision_ratio": "0.976813:0.023187",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.370775,
      "aei_text": 2.367139,
      "aei_vision": 0.073126,
      "text_ratio": 0.970034,
      "vision_ratio": 0.029966
    },
    "middle": {
      "mdi": 43.889735,
      "aei_text": 2.394527,
      "aei_vision": 0.054558,
      "text_ratio": 0.977723,
      "vision_ratio": 0.022277
    },
    "late": {
      "mdi": 36.250784,
      "aei_text": 2.378233,
      "aei_vision": 0.065605,
      "text_ratio": 0.973155,
      "vision_ratio": 0.026845
    },
    "all": {
      "mdi": 36.250784,
      "aei_text": 2.37997,
      "aei_vision": 0.064427,
      "text_ratio": 0.973155,
      "vision_ratio": 0.026845
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973155,
      0.026845
    ],
    "text_vision_ratio": "0.973155:0.026845",
    "skip_reason": null
  }
}
```


## === Rollout Step 35 ===
Step: 34/43 | 2025-10-22 19:01:42

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 42.703 | 54.030 | 48.515 | 48.515 |
| MDI Std | 12.578 | 24.573 | 15.747 | 15.747 |
| Vision Tokens | 361.9 ± 51.4 |
| Text Tokens | 163.2 ± 3.5 |
| Total Tokens | 525.1 ± 49.7 |
| Vision Ratio | 0.685 |
| Text Ratio | 0.315 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.448389,
      "aei_text": 2.907462,
      "aei_vision": 0.060012,
      "text_ratio": 0.979777,
      "vision_ratio": 0.020223
    },
    "middle": {
      "mdi": 50.839501,
      "aei_text": 2.91297,
      "aei_vision": 0.057297,
      "text_ratio": 0.98071,
      "vision_ratio": 0.01929
    },
    "late": {
      "mdi": 53.807749,
      "aei_text": 2.91915,
      "aei_vision": 0.054251,
      "text_ratio": 0.981754,
      "vision_ratio": 0.018246
    },
    "all": {
      "mdi": 53.807749,
      "aei_text": 2.913194,
      "aei_vision": 0.057187,
      "text_ratio": 0.981754,
      "vision_ratio": 0.018246
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981754,
      0.018246
    ],
    "text_vision_ratio": "0.981754:0.018246",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.030151,
      "aei_text": 2.901334,
      "aei_vision": 0.063031,
      "text_ratio": 0.978737,
      "vision_ratio": 0.021263
    },
    "middle": {
      "mdi": 53.670207,
      "aei_text": 2.918879,
      "aei_vision": 0.054385,
      "text_ratio": 0.981709,
      "vision_ratio": 0.018291
    },
    "late": {
      "mdi": 49.831789,
      "aei_text": 2.91071,
      "aei_vision": 0.058411,
      "text_ratio": 0.980327,
      "vision_ratio": 0.019673
    },
    "all": {
      "mdi": 49.831789,
      "aei_text": 2.91031,
      "aei_vision": 0.058608,
      "text_ratio": 0.980327,
      "vision_ratio": 0.019673
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980327,
      0.019673
    ],
    "text_vision_ratio": "0.980327:0.019673",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.773942,
      "aei_text": 3.257002,
      "aei_vision": 0.069633,
      "text_ratio": 0.979068,
      "vision_ratio": 0.020932
    },
    "middle": {
      "mdi": 71.494618,
      "aei_text": 3.313494,
      "aei_vision": 0.046346,
      "text_ratio": 0.986206,
      "vision_ratio": 0.013794
    },
    "late": {
      "mdi": 60.854349,
      "aei_text": 3.294589,
      "aei_vision": 0.054139,
      "text_ratio": 0.983833,
      "vision_ratio": 0.016167
    },
    "all": {
      "mdi": 60.854349,
      "aei_text": 3.288363,
      "aei_vision": 0.056705,
      "text_ratio": 0.983833,
      "vision_ratio": 0.016167
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983833,
      0.016167
    ],
    "text_vision_ratio": "0.983833:0.016167",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.949405,
      "aei_text": 3.267244,
      "aei_vision": 0.065411,
      "text_ratio": 0.980373,
      "vision_ratio": 0.019627
    },
    "middle": {
      "mdi": 101.980675,
      "aei_text": 3.346323,
      "aei_vision": 0.032813,
      "text_ratio": 0.990289,
      "vision_ratio": 0.009711
    },
    "late": {
      "mdi": 76.583547,
      "aei_text": 3.320735,
      "aei_vision": 0.043361,
      "text_ratio": 0.987111,
      "vision_ratio": 0.012889
    },
    "all": {
      "mdi": 76.583547,
      "aei_text": 3.311428,
      "aei_vision": 0.047198,
      "text_ratio": 0.987111,
      "vision_ratio": 0.012889
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987111,
      0.012889
    ],
    "text_vision_ratio": "0.987111:0.012889",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.736102,
      "aei_text": 3.297315,
      "aei_vision": 0.070552,
      "text_ratio": 0.979051,
      "vision_ratio": 0.020949
    },
    "middle": {
      "mdi": 55.027867,
      "aei_text": 3.322462,
      "aei_vision": 0.060378,
      "text_ratio": 0.982152,
      "vision_ratio": 0.017848
    },
    "late": {
      "mdi": 39.747147,
      "aei_text": 3.268448,
      "aei_vision": 0.082231,
      "text_ratio": 0.975458,
      "vision_ratio": 0.024542
    },
    "all": {
      "mdi": 39.747147,
      "aei_text": 3.296073,
      "aei_vision": 0.071054,
      "text_ratio": 0.975458,
      "vision_ratio": 0.024542
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975458,
      0.024542
    ],
    "text_vision_ratio": "0.975458:0.024542",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.921882,
      "aei_text": 3.307919,
      "aei_vision": 0.066262,
      "text_ratio": 0.980362,
      "vision_ratio": 0.019638
    },
    "middle": {
      "mdi": 60.629377,
      "aei_text": 3.33571,
      "aei_vision": 0.055018,
      "text_ratio": 0.983774,
      "vision_ratio": 0.016226
    },
    "late": {
      "mdi": 47.20984,
      "aei_text": 3.298978,
      "aei_vision": 0.069879,
      "text_ratio": 0.979257,
      "vision_ratio": 0.020743
    },
    "all": {
      "mdi": 47.20984,
      "aei_text": 3.314206,
      "aei_vision": 0.063718,
      "text_ratio": 0.979257,
      "vision_ratio": 0.020743
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979257,
      0.020743
    ],
    "text_vision_ratio": "0.979257:0.020743",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.29969,
      "aei_text": 3.268665,
      "aei_vision": 0.070598,
      "text_ratio": 0.978858,
      "vision_ratio": 0.021142
    },
    "middle": {
      "mdi": 53.363327,
      "aei_text": 3.290478,
      "aei_vision": 0.061662,
      "text_ratio": 0.981605,
      "vision_ratio": 0.018395
    },
    "late": {
      "mdi": 42.48366,
      "aei_text": 3.254026,
      "aei_vision": 0.076595,
      "text_ratio": 0.977003,
      "vision_ratio": 0.022997
    },
    "all": {
      "mdi": 42.48366,
      "aei_text": 3.271056,
      "aei_vision": 0.069618,
      "text_ratio": 0.977003,
      "vision_ratio": 0.022997
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977003,
      0.022997
    ],
    "text_vision_ratio": "0.977003:0.022997",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.430079,
      "aei_text": 3.265534,
      "aei_vision": 0.07188,
      "text_ratio": 0.978462,
      "vision_ratio": 0.021538
    },
    "middle": {
      "mdi": 66.149742,
      "aei_text": 3.318536,
      "aei_vision": 0.050167,
      "text_ratio": 0.985108,
      "vision_ratio": 0.014892
    },
    "late": {
      "mdi": 60.24831,
      "aei_text": 3.307009,
      "aei_vision": 0.05489,
      "text_ratio": 0.983673,
      "vision_ratio": 0.016327
    },
    "all": {
      "mdi": 60.24831,
      "aei_text": 3.297035,
      "aei_vision": 0.058976,
      "text_ratio": 0.983673,
      "vision_ratio": 0.016327
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983673,
      0.016327
    ],
    "text_vision_ratio": "0.983673:0.016327",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.777181,
      "aei_text": 2.85996,
      "aei_vision": 0.223833,
      "text_ratio": 0.927416,
      "vision_ratio": 0.072584
    },
    "middle": {
      "mdi": 16.408325,
      "aei_text": 2.963534,
      "aei_vision": 0.180612,
      "text_ratio": 0.942556,
      "vision_ratio": 0.057444
    },
    "late": {
      "mdi": 26.091557,
      "aei_text": 3.110648,
      "aei_vision": 0.119221,
      "text_ratio": 0.963088,
      "vision_ratio": 0.036912
    },
    "all": {
      "mdi": 26.091557,
      "aei_text": 2.978071,
      "aei_vision": 0.174546,
      "text_ratio": 0.963088,
      "vision_ratio": 0.036912
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963088,
      0.036912
    ],
    "text_vision_ratio": "0.963088:0.036912",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.2973,
      "aei_text": 2.842442,
      "aei_vision": 0.231144,
      "text_ratio": 0.924797,
      "vision_ratio": 0.075203
    },
    "middle": {
      "mdi": 8.62917,
      "aei_text": 2.658163,
      "aei_vision": 0.308044,
      "text_ratio": 0.896149,
      "vision_ratio": 0.103851
    },
    "late": {
      "mdi": 24.932671,
      "aei_text": 3.098534,
      "aei_vision": 0.124276,
      "text_ratio": 0.961439,
      "vision_ratio": 0.038561
    },
    "all": {
      "mdi": 24.932671,
      "aei_text": 2.866326,
      "aei_vision": 0.221177,
      "text_ratio": 0.961439,
      "vision_ratio": 0.038561
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961439,
      0.038561
    ],
    "text_vision_ratio": "0.961439:0.038561",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.612286,
      "aei_text": 3.282673,
      "aei_vision": 0.064859,
      "text_ratio": 0.980625,
      "vision_ratio": 0.019375
    },
    "middle": {
      "mdi": 99.155316,
      "aei_text": 3.358319,
      "aei_vision": 0.033869,
      "text_ratio": 0.990016,
      "vision_ratio": 0.009984
    },
    "late": {
      "mdi": 76.625803,
      "aei_text": 3.334762,
      "aei_vision": 0.04352,
      "text_ratio": 0.987118,
      "vision_ratio": 0.012882
    },
    "all": {
      "mdi": 76.625803,
      "aei_text": 3.325246,
      "aei_vision": 0.047418,
      "text_ratio": 0.987118,
      "vision_ratio": 0.012882
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987118,
      0.012882
    ],
    "text_vision_ratio": "0.987118:0.012882",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 161.0,
    "total_tokens": 554.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.301734,
      "aei_text": 3.278663,
      "aei_vision": 0.066502,
      "text_ratio": 0.98012,
      "vision_ratio": 0.01988
    },
    "middle": {
      "mdi": 55.666754,
      "aei_text": 3.296444,
      "aei_vision": 0.059217,
      "text_ratio": 0.982353,
      "vision_ratio": 0.017647
    },
    "late": {
      "mdi": 47.510124,
      "aei_text": 3.272841,
      "aei_vision": 0.068887,
      "text_ratio": 0.979386,
      "vision_ratio": 0.020614
    },
    "all": {
      "mdi": 47.510124,
      "aei_text": 3.282652,
      "aei_vision": 0.064868,
      "text_ratio": 0.979386,
      "vision_ratio": 0.020614
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979386,
      0.020614
    ],
    "text_vision_ratio": "0.979386:0.020614",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 166.0,
    "total_tokens": 402.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.816999,
      "aei_text": 2.326681,
      "aei_vision": 0.066826,
      "text_ratio": 0.97208,
      "vision_ratio": 0.02792
    },
    "middle": {
      "mdi": 43.426068,
      "aei_text": 2.344919,
      "aei_vision": 0.053998,
      "text_ratio": 0.977491,
      "vision_ratio": 0.022509
    },
    "late": {
      "mdi": 45.219732,
      "aei_text": 2.347871,
      "aei_vision": 0.051921,
      "text_ratio": 0.978364,
      "vision_ratio": 0.021636
    },
    "all": {
      "mdi": 45.219732,
      "aei_text": 2.339819,
      "aei_vision": 0.057585,
      "text_ratio": 0.978364,
      "vision_ratio": 0.021636
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978364,
      0.021636
    ],
    "text_vision_ratio": "0.978364:0.021636",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 166.0,
    "total_tokens": 402.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.511615,
      "aei_text": 2.328468,
      "aei_vision": 0.065569,
      "text_ratio": 0.972611,
      "vision_ratio": 0.027389
    },
    "middle": {
      "mdi": 22.350645,
      "aei_text": 2.27686,
      "aei_vision": 0.10187,
      "text_ratio": 0.957175,
      "vision_ratio": 0.042825
    },
    "late": {
      "mdi": 19.515026,
      "aei_text": 2.257245,
      "aei_vision": 0.115667,
      "text_ratio": 0.951255,
      "vision_ratio": 0.048745
    },
    "all": {
      "mdi": 19.515026,
      "aei_text": 2.287532,
      "aei_vision": 0.094363,
      "text_ratio": 0.951255,
      "vision_ratio": 0.048745
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951255,
      0.048745
    ],
    "text_vision_ratio": "0.951255:0.048745",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.538138,
      "aei_text": 3.014222,
      "aei_vision": 0.059643,
      "text_ratio": 0.980597,
      "vision_ratio": 0.019403
    },
    "middle": {
      "mdi": 42.338077,
      "aei_text": 2.990671,
      "aei_vision": 0.070638,
      "text_ratio": 0.976926,
      "vision_ratio": 0.023074
    },
    "late": {
      "mdi": 50.999205,
      "aei_text": 3.015331,
      "aei_vision": 0.059125,
      "text_ratio": 0.980769,
      "vision_ratio": 0.019231
    },
    "all": {
      "mdi": 50.999205,
      "aei_text": 3.00674,
      "aei_vision": 0.063136,
      "text_ratio": 0.980769,
      "vision_ratio": 0.019231
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980769,
      0.019231
    ],
    "text_vision_ratio": "0.980769:0.019231",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.801035,
      "aei_text": 3.029701,
      "aei_vision": 0.052416,
      "text_ratio": 0.982993,
      "vision_ratio": 0.017007
    },
    "middle": {
      "mdi": 63.343085,
      "aei_text": 3.039203,
      "aei_vision": 0.04798,
      "text_ratio": 0.984458,
      "vision_ratio": 0.015542
    },
    "late": {
      "mdi": 54.582421,
      "aei_text": 3.023331,
      "aei_vision": 0.05539,
      "text_ratio": 0.982009,
      "vision_ratio": 0.017991
    },
    "all": {
      "mdi": 54.582421,
      "aei_text": 3.030746,
      "aei_vision": 0.051929,
      "text_ratio": 0.982009,
      "vision_ratio": 0.017991
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982009,
      0.017991
    ],
    "text_vision_ratio": "0.982009:0.017991",
    "skip_reason": null
  }
}
```


## === Rollout Step 36 ===
Step: 35/43 | 2025-10-22 19:02:59

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 43.519 | 61.804 | 42.312 | 42.312 |
| MDI Std | 14.666 | 31.686 | 17.672 | 17.672 |
| Vision Tokens | 321.1 ± 66.5 |
| Text Tokens | 165.6 ± 2.4 |
| Total Tokens | 486.8 ± 67.4 |
| Vision Ratio | 0.652 |
| Text Ratio | 0.348 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.057666,
      "aei_text": 2.961887,
      "aei_vision": 0.050152,
      "text_ratio": 0.983349,
      "vision_ratio": 0.016651
    },
    "middle": {
      "mdi": 121.179636,
      "aei_text": 3.014102,
      "aei_vision": 0.024873,
      "text_ratio": 0.991815,
      "vision_ratio": 0.008185
    },
    "late": {
      "mdi": 83.291994,
      "aei_text": 2.991298,
      "aei_vision": 0.035913,
      "text_ratio": 0.988136,
      "vision_ratio": 0.011864
    },
    "all": {
      "mdi": 83.291994,
      "aei_text": 2.989101,
      "aei_vision": 0.036977,
      "text_ratio": 0.988136,
      "vision_ratio": 0.011864
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988136,
      0.011864
    ],
    "text_vision_ratio": "0.988136:0.011864",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 168.0,
    "total_tokens": 515.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.366997,
      "aei_text": 2.960704,
      "aei_vision": 0.050726,
      "text_ratio": 0.983156,
      "vision_ratio": 0.016844
    },
    "middle": {
      "mdi": 70.869908,
      "aei_text": 2.978664,
      "aei_vision": 0.04203,
      "text_ratio": 0.986086,
      "vision_ratio": 0.013914
    },
    "late": {
      "mdi": 47.144293,
      "aei_text": 2.936809,
      "aei_vision": 0.062294,
      "text_ratio": 0.979229,
      "vision_ratio": 0.020771
    },
    "all": {
      "mdi": 47.144293,
      "aei_text": 2.958728,
      "aei_vision": 0.051682,
      "text_ratio": 0.979229,
      "vision_ratio": 0.020771
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979229,
      0.020771
    ],
    "text_vision_ratio": "0.979229:0.020771",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 164.0,
    "total_tokens": 373.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 29.85451,
      "aei_text": 2.181279,
      "aei_vision": 0.073064,
      "text_ratio": 0.96759,
      "vision_ratio": 0.03241
    },
    "middle": {
      "mdi": 50.979881,
      "aei_text": 2.218922,
      "aei_vision": 0.043525,
      "text_ratio": 0.980762,
      "vision_ratio": 0.019238
    },
    "late": {
      "mdi": 27.131281,
      "aei_text": 2.172352,
      "aei_vision": 0.080068,
      "text_ratio": 0.964452,
      "vision_ratio": 0.035548
    },
    "all": {
      "mdi": 27.131281,
      "aei_text": 2.190847,
      "aei_vision": 0.065556,
      "text_ratio": 0.964452,
      "vision_ratio": 0.035548
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.964452,
      0.035548
    ],
    "text_vision_ratio": "0.964452:0.035548",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 164.0,
    "total_tokens": 373.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.943887,
      "aei_text": 2.189685,
      "aei_vision": 0.066467,
      "text_ratio": 0.97054,
      "vision_ratio": 0.02946
    },
    "middle": {
      "mdi": 45.804004,
      "aei_text": 2.212824,
      "aei_vision": 0.048311,
      "text_ratio": 0.978634,
      "vision_ratio": 0.021366
    },
    "late": {
      "mdi": 33.649037,
      "aei_text": 2.191396,
      "aei_vision": 0.065125,
      "text_ratio": 0.971139,
      "vision_ratio": 0.028861
    },
    "all": {
      "mdi": 33.649037,
      "aei_text": 2.197965,
      "aei_vision": 0.05997,
      "text_ratio": 0.971139,
      "vision_ratio": 0.028861
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971139,
      0.028861
    ],
    "text_vision_ratio": "0.971139:0.028861",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.468471,
      "aei_text": 2.971387,
      "aei_vision": 0.062597,
      "text_ratio": 0.979368,
      "vision_ratio": 0.020632
    },
    "middle": {
      "mdi": 55.987432,
      "aei_text": 2.990692,
      "aei_vision": 0.053417,
      "text_ratio": 0.982452,
      "vision_ratio": 0.017548
    },
    "late": {
      "mdi": 35.775475,
      "aei_text": 2.930749,
      "aei_vision": 0.081921,
      "text_ratio": 0.972808,
      "vision_ratio": 0.027192
    },
    "all": {
      "mdi": 35.775475,
      "aei_text": 2.96426,
      "aei_vision": 0.065986,
      "text_ratio": 0.972808,
      "vision_ratio": 0.027192
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972808,
      0.027192
    ],
    "text_vision_ratio": "0.972808:0.027192",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.979926,
      "aei_text": 2.980095,
      "aei_vision": 0.058456,
      "text_ratio": 0.980762,
      "vision_ratio": 0.019238
    },
    "middle": {
      "mdi": 55.790626,
      "aei_text": 2.99031,
      "aei_vision": 0.053599,
      "text_ratio": 0.982391,
      "vision_ratio": 0.017609
    },
    "late": {
      "mdi": 34.534602,
      "aei_text": 2.924914,
      "aei_vision": 0.084695,
      "text_ratio": 0.971858,
      "vision_ratio": 0.028142
    },
    "all": {
      "mdi": 34.534602,
      "aei_text": 2.965108,
      "aei_vision": 0.065583,
      "text_ratio": 0.971858,
      "vision_ratio": 0.028142
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971858,
      0.028142
    ],
    "text_vision_ratio": "0.971858:0.028142",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.569217,
      "aei_text": 2.896397,
      "aei_vision": 0.213454,
      "text_ratio": 0.931362,
      "vision_ratio": 0.068638
    },
    "middle": {
      "mdi": 13.984049,
      "aei_text": 2.909419,
      "aei_vision": 0.208053,
      "text_ratio": 0.933262,
      "vision_ratio": 0.066738
    },
    "late": {
      "mdi": 15.386448,
      "aei_text": 2.948946,
      "aei_vision": 0.191659,
      "text_ratio": 0.938974,
      "vision_ratio": 0.061026
    },
    "all": {
      "mdi": 15.386448,
      "aei_text": 2.918249,
      "aei_vision": 0.20439,
      "text_ratio": 0.938974,
      "vision_ratio": 0.061026
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.938974,
      0.061026
    ],
    "text_vision_ratio": "0.938974:0.061026",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 13.96613,
      "aei_text": 2.90887,
      "aei_vision": 0.20828,
      "text_ratio": 0.933182,
      "vision_ratio": 0.066818
    },
    "middle": {
      "mdi": 12.377211,
      "aei_text": 2.854914,
      "aei_vision": 0.230659,
      "text_ratio": 0.925246,
      "vision_ratio": 0.074754
    },
    "late": {
      "mdi": 14.74958,
      "aei_text": 2.931796,
      "aei_vision": 0.198772,
      "text_ratio": 0.936506,
      "vision_ratio": 0.063494
    },
    "all": {
      "mdi": 14.74958,
      "aei_text": 2.898525,
      "aei_vision": 0.212571,
      "text_ratio": 0.936506,
      "vision_ratio": 0.063494
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.936506,
      0.063494
    ],
    "text_vision_ratio": "0.936506:0.063494",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.549596,
      "aei_text": 2.971602,
      "aei_vision": 0.062495,
      "text_ratio": 0.979403,
      "vision_ratio": 0.020597
    },
    "middle": {
      "mdi": 50.757884,
      "aei_text": 2.979579,
      "aei_vision": 0.058702,
      "text_ratio": 0.980679,
      "vision_ratio": 0.019321
    },
    "late": {
      "mdi": 42.860098,
      "aei_text": 2.957894,
      "aei_vision": 0.069013,
      "text_ratio": 0.9772,
      "vision_ratio": 0.0228
    },
    "all": {
      "mdi": 42.860098,
      "aei_text": 2.969692,
      "aei_vision": 0.063403,
      "text_ratio": 0.9772,
      "vision_ratio": 0.0228
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.9772,
      0.0228
    ],
    "text_vision_ratio": "0.977200:0.022800",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.692801,
      "aei_text": 2.97456,
      "aei_vision": 0.061088,
      "text_ratio": 0.979876,
      "vision_ratio": 0.020124
    },
    "middle": {
      "mdi": 60.861299,
      "aei_text": 2.999388,
      "aei_vision": 0.049282,
      "text_ratio": 0.983835,
      "vision_ratio": 0.016165
    },
    "late": {
      "mdi": 47.769122,
      "aei_text": 2.97218,
      "aei_vision": 0.06222,
      "text_ratio": 0.979495,
      "vision_ratio": 0.020505
    },
    "all": {
      "mdi": 47.769122,
      "aei_text": 2.982044,
      "aei_vision": 0.057529,
      "text_ratio": 0.979495,
      "vision_ratio": 0.020505
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979495,
      0.020505
    ],
    "text_vision_ratio": "0.979495:0.020505",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.337368,
      "aei_text": 2.985323,
      "aei_vision": 0.055971,
      "text_ratio": 0.981596,
      "vision_ratio": 0.018404
    },
    "middle": {
      "mdi": 83.49382,
      "aei_text": 3.026792,
      "aei_vision": 0.036252,
      "text_ratio": 0.988165,
      "vision_ratio": 0.011835
    },
    "late": {
      "mdi": 45.883585,
      "aei_text": 2.967039,
      "aei_vision": 0.064664,
      "text_ratio": 0.978671,
      "vision_ratio": 0.021329
    },
    "all": {
      "mdi": 45.883585,
      "aei_text": 2.993053,
      "aei_vision": 0.052295,
      "text_ratio": 0.978671,
      "vision_ratio": 0.021329
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978671,
      0.021329
    ],
    "text_vision_ratio": "0.978671:0.021329",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.93781,
      "aei_text": 2.996122,
      "aei_vision": 0.050835,
      "text_ratio": 0.983316,
      "vision_ratio": 0.016684
    },
    "middle": {
      "mdi": 65.983967,
      "aei_text": 3.007186,
      "aei_vision": 0.045574,
      "text_ratio": 0.985071,
      "vision_ratio": 0.014929
    },
    "late": {
      "mdi": 41.199049,
      "aei_text": 2.952327,
      "aei_vision": 0.07166,
      "text_ratio": 0.976303,
      "vision_ratio": 0.023697
    },
    "all": {
      "mdi": 41.199049,
      "aei_text": 2.985214,
      "aei_vision": 0.056022,
      "text_ratio": 0.976303,
      "vision_ratio": 0.023697
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976303,
      0.023697
    ],
    "text_vision_ratio": "0.976303:0.023697",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 164.0,
    "total_tokens": 373.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.383777,
      "aei_text": 2.193106,
      "aei_vision": 0.063783,
      "text_ratio": 0.971738,
      "vision_ratio": 0.028262
    },
    "middle": {
      "mdi": 54.030531,
      "aei_text": 2.221982,
      "aei_vision": 0.041125,
      "text_ratio": 0.981828,
      "vision_ratio": 0.018172
    },
    "late": {
      "mdi": 40.14435,
      "aei_text": 2.204411,
      "aei_vision": 0.054912,
      "text_ratio": 0.975695,
      "vision_ratio": 0.024305
    },
    "all": {
      "mdi": 40.14435,
      "aei_text": 2.206498,
      "aei_vision": 0.053274,
      "text_ratio": 0.975695,
      "vision_ratio": 0.024305
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975695,
      0.024305
    ],
    "text_vision_ratio": "0.975695:0.024305",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 164.0,
    "total_tokens": 373.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 35.333922,
      "aei_text": 2.195215,
      "aei_vision": 0.062128,
      "text_ratio": 0.972478,
      "vision_ratio": 0.027522
    },
    "middle": {
      "mdi": 55.042617,
      "aei_text": 2.222923,
      "aei_vision": 0.040385,
      "text_ratio": 0.982156,
      "vision_ratio": 0.017844
    },
    "late": {
      "mdi": 46.792643,
      "aei_text": 2.21409,
      "aei_vision": 0.047317,
      "text_ratio": 0.979076,
      "vision_ratio": 0.020924
    },
    "all": {
      "mdi": 46.792643,
      "aei_text": 2.21074,
      "aei_vision": 0.049946,
      "text_ratio": 0.979076,
      "vision_ratio": 0.020924
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979076,
      0.020924
    ],
    "text_vision_ratio": "0.979076:0.020924",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 171.0,
    "total_tokens": 541.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.623925,
      "aei_text": 3.043197,
      "aei_vision": 0.055712,
      "text_ratio": 0.982022,
      "vision_ratio": 0.017978
    },
    "middle": {
      "mdi": 49.779337,
      "aei_text": 3.031954,
      "aei_vision": 0.060908,
      "text_ratio": 0.980307,
      "vision_ratio": 0.019693
    },
    "late": {
      "mdi": 41.880632,
      "aei_text": 3.008319,
      "aei_vision": 0.071831,
      "text_ratio": 0.976679,
      "vision_ratio": 0.023321
    },
    "all": {
      "mdi": 41.880632,
      "aei_text": 3.027826,
      "aei_vision": 0.062816,
      "text_ratio": 0.976679,
      "vision_ratio": 0.023321
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976679,
      0.023321
    ],
    "text_vision_ratio": "0.976679:0.023321",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 171.0,
    "total_tokens": 541.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.243642,
      "aei_text": 3.048512,
      "aei_vision": 0.053255,
      "text_ratio": 0.982831,
      "vision_ratio": 0.017169
    },
    "middle": {
      "mdi": 141.940932,
      "aei_text": 3.116239,
      "aei_vision": 0.021954,
      "text_ratio": 0.993004,
      "vision_ratio": 0.006996
    },
    "late": {
      "mdi": 78.806048,
      "aei_text": 3.079199,
      "aei_vision": 0.039073,
      "text_ratio": 0.98747,
      "vision_ratio": 0.01253
    },
    "all": {
      "mdi": 78.806048,
      "aei_text": 3.081315,
      "aei_vision": 0.038095,
      "text_ratio": 0.98747,
      "vision_ratio": 0.01253
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98747,
      0.01253
    ],
    "text_vision_ratio": "0.987470:0.012530",
    "skip_reason": null
  }
}
```


## === Rollout Step 37 ===
Step: 36/43 | 2025-10-22 19:04:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 46.993 | 62.429 | 56.384 | 56.384 |
| MDI Std | 13.719 | 21.902 | 20.484 | 20.484 |
| Vision Tokens | 387.4 ± 42.9 |
| Text Tokens | 165.1 ± 3.3 |
| Total Tokens | 552.5 ± 43.6 |
| Vision Ratio | 0.700 |
| Text Ratio | 0.300 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.266641,
      "aei_text": 3.184925,
      "aei_vision": 0.065986,
      "text_ratio": 0.979702,
      "vision_ratio": 0.020298
    },
    "middle": {
      "mdi": 62.361555,
      "aei_text": 3.218552,
      "aei_vision": 0.051611,
      "text_ratio": 0.984218,
      "vision_ratio": 0.015782
    },
    "late": {
      "mdi": 36.726467,
      "aei_text": 3.139327,
      "aei_vision": 0.085479,
      "text_ratio": 0.973493,
      "vision_ratio": 0.026507
    },
    "all": {
      "mdi": 36.726467,
      "aei_text": 3.180923,
      "aei_vision": 0.067697,
      "text_ratio": 0.973493,
      "vision_ratio": 0.026507
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973493,
      0.026507
    ],
    "text_vision_ratio": "0.973493:0.026507",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.498058,
      "aei_text": 3.185628,
      "aei_vision": 0.065686,
      "text_ratio": 0.979797,
      "vision_ratio": 0.020203
    },
    "middle": {
      "mdi": 68.688617,
      "aei_text": 3.229307,
      "aei_vision": 0.047014,
      "text_ratio": 0.98565,
      "vision_ratio": 0.01435
    },
    "late": {
      "mdi": 62.268301,
      "aei_text": 3.218378,
      "aei_vision": 0.051686,
      "text_ratio": 0.984194,
      "vision_ratio": 0.015806
    },
    "all": {
      "mdi": 62.268301,
      "aei_text": 3.21111,
      "aei_vision": 0.054793,
      "text_ratio": 0.984194,
      "vision_ratio": 0.015806
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984194,
      0.015806
    ],
    "text_vision_ratio": "0.984194:0.015806",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.721843,
      "aei_text": 2.944051,
      "aei_vision": 0.06439,
      "text_ratio": 0.978597,
      "vision_ratio": 0.021403
    },
    "middle": {
      "mdi": 75.10999,
      "aei_text": 2.994991,
      "aei_vision": 0.039875,
      "text_ratio": 0.986861,
      "vision_ratio": 0.013139
    },
    "late": {
      "mdi": 57.364038,
      "aei_text": 2.970256,
      "aei_vision": 0.051779,
      "text_ratio": 0.982866,
      "vision_ratio": 0.017134
    },
    "all": {
      "mdi": 57.364038,
      "aei_text": 2.969755,
      "aei_vision": 0.05202,
      "text_ratio": 0.982866,
      "vision_ratio": 0.017134
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982866,
      0.017134
    ],
    "text_vision_ratio": "0.982866:0.017134",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.550887,
      "aei_text": 2.940691,
      "aei_vision": 0.066007,
      "text_ratio": 0.978047,
      "vision_ratio": 0.021953
    },
    "middle": {
      "mdi": 70.725509,
      "aei_text": 2.990001,
      "aei_vision": 0.042276,
      "text_ratio": 0.986058,
      "vision_ratio": 0.013942
    },
    "late": {
      "mdi": 62.60216,
      "aei_text": 2.978969,
      "aei_vision": 0.047586,
      "text_ratio": 0.984277,
      "vision_ratio": 0.015723
    },
    "all": {
      "mdi": 62.60216,
      "aei_text": 2.96989,
      "aei_vision": 0.051955,
      "text_ratio": 0.984277,
      "vision_ratio": 0.015723
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984277,
      0.015723
    ],
    "text_vision_ratio": "0.984277:0.015723",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.734483,
      "aei_text": 3.283668,
      "aei_vision": 0.070262,
      "text_ratio": 0.979051,
      "vision_ratio": 0.020949
    },
    "middle": {
      "mdi": 88.39067,
      "aei_text": 3.362803,
      "aei_vision": 0.038045,
      "text_ratio": 0.988813,
      "vision_ratio": 0.011187
    },
    "late": {
      "mdi": 73.954433,
      "aei_text": 3.345148,
      "aei_vision": 0.045233,
      "text_ratio": 0.986659,
      "vision_ratio": 0.013341
    },
    "all": {
      "mdi": 73.954433,
      "aei_text": 3.330549,
      "aei_vision": 0.051176,
      "text_ratio": 0.986659,
      "vision_ratio": 0.013341
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986659,
      0.013341
    ],
    "text_vision_ratio": "0.986659:0.013341",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 160.0,
    "total_tokens": 553.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.268536,
      "aei_text": 3.288888,
      "aei_vision": 0.068137,
      "text_ratio": 0.979703,
      "vision_ratio": 0.020297
    },
    "middle": {
      "mdi": 57.043366,
      "aei_text": 3.31357,
      "aei_vision": 0.058089,
      "text_ratio": 0.982772,
      "vision_ratio": 0.017228
    },
    "late": {
      "mdi": 46.713427,
      "aei_text": 3.283595,
      "aei_vision": 0.070292,
      "text_ratio": 0.979042,
      "vision_ratio": 0.020958
    },
    "all": {
      "mdi": 46.713427,
      "aei_text": 3.295345,
      "aei_vision": 0.065508,
      "text_ratio": 0.979042,
      "vision_ratio": 0.020958
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979042,
      0.020958
    ],
    "text_vision_ratio": "0.979042:0.020958",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.446981,
      "aei_text": 2.94605,
      "aei_vision": 0.063428,
      "text_ratio": 0.978924,
      "vision_ratio": 0.021076
    },
    "middle": {
      "mdi": 75.074977,
      "aei_text": 2.994953,
      "aei_vision": 0.039893,
      "text_ratio": 0.986855,
      "vision_ratio": 0.013145
    },
    "late": {
      "mdi": 55.962483,
      "aei_text": 2.967657,
      "aei_vision": 0.053029,
      "text_ratio": 0.982445,
      "vision_ratio": 0.017555
    },
    "all": {
      "mdi": 55.962483,
      "aei_text": 2.969555,
      "aei_vision": 0.052116,
      "text_ratio": 0.982445,
      "vision_ratio": 0.017555
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982445,
      0.017555
    ],
    "text_vision_ratio": "0.982445:0.017555",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.781854,
      "aei_text": 2.941367,
      "aei_vision": 0.065682,
      "text_ratio": 0.978157,
      "vision_ratio": 0.021843
    },
    "middle": {
      "mdi": 61.601973,
      "aei_text": 2.977416,
      "aei_vision": 0.048333,
      "text_ratio": 0.984026,
      "vision_ratio": 0.015974
    },
    "late": {
      "mdi": 39.643856,
      "aei_text": 2.92456,
      "aei_vision": 0.073771,
      "text_ratio": 0.975396,
      "vision_ratio": 0.024604
    },
    "all": {
      "mdi": 39.643856,
      "aei_text": 2.947781,
      "aei_vision": 0.062595,
      "text_ratio": 0.975396,
      "vision_ratio": 0.024604
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975396,
      0.024604
    ],
    "text_vision_ratio": "0.975396:0.024604",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.442038,
      "aei_text": 3.199247,
      "aei_vision": 0.059864,
      "text_ratio": 0.981632,
      "vision_ratio": 0.018368
    },
    "middle": {
      "mdi": 75.827655,
      "aei_text": 3.239352,
      "aei_vision": 0.04272,
      "text_ratio": 0.986984,
      "vision_ratio": 0.013016
    },
    "late": {
      "mdi": 61.066851,
      "aei_text": 3.216087,
      "aei_vision": 0.052665,
      "text_ratio": 0.983888,
      "vision_ratio": 0.016112
    },
    "all": {
      "mdi": 61.066851,
      "aei_text": 3.218231,
      "aei_vision": 0.051748,
      "text_ratio": 0.983888,
      "vision_ratio": 0.016112
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983888,
      0.016112
    ],
    "text_vision_ratio": "0.983888:0.016112",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 168.0,
    "total_tokens": 561.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.528183,
      "aei_text": 3.196915,
      "aei_vision": 0.060861,
      "text_ratio": 0.981318,
      "vision_ratio": 0.018682
    },
    "middle": {
      "mdi": 76.269057,
      "aei_text": 3.239913,
      "aei_vision": 0.04248,
      "text_ratio": 0.987058,
      "vision_ratio": 0.012942
    },
    "late": {
      "mdi": 94.649879,
      "aei_text": 3.258745,
      "aei_vision": 0.034429,
      "text_ratio": 0.989545,
      "vision_ratio": 0.010455
    },
    "all": {
      "mdi": 94.649879,
      "aei_text": 3.231851,
      "aei_vision": 0.045926,
      "text_ratio": 0.989545,
      "vision_ratio": 0.010455
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.989545,
      0.010455
    ],
    "text_vision_ratio": "0.989545:0.010455",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 159.0,
    "total_tokens": 506.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.618345,
      "aei_text": 3.068161,
      "aei_vision": 0.052341,
      "text_ratio": 0.983227,
      "vision_ratio": 0.016773
    },
    "middle": {
      "mdi": 76.873062,
      "aei_text": 3.094537,
      "aei_vision": 0.040255,
      "text_ratio": 0.987159,
      "vision_ratio": 0.012841
    },
    "late": {
      "mdi": 85.34298,
      "aei_text": 3.103039,
      "aei_vision": 0.03636,
      "text_ratio": 0.988418,
      "vision_ratio": 0.011582
    },
    "all": {
      "mdi": 85.34298,
      "aei_text": 3.088577,
      "aei_vision": 0.042986,
      "text_ratio": 0.988418,
      "vision_ratio": 0.011582
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988418,
      0.011582
    ],
    "text_vision_ratio": "0.988418:0.011582",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 159.0,
    "total_tokens": 506.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 57.971152,
      "aei_text": 3.066932,
      "aei_vision": 0.052904,
      "text_ratio": 0.983043,
      "vision_ratio": 0.016957
    },
    "middle": {
      "mdi": 51.25757,
      "aei_text": 3.052427,
      "aei_vision": 0.059551,
      "text_ratio": 0.980864,
      "vision_ratio": 0.019136
    },
    "late": {
      "mdi": 56.853066,
      "aei_text": 3.064745,
      "aei_vision": 0.053906,
      "text_ratio": 0.982715,
      "vision_ratio": 0.017285
    },
    "all": {
      "mdi": 56.853066,
      "aei_text": 3.061363,
      "aei_vision": 0.055456,
      "text_ratio": 0.982715,
      "vision_ratio": 0.017285
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982715,
      0.017285
    ],
    "text_vision_ratio": "0.982715:0.017285",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 166.0,
    "total_tokens": 652.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.826572,
      "aei_text": 3.280025,
      "aei_vision": 0.221226,
      "text_ratio": 0.936815,
      "vision_ratio": 0.063185
    },
    "middle": {
      "mdi": 8.779305,
      "aei_text": 2.945462,
      "aei_vision": 0.335501,
      "text_ratio": 0.897743,
      "vision_ratio": 0.102257
    },
    "late": {
      "mdi": 17.084516,
      "aei_text": 3.353102,
      "aei_vision": 0.196266,
      "text_ratio": 0.944704,
      "vision_ratio": 0.055296
    },
    "all": {
      "mdi": 17.084516,
      "aei_text": 3.192835,
      "aei_vision": 0.251007,
      "text_ratio": 0.944704,
      "vision_ratio": 0.055296
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.944704,
      0.055296
    ],
    "text_vision_ratio": "0.944704:0.055296",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 166.0,
    "total_tokens": 652.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 14.126571,
      "aei_text": 3.25344,
      "aei_vision": 0.230306,
      "text_ratio": 0.933891,
      "vision_ratio": 0.066109
    },
    "middle": {
      "mdi": 9.711532,
      "aei_text": 3.017909,
      "aei_vision": 0.310755,
      "text_ratio": 0.906643,
      "vision_ratio": 0.093357
    },
    "late": {
      "mdi": 18.481229,
      "aei_text": 3.390589,
      "aei_vision": 0.183461,
      "text_ratio": 0.948669,
      "vision_ratio": 0.051331
    },
    "all": {
      "mdi": 18.481229,
      "aei_text": 3.220642,
      "aei_vision": 0.241509,
      "text_ratio": 0.948669,
      "vision_ratio": 0.051331
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.948669,
      0.051331
    ],
    "text_vision_ratio": "0.948669:0.051331",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 64.46556,
      "aei_text": 3.248182,
      "aei_vision": 0.050386,
      "text_ratio": 0.984725,
      "vision_ratio": 0.015275
    },
    "middle": {
      "mdi": 75.479295,
      "aei_text": 3.265059,
      "aei_vision": 0.043258,
      "text_ratio": 0.986925,
      "vision_ratio": 0.013075
    },
    "late": {
      "mdi": 61.68233,
      "aei_text": 3.242998,
      "aei_vision": 0.052576,
      "text_ratio": 0.984047,
      "vision_ratio": 0.015953
    },
    "all": {
      "mdi": 61.68233,
      "aei_text": 3.252078,
      "aei_vision": 0.048741,
      "text_ratio": 0.984047,
      "vision_ratio": 0.015953
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984047,
      0.015953
    ],
    "text_vision_ratio": "0.984047:0.015953",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 62.638519,
      "aei_text": 3.244829,
      "aei_vision": 0.051802,
      "text_ratio": 0.984286,
      "vision_ratio": 0.015714
    },
    "middle": {
      "mdi": 65.666723,
      "aei_text": 3.250288,
      "aei_vision": 0.049497,
      "text_ratio": 0.985,
      "vision_ratio": 0.015
    },
    "late": {
      "mdi": 71.742428,
      "aei_text": 3.259895,
      "aei_vision": 0.045439,
      "text_ratio": 0.986253,
      "vision_ratio": 0.013747
    },
    "all": {
      "mdi": 71.742428,
      "aei_text": 3.251673,
      "aei_vision": 0.048911,
      "text_ratio": 0.986253,
      "vision_ratio": 0.013747
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986253,
      0.013747
    ],
    "text_vision_ratio": "0.986253:0.013747",
    "skip_reason": null
  }
}
```


## === Rollout Step 38 ===
Step: 37/43 | 2025-10-22 19:05:34

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 46.762 | 53.862 | 49.812 | 49.812 |
| MDI Std | 15.363 | 25.018 | 26.266 | 26.266 |
| Vision Tokens | 378.8 ± 52.9 |
| Text Tokens | 163.1 ± 4.0 |
| Total Tokens | 541.9 ± 52.9 |
| Vision Ratio | 0.696 |
| Text Ratio | 0.304 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 161.0,
    "total_tokens": 462.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.432852,
      "aei_text": 2.736451,
      "aei_vision": 0.071201,
      "text_ratio": 0.97464,
      "vision_ratio": 0.02536
    },
    "middle": {
      "mdi": 36.669635,
      "aei_text": 2.73036,
      "aei_vision": 0.074458,
      "text_ratio": 0.973453,
      "vision_ratio": 0.026547
    },
    "late": {
      "mdi": 29.392195,
      "aei_text": 2.697955,
      "aei_vision": 0.091792,
      "text_ratio": 0.967097,
      "vision_ratio": 0.032903
    },
    "all": {
      "mdi": 29.392195,
      "aei_text": 2.72159,
      "aei_vision": 0.079149,
      "text_ratio": 0.967097,
      "vision_ratio": 0.032903
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967097,
      0.032903
    ],
    "text_vision_ratio": "0.967097:0.032903",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 301.0,
    "text_tokens": 161.0,
    "total_tokens": 462.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.081023,
      "aei_text": 2.738558,
      "aei_vision": 0.070074,
      "text_ratio": 0.975051,
      "vision_ratio": 0.024949
    },
    "middle": {
      "mdi": 54.937213,
      "aei_text": 2.775125,
      "aei_vision": 0.050514,
      "text_ratio": 0.982123,
      "vision_ratio": 0.017877
    },
    "late": {
      "mdi": 62.323212,
      "aei_text": 2.785991,
      "aei_vision": 0.044702,
      "text_ratio": 0.984208,
      "vision_ratio": 0.015792
    },
    "all": {
      "mdi": 62.323212,
      "aei_text": 2.766559,
      "aei_vision": 0.055097,
      "text_ratio": 0.984208,
      "vision_ratio": 0.015792
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984208,
      0.015792
    ],
    "text_vision_ratio": "0.984208:0.015792",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 39.362366,
      "aei_text": 2.991481,
      "aei_vision": 0.075999,
      "text_ratio": 0.975224,
      "vision_ratio": 0.024776
    },
    "middle": {
      "mdi": 45.687529,
      "aei_text": 3.013137,
      "aei_vision": 0.065951,
      "text_ratio": 0.978581,
      "vision_ratio": 0.021419
    },
    "late": {
      "mdi": 33.866892,
      "aei_text": 2.966493,
      "aei_vision": 0.087593,
      "text_ratio": 0.971319,
      "vision_ratio": 0.028681
    },
    "all": {
      "mdi": 33.866892,
      "aei_text": 2.990367,
      "aei_vision": 0.076516,
      "text_ratio": 0.971319,
      "vision_ratio": 0.028681
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.971319,
      0.028681
    ],
    "text_vision_ratio": "0.971319:0.028681",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 161.0,
    "total_tokens": 508.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 41.787615,
      "aei_text": 3.000522,
      "aei_vision": 0.071804,
      "text_ratio": 0.976629,
      "vision_ratio": 0.023371
    },
    "middle": {
      "mdi": 31.718634,
      "aei_text": 2.95452,
      "aei_vision": 0.093148,
      "text_ratio": 0.969436,
      "vision_ratio": 0.030564
    },
    "late": {
      "mdi": 24.722066,
      "aei_text": 2.902259,
      "aei_vision": 0.117396,
      "text_ratio": 0.961123,
      "vision_ratio": 0.038877
    },
    "all": {
      "mdi": 24.722066,
      "aei_text": 2.952432,
      "aei_vision": 0.094117,
      "text_ratio": 0.961123,
      "vision_ratio": 0.038877
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961123,
      0.038877
    ],
    "text_vision_ratio": "0.961123:0.038877",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.099088,
      "aei_text": 3.251028,
      "aei_vision": 0.049184,
      "text_ratio": 0.985097,
      "vision_ratio": 0.014903
    },
    "middle": {
      "mdi": 68.305436,
      "aei_text": 3.254663,
      "aei_vision": 0.047649,
      "text_ratio": 0.985571,
      "vision_ratio": 0.014429
    },
    "late": {
      "mdi": 56.717892,
      "aei_text": 3.23254,
      "aei_vision": 0.056993,
      "text_ratio": 0.982674,
      "vision_ratio": 0.017326
    },
    "all": {
      "mdi": 56.717892,
      "aei_text": 3.246081,
      "aei_vision": 0.051274,
      "text_ratio": 0.982674,
      "vision_ratio": 0.017326
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982674,
      0.017326
    ],
    "text_vision_ratio": "0.982674:0.017326",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 63.619063,
      "aei_text": 3.246652,
      "aei_vision": 0.051033,
      "text_ratio": 0.984525,
      "vision_ratio": 0.015475
    },
    "middle": {
      "mdi": 83.08064,
      "aei_text": 3.274169,
      "aei_vision": 0.03941,
      "text_ratio": 0.988107,
      "vision_ratio": 0.011893
    },
    "late": {
      "mdi": 65.503349,
      "aei_text": 3.250006,
      "aei_vision": 0.049616,
      "text_ratio": 0.984963,
      "vision_ratio": 0.015037
    },
    "all": {
      "mdi": 65.503349,
      "aei_text": 3.256934,
      "aei_vision": 0.046689,
      "text_ratio": 0.984963,
      "vision_ratio": 0.015037
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984963,
      0.015037
    ],
    "text_vision_ratio": "0.984963:0.015037",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 157.0,
    "total_tokens": 504.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.110115,
      "aei_text": 3.081936,
      "aei_vision": 0.058029,
      "text_ratio": 0.981519,
      "vision_ratio": 0.018481
    },
    "middle": {
      "mdi": 93.333491,
      "aei_text": 3.13593,
      "aei_vision": 0.033599,
      "text_ratio": 0.989399,
      "vision_ratio": 0.010601
    },
    "late": {
      "mdi": 112.846025,
      "aei_text": 3.148524,
      "aei_vision": 0.027901,
      "text_ratio": 0.991216,
      "vision_ratio": 0.008784
    },
    "all": {
      "mdi": 112.846025,
      "aei_text": 3.122131,
      "aei_vision": 0.039843,
      "text_ratio": 0.991216,
      "vision_ratio": 0.008784
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.991216,
      0.008784
    ],
    "text_vision_ratio": "0.991216:0.008784",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 157.0,
    "total_tokens": 504.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.189137,
      "aei_text": 3.074786,
      "aei_vision": 0.061264,
      "text_ratio": 0.980465,
      "vision_ratio": 0.019535
    },
    "middle": {
      "mdi": 56.347308,
      "aei_text": 3.089026,
      "aei_vision": 0.054821,
      "text_ratio": 0.982562,
      "vision_ratio": 0.017438
    },
    "late": {
      "mdi": 52.900394,
      "aei_text": 3.081447,
      "aei_vision": 0.05825,
      "text_ratio": 0.981447,
      "vision_ratio": 0.018553
    },
    "all": {
      "mdi": 52.900394,
      "aei_text": 3.081751,
      "aei_vision": 0.058113,
      "text_ratio": 0.981447,
      "vision_ratio": 0.018553
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981447,
      0.018553
    ],
    "text_vision_ratio": "0.981447:0.018553",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 160.0,
    "total_tokens": 646.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.37396,
      "aei_text": 3.371398,
      "aei_vision": 0.219293,
      "text_ratio": 0.938927,
      "vision_ratio": 0.061073
    },
    "middle": {
      "mdi": 6.628995,
      "aei_text": 2.768797,
      "aei_vision": 0.41768,
      "text_ratio": 0.868921,
      "vision_ratio": 0.131079
    },
    "late": {
      "mdi": 8.824737,
      "aei_text": 3.003639,
      "aei_vision": 0.340366,
      "text_ratio": 0.898216,
      "vision_ratio": 0.101784
    },
    "all": {
      "mdi": 8.824737,
      "aei_text": 3.047908,
      "aei_vision": 0.325792,
      "text_ratio": 0.898216,
      "vision_ratio": 0.101784
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.898216,
      0.101784
    ],
    "text_vision_ratio": "0.898216:0.101784",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 486.0,
    "text_tokens": 160.0,
    "total_tokens": 646.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.372365,
      "aei_text": 3.371341,
      "aei_vision": 0.219312,
      "text_ratio": 0.938921,
      "vision_ratio": 0.061079
    },
    "middle": {
      "mdi": 6.32118,
      "aei_text": 2.727069,
      "aei_vision": 0.431418,
      "text_ratio": 0.86341,
      "vision_ratio": 0.13659
    },
    "late": {
      "mdi": 8.190475,
      "aei_text": 2.945237,
      "aei_vision": 0.359593,
      "text_ratio": 0.891192,
      "vision_ratio": 0.108808
    },
    "all": {
      "mdi": 8.190475,
      "aei_text": 3.01462,
      "aei_vision": 0.336751,
      "text_ratio": 0.891192,
      "vision_ratio": 0.108808
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.891192,
      0.108808
    ],
    "text_vision_ratio": "0.891192:0.108808",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.997429,
      "aei_text": 3.365823,
      "aei_vision": 0.06732,
      "text_ratio": 0.980391,
      "vision_ratio": 0.019609
    },
    "middle": {
      "mdi": 50.967669,
      "aei_text": 3.368919,
      "aei_vision": 0.066099,
      "text_ratio": 0.980757,
      "vision_ratio": 0.019243
    },
    "late": {
      "mdi": 44.320873,
      "aei_text": 3.345136,
      "aei_vision": 0.075475,
      "text_ratio": 0.977935,
      "vision_ratio": 0.022065
    },
    "all": {
      "mdi": 44.320873,
      "aei_text": 3.35996,
      "aei_vision": 0.069631,
      "text_ratio": 0.977935,
      "vision_ratio": 0.022065
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977935,
      0.022065
    ],
    "text_vision_ratio": "0.977935:0.022065",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.43569,
      "aei_text": 3.357069,
      "aei_vision": 0.070771,
      "text_ratio": 0.979354,
      "vision_ratio": 0.020646
    },
    "middle": {
      "mdi": 51.500821,
      "aei_text": 3.370573,
      "aei_vision": 0.065447,
      "text_ratio": 0.980953,
      "vision_ratio": 0.019047
    },
    "late": {
      "mdi": 58.197508,
      "aei_text": 3.388878,
      "aei_vision": 0.058231,
      "text_ratio": 0.983107,
      "vision_ratio": 0.016893
    },
    "all": {
      "mdi": 58.197508,
      "aei_text": 3.372172,
      "aei_vision": 0.064817,
      "text_ratio": 0.983107,
      "vision_ratio": 0.016893
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983107,
      0.016893
    ],
    "text_vision_ratio": "0.983107:0.016893",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 72.321147,
      "aei_text": 3.273993,
      "aei_vision": 0.04527,
      "text_ratio": 0.986361,
      "vision_ratio": 0.013639
    },
    "middle": {
      "mdi": 41.939551,
      "aei_text": 3.20008,
      "aei_vision": 0.076302,
      "text_ratio": 0.976711,
      "vision_ratio": 0.023289
    },
    "late": {
      "mdi": 27.643443,
      "aei_text": 3.113548,
      "aei_vision": 0.112632,
      "text_ratio": 0.965088,
      "vision_ratio": 0.034912
    },
    "all": {
      "mdi": 27.643443,
      "aei_text": 3.195855,
      "aei_vision": 0.078076,
      "text_ratio": 0.965088,
      "vision_ratio": 0.034912
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965088,
      0.034912
    ],
    "text_vision_ratio": "0.965088:0.034912",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 61.677519,
      "aei_text": 3.256077,
      "aei_vision": 0.052792,
      "text_ratio": 0.984045,
      "vision_ratio": 0.015955
    },
    "middle": {
      "mdi": 80.829633,
      "aei_text": 3.285018,
      "aei_vision": 0.040641,
      "text_ratio": 0.987779,
      "vision_ratio": 0.012221
    },
    "late": {
      "mdi": 73.525793,
      "aei_text": 3.275704,
      "aei_vision": 0.044552,
      "text_ratio": 0.986582,
      "vision_ratio": 0.013418
    },
    "all": {
      "mdi": 73.525793,
      "aei_text": 3.272261,
      "aei_vision": 0.045997,
      "text_ratio": 0.986582,
      "vision_ratio": 0.013418
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986582,
      0.013418
    ],
    "text_vision_ratio": "0.986582:0.013418",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.501898,
      "aei_text": 2.902578,
      "aei_vision": 0.062418,
      "text_ratio": 0.978948,
      "vision_ratio": 0.021052
    },
    "middle": {
      "mdi": 69.315976,
      "aei_text": 2.94308,
      "aei_vision": 0.042459,
      "text_ratio": 0.985778,
      "vision_ratio": 0.014222
    },
    "late": {
      "mdi": 68.353339,
      "aei_text": 2.941902,
      "aei_vision": 0.04304,
      "text_ratio": 0.985581,
      "vision_ratio": 0.014419
    },
    "all": {
      "mdi": 68.353339,
      "aei_text": 2.929191,
      "aei_vision": 0.049304,
      "text_ratio": 0.985581,
      "vision_ratio": 0.014419
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985581,
      0.014419
    ],
    "text_vision_ratio": "0.985581:0.014419",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 171.0,
    "total_tokens": 518.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.82419,
      "aei_text": 2.905937,
      "aei_vision": 0.060763,
      "text_ratio": 0.979518,
      "vision_ratio": 0.020482
    },
    "middle": {
      "mdi": 84.211908,
      "aei_text": 2.957962,
      "aei_vision": 0.035125,
      "text_ratio": 0.988265,
      "vision_ratio": 0.011735
    },
    "late": {
      "mdi": 69.65848,
      "aei_text": 2.943492,
      "aei_vision": 0.042256,
      "text_ratio": 0.985847,
      "vision_ratio": 0.014153
    },
    "all": {
      "mdi": 69.65848,
      "aei_text": 2.935789,
      "aei_vision": 0.046052,
      "text_ratio": 0.985847,
      "vision_ratio": 0.014153
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985847,
      0.014153
    ],
    "text_vision_ratio": "0.985847:0.014153",
    "skip_reason": null
  }
}
```


## === Rollout Step 39 ===
Step: 38/43 | 2025-10-22 19:06:51

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.381 | 55.265 | 52.164 | 52.164 |
| MDI Std | 15.738 | 23.225 | 20.475 | 20.475 |
| Vision Tokens | 348.1 ± 53.6 |
| Text Tokens | 163.2 ± 2.3 |
| Total Tokens | 511.4 ± 53.2 |
| Vision Ratio | 0.676 |
| Text Ratio | 0.324 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.938957,
      "aei_text": 3.301476,
      "aei_vision": 0.068868,
      "text_ratio": 0.979566,
      "vision_ratio": 0.020434
    },
    "middle": {
      "mdi": 52.406945,
      "aei_text": 3.315335,
      "aei_vision": 0.063261,
      "text_ratio": 0.981276,
      "vision_ratio": 0.018724
    },
    "late": {
      "mdi": 50.44273,
      "aei_text": 3.309531,
      "aei_vision": 0.06561,
      "text_ratio": 0.980561,
      "vision_ratio": 0.019439
    },
    "all": {
      "mdi": 50.44273,
      "aei_text": 3.308781,
      "aei_vision": 0.065913,
      "text_ratio": 0.980561,
      "vision_ratio": 0.019439
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980561,
      0.019439
    ],
    "text_vision_ratio": "0.980561:0.019439",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 159.0,
    "total_tokens": 552.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.903,
      "aei_text": 3.297905,
      "aei_vision": 0.070313,
      "text_ratio": 0.979124,
      "vision_ratio": 0.020876
    },
    "middle": {
      "mdi": 51.006067,
      "aei_text": 3.311239,
      "aei_vision": 0.064919,
      "text_ratio": 0.980771,
      "vision_ratio": 0.019229
    },
    "late": {
      "mdi": 51.959006,
      "aei_text": 3.314048,
      "aei_vision": 0.063782,
      "text_ratio": 0.981117,
      "vision_ratio": 0.018883
    },
    "all": {
      "mdi": 51.959006,
      "aei_text": 3.307733,
      "aei_vision": 0.066337,
      "text_ratio": 0.981117,
      "vision_ratio": 0.018883
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981117,
      0.018883
    ],
    "text_vision_ratio": "0.981117:0.018883",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.927434,
      "aei_text": 3.000881,
      "aei_vision": 0.060105,
      "text_ratio": 0.980364,
      "vision_ratio": 0.019636
    },
    "middle": {
      "mdi": 70.142637,
      "aei_text": 3.036671,
      "aei_vision": 0.043293,
      "text_ratio": 0.985944,
      "vision_ratio": 0.014056
    },
    "late": {
      "mdi": 63.511119,
      "aei_text": 3.02736,
      "aei_vision": 0.047667,
      "text_ratio": 0.984499,
      "vision_ratio": 0.015501
    },
    "all": {
      "mdi": 63.511119,
      "aei_text": 3.021638,
      "aei_vision": 0.050354,
      "text_ratio": 0.984499,
      "vision_ratio": 0.015501
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984499,
      0.015501
    ],
    "text_vision_ratio": "0.984499:0.015501",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.369214,
      "aei_text": 3.006614,
      "aei_vision": 0.057412,
      "text_ratio": 0.981263,
      "vision_ratio": 0.018737
    },
    "middle": {
      "mdi": 63.631329,
      "aei_text": 3.027546,
      "aei_vision": 0.047579,
      "text_ratio": 0.984528,
      "vision_ratio": 0.015472
    },
    "late": {
      "mdi": 50.278594,
      "aei_text": 3.001738,
      "aei_vision": 0.059702,
      "text_ratio": 0.980499,
      "vision_ratio": 0.019501
    },
    "all": {
      "mdi": 50.278594,
      "aei_text": 3.011965,
      "aei_vision": 0.054898,
      "text_ratio": 0.980499,
      "vision_ratio": 0.019501
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980499,
      0.019501
    ],
    "text_vision_ratio": "0.980499:0.019501",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.803753,
      "aei_text": 2.779771,
      "aei_vision": 0.257297,
      "text_ratio": 0.915281,
      "vision_ratio": 0.084719
    },
    "middle": {
      "mdi": 10.926098,
      "aei_text": 2.785433,
      "aei_vision": 0.254934,
      "text_ratio": 0.91615,
      "vision_ratio": 0.08385
    },
    "late": {
      "mdi": 16.356736,
      "aei_text": 2.962344,
      "aei_vision": 0.181108,
      "text_ratio": 0.942385,
      "vision_ratio": 0.057615
    },
    "all": {
      "mdi": 16.356736,
      "aei_text": 2.842494,
      "aei_vision": 0.231122,
      "text_ratio": 0.942385,
      "vision_ratio": 0.057615
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.942385,
      0.057615
    ],
    "text_vision_ratio": "0.942385:0.057615",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 10.962812,
      "aei_text": 2.787112,
      "aei_vision": 0.254233,
      "text_ratio": 0.916408,
      "vision_ratio": 0.083592
    },
    "middle": {
      "mdi": 13.113348,
      "aei_text": 2.871586,
      "aei_vision": 0.218982,
      "text_ratio": 0.929145,
      "vision_ratio": 0.070855
    },
    "late": {
      "mdi": 20.360537,
      "aei_text": 3.0387,
      "aei_vision": 0.149245,
      "text_ratio": 0.953185,
      "vision_ratio": 0.046815
    },
    "all": {
      "mdi": 20.360537,
      "aei_text": 2.899139,
      "aei_vision": 0.207484,
      "text_ratio": 0.953185,
      "vision_ratio": 0.046815
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.953185,
      0.046815
    ],
    "text_vision_ratio": "0.953185:0.046815",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.455244,
      "aei_text": 2.996118,
      "aei_vision": 0.045085,
      "text_ratio": 0.985175,
      "vision_ratio": 0.014825
    },
    "middle": {
      "mdi": 74.538105,
      "aei_text": 3.006059,
      "aei_vision": 0.040329,
      "text_ratio": 0.986762,
      "vision_ratio": 0.013238
    },
    "late": {
      "mdi": 73.017258,
      "aei_text": 3.004352,
      "aei_vision": 0.041146,
      "text_ratio": 0.98649,
      "vision_ratio": 0.01351
    },
    "all": {
      "mdi": 73.017258,
      "aei_text": 3.002174,
      "aei_vision": 0.042187,
      "text_ratio": 0.98649,
      "vision_ratio": 0.01351
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98649,
      0.01351
    ],
    "text_vision_ratio": "0.986490:0.013510",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 166.0,
    "total_tokens": 513.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 67.077894,
      "aei_text": 2.996966,
      "aei_vision": 0.044679,
      "text_ratio": 0.985311,
      "vision_ratio": 0.014689
    },
    "middle": {
      "mdi": 75.35581,
      "aei_text": 3.006949,
      "aei_vision": 0.039903,
      "text_ratio": 0.986903,
      "vision_ratio": 0.013097
    },
    "late": {
      "mdi": 59.356608,
      "aei_text": 2.985231,
      "aei_vision": 0.050293,
      "text_ratio": 0.983432,
      "vision_ratio": 0.016568
    },
    "all": {
      "mdi": 59.356608,
      "aei_text": 2.99638,
      "aei_vision": 0.044959,
      "text_ratio": 0.983432,
      "vision_ratio": 0.016568
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983432,
      0.016568
    ],
    "text_vision_ratio": "0.983432:0.016568",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.366143,
      "aei_text": 2.955899,
      "aei_vision": 0.058688,
      "text_ratio": 0.980532,
      "vision_ratio": 0.019468
    },
    "middle": {
      "mdi": 82.323527,
      "aei_text": 3.002072,
      "aei_vision": 0.036467,
      "text_ratio": 0.987999,
      "vision_ratio": 0.012001
    },
    "late": {
      "mdi": 77.596724,
      "aei_text": 2.997577,
      "aei_vision": 0.03863,
      "text_ratio": 0.987277,
      "vision_ratio": 0.012723
    },
    "all": {
      "mdi": 77.596724,
      "aei_text": 2.985173,
      "aei_vision": 0.0446,
      "text_ratio": 0.987277,
      "vision_ratio": 0.012723
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987277,
      0.012723
    ],
    "text_vision_ratio": "0.987277:0.012723",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.868263,
      "aei_text": 2.954731,
      "aei_vision": 0.059251,
      "text_ratio": 0.980341,
      "vision_ratio": 0.019659
    },
    "middle": {
      "mdi": 93.672684,
      "aei_text": 3.011053,
      "aei_vision": 0.032144,
      "text_ratio": 0.989437,
      "vision_ratio": 0.010563
    },
    "late": {
      "mdi": 85.755039,
      "aei_text": 3.005032,
      "aei_vision": 0.035042,
      "text_ratio": 0.988473,
      "vision_ratio": 0.011527
    },
    "all": {
      "mdi": 85.755039,
      "aei_text": 2.99026,
      "aei_vision": 0.042152,
      "text_ratio": 0.988473,
      "vision_ratio": 0.011527
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988473,
      0.011527
    ],
    "text_vision_ratio": "0.988473:0.011527",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.502234,
      "aei_text": 3.248825,
      "aei_vision": 0.073004,
      "text_ratio": 0.978023,
      "vision_ratio": 0.021977
    },
    "middle": {
      "mdi": 53.646343,
      "aei_text": 3.277706,
      "aei_vision": 0.061098,
      "text_ratio": 0.981701,
      "vision_ratio": 0.018299
    },
    "late": {
      "mdi": 76.903877,
      "aei_text": 3.32116,
      "aei_vision": 0.043186,
      "text_ratio": 0.987164,
      "vision_ratio": 0.012836
    },
    "all": {
      "mdi": 76.903877,
      "aei_text": 3.282569,
      "aei_vision": 0.059094,
      "text_ratio": 0.987164,
      "vision_ratio": 0.012836
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987164,
      0.012836
    ],
    "text_vision_ratio": "0.987164:0.012836",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.667212,
      "aei_text": 3.263261,
      "aei_vision": 0.067053,
      "text_ratio": 0.979866,
      "vision_ratio": 0.020134
    },
    "middle": {
      "mdi": 49.740277,
      "aei_text": 3.266607,
      "aei_vision": 0.065673,
      "text_ratio": 0.980292,
      "vision_ratio": 0.019708
    },
    "late": {
      "mdi": 53.226031,
      "aei_text": 3.276586,
      "aei_vision": 0.06156,
      "text_ratio": 0.981559,
      "vision_ratio": 0.018441
    },
    "all": {
      "mdi": 53.226031,
      "aei_text": 3.268819,
      "aei_vision": 0.064762,
      "text_ratio": 0.981559,
      "vision_ratio": 0.018441
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.981559,
      0.018441
    ],
    "text_vision_ratio": "0.981559:0.018441",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.204808,
      "aei_text": 3.01814,
      "aei_vision": 0.057813,
      "text_ratio": 0.981205,
      "vision_ratio": 0.018795
    },
    "middle": {
      "mdi": 76.939947,
      "aei_text": 3.056873,
      "aei_vision": 0.039731,
      "text_ratio": 0.98717,
      "vision_ratio": 0.01283
    },
    "late": {
      "mdi": 57.967859,
      "aei_text": 3.030013,
      "aei_vision": 0.052271,
      "text_ratio": 0.983042,
      "vision_ratio": 0.016958
    },
    "all": {
      "mdi": 57.967859,
      "aei_text": 3.035007,
      "aei_vision": 0.049939,
      "text_ratio": 0.983042,
      "vision_ratio": 0.016958
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983042,
      0.016958
    ],
    "text_vision_ratio": "0.983042:0.016958",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.704179,
      "aei_text": 3.016989,
      "aei_vision": 0.058351,
      "text_ratio": 0.981026,
      "vision_ratio": 0.018974
    },
    "middle": {
      "mdi": 52.67457,
      "aei_text": 3.019202,
      "aei_vision": 0.057318,
      "text_ratio": 0.981369,
      "vision_ratio": 0.018631
    },
    "late": {
      "mdi": 44.740078,
      "aei_text": 2.998423,
      "aei_vision": 0.067019,
      "text_ratio": 0.978137,
      "vision_ratio": 0.021863
    },
    "all": {
      "mdi": 44.740078,
      "aei_text": 3.011541,
      "aei_vision": 0.060894,
      "text_ratio": 0.978137,
      "vision_ratio": 0.021863
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978137,
      0.021863
    ],
    "text_vision_ratio": "0.978137:0.021863",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 163.0,
    "total_tokens": 381.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 29.990045,
      "aei_text": 2.237635,
      "aei_vision": 0.074613,
      "text_ratio": 0.967732,
      "vision_ratio": 0.032268
    },
    "middle": {
      "mdi": 31.184409,
      "aei_text": 2.241299,
      "aei_vision": 0.071872,
      "text_ratio": 0.968929,
      "vision_ratio": 0.031071
    },
    "late": {
      "mdi": 24.943776,
      "aei_text": 2.218474,
      "aei_vision": 0.088939,
      "text_ratio": 0.961455,
      "vision_ratio": 0.038545
    },
    "all": {
      "mdi": 24.943776,
      "aei_text": 2.232466,
      "aei_vision": 0.078477,
      "text_ratio": 0.961455,
      "vision_ratio": 0.038545
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961455,
      0.038545
    ],
    "text_vision_ratio": "0.961455:0.038545",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 163.0,
    "total_tokens": 381.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 30.358085,
      "aei_text": 2.238793,
      "aei_vision": 0.073746,
      "text_ratio": 0.96811,
      "vision_ratio": 0.03189
    },
    "middle": {
      "mdi": 32.938425,
      "aei_text": 2.246218,
      "aei_vision": 0.068194,
      "text_ratio": 0.970535,
      "vision_ratio": 0.029465
    },
    "late": {
      "mdi": 28.209887,
      "aei_text": 2.231623,
      "aei_vision": 0.079108,
      "text_ratio": 0.965765,
      "vision_ratio": 0.034235
    },
    "all": {
      "mdi": 28.209887,
      "aei_text": 2.238877,
      "aei_vision": 0.073684,
      "text_ratio": 0.965765,
      "vision_ratio": 0.034235
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.965765,
      0.034235
    ],
    "text_vision_ratio": "0.965765:0.034235",
    "skip_reason": null
  }
}
```


## === Rollout Step 40 ===
Step: 39/43 | 2025-10-22 19:08:08

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 41.798 | 54.651 | 41.471 | 41.471 |
| MDI Std | 15.210 | 27.122 | 17.854 | 17.854 |
| Vision Tokens | 310.6 ± 66.8 |
| Text Tokens | 162.5 ± 2.2 |
| Total Tokens | 473.1 ± 67.3 |
| Vision Ratio | 0.649 |
| Text Ratio | 0.351 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.781454,
      "aei_text": 3.08207,
      "aei_vision": 0.065882,
      "text_ratio": 0.979071,
      "vision_ratio": 0.020929
    },
    "middle": {
      "mdi": 66.253827,
      "aei_text": 3.123824,
      "aei_vision": 0.047149,
      "text_ratio": 0.985131,
      "vision_ratio": 0.014869
    },
    "late": {
      "mdi": 47.003277,
      "aei_text": 3.082731,
      "aei_vision": 0.065585,
      "text_ratio": 0.979168,
      "vision_ratio": 0.020832
    },
    "all": {
      "mdi": 47.003277,
      "aei_text": 3.096203,
      "aei_vision": 0.059541,
      "text_ratio": 0.979168,
      "vision_ratio": 0.020832
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979168,
      0.020832
    ],
    "text_vision_ratio": "0.979168:0.020832",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 370.0,
    "text_tokens": 166.0,
    "total_tokens": 536.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.056005,
      "aei_text": 3.082888,
      "aei_vision": 0.065515,
      "text_ratio": 0.979191,
      "vision_ratio": 0.020809
    },
    "middle": {
      "mdi": 55.435442,
      "aei_text": 3.104108,
      "aei_vision": 0.055995,
      "text_ratio": 0.982281,
      "vision_ratio": 0.017719
    },
    "late": {
      "mdi": 41.581377,
      "aei_text": 3.06464,
      "aei_vision": 0.073702,
      "text_ratio": 0.976516,
      "vision_ratio": 0.023484
    },
    "all": {
      "mdi": 41.581377,
      "aei_text": 3.083875,
      "aei_vision": 0.065072,
      "text_ratio": 0.976516,
      "vision_ratio": 0.023484
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976516,
      0.023484
    ],
    "text_vision_ratio": "0.976516:0.023484",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.720522,
      "aei_text": 2.867532,
      "aei_vision": 0.225426,
      "text_ratio": 0.927116,
      "vision_ratio": 0.072884
    },
    "middle": {
      "mdi": 13.980166,
      "aei_text": 2.9093,
      "aei_vision": 0.208102,
      "text_ratio": 0.933245,
      "vision_ratio": 0.066755
    },
    "late": {
      "mdi": 17.91915,
      "aei_text": 3.006513,
      "aei_vision": 0.167782,
      "text_ratio": 0.947144,
      "vision_ratio": 0.052856
    },
    "all": {
      "mdi": 17.91915,
      "aei_text": 2.927758,
      "aei_vision": 0.200446,
      "text_ratio": 0.947144,
      "vision_ratio": 0.052856
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.947144,
      0.052856
    ],
    "text_vision_ratio": "0.947144:0.052856",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 163.0,
    "total_tokens": 556.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 12.544748,
      "aei_text": 2.861144,
      "aei_vision": 0.228075,
      "text_ratio": 0.926171,
      "vision_ratio": 0.073829
    },
    "middle": {
      "mdi": 12.950888,
      "aei_text": 2.875682,
      "aei_vision": 0.222045,
      "text_ratio": 0.92832,
      "vision_ratio": 0.07168
    },
    "late": {
      "mdi": 16.567398,
      "aei_text": 2.9777,
      "aei_vision": 0.179733,
      "text_ratio": 0.943076,
      "vision_ratio": 0.056924
    },
    "all": {
      "mdi": 16.567398,
      "aei_text": 2.90484,
      "aei_vision": 0.209952,
      "text_ratio": 0.943076,
      "vision_ratio": 0.056924
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.943076,
      0.056924
    ],
    "text_vision_ratio": "0.943076:0.056924",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 161.0,
    "total_tokens": 370.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 27.690424,
      "aei_text": 2.195224,
      "aei_vision": 0.079277,
      "text_ratio": 0.965145,
      "vision_ratio": 0.034855
    },
    "middle": {
      "mdi": 33.958246,
      "aei_text": 2.213519,
      "aei_vision": 0.065184,
      "text_ratio": 0.971394,
      "vision_ratio": 0.028606
    },
    "late": {
      "mdi": 25.882848,
      "aei_text": 2.18838,
      "aei_vision": 0.084549,
      "text_ratio": 0.962802,
      "vision_ratio": 0.037198
    },
    "all": {
      "mdi": 25.882848,
      "aei_text": 2.199038,
      "aei_vision": 0.076339,
      "text_ratio": 0.962802,
      "vision_ratio": 0.037198
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962802,
      0.037198
    ],
    "text_vision_ratio": "0.962802:0.037198",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 209.0,
    "text_tokens": 161.0,
    "total_tokens": 370.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 32.84406,
      "aei_text": 2.210758,
      "aei_vision": 0.067311,
      "text_ratio": 0.970453,
      "vision_ratio": 0.029547
    },
    "middle": {
      "mdi": 63.58534,
      "aei_text": 2.252157,
      "aei_vision": 0.035419,
      "text_ratio": 0.984517,
      "vision_ratio": 0.015483
    },
    "late": {
      "mdi": 38.588563,
      "aei_text": 2.223342,
      "aei_vision": 0.057617,
      "text_ratio": 0.97474,
      "vision_ratio": 0.02526
    },
    "all": {
      "mdi": 38.588563,
      "aei_text": 2.228752,
      "aei_vision": 0.053449,
      "text_ratio": 0.97474,
      "vision_ratio": 0.02526
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97474,
      0.02526
    ],
    "text_vision_ratio": "0.974740:0.025260",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 64.157962,
      "aei_text": 3.040466,
      "aei_vision": 0.04739,
      "text_ratio": 0.984653,
      "vision_ratio": 0.015347
    },
    "middle": {
      "mdi": 75.093371,
      "aei_text": 3.054839,
      "aei_vision": 0.040681,
      "text_ratio": 0.986858,
      "vision_ratio": 0.013142
    },
    "late": {
      "mdi": 69.409068,
      "aei_text": 3.047916,
      "aei_vision": 0.043912,
      "text_ratio": 0.985797,
      "vision_ratio": 0.014203
    },
    "all": {
      "mdi": 69.409068,
      "aei_text": 3.047742,
      "aei_vision": 0.043994,
      "text_ratio": 0.985797,
      "vision_ratio": 0.014203
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985797,
      0.014203
    ],
    "text_vision_ratio": "0.985797:0.014203",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 162.0,
    "total_tokens": 509.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 62.857378,
      "aei_text": 3.038435,
      "aei_vision": 0.048339,
      "text_ratio": 0.98434,
      "vision_ratio": 0.01566
    },
    "middle": {
      "mdi": 59.464506,
      "aei_text": 3.032733,
      "aei_vision": 0.051001,
      "text_ratio": 0.983461,
      "vision_ratio": 0.016539
    },
    "late": {
      "mdi": 49.259138,
      "aei_text": 3.011044,
      "aei_vision": 0.061127,
      "text_ratio": 0.980103,
      "vision_ratio": 0.019897
    },
    "all": {
      "mdi": 49.259138,
      "aei_text": 3.027401,
      "aei_vision": 0.05349,
      "text_ratio": 0.980103,
      "vision_ratio": 0.019897
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980103,
      0.019897
    ],
    "text_vision_ratio": "0.980103:0.019897",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 38.090596,
      "aei_text": 2.358215,
      "aei_vision": 0.061911,
      "text_ratio": 0.974418,
      "vision_ratio": 0.025582
    },
    "middle": {
      "mdi": 22.004104,
      "aei_text": 2.29673,
      "aei_vision": 0.104377,
      "text_ratio": 0.956529,
      "vision_ratio": 0.043471
    },
    "late": {
      "mdi": 21.830701,
      "aei_text": 2.295604,
      "aei_vision": 0.105155,
      "text_ratio": 0.956199,
      "vision_ratio": 0.043801
    },
    "all": {
      "mdi": 21.830701,
      "aei_text": 2.316856,
      "aei_vision": 0.090476,
      "text_ratio": 0.956199,
      "vision_ratio": 0.043801
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.956199,
      0.043801
    ],
    "text_vision_ratio": "0.956199:0.043801",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 40.116198,
      "aei_text": 2.362584,
      "aei_vision": 0.058894,
      "text_ratio": 0.975679,
      "vision_ratio": 0.024321
    },
    "middle": {
      "mdi": 58.001491,
      "aei_text": 2.388237,
      "aei_vision": 0.041175,
      "text_ratio": 0.983051,
      "vision_ratio": 0.016949
    },
    "late": {
      "mdi": 41.166352,
      "aei_text": 2.364685,
      "aei_vision": 0.057442,
      "text_ratio": 0.976284,
      "vision_ratio": 0.023716
    },
    "all": {
      "mdi": 41.166352,
      "aei_text": 2.371838,
      "aei_vision": 0.052502,
      "text_ratio": 0.976284,
      "vision_ratio": 0.023716
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.976284,
      0.023716
    ],
    "text_vision_ratio": "0.976284:0.023716",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 158.0,
    "total_tokens": 505.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.370992,
      "aei_text": 3.072111,
      "aei_vision": 0.056503,
      "text_ratio": 0.98194,
      "vision_ratio": 0.01806
    },
    "middle": {
      "mdi": 82.498421,
      "aei_text": 3.113322,
      "aei_vision": 0.037738,
      "text_ratio": 0.988024,
      "vision_ratio": 0.011976
    },
    "late": {
      "mdi": 51.524688,
      "aei_text": 3.065536,
      "aei_vision": 0.059496,
      "text_ratio": 0.980961,
      "vision_ratio": 0.019039
    },
    "all": {
      "mdi": 51.524688,
      "aei_text": 3.083662,
      "aei_vision": 0.051243,
      "text_ratio": 0.980961,
      "vision_ratio": 0.019039
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.980961,
      0.019039
    ],
    "text_vision_ratio": "0.980961:0.019039",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 158.0,
    "total_tokens": 505.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 55.558498,
      "aei_text": 3.074663,
      "aei_vision": 0.055341,
      "text_ratio": 0.982319,
      "vision_ratio": 0.017681
    },
    "middle": {
      "mdi": 124.378636,
      "aei_text": 3.140745,
      "aei_vision": 0.025251,
      "text_ratio": 0.992024,
      "vision_ratio": 0.007976
    },
    "late": {
      "mdi": 83.771949,
      "aei_text": 3.11455,
      "aei_vision": 0.037179,
      "text_ratio": 0.988204,
      "vision_ratio": 0.011796
    },
    "all": {
      "mdi": 83.771949,
      "aei_text": 3.10998,
      "aei_vision": 0.03926,
      "text_ratio": 0.988204,
      "vision_ratio": 0.011796
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.988204,
      0.011796
    ],
    "text_vision_ratio": "0.988204:0.011796",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.041703,
      "aei_text": 2.994122,
      "aei_vision": 0.057533,
      "text_ratio": 0.981147,
      "vision_ratio": 0.018853
    },
    "middle": {
      "mdi": 43.908903,
      "aei_text": 2.972611,
      "aei_vision": 0.0677,
      "text_ratio": 0.977733,
      "vision_ratio": 0.022267
    },
    "late": {
      "mdi": 35.157128,
      "aei_text": 2.938978,
      "aei_vision": 0.083596,
      "text_ratio": 0.972343,
      "vision_ratio": 0.027657
    },
    "all": {
      "mdi": 35.157128,
      "aei_text": 2.968569,
      "aei_vision": 0.06961,
      "text_ratio": 0.972343,
      "vision_ratio": 0.027657
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972343,
      0.027657
    ],
    "text_vision_ratio": "0.972343:0.027657",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 53.587221,
      "aei_text": 2.9975,
      "aei_vision": 0.055937,
      "text_ratio": 0.981681,
      "vision_ratio": 0.018319
    },
    "middle": {
      "mdi": 58.003977,
      "aei_text": 3.006194,
      "aei_vision": 0.051827,
      "text_ratio": 0.983052,
      "vision_ratio": 0.016948
    },
    "late": {
      "mdi": 43.149722,
      "aei_text": 2.970209,
      "aei_vision": 0.068835,
      "text_ratio": 0.97735,
      "vision_ratio": 0.02265
    },
    "all": {
      "mdi": 43.149722,
      "aei_text": 2.991308,
      "aei_vision": 0.058863,
      "text_ratio": 0.97735,
      "vision_ratio": 0.02265
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97735,
      0.02265
    ],
    "text_vision_ratio": "0.977350:0.022650",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.886551,
      "aei_text": 2.350311,
      "aei_vision": 0.06737,
      "text_ratio": 0.972134,
      "vision_ratio": 0.027866
    },
    "middle": {
      "mdi": 67.30111,
      "aei_text": 2.396301,
      "aei_vision": 0.035606,
      "text_ratio": 0.985359,
      "vision_ratio": 0.014641
    },
    "late": {
      "mdi": 55.863473,
      "aei_text": 2.386013,
      "aei_vision": 0.042712,
      "text_ratio": 0.982414,
      "vision_ratio": 0.017586
    },
    "all": {
      "mdi": 55.863473,
      "aei_text": 2.377546,
      "aei_vision": 0.048559,
      "text_ratio": 0.982414,
      "vision_ratio": 0.017586
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982414,
      0.017586
    ],
    "text_vision_ratio": "0.982414:0.017586",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 163.0,
    "total_tokens": 399.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.469408,
      "aei_text": 2.346352,
      "aei_vision": 0.070104,
      "text_ratio": 0.970989,
      "vision_ratio": 0.029011
    },
    "middle": {
      "mdi": 37.596282,
      "aei_text": 2.35708,
      "aei_vision": 0.062695,
      "text_ratio": 0.974091,
      "vision_ratio": 0.025909
    },
    "late": {
      "mdi": 24.859643,
      "aei_text": 2.313133,
      "aei_vision": 0.093048,
      "text_ratio": 0.96133,
      "vision_ratio": 0.03867
    },
    "all": {
      "mdi": 24.859643,
      "aei_text": 2.338853,
      "aei_vision": 0.075284,
      "text_ratio": 0.96133,
      "vision_ratio": 0.03867
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.96133,
      0.03867
    ],
    "text_vision_ratio": "0.961330:0.038670",
    "skip_reason": null
  }
}
```


## === Rollout Step 41 ===
Step: 40/43 | 2025-10-22 19:09:24

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.310 | 58.398 | 45.664 | 45.664 |
| MDI Std | 12.744 | 28.886 | 21.326 | 21.326 |
| Vision Tokens | 345.2 ± 71.1 |
| Text Tokens | 163.8 ± 2.8 |
| Total Tokens | 509.0 ± 72.3 |
| Vision Ratio | 0.671 |
| Text Ratio | 0.329 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 160.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 31.721734,
      "aei_text": 2.46967,
      "aei_vision": 0.077854,
      "text_ratio": 0.969439,
      "vision_ratio": 0.030561
    },
    "middle": {
      "mdi": 44.102459,
      "aei_text": 2.503288,
      "aei_vision": 0.056761,
      "text_ratio": 0.977828,
      "vision_ratio": 0.022172
    },
    "late": {
      "mdi": 48.116579,
      "aei_text": 2.510592,
      "aei_vision": 0.052177,
      "text_ratio": 0.97964,
      "vision_ratio": 0.02036
    },
    "all": {
      "mdi": 48.116579,
      "aei_text": 2.494508,
      "aei_vision": 0.06227,
      "text_ratio": 0.97964,
      "vision_ratio": 0.02036
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.97964,
      0.02036
    ],
    "text_vision_ratio": "0.979640:0.020360",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 255.0,
    "text_tokens": 160.0,
    "total_tokens": 415.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 34.727696,
      "aei_text": 2.479939,
      "aei_vision": 0.071411,
      "text_ratio": 0.972011,
      "vision_ratio": 0.027989
    },
    "middle": {
      "mdi": 70.196827,
      "aei_text": 2.536169,
      "aei_vision": 0.036129,
      "text_ratio": 0.985954,
      "vision_ratio": 0.014046
    },
    "late": {
      "mdi": 42.790102,
      "aei_text": 2.500613,
      "aei_vision": 0.058439,
      "text_ratio": 0.977164,
      "vision_ratio": 0.022836
    },
    "all": {
      "mdi": 42.790102,
      "aei_text": 2.505573,
      "aei_vision": 0.055327,
      "text_ratio": 0.977164,
      "vision_ratio": 0.022836
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977164,
      0.022836
    ],
    "text_vision_ratio": "0.977164:0.022836",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.095991,
      "aei_text": 3.001294,
      "aei_vision": 0.059911,
      "text_ratio": 0.980429,
      "vision_ratio": 0.019571
    },
    "middle": {
      "mdi": 76.129611,
      "aei_text": 3.043722,
      "aei_vision": 0.039981,
      "text_ratio": 0.987035,
      "vision_ratio": 0.012965
    },
    "late": {
      "mdi": 66.33294,
      "aei_text": 3.031543,
      "aei_vision": 0.045702,
      "text_ratio": 0.985148,
      "vision_ratio": 0.014852
    },
    "all": {
      "mdi": 66.33294,
      "aei_text": 3.025516,
      "aei_vision": 0.048533,
      "text_ratio": 0.985148,
      "vision_ratio": 0.014852
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985148,
      0.014852
    ],
    "text_vision_ratio": "0.985148:0.014852",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 163.0,
    "total_tokens": 510.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.592953,
      "aei_text": 3.000054,
      "aei_vision": 0.060494,
      "text_ratio": 0.980234,
      "vision_ratio": 0.019766
    },
    "middle": {
      "mdi": 69.742991,
      "aei_text": 3.036159,
      "aei_vision": 0.043534,
      "text_ratio": 0.985864,
      "vision_ratio": 0.014136
    },
    "late": {
      "mdi": 48.564357,
      "aei_text": 2.997441,
      "aei_vision": 0.061721,
      "text_ratio": 0.979824,
      "vision_ratio": 0.020176
    },
    "all": {
      "mdi": 48.564357,
      "aei_text": 3.011222,
      "aei_vision": 0.055247,
      "text_ratio": 0.979824,
      "vision_ratio": 0.020176
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979824,
      0.020176
    ],
    "text_vision_ratio": "0.979824:0.020176",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 58.246996,
      "aei_text": 3.288945,
      "aei_vision": 0.056465,
      "text_ratio": 0.983122,
      "vision_ratio": 0.016878
    },
    "middle": {
      "mdi": 39.583153,
      "aei_text": 3.228087,
      "aei_vision": 0.081552,
      "text_ratio": 0.975359,
      "vision_ratio": 0.024641
    },
    "late": {
      "mdi": 29.687166,
      "aei_text": 3.16712,
      "aei_vision": 0.106683,
      "text_ratio": 0.967413,
      "vision_ratio": 0.032587
    },
    "all": {
      "mdi": 29.687166,
      "aei_text": 3.228066,
      "aei_vision": 0.081561,
      "text_ratio": 0.967413,
      "vision_ratio": 0.032587
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967413,
      0.032587
    ],
    "text_vision_ratio": "0.967413:0.032587",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.330456,
      "aei_text": 3.284477,
      "aei_vision": 0.058307,
      "text_ratio": 0.982557,
      "vision_ratio": 0.017443
    },
    "middle": {
      "mdi": 108.056688,
      "aei_text": 3.350701,
      "aei_vision": 0.031009,
      "text_ratio": 0.99083,
      "vision_ratio": 0.00917
    },
    "late": {
      "mdi": 80.446615,
      "aei_text": 3.325639,
      "aei_vision": 0.04134,
      "text_ratio": 0.987722,
      "vision_ratio": 0.012278
    },
    "all": {
      "mdi": 80.446615,
      "aei_text": 3.320272,
      "aei_vision": 0.043552,
      "text_ratio": 0.987722,
      "vision_ratio": 0.012278
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987722,
      0.012278
    ],
    "text_vision_ratio": "0.987722:0.012278",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 54.083381,
      "aei_text": 3.213468,
      "aei_vision": 0.059417,
      "text_ratio": 0.981846,
      "vision_ratio": 0.018154
    },
    "middle": {
      "mdi": 93.009636,
      "aei_text": 3.270543,
      "aei_vision": 0.035163,
      "text_ratio": 0.989363,
      "vision_ratio": 0.010637
    },
    "late": {
      "mdi": 67.228829,
      "aei_text": 3.239884,
      "aei_vision": 0.048192,
      "text_ratio": 0.985343,
      "vision_ratio": 0.014657
    },
    "all": {
      "mdi": 67.228829,
      "aei_text": 3.241298,
      "aei_vision": 0.047591,
      "text_ratio": 0.985343,
      "vision_ratio": 0.014657
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985343,
      0.014657
    ],
    "text_vision_ratio": "0.985343:0.014657",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 167.0,
    "total_tokens": 560.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.876652,
      "aei_text": 3.207778,
      "aei_vision": 0.061835,
      "text_ratio": 0.981088,
      "vision_ratio": 0.018912
    },
    "middle": {
      "mdi": 94.372644,
      "aei_text": 3.271709,
      "aei_vision": 0.034668,
      "text_ratio": 0.989515,
      "vision_ratio": 0.010485
    },
    "late": {
      "mdi": 75.932401,
      "aei_text": 3.252492,
      "aei_vision": 0.042834,
      "text_ratio": 0.987002,
      "vision_ratio": 0.012998
    },
    "all": {
      "mdi": 75.932401,
      "aei_text": 3.244006,
      "aei_vision": 0.04644,
      "text_ratio": 0.987002,
      "vision_ratio": 0.012998
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987002,
      0.012998
    ],
    "text_vision_ratio": "0.987002:0.012998",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 169.0,
    "total_tokens": 493.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.465081,
      "aei_text": 2.808316,
      "aei_vision": 0.056774,
      "text_ratio": 0.980184,
      "vision_ratio": 0.019816
    },
    "middle": {
      "mdi": 81.589682,
      "aei_text": 2.850187,
      "aei_vision": 0.034933,
      "text_ratio": 0.987892,
      "vision_ratio": 0.012108
    },
    "late": {
      "mdi": 55.789055,
      "aei_text": 2.820244,
      "aei_vision": 0.050552,
      "text_ratio": 0.982391,
      "vision_ratio": 0.017609
    },
    "all": {
      "mdi": 55.789055,
      "aei_text": 2.826245,
      "aei_vision": 0.047422,
      "text_ratio": 0.982391,
      "vision_ratio": 0.017609
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982391,
      0.017609
    ],
    "text_vision_ratio": "0.982391:0.017609",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 169.0,
    "total_tokens": 493.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.503379,
      "aei_text": 2.803995,
      "aei_vision": 0.059027,
      "text_ratio": 0.979383,
      "vision_ratio": 0.020617
    },
    "middle": {
      "mdi": 49.022732,
      "aei_text": 2.80737,
      "aei_vision": 0.057267,
      "text_ratio": 0.980009,
      "vision_ratio": 0.019991
    },
    "late": {
      "mdi": 43.254074,
      "aei_text": 2.79335,
      "aei_vision": 0.06458,
      "text_ratio": 0.977403,
      "vision_ratio": 0.022597
    },
    "all": {
      "mdi": 43.254074,
      "aei_text": 2.801571,
      "aei_vision": 0.060292,
      "text_ratio": 0.977403,
      "vision_ratio": 0.022597
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977403,
      0.022597
    ],
    "text_vision_ratio": "0.977403:0.022597",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 45.499684,
      "aei_text": 3.226415,
      "aei_vision": 0.070911,
      "text_ratio": 0.978494,
      "vision_ratio": 0.021506
    },
    "middle": {
      "mdi": 85.212793,
      "aei_text": 3.303443,
      "aei_vision": 0.038767,
      "text_ratio": 0.988401,
      "vision_ratio": 0.011599
    },
    "late": {
      "mdi": 70.648469,
      "aei_text": 3.28492,
      "aei_vision": 0.046497,
      "text_ratio": 0.986043,
      "vision_ratio": 0.013957
    },
    "all": {
      "mdi": 70.648469,
      "aei_text": 3.271593,
      "aei_vision": 0.052058,
      "text_ratio": 0.986043,
      "vision_ratio": 0.013957
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.986043,
      0.013957
    ],
    "text_vision_ratio": "0.986043:0.013957",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.125546,
      "aei_text": 3.228607,
      "aei_vision": 0.069996,
      "text_ratio": 0.97878,
      "vision_ratio": 0.02122
    },
    "middle": {
      "mdi": 35.079532,
      "aei_text": 3.179167,
      "aei_vision": 0.090627,
      "text_ratio": 0.972283,
      "vision_ratio": 0.027717
    },
    "late": {
      "mdi": 24.670822,
      "aei_text": 3.095653,
      "aei_vision": 0.125478,
      "text_ratio": 0.961045,
      "vision_ratio": 0.038955
    },
    "all": {
      "mdi": 24.670822,
      "aei_text": 3.167797,
      "aei_vision": 0.095372,
      "text_ratio": 0.961045,
      "vision_ratio": 0.038955
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.961045,
      0.038955
    ],
    "text_vision_ratio": "0.961045:0.038955",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 164.0,
    "total_tokens": 603.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.24511,
      "aei_text": 3.127656,
      "aei_vision": 0.205158,
      "text_ratio": 0.938443,
      "vision_ratio": 0.061557
    },
    "middle": {
      "mdi": 21.289265,
      "aei_text": 3.266156,
      "aei_vision": 0.153418,
      "text_ratio": 0.955135,
      "vision_ratio": 0.044865
    },
    "late": {
      "mdi": 20.122083,
      "aei_text": 3.245131,
      "aei_vision": 0.161272,
      "text_ratio": 0.952656,
      "vision_ratio": 0.047344
    },
    "all": {
      "mdi": 20.122083,
      "aei_text": 3.212985,
      "aei_vision": 0.173281,
      "text_ratio": 0.952656,
      "vision_ratio": 0.047344
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.952656,
      0.047344
    ],
    "text_vision_ratio": "0.952656:0.047344",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 439.0,
    "text_tokens": 164.0,
    "total_tokens": 603.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 15.828208,
      "aei_text": 3.144961,
      "aei_vision": 0.198693,
      "text_ratio": 0.940576,
      "vision_ratio": 0.059424
    },
    "middle": {
      "mdi": 15.156317,
      "aei_text": 3.124922,
      "aei_vision": 0.20618,
      "text_ratio": 0.938105,
      "vision_ratio": 0.061895
    },
    "late": {
      "mdi": 15.287783,
      "aei_text": 3.128961,
      "aei_vision": 0.204671,
      "text_ratio": 0.938604,
      "vision_ratio": 0.061396
    },
    "all": {
      "mdi": 15.287783,
      "aei_text": 3.132948,
      "aei_vision": 0.203181,
      "text_ratio": 0.938604,
      "vision_ratio": 0.061396
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.938604,
      0.061396
    ],
    "text_vision_ratio": "0.938604:0.061396",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 161.0,
    "total_tokens": 379.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.161216,
      "aei_text": 2.293341,
      "aei_vision": 0.044826,
      "text_ratio": 0.980829,
      "vision_ratio": 0.019171
    },
    "middle": {
      "mdi": 27.572263,
      "aei_text": 2.243845,
      "aei_vision": 0.081381,
      "text_ratio": 0.965001,
      "vision_ratio": 0.034999
    },
    "late": {
      "mdi": 22.27851,
      "aei_text": 2.219162,
      "aei_vision": 0.09961,
      "text_ratio": 0.957042,
      "vision_ratio": 0.042958
    },
    "all": {
      "mdi": 22.27851,
      "aei_text": 2.252119,
      "aei_vision": 0.07527,
      "text_ratio": 0.957042,
      "vision_ratio": 0.042958
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.957042,
      0.042958
    ],
    "text_vision_ratio": "0.957042:0.042958",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 218.0,
    "text_tokens": 161.0,
    "total_tokens": 379.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.449641,
      "aei_text": 2.293673,
      "aei_vision": 0.044581,
      "text_ratio": 0.980934,
      "vision_ratio": 0.019066
    },
    "middle": {
      "mdi": 24.254974,
      "aei_text": 2.229571,
      "aei_vision": 0.091922,
      "text_ratio": 0.960404,
      "vision_ratio": 0.039596
    },
    "late": {
      "mdi": 19.481448,
      "aei_text": 2.201055,
      "aei_vision": 0.112982,
      "text_ratio": 0.951175,
      "vision_ratio": 0.048825
    },
    "all": {
      "mdi": 19.481448,
      "aei_text": 2.241436,
      "aei_vision": 0.08316,
      "text_ratio": 0.951175,
      "vision_ratio": 0.048825
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951175,
      0.048825
    ],
    "text_vision_ratio": "0.951175:0.048825",
    "skip_reason": null
  }
}
```


## === Rollout Step 42 ===
Step: 41/43 | 2025-10-22 19:10:43

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 44.103 | 57.668 | 51.754 | 51.754 |
| MDI Std | 15.937 | 23.665 | 19.451 | 19.451 |
| Vision Tokens | 342.5 ± 106.4 |
| Text Tokens | 162.5 ± 2.6 |
| Total Tokens | 505.0 ± 106.7 |
| Vision Ratio | 0.661 |
| Text Ratio | 0.339 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 61.493984,
      "aei_text": 3.295903,
      "aei_vision": 0.053597,
      "text_ratio": 0.983998,
      "vision_ratio": 0.016002
    },
    "middle": {
      "mdi": 82.516187,
      "aei_text": 3.328082,
      "aei_vision": 0.040332,
      "text_ratio": 0.988026,
      "vision_ratio": 0.011974
    },
    "late": {
      "mdi": 79.107402,
      "aei_text": 3.323992,
      "aei_vision": 0.042019,
      "text_ratio": 0.987517,
      "vision_ratio": 0.012483
    },
    "all": {
      "mdi": 79.107402,
      "aei_text": 3.315991,
      "aei_vision": 0.045317,
      "text_ratio": 0.987517,
      "vision_ratio": 0.012483
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987517,
      0.012483
    ],
    "text_vision_ratio": "0.987517:0.012483",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 162.0,
    "total_tokens": 555.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 59.306858,
      "aei_text": 3.291297,
      "aei_vision": 0.055496,
      "text_ratio": 0.983418,
      "vision_ratio": 0.016582
    },
    "middle": {
      "mdi": 69.79588,
      "aei_text": 3.310849,
      "aei_vision": 0.047436,
      "text_ratio": 0.985875,
      "vision_ratio": 0.014125
    },
    "late": {
      "mdi": 54.642758,
      "aei_text": 3.280294,
      "aei_vision": 0.060032,
      "text_ratio": 0.982028,
      "vision_ratio": 0.017972
    },
    "all": {
      "mdi": 54.642758,
      "aei_text": 3.294147,
      "aei_vision": 0.054321,
      "text_ratio": 0.982028,
      "vision_ratio": 0.017972
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982028,
      0.017972
    ],
    "text_vision_ratio": "0.982028:0.017972",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 146.0,
    "text_tokens": 161.0,
    "total_tokens": 307.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 25.949376,
      "aei_text": 1.842446,
      "aei_vision": 0.071002,
      "text_ratio": 0.962893,
      "vision_ratio": 0.037107
    },
    "middle": {
      "mdi": 51.421531,
      "aei_text": 1.873788,
      "aei_vision": 0.03644,
      "text_ratio": 0.980924,
      "vision_ratio": 0.019076
    },
    "late": {
      "mdi": 44.131279,
      "aei_text": 1.868439,
      "aei_vision": 0.042338,
      "text_ratio": 0.977842,
      "vision_ratio": 0.022158
    },
    "all": {
      "mdi": 44.131279,
      "aei_text": 1.861559,
      "aei_vision": 0.049925,
      "text_ratio": 0.977842,
      "vision_ratio": 0.022158
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.977842,
      0.022158
    ],
    "text_vision_ratio": "0.977842:0.022158",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 146.0,
    "text_tokens": 161.0,
    "total_tokens": 307.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 23.805814,
      "aei_text": 1.836861,
      "aei_vision": 0.07716,
      "text_ratio": 0.959687,
      "vision_ratio": 0.040313
    },
    "middle": {
      "mdi": 34.671161,
      "aei_text": 1.85823,
      "aei_vision": 0.053596,
      "text_ratio": 0.971966,
      "vision_ratio": 0.028034
    },
    "late": {
      "mdi": 29.240225,
      "aei_text": 1.849474,
      "aei_vision": 0.063251,
      "text_ratio": 0.966931,
      "vision_ratio": 0.033069
    },
    "all": {
      "mdi": 29.240225,
      "aei_text": 1.848186,
      "aei_vision": 0.064672,
      "text_ratio": 0.966931,
      "vision_ratio": 0.033069
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.966931,
      0.033069
    ],
    "text_vision_ratio": "0.966931:0.033069",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.681442,
      "aei_text": 2.371161,
      "aei_vision": 0.0704,
      "text_ratio": 0.971166,
      "vision_ratio": 0.028834
    },
    "middle": {
      "mdi": 27.545202,
      "aei_text": 2.349204,
      "aei_vision": 0.085285,
      "text_ratio": 0.964968,
      "vision_ratio": 0.035032
    },
    "late": {
      "mdi": 26.173068,
      "aei_text": 2.342961,
      "aei_vision": 0.089518,
      "text_ratio": 0.963199,
      "vision_ratio": 0.036801
    },
    "all": {
      "mdi": 26.173068,
      "aei_text": 2.354438,
      "aei_vision": 0.081737,
      "text_ratio": 0.963199,
      "vision_ratio": 0.036801
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.963199,
      0.036801
    ],
    "text_vision_ratio": "0.963199:0.036801",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 236.0,
    "text_tokens": 160.0,
    "total_tokens": 396.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 33.258928,
      "aei_text": 2.369897,
      "aei_vision": 0.071256,
      "text_ratio": 0.970811,
      "vision_ratio": 0.029189
    },
    "middle": {
      "mdi": 36.568809,
      "aei_text": 2.379042,
      "aei_vision": 0.065057,
      "text_ratio": 0.973382,
      "vision_ratio": 0.026618
    },
    "late": {
      "mdi": 35.548218,
      "aei_text": 2.376396,
      "aei_vision": 0.06685,
      "text_ratio": 0.972639,
      "vision_ratio": 0.027361
    },
    "all": {
      "mdi": 35.548218,
      "aei_text": 2.37511,
      "aei_vision": 0.067722,
      "text_ratio": 0.972639,
      "vision_ratio": 0.027361
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972639,
      0.027361
    ],
    "text_vision_ratio": "0.972639:0.027361",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 66.365478,
      "aei_text": 3.264652,
      "aei_vision": 0.049192,
      "text_ratio": 0.985156,
      "vision_ratio": 0.014844
    },
    "middle": {
      "mdi": 82.516517,
      "aei_text": 3.286941,
      "aei_vision": 0.039834,
      "text_ratio": 0.988026,
      "vision_ratio": 0.011974
    },
    "late": {
      "mdi": 68.918839,
      "aei_text": 3.268848,
      "aei_vision": 0.04743,
      "text_ratio": 0.985698,
      "vision_ratio": 0.014302
    },
    "all": {
      "mdi": 68.918839,
      "aei_text": 3.273476,
      "aei_vision": 0.045487,
      "text_ratio": 0.985698,
      "vision_ratio": 0.014302
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985698,
      0.014302
    ],
    "text_vision_ratio": "0.985698:0.014302",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 64.840817,
      "aei_text": 3.261994,
      "aei_vision": 0.050308,
      "text_ratio": 0.984812,
      "vision_ratio": 0.015188
    },
    "middle": {
      "mdi": 91.293549,
      "aei_text": 3.295831,
      "aei_vision": 0.036101,
      "text_ratio": 0.989165,
      "vision_ratio": 0.010835
    },
    "late": {
      "mdi": 91.425027,
      "aei_text": 3.295952,
      "aei_vision": 0.036051,
      "text_ratio": 0.98918,
      "vision_ratio": 0.01082
    },
    "all": {
      "mdi": 91.425027,
      "aei_text": 3.284598,
      "aei_vision": 0.040818,
      "text_ratio": 0.98918,
      "vision_ratio": 0.01082
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98918,
      0.01082
    ],
    "text_vision_ratio": "0.989180:0.010820",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 160.0,
    "total_tokens": 691.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.400428,
      "aei_text": 3.658833,
      "aei_vision": 0.198845,
      "text_ratio": 0.948455,
      "vision_ratio": 0.051545
    },
    "middle": {
      "mdi": 21.204739,
      "aei_text": 3.734296,
      "aei_vision": 0.176107,
      "text_ratio": 0.954965,
      "vision_ratio": 0.045035
    },
    "late": {
      "mdi": 29.464286,
      "aei_text": 3.881547,
      "aei_vision": 0.131737,
      "text_ratio": 0.967175,
      "vision_ratio": 0.032825
    },
    "all": {
      "mdi": 29.464286,
      "aei_text": 3.758227,
      "aei_vision": 0.168896,
      "text_ratio": 0.967175,
      "vision_ratio": 0.032825
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.967175,
      0.032825
    ],
    "text_vision_ratio": "0.967175:0.032825",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 160.0,
    "total_tokens": 691.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 17.164448,
      "aei_text": 3.619013,
      "aei_vision": 0.210844,
      "text_ratio": 0.944947,
      "vision_ratio": 0.055053
    },
    "middle": {
      "mdi": 15.030223,
      "aei_text": 3.537624,
      "aei_vision": 0.235367,
      "text_ratio": 0.937618,
      "vision_ratio": 0.062382
    },
    "late": {
      "mdi": 19.422658,
      "aei_text": 3.688497,
      "aei_vision": 0.189907,
      "text_ratio": 0.951035,
      "vision_ratio": 0.048965
    },
    "all": {
      "mdi": 19.422658,
      "aei_text": 3.615006,
      "aei_vision": 0.212051,
      "text_ratio": 0.951035,
      "vision_ratio": 0.048965
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.951035,
      0.048965
    ],
    "text_vision_ratio": "0.951035:0.048965",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 50.906342,
      "aei_text": 3.039269,
      "aei_vision": 0.059703,
      "text_ratio": 0.980735,
      "vision_ratio": 0.019265
    },
    "middle": {
      "mdi": 74.595588,
      "aei_text": 3.079226,
      "aei_vision": 0.041279,
      "text_ratio": 0.986772,
      "vision_ratio": 0.013228
    },
    "late": {
      "mdi": 49.429383,
      "aei_text": 3.035562,
      "aei_vision": 0.061412,
      "text_ratio": 0.98017,
      "vision_ratio": 0.01983
    },
    "all": {
      "mdi": 49.429383,
      "aei_text": 3.051345,
      "aei_vision": 0.054135,
      "text_ratio": 0.98017,
      "vision_ratio": 0.01983
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98017,
      0.01983
    ],
    "text_vision_ratio": "0.980170:0.019830",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.129872,
      "aei_text": 3.042186,
      "aei_vision": 0.058358,
      "text_ratio": 0.981178,
      "vision_ratio": 0.018822
    },
    "middle": {
      "mdi": 88.107313,
      "aei_text": 3.092625,
      "aei_vision": 0.035101,
      "text_ratio": 0.988778,
      "vision_ratio": 0.011222
    },
    "late": {
      "mdi": 65.581949,
      "aei_text": 3.067316,
      "aei_vision": 0.046771,
      "text_ratio": 0.984981,
      "vision_ratio": 0.015019
    },
    "all": {
      "mdi": 65.581949,
      "aei_text": 3.067377,
      "aei_vision": 0.046743,
      "text_ratio": 0.984981,
      "vision_ratio": 0.015019
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.984981,
      0.015019
    ],
    "text_vision_ratio": "0.984981:0.015019",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.118878,
      "aei_text": 2.957625,
      "aei_vision": 0.057858,
      "text_ratio": 0.980813,
      "vision_ratio": 0.019187
    },
    "middle": {
      "mdi": 57.169304,
      "aei_text": 2.969902,
      "aei_vision": 0.051949,
      "text_ratio": 0.982809,
      "vision_ratio": 0.017191
    },
    "late": {
      "mdi": 55.736786,
      "aei_text": 2.967227,
      "aei_vision": 0.053236,
      "text_ratio": 0.982375,
      "vision_ratio": 0.017625
    },
    "all": {
      "mdi": 55.736786,
      "aei_text": 2.964916,
      "aei_vision": 0.054349,
      "text_ratio": 0.982375,
      "vision_ratio": 0.017625
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.982375,
      0.017625
    ],
    "text_vision_ratio": "0.982375:0.017625",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 167.0,
    "total_tokens": 514.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 52.394958,
      "aei_text": 2.960441,
      "aei_vision": 0.056502,
      "text_ratio": 0.981272,
      "vision_ratio": 0.018728
    },
    "middle": {
      "mdi": 69.887854,
      "aei_text": 2.988979,
      "aei_vision": 0.042768,
      "text_ratio": 0.985893,
      "vision_ratio": 0.014107
    },
    "late": {
      "mdi": 59.557113,
      "aei_text": 2.974084,
      "aei_vision": 0.049937,
      "text_ratio": 0.983487,
      "vision_ratio": 0.016513
    },
    "all": {
      "mdi": 59.557113,
      "aei_text": 2.974505,
      "aei_vision": 0.049734,
      "text_ratio": 0.983487,
      "vision_ratio": 0.016513
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983487,
      0.016513
    ],
    "text_vision_ratio": "0.983487:0.016513",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.337374,
      "aei_text": 2.971038,
      "aei_vision": 0.062763,
      "text_ratio": 0.979312,
      "vision_ratio": 0.020688
    },
    "middle": {
      "mdi": 58.65897,
      "aei_text": 2.995631,
      "aei_vision": 0.051069,
      "text_ratio": 0.983238,
      "vision_ratio": 0.016762
    },
    "late": {
      "mdi": 59.417516,
      "aei_text": 2.996956,
      "aei_vision": 0.050439,
      "text_ratio": 0.983449,
      "vision_ratio": 0.016551
    },
    "all": {
      "mdi": 59.417516,
      "aei_text": 2.987877,
      "aei_vision": 0.054756,
      "text_ratio": 0.983449,
      "vision_ratio": 0.016551
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983449,
      0.016551
    ],
    "text_vision_ratio": "0.983449:0.016551",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 165.0,
    "total_tokens": 512.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 47.494195,
      "aei_text": 2.971455,
      "aei_vision": 0.062565,
      "text_ratio": 0.979379,
      "vision_ratio": 0.020621
    },
    "middle": {
      "mdi": 61.708005,
      "aei_text": 3.000763,
      "aei_vision": 0.048628,
      "text_ratio": 0.984053,
      "vision_ratio": 0.015947
    },
    "late": {
      "mdi": 60.265639,
      "aei_text": 2.998398,
      "aei_vision": 0.049753,
      "text_ratio": 0.983678,
      "vision_ratio": 0.016322
    },
    "all": {
      "mdi": 60.265639,
      "aei_text": 2.990215,
      "aei_vision": 0.053644,
      "text_ratio": 0.983678,
      "vision_ratio": 0.016322
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983678,
      0.016322
    ],
    "text_vision_ratio": "0.983678:0.016322",
    "skip_reason": null
  }
}
```


## === Rollout Step 43 ===
Step: 42/43 | 2025-10-22 19:12:02

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 47.285 | 64.827 | 56.522 | 56.522 |
| MDI Std | 12.405 | 27.810 | 26.001 | 26.001 |
| Vision Tokens | 393.0 ± 59.8 |
| Text Tokens | 163.1 ± 2.5 |
| Total Tokens | 556.1 ± 58.4 |
| Vision Ratio | 0.704 |
| Text Ratio | 0.296 |

#### Sample 1

```json
{
  "sample": 1,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.017296,
      "aei_text": 2.972948,
      "aei_vision": 0.06754,
      "text_ratio": 0.977786,
      "vision_ratio": 0.022214
    },
    "middle": {
      "mdi": 44.413934,
      "aei_text": 2.974166,
      "aei_vision": 0.066965,
      "text_ratio": 0.97798,
      "vision_ratio": 0.02202
    },
    "late": {
      "mdi": 39.82622,
      "aei_text": 2.958668,
      "aei_vision": 0.074289,
      "text_ratio": 0.975506,
      "vision_ratio": 0.024494
    },
    "all": {
      "mdi": 39.82622,
      "aei_text": 2.968597,
      "aei_vision": 0.069597,
      "text_ratio": 0.975506,
      "vision_ratio": 0.024494
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.975506,
      0.024494
    ],
    "text_vision_ratio": "0.975506:0.024494",
    "skip_reason": null
  }
}
```

#### Sample 2

```json
{
  "sample": 2,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 164.0,
    "total_tokens": 511.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 42.983397,
      "aei_text": 2.969672,
      "aei_vision": 0.069089,
      "text_ratio": 0.977264,
      "vision_ratio": 0.022736
    },
    "middle": {
      "mdi": 72.45828,
      "aei_text": 3.027449,
      "aei_vision": 0.041782,
      "text_ratio": 0.986387,
      "vision_ratio": 0.013613
    },
    "late": {
      "mdi": 67.231462,
      "aei_text": 3.020786,
      "aei_vision": 0.044931,
      "text_ratio": 0.985344,
      "vision_ratio": 0.014656
    },
    "all": {
      "mdi": 67.231462,
      "aei_text": 3.005961,
      "aei_vision": 0.051938,
      "text_ratio": 0.985344,
      "vision_ratio": 0.014656
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985344,
      0.014656
    ],
    "text_vision_ratio": "0.985344:0.014656",
    "skip_reason": null
  }
}
```

#### Sample 3

```json
{
  "sample": 3,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 56.179591,
      "aei_text": 3.050971,
      "aei_vision": 0.054307,
      "text_ratio": 0.982511,
      "vision_ratio": 0.017489
    },
    "middle": {
      "mdi": 81.658338,
      "aei_text": 3.086769,
      "aei_vision": 0.037801,
      "text_ratio": 0.987902,
      "vision_ratio": 0.012098
    },
    "late": {
      "mdi": 113.915387,
      "aei_text": 3.10955,
      "aei_vision": 0.027297,
      "text_ratio": 0.991298,
      "vision_ratio": 0.008702
    },
    "all": {
      "mdi": 113.915387,
      "aei_text": 3.082428,
      "aei_vision": 0.039803,
      "text_ratio": 0.991298,
      "vision_ratio": 0.008702
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.991298,
      0.008702
    ],
    "text_vision_ratio": "0.991298:0.008702",
    "skip_reason": null
  }
}
```

#### Sample 4

```json
{
  "sample": 4,
  "token_counts": {
    "vision_tokens": 347.0,
    "text_tokens": 160.0,
    "total_tokens": 507.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 62.853231,
      "aei_text": 3.063059,
      "aei_vision": 0.048734,
      "text_ratio": 0.984339,
      "vision_ratio": 0.015661
    },
    "middle": {
      "mdi": 117.072919,
      "aei_text": 3.111117,
      "aei_vision": 0.026574,
      "text_ratio": 0.991531,
      "vision_ratio": 0.008469
    },
    "late": {
      "mdi": 106.87885,
      "aei_text": 3.10573,
      "aei_vision": 0.029058,
      "text_ratio": 0.99073,
      "vision_ratio": 0.00927
    },
    "all": {
      "mdi": 106.87885,
      "aei_text": 3.093306,
      "aei_vision": 0.034787,
      "text_ratio": 0.99073,
      "vision_ratio": 0.00927
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.99073,
      0.00927
    ],
    "text_vision_ratio": "0.990730:0.009270",
    "skip_reason": null
  }
}
```

#### Sample 5

```json
{
  "sample": 5,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 48.486456,
      "aei_text": 3.23639,
      "aei_vision": 0.066748,
      "text_ratio": 0.979792,
      "vision_ratio": 0.020208
    },
    "middle": {
      "mdi": 104.029923,
      "aei_text": 3.319868,
      "aei_vision": 0.031913,
      "text_ratio": 0.990479,
      "vision_ratio": 0.009521
    },
    "late": {
      "mdi": 77.663193,
      "aei_text": 3.294682,
      "aei_vision": 0.042423,
      "text_ratio": 0.987288,
      "vision_ratio": 0.012712
    },
    "all": {
      "mdi": 77.663193,
      "aei_text": 3.283645,
      "aei_vision": 0.047029,
      "text_ratio": 0.987288,
      "vision_ratio": 0.012712
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.987288,
      0.012712
    ],
    "text_vision_ratio": "0.987288:0.012712",
    "skip_reason": null
  }
}
```

#### Sample 6

```json
{
  "sample": 6,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 164.0,
    "total_tokens": 557.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.964107,
      "aei_text": 3.240904,
      "aei_vision": 0.064865,
      "text_ratio": 0.980378,
      "vision_ratio": 0.019622
    },
    "middle": {
      "mdi": 49.863547,
      "aei_text": 3.240605,
      "aei_vision": 0.064989,
      "text_ratio": 0.98034,
      "vision_ratio": 0.01966
    },
    "late": {
      "mdi": 36.841145,
      "aei_text": 3.188918,
      "aei_vision": 0.086559,
      "text_ratio": 0.973574,
      "vision_ratio": 0.026426
    },
    "all": {
      "mdi": 36.841145,
      "aei_text": 3.223474,
      "aei_vision": 0.072138,
      "text_ratio": 0.973574,
      "vision_ratio": 0.026426
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973574,
      0.026426
    ],
    "text_vision_ratio": "0.973574:0.026426",
    "skip_reason": null
  }
}
```

#### Sample 7

```json
{
  "sample": 7,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 164.0,
    "total_tokens": 488.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 46.972218,
      "aei_text": 2.85551,
      "aei_vision": 0.060791,
      "text_ratio": 0.979155,
      "vision_ratio": 0.020845
    },
    "middle": {
      "mdi": 51.992629,
      "aei_text": 2.866682,
      "aei_vision": 0.055136,
      "text_ratio": 0.981129,
      "vision_ratio": 0.018871
    },
    "late": {
      "mdi": 35.855289,
      "aei_text": 2.820217,
      "aei_vision": 0.078656,
      "text_ratio": 0.972867,
      "vision_ratio": 0.027133
    },
    "all": {
      "mdi": 35.855289,
      "aei_text": 2.847468,
      "aei_vision": 0.064862,
      "text_ratio": 0.972867,
      "vision_ratio": 0.027133
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.972867,
      0.027133
    ],
    "text_vision_ratio": "0.972867:0.027133",
    "skip_reason": null
  }
}
```

#### Sample 8

```json
{
  "sample": 8,
  "token_counts": {
    "vision_tokens": 324.0,
    "text_tokens": 164.0,
    "total_tokens": 488.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 44.816153,
      "aei_text": 2.849976,
      "aei_vision": 0.063593,
      "text_ratio": 0.978174,
      "vision_ratio": 0.021826
    },
    "middle": {
      "mdi": 76.820779,
      "aei_text": 2.901004,
      "aei_vision": 0.037763,
      "text_ratio": 0.98715,
      "vision_ratio": 0.01285
    },
    "late": {
      "mdi": 58.924006,
      "aei_text": 2.87908,
      "aei_vision": 0.048861,
      "text_ratio": 0.983312,
      "vision_ratio": 0.016688
    },
    "all": {
      "mdi": 58.924006,
      "aei_text": 2.876688,
      "aei_vision": 0.050071,
      "text_ratio": 0.983312,
      "vision_ratio": 0.016688
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.983312,
      0.016688
    ],
    "text_vision_ratio": "0.983312:0.016688",
    "skip_reason": null
  }
}
```

#### Sample 9

```json
{
  "sample": 9,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.900999,
      "aei_text": 3.227755,
      "aei_vision": 0.064683,
      "text_ratio": 0.980354,
      "vision_ratio": 0.019646
    },
    "middle": {
      "mdi": 86.365144,
      "aei_text": 3.291056,
      "aei_vision": 0.038106,
      "text_ratio": 0.988554,
      "vision_ratio": 0.011446
    },
    "late": {
      "mdi": 70.238424,
      "aei_text": 3.2709,
      "aei_vision": 0.046569,
      "text_ratio": 0.985963,
      "vision_ratio": 0.014037
    },
    "all": {
      "mdi": 70.238424,
      "aei_text": 3.263239,
      "aei_vision": 0.049785,
      "text_ratio": 0.985963,
      "vision_ratio": 0.014037
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985963,
      0.014037
    ],
    "text_vision_ratio": "0.985963:0.014037",
    "skip_reason": null
  }
}
```

#### Sample 10

```json
{
  "sample": 10,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 165.0,
    "total_tokens": 558.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.018094,
      "aei_text": 3.225108,
      "aei_vision": 0.065794,
      "text_ratio": 0.980007,
      "vision_ratio": 0.019993
    },
    "middle": {
      "mdi": 84.397072,
      "aei_text": 3.288997,
      "aei_vision": 0.038971,
      "text_ratio": 0.98829,
      "vision_ratio": 0.01171
    },
    "late": {
      "mdi": 69.942503,
      "aei_text": 3.270447,
      "aei_vision": 0.046759,
      "text_ratio": 0.985904,
      "vision_ratio": 0.014096
    },
    "all": {
      "mdi": 69.942503,
      "aei_text": 3.261517,
      "aei_vision": 0.050508,
      "text_ratio": 0.985904,
      "vision_ratio": 0.014096
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.985904,
      0.014096
    ],
    "text_vision_ratio": "0.985904:0.014096",
    "skip_reason": null
  }
}
```

#### Sample 11

```json
{
  "sample": 11,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 158.0,
    "total_tokens": 689.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.567098,
      "aei_text": 3.69241,
      "aei_vision": 0.198868,
      "text_ratio": 0.948894,
      "vision_ratio": 0.051106
    },
    "middle": {
      "mdi": 14.80158,
      "aei_text": 3.553844,
      "aei_vision": 0.240099,
      "text_ratio": 0.936715,
      "vision_ratio": 0.063285
    },
    "late": {
      "mdi": 25.400242,
      "aei_text": 3.851199,
      "aei_vision": 0.151621,
      "text_ratio": 0.962122,
      "vision_ratio": 0.037878
    },
    "all": {
      "mdi": 25.400242,
      "aei_text": 3.699102,
      "aei_vision": 0.196877,
      "text_ratio": 0.962122,
      "vision_ratio": 0.037878
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.962122,
      0.037878
    ],
    "text_vision_ratio": "0.962122:0.037878",
    "skip_reason": null
  }
}
```

#### Sample 12

```json
{
  "sample": 12,
  "token_counts": {
    "vision_tokens": 531.0,
    "text_tokens": 158.0,
    "total_tokens": 689.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 18.692705,
      "aei_text": 3.696217,
      "aei_vision": 0.197736,
      "text_ratio": 0.94922,
      "vision_ratio": 0.05078
    },
    "middle": {
      "mdi": 13.609481,
      "aei_text": 3.497162,
      "aei_vision": 0.256965,
      "text_ratio": 0.931551,
      "vision_ratio": 0.068449
    },
    "late": {
      "mdi": 19.38982,
      "aei_text": 3.71658,
      "aei_vision": 0.191677,
      "text_ratio": 0.950956,
      "vision_ratio": 0.049044
    },
    "all": {
      "mdi": 19.38982,
      "aei_text": 3.636654,
      "aei_vision": 0.215459,
      "text_ratio": 0.950956,
      "vision_ratio": 0.049044
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.950956,
      0.049044
    ],
    "text_vision_ratio": "0.950956:0.049044",
    "skip_reason": null
  }
}
```

#### Sample 13

```json
{
  "sample": 13,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 60.499156,
      "aei_text": 3.394272,
      "aei_vision": 0.056104,
      "text_ratio": 0.98374,
      "vision_ratio": 0.01626
    },
    "middle": {
      "mdi": 65.690003,
      "aei_text": 3.405099,
      "aei_vision": 0.051836,
      "text_ratio": 0.985005,
      "vision_ratio": 0.014995
    },
    "late": {
      "mdi": 53.083659,
      "aei_text": 3.375298,
      "aei_vision": 0.063584,
      "text_ratio": 0.98151,
      "vision_ratio": 0.01849
    },
    "all": {
      "mdi": 53.083659,
      "aei_text": 3.391557,
      "aei_vision": 0.057174,
      "text_ratio": 0.98151,
      "vision_ratio": 0.01849
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.98151,
      0.01849
    ],
    "text_vision_ratio": "0.981510:0.018490",
    "skip_reason": null
  }
}
```

#### Sample 14

```json
{
  "sample": 14,
  "token_counts": {
    "vision_tokens": 416.0,
    "text_tokens": 164.0,
    "total_tokens": 580.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 63.129811,
      "aei_text": 3.399973,
      "aei_vision": 0.053857,
      "text_ratio": 0.984407,
      "vision_ratio": 0.015593
    },
    "middle": {
      "mdi": 52.010583,
      "aei_text": 3.372125,
      "aei_vision": 0.064835,
      "text_ratio": 0.981136,
      "vision_ratio": 0.018864
    },
    "late": {
      "mdi": 45.16067,
      "aei_text": 3.348506,
      "aei_vision": 0.074147,
      "text_ratio": 0.978337,
      "vision_ratio": 0.021663
    },
    "all": {
      "mdi": 45.16067,
      "aei_text": 3.373536,
      "aei_vision": 0.064279,
      "text_ratio": 0.978337,
      "vision_ratio": 0.021663
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.978337,
      0.021663
    ],
    "text_vision_ratio": "0.978337:0.021663",
    "skip_reason": null
  }
}
```

#### Sample 15

```json
{
  "sample": 15,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 51.100007,
      "aei_text": 3.218363,
      "aei_vision": 0.062982,
      "text_ratio": 0.980806,
      "vision_ratio": 0.019194
    },
    "middle": {
      "mdi": 42.989952,
      "aei_text": 3.191702,
      "aei_vision": 0.074243,
      "text_ratio": 0.977268,
      "vision_ratio": 0.022732
    },
    "late": {
      "mdi": 37.086466,
      "aei_text": 3.165402,
      "aei_vision": 0.085352,
      "text_ratio": 0.973744,
      "vision_ratio": 0.026256
    },
    "all": {
      "mdi": 37.086466,
      "aei_text": 3.191825,
      "aei_vision": 0.074191,
      "text_ratio": 0.973744,
      "vision_ratio": 0.026256
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.973744,
      0.026256
    ],
    "text_vision_ratio": "0.973744:0.026256",
    "skip_reason": null
  }
}
```

#### Sample 16

```json
{
  "sample": 16,
  "token_counts": {
    "vision_tokens": 393.0,
    "text_tokens": 166.0,
    "total_tokens": 559.0
  },
  "attention_metrics": {
    "early": {
      "mdi": 49.373905,
      "aei_text": 3.213388,
      "aei_vision": 0.065083,
      "text_ratio": 0.980148,
      "vision_ratio": 0.019852
    },
    "middle": {
      "mdi": 79.058692,
      "aei_text": 3.269561,
      "aei_vision": 0.041356,
      "text_ratio": 0.987509,
      "vision_ratio": 0.012491
    },
    "late": {
      "mdi": 46.910716,
      "aei_text": 3.205687,
      "aei_vision": 0.068336,
      "text_ratio": 0.979128,
      "vision_ratio": 0.020872
    },
    "all": {
      "mdi": 46.910716,
      "aei_text": 3.229539,
      "aei_vision": 0.058261,
      "text_ratio": 0.979128,
      "vision_ratio": 0.020872
    }
  },
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.979128,
      0.020872
    ],
    "text_vision_ratio": "0.979128:0.020872",
    "skip_reason": null
  }
}
```

