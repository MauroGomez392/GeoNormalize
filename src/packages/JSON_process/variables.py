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
            'ranges': [(0, 20), (20, 50), (50, 80), (80, float('inf'))],
            'subscores': [1, 0.75, 0.25, 1],
            'score': [1]
        }
    },
    'CSU': {
        'RURAP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0, 0.25, 0.5, 1],
            'score': [0.75]
        },
        'RNATP': {
            'ranges': [(0, 25), (25, 50), (50, float('inf'))],
            'subscores': [0, 0.5, 1],
            'score': [1]
        },
        'SUBUP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0, 0.25, 0.5, 1],
            'score': [0.2]
        },
        'URBAP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0, 0.25, 0.5, 1],
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
            'ranges': [(0, 500), (500, 1000), (1000, 1250), (1250, float('inf'))],
            'subscores': [0, 0.5, 0.75, 1],
            'score': [1]
        },
        'SEGUV': {
            'ranges': [(0, 3500), (3500, 6500), (6500, 11500), (11500, float('inf'))],
            'subscores': [0, 0.5, 0.75, 1],
            'score': [0.5]
        },
        'TERCV': {
            'ranges': [(0, 6000), (6000, 10000), (10000, 20000), (20000, float('inf'))],
            'subscores': [0, 0.5, 0.75, 1],
            'score': [0.5]
        }
    },
    'CENTAPOYV': {
        'ranges': [(0, 2000), (2000, 3500), (3500, 6000), (6000, float('inf'))],
        'subscores': [0, 0.25, 0.5, 1],
        'score': [1]
    },
    'CENTINAUV': {
        'ranges': [(0, 500), (500, 1000), (1000, 1500), (1500, float('inf'))],
        'subscores': [0, 0.25, 0.5, 1],
        'score': [1]
    },
    'PARAOMNIV': {
        'ranges': [(0, 180), (180, 300), (300, 500), (500, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'AMBUSV': {
        'ranges': [(0, 2000), (2000, 3500), (3500, 5000), (5000, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'CED': {
        'ESJAV': {
            'ranges': [(0, 500), (500, 800), (800, 1200), (1200, float('inf'))],
            'subscores': [0, 0.25, 0.75, 1],
            'score': [1]
        },
        'LTECV': {
            'ranges': [(0, 900), (900, 1400), (1400, 2000), (2000, float('inf'))],
            'subscores': [0, 0.25, 0.75, 1],
            'score': [0.75]
        }
    },
    'ARIMPERMEP': {
        'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'ESPALIBRSV': {
        'ranges': [(0, 3000), (3000, 5000), (5000, 12500), (12500, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'COHEGEOGV': {
        'ranges': [(0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, float('inf'))],
        'subscores': [1, 0.5, 0.25, 0],
        'score': [1]
    },
    'CERCASENV': {
        'ranges': [(0, 10000), (10000, 40000), (40000, 100000), (100000, float('inf'))],
        'subscores': [0, 0.25, 0.5, 0.75, 1],
        'score': [1]
    },
    'TAMAASENV': {
        'ranges': [(0, 100), (100, 500), (500, 1000), (1000, 2500), (2500, float('inf'))],
        'subscores': [0, 0.25, 0.5, 0.75, 1],
        'score': [1]
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
    'RVI': {
        'CALLP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0],
            'score': [0]
        },
        'CAMIP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0],
            'score': [0]
        },
        'VIRTP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0, 0.25, 0.5, 1],
            'score': [1]
        },
        'PASAP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0, 0.25, 0.5, 1],
            'score': [1]
        },
        'SN9000V': {
            'ranges': [(0, 1), (1, 2), (2, float('inf'))],
            'subscores': [0, 0.25, 1],
            'score': [1]
        }
    },
    'AREASNAPV': {
        'ranges':[(0, 1), (1, 2), (2, float('inf'))],
        'subscores': [0, 0.75, 1],
        'score': [1]
    },
    'AREAPOTESV': {
        'ranges': [(0, 1), (1, float('inf'))],
        'subscores': [1, 0],
        'score': [1]
    },
    'LINECOSTV': {
        'ranges': [(0, 150), (150, float('inf'))],
        'subscores': [1, 0],
        'score': [1]
    },
    'FOCOINCESV': {
        'ranges': [(0, 200), (200, 500), (500, 2000), (2000, float('inf'))],
        'subscores': [1, 0.75, 0.5, 0],
        'score': [1]
    },
    'SDF': {
        'NOOPV': {
            'ranges': [(0, 800), (800, 4000), (4000, float('inf'))],
            'subscores': [1, 0.75, 0],
            'score': [0.75]
        },
        'OPERV': {
            'ranges': [(0, 800), (800, 4000), (4000, float('inf'))],
            'subscores': [1, 0.75, 0],
            'score': [1]
        }
    },
    'CVE': {
        'DOMV': {
            'ranges': [(0, 800), (800, 4000), (4000, float('inf'))],
            'subscores': [1, 0.75, 0],
            'score': [0.75]
        },
        'INDV': {
            'ranges': [(0, 800), (800, 4000), (4000, float('inf'))],
            'subscores': [1, 0.75, 0],
            'score': [1]
        },
        'NOAPV': {
            'ranges': [(0, 800), (800, 4000), (4000, float('inf'))],
            'subscores': [1, 0.75, 0],
            'score': [0.75]
        }
    },
    'LTE': {
        'TALTV': {
            'ranges': [(0, 30), (30, float('inf'))],
            'subscores': [1, 0],
            'score': [1]
        },
        'TMEDV': {
            'ranges': [(0, 15), (15, float('inf'))],
            'subscores': [1, 0],
            'score': [0.5]
        }
    },
    'DISTAGUAV': {
        'ranges': [(0, 20), (20, 200), (200, float('inf'))],
        'subscores': [0, 0.5, 1],
        'score': [1]
    },
    'SANEV': {
        'ranges': [(0, 20), (20, 200), (200, float('inf'))],
        'subscores': [0, 0.5, 1],
        'score': [1]
    },
    'COOPVIVV': {
        'ranges': [(0, 500), (500, 1000), (1000, 2500), (2500, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'PROYPMBV': {
        'ranges': [(0, 700), (700, 1500), (1500, 3500), (3500, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    },
    'CENTMECV': {
        'ranges': [(0, 1500), (1500, 2000), (2000, 3250), (3250, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
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
    'CONJHABISV': {
        'ranges': [(0, 200), (200, 500), (500, 1000), (1000, float('inf'))],
        'subscores': [0, 0.5, 0.75, 1],
        'score': [1]
    }
}