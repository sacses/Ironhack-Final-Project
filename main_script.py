from package1.acquire import acquire
from package1.wrangle import wrangle
from package2.variables import *
from package1.analysis import analysis


def main():
    MM = acquire()
    dict_series_end_start = wrangle(MM)
    analysis(MM, dict_series_end_start, grid)


if __name__ == "__main__":
    main()