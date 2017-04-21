from collections import OrderedDict
from config import *

# from math import log10, floor
#
# def round_sig( x, sig=2):
#     return round(x, sig-int(floor(log10(abs(x))))-1)
#
# def convert(x, ROUND=0):
#
#     conv = []
#
#     for _ in range(x.size[0]):
#         lst = x._data[_::x.size[0]].tolist()
#
#         if ROUND is not 0:
#             lst = [round_sig(elem, ROUND) if elem != 0 and
#                    elem == elem else elem for elem in lst]
#
#         conv.append(lst)
#
#     return conv

class Result:
    # tracker : trakcer name
    # seqName : Sequence name
    # startFrame : start frame number
    # endFrame : end frame number
    # res : results 
    # resType : result type
    # fps

    def __init__(self, tracker, seqName, startFrame, endFrame, 
        resType, evalType, res, fps, shiftType=None, tmplsize=None):
        self.tracker = tracker
        self.seqName = seqName
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.resType = resType
        self.evalType = evalType
        self.res = res
        self.fps = fps
        self.shiftType = shiftType
        self.tmplsize = tmplsize
        
        self.__dict__ =     OrderedDict([
        ('tracker', self.tracker),
        ('seqName', self.seqName),
        ('startFrame', self.startFrame),
        ('endFrame', self.endFrame),
        ('evalType', self.evalType),
        ('fps', self.fps),
        ('shiftType', self.shiftType),
        ('resType', self.resType),
        ('tmplsize', self.tmplsize),
        ('res', self.res)])

    def refresh_dict(self):
        self.__dict__ = OrderedDict([
            ('tracker', self.tracker),
            ('seqName', self.seqName),
            ('startFrame', self.startFrame),
            ('endFrame', self.endFrame),
            ('evalType', self.evalType),
            ('fps', self.fps),
            ('shiftType', self.shiftType),
            ('resType', self.resType),
            ('tmplsize', self.tmplsize),
            ('res', self.res)])
        
        
