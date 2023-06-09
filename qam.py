MOD_QPSK_NBITS  = 2
MOD_16QAM_NBITS = 4
MOD_64QAM_NBITS = 6
MOD_256QAM_NBITS = 8

NORM_QPSK = 1.0/1.414213562
NORM_16QAM  = 1.0/3.16227766
NORM_64QAM  = 1.0/6.4807407
NORM_256QAM = 1.0/13.038413

DENORM_QPSK = 1.414213562
DENORM_16QAM = 3.16227766
DENORM_64QAM = 6.4807407
DENORM_256QAM = 13.038413

qam_map = [
        [ # QPSK
          -1 * NORM_QPSK,  +1 * NORM_QPSK
        ],
        [ # 16QAM
          -3 * NORM_16QAM, -1 * NORM_16QAM, +3 * NORM_16QAM, +1 * NORM_16QAM
        ],                                                      
        [ # 64 QAM
          -7 * NORM_64QAM, -5 * NORM_64QAM, -1 * NORM_64QAM, -3 * NORM_64QAM,  +7 * NORM_64QAM, +5 * NORM_64QAM, +1 * NORM_64QAM, +3 * NORM_64QAM,
        ],                               
        [ # 256 QAM
          -15 * NORM_256QAM, -13 * NORM_256QAM, -9 * NORM_256QAM, -11 * NORM_256QAM, -1 * NORM_256QAM, -3 * NORM_256QAM, -7 * NORM_256QAM, -5 * NORM_256QAM,
          +15 * NORM_256QAM, +13 * NORM_256QAM, +9 * NORM_256QAM, +11 * NORM_256QAM, +1 * NORM_256QAM, +3 * NORM_256QAM, +7 * NORM_256QAM, +5 * NORM_256QAM
        ]
    ]