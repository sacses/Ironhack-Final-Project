from package1.acquire import acquire
from package1.wrangle import wrangle
from package2.variables import *
from package1.analysis import analysis
from package1.load import complete_load
#import argparse

"""
def parse():
    parser = argparse.ArgumentParser(description='Create predictions over a given time horizon')
    parser.add_argument('threshold', type=float, help='Maximum MAPE threshold')

"""

def main():
    MM = acquire()
    dict_series_end_start = wrangle(MM)
    output_df = analysis(MM, dict_series_end_start, grid)
    complete_load(output_df)



if __name__ == "__main__":
    main()