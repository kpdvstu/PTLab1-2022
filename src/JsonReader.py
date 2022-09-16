# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json

class JsonReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                self.key = i
                self.students[self.key] = []
                for x in data[i]:
                    self.students[self.key].append((x,int(data[i][x])))

        return self.students








        '''with open(path, encoding='utf-8') as file:
            for line in file:
                if not line.startswith(" "):
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    subj, score = line.split(":", maxsplit=1)
                    self.students[self.key].append(
                        (subj.strip(), int(score.strip())))
        return self.students'''
