# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.countStudent: int = 0
    def calc(self) -> RatingType:

        for key in self.data:
            self.rating[key] = 0.0
            x=0
            for subject in self.data[key]:
                if subject[1]>=90:
                    x+=1
                self.rating[key] += subject[1]
            if x==len(self.data[key]):
                self.countStudent+=1
            self.rating[key] /= len(self.data[key])
        print(self)
        return self
