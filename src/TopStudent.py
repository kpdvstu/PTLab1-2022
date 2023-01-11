# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class TopStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.nameStudent: str = ""
    def calc(self) -> RatingType:
        studentName = "Таких студентов нет"
        for key in self.data:
            x = 0
            for subject in self.data[key]:
                if subject[1] >= 90:
                    x += 1
                    
            if x == len(self.data[key]):
                studentName = key

        self.nameStudent = studentName
        return self.nameStudent
