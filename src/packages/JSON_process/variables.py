variables = {
    'TPR': {
        'PRIVP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'SNDAP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'EPUBP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'OPUBP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [1]
        }
    },
    'CSU': {
        'RURAP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.8]
        },
        'RNATP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SUBUP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.5]
        },
        'URBAP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.1]
        }
    },
    'INSTAPROSV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
    },
    'UAS': {
        'PRIMV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0.25]
        },
        'SEGUV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0.50]
        },
        'TERCV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [1]
        }
    },
    'CENTAPOYV': {
            'ranges': [(0, 3000), (3000, 6000), (6000, 9000), (9000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
    },
    'CIN': {
        'CENTV': {
            'ranges': [(0, 800), (800, 1600), (1600, 4000), (4000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'ESPAV': {
            'ranges': [(0, 8000), (8000, 16000), (16000, 32000), (32000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'PROGV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SISTV': {
            'ranges': [(0, 8000), (8000, 16000), (16000, 32000), (32000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        }
    },
    'POM': {
        'URBAV': {
            'ranges': [(0, 250), (250, 1500), (1500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'SUBUV': {
            'ranges': [(0, 250), (250, 1500), (1500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75] 
        }
    },
    'BSA': {
        'BSAMV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.5]
        },
        'ACOMV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.8]
        },
        'AESPV': {
            'ranges': [(0, 4250), (4250, 9500), (9500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    },
    'CED': {
        'FEDUV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.25]
        },
        'PRIMV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SECV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.75]
        },
        'TECV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.5]
        }
    },
    'AREAPOBLSV': {
            'ranges': [(0, 250), (250, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'ESPALIBRSV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'COHEGEOGV': {
            'ranges': [(0, 0.2), (0.2, 0.5), (0.5, 0.7), (0.7, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [1]
    },
    'RVI': {
        'CALLP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.1]
        },
        'CAMIP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.5]
        },
        'VIRTP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'PASAP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.75]
        },
        'SN9000V': {
            'ranges': [(0, 0.5), (0.5, 1.5), (1.5, 2.5)],
            'subscores': [0, 0.25, 1],
            'score': [1]
        }
    },
    'CERCASENV': {
            'ranges': [(0, 50), (50, 150), (150, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 0.75, 1],
            'score': [1]
    },
    'AREAPROTSV': {
            'ranges':[(0, 1000), (1000, 5000), (5000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
    },
    'AREAPOTESV': {
            'ranges': [(0, 1000), (1000, 5000), (5000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
    },
    'LINECOSTV': {
            'ranges': [(0, 200), (200, float('inf'))],
            'subscores': [1, 0],
            'score': [1]
    },
    'FOCOINCESV': {
        'ranges': [(0, 1000), (1000, float('inf'))],
        'subscores': [1, 0],
        'score': [1]
    },
    'SDI': {
        'NOOPV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.5]
        },
        'OPERV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        }
    },
    'CVE': {
        'DOMV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.5]
        },
        'INDV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        },
        'NOAPV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.75]
        }
    },
    'LTE': {
        'TALTV': {
            'ranges': [(0, 300), (300, 500), (500, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        },
        'TMEDV': {
            'ranges': [(0, 300), (300, 500), (500, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.25]
        }
    },
    'DISTAGUAV': {
            'ranges': [(0, 20), (20, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
    },
    'SANEV': {
            'ranges': [(0, 20), (20, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
    },
    'DENSPOBLV':{
            'Montevideo':{
                'ranges': [(0, 50), (50, 100), (100, 200), (200, 300), (300, float('inf'))],
                'subscores': [3, 2, 1, 2, 3],
                'score': [1]
            },
            'ranges': [(0, 30), (30, 70), (70, 150), (150, 300), (300, float('inf'))],
            'subscores': [3, 2, 1, 2, 3],
            'score': [1]
    },
    'COOP': {
        'AGRV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'AHCV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'ARTV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'CONSV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'SOCV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'FRURV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'TRAV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.5]
        },
        'VIVV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    },
    'IMV': {
        'JUNTV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'AVANV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'MEVV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'ANVV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'PMBV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'ETMV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        }
    },
    'PROYPMBV': {
            'ranges': [(0, 500), (500, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'MEC': {
        'CENTV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, 10000), (10000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'CECAPV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'USCULV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, 10000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'PASV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'BIBLIV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        }
    },
    'CHA': {
        'AUTOV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'BHUV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'INTEV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'LPROV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'MVOTV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'MEVIV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    }
}

