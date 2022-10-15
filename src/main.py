# -*- coding: utf-8 -*-
import argparse
import sys

from JsonDataReader import JsonDataReader
from CalcAcademicFailure import CalcAcadFail


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")

    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
#    reader = TextDataReader()
    reader = JsonDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcAcadFail(students).calc()
    print("Число студентов имеющих задолженность(ти): " + str(rating[0]))
    print(rating[1])
    print(rating[2])


if __name__ == "__main__":
    main()
