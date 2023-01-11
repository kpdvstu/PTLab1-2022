# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import yaml


class TextDataReaderYAML(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as stream:
            file = yaml.safe_load(stream)
            for string in file:
                for name in string:
                    self.key = name
                    self.students[self.key] = []
                    for subject in string[name]:
                        for points in subject:
                            self.students[self.key].append(
                                (points, int(subject[points])))
        return self.students
