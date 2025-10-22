# Attention Diagnostics Log

This file contains MDI attention diagnostics from GRPO training.


## === Rollout Step 1 ===
Step: 0/29790 | 2025-10-22 12:02:52

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
Step: 1/29790 | 2025-10-22 12:02:56

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.472 | 9.683 | 6.696 | 6.696 |
| MDI Std | 4.967 | 1.514 | 0.577 | 0.577 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.859531,
      0.140469
    ],
    "text_vision_ratio": "0.859531:0.140469"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.879117,
      0.120883
    ],
    "text_vision_ratio": "0.879117:0.120883"
  }
}
```


## === Rollout Step 3 ===
Step: 2/29790 | 2025-10-22 12:03:00

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 24.276 | 21.927 | 11.834 | 11.834 |
| MDI Std | 16.029 | 13.038 | 3.686 | 3.686 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.890691,
      0.109309
    ],
    "text_vision_ratio": "0.890691:0.109309"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.939468,
      0.060532
    ],
    "text_vision_ratio": "0.939468:0.060532"
  }
}
```


## === Rollout Step 4 ===
Step: 3/29790 | 2025-10-22 12:03:03

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.313 | 9.285 | 8.826 | 8.826 |
| MDI Std | 5.832 | 4.221 | 0.807 | 0.807 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.889129,
      0.110871
    ],
    "text_vision_ratio": "0.889129:0.110871"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.905955,
      0.094045
    ],
    "text_vision_ratio": "0.905955:0.094045"
  }
}
```


## === Rollout Step 5 ===
Step: 4/29790 | 2025-10-22 12:03:06

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 25.424 | 23.805 | 14.910 | 14.910 |
| MDI Std | 7.512 | 13.845 | 0.032 | 0.032 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.93727,
      0.06273
    ],
    "text_vision_ratio": "0.937270:0.062730"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.937021,
      0.062979
    ],
    "text_vision_ratio": "0.937021:0.062979"
  }
}
```


## === Rollout Step 6 ===
Step: 5/29790 | 2025-10-22 12:03:09

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 16.428 | 8.704 | 10.585 | 10.585 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.913681,
      0.086319
    ],
    "text_vision_ratio": "0.913681:0.086319"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.913681,
      0.086319
    ],
    "text_vision_ratio": "0.913681:0.086319"
  }
}
```


## === Rollout Step 7 ===
Step: 6/29790 | 2025-10-22 12:03:12

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 12.726 | 9.492 | 8.986 | 8.986 |
| MDI Std | 4.599 | 1.307 | 3.058 | 3.058 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.855655,
      0.144345
    ],
    "text_vision_ratio": "0.855655:0.144345"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.923335,
      0.076665
    ],
    "text_vision_ratio": "0.923335:0.076665"
  }
}
```


## === Rollout Step 8 ===
Step: 7/29790 | 2025-10-22 12:03:16

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 14.888 | 11.742 | 15.767 | 15.767 |
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940359,
      0.059641
    ],
    "text_vision_ratio": "0.940359:0.059641"
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
  "overall": {
    "balance_score": 0.0,
    "attention_distribution": [
      0.940359,
      0.059641
    ],
    "text_vision_ratio": "0.940359:0.059641"
  }
}
```


## === Rollout Step 9 ===
Step: 8/29790 | 2025-10-22 12:03:19

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


## === Rollout Step 10 ===
Step: 9/29790 | 2025-10-22 12:03:22

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


## === Rollout Step 11 ===
Step: 10/29790 | 2025-10-22 12:03:25

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


## === Rollout Step 12 ===
Step: 11/29790 | 2025-10-22 12:03:29

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
Step: 12/29790 | 2025-10-22 12:03:32

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
Step: 13/29790 | 2025-10-22 12:03:35

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
Step: 14/29790 | 2025-10-22 12:03:37

### Enhanced MDI Attention Diagnostics

#### Overall Statistics

| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 1.000 | 1.000 | 1.000 | 1.000 |
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
    "vision_tokens": 324,
    "text_tokens": 0,
    "total_tokens": 324
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


## === Rollout Step 16 ===
Step: 15/29790 | 2025-10-22 12:03:40

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


## === Rollout Step 17 ===
Step: 16/29790 | 2025-10-22 12:03:43

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
Step: 17/29790 | 2025-10-22 12:03:47

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
Step: 18/29790 | 2025-10-22 12:03:50

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
Step: 19/29790 | 2025-10-22 12:03:52

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


## === Rollout Step 21 ===
Step: 20/29790 | 2025-10-22 12:03:55

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
Step: 21/29790 | 2025-10-22 12:03:58

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


## === Rollout Step 23 ===
Step: 22/29790 | 2025-10-22 12:04:01

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


## === Rollout Step 24 ===
Step: 23/29790 | 2025-10-22 12:04:05

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
Step: 24/29790 | 2025-10-22 12:04:08

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
Step: 25/29790 | 2025-10-22 12:04:11

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


## === Rollout Step 27 ===
Step: 26/29790 | 2025-10-22 12:04:14

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
Step: 27/29790 | 2025-10-22 12:04:17

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
Step: 28/29790 | 2025-10-22 12:04:21

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
Step: 29/29790 | 2025-10-22 12:04:24

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
Step: 30/29790 | 2025-10-22 12:04:27

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


## === Rollout Step 32 ===
Step: 31/29790 | 2025-10-22 12:04:31

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
Step: 32/29790 | 2025-10-22 12:04:34

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
Step: 33/29790 | 2025-10-22 12:04:37

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
Step: 34/29790 | 2025-10-22 12:04:40

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
Step: 35/29790 | 2025-10-22 12:04:43

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
Step: 36/29790 | 2025-10-22 12:04:46

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
Step: 37/29790 | 2025-10-22 12:04:50

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


## === Rollout Step 39 ===
Step: 38/29790 | 2025-10-22 12:04:53

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
Step: 39/29790 | 2025-10-22 12:04:56

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
Step: 40/29790 | 2025-10-22 12:04:59

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
Step: 41/29790 | 2025-10-22 12:05:02

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


## === Rollout Step 43 ===
Step: 42/29790 | 2025-10-22 12:05:05

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
Step: 43/29790 | 2025-10-22 12:05:08

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

