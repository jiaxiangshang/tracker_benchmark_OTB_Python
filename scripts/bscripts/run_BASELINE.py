import time
from config import *

import sys
sys.path.append('../tracking_Lib')
sys.path.append('../tracking_Lib/tracker_template_sildeWin_HOG')
print(sys.path)
from tracker_template_sildeWin_HOG import *



def run_BASELINE(seq, rp, bSaveImage):
    x = seq.init_rect[0] - 1
    y = seq.init_rect[1] - 1
    w = seq.init_rect[2]
    h = seq.init_rect[3]

    tic = time.clock()
    res = tracker_template_sildeWin_HOG(seq.path, seq.startFrame, seq.endFrame, x, y, w, h)
    duration = time.clock() - tic

    result = dict()
    result['res'] = res
    result['type'] = 'rect'
    result['fps'] = round(seq.len / duration, 3)

    return result