import time
from config import *

import sys
sys.path.append(os.path.abspath('../tracking_Staple_cvpr16/tracker_cf_Staple'))
print(sys.path)
from tracker_cf_Staple import *

def run_STAPLE(seq, rp, bSaveImage):
    tic = time.clock()
    res = run_Staple(seq, rp, bSaveImage)
    duration = time.clock() - tic
    return res