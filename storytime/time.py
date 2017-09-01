

"""
description
"""


#----------------------------------------------------------------------#

class GameTime:
    def __init__(self, start=0, end=None):
        self._count=start
        self._end=end

    @property
    def count(self):
        return self._count

    def __iter__(self):
        return self

    def __next__(self):
        if self._count > self._end:
            raise StopIteration
        self._count+=1
        return self.count




#----------------------------------------------------------------------#
