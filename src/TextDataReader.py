# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader


class TextDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        try:
            with open(path, encoding='utf-8') as file:
                for line in file:
                    if not line.startswith(" "):
                        self.key = line.strip()
                        self.students[self.key] = []
                    else:
                        subj, score = line.split(":", maxsplit=1)
                        self.students[self.key].append(
                            (subj.strip(), int(score.strip())))
            return self.students
        except FileNotFoundError:
            return {"Error":[("no such file of directory", 1)]}

class JsonDataReader(DataReader):

    def __init__(self):
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.endswith(": {"):
                        self.key = line.strip("\" : {")
                        self.students[self.key] = []
                    elif not line.startswith(('{','}')):
                        subj, score = line.split(":", maxsplit=1)
                        subj = subj.strip("\"")
                        score = score.strip(",")
                        self.students[self.key].append(
                            (subj.strip(), int(score.strip())))
            return self.students

        except FileNotFoundError:
            return {"Error": [("no such file of directory", 1)]}




