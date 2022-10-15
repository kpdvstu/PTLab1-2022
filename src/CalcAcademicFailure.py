# -*- coding: utf-8 -*-

from Types import DataType

RatingType = list[int, str, dict[str, int]]


class CalcAcadFail:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = [0, "Все студенты сдали сессию !", {}]

    def calc(self) -> RatingType:

        for key in self.data:
            self.rating[2][key] = 0
            for rat in self.data[key]:
                if rat[1] < 61:
                    self.rating[1] = "Число задолженностей у студентов:"
                    self.rating[2][key] += 1
            if self.rating[2][key] != 0:
                self.rating[0] += 1
            else:
                del self.rating[2][key]

        return self.rating
