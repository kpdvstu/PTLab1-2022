# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from CustomXmlDataReader import CustomXmlDataReader

import numpy as np


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = CustomXmlDataReader()
    students = reader.read(path)

    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)


    arr = list()
    for x in rating:
        arr.append(rating[x])

    print(np.quantile(arr, q=np.arange(0.25, 1, 0.25)))


if __name__ == "__main__":
    main()
