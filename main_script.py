from package1.acquire import acquire
from package1.wrangle import wrangle
from package2.variables import *
from package1.analysis import analysis
from package1.load import complete_load
from dotenv import load_dotenv
import argparse
import os


def parse():
    parser = argparse.ArgumentParser(description='Input the desired variables for your forecast')

    parser.add_argument('-t', '--threshold', type=float, metavar='',
                        default=os.environ.get('MAPE_THRESHOLD'),
                        help='Maximum MAPE threshold')
    parser.add_argument('-u', '--units', type=str, metavar='',
                        default=os.environ.get('INPUT_FREQ'),
                        help='Time units such as M, W or D')
    parser.add_argument('-c', '--x_cutoff', type=int, metavar='',
                        default=os.environ.get('X_CUTOFF'),
                        help='How often is the forecast x-validated')
    parser.add_argument('-f', '--x_forecast', type=int, metavar='',
                        default=os.environ.get('X_FCST'),
                        help='Horizon of the forecast in x-validation')
    parser.add_argument('-H', '--horizon', type=int, metavar='',
                        default=os.environ.get('HORIZON'),
                        help='Horizon of the forecast')
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse()
    MM = acquire()
    dict_series_end_start = wrangle(MM)
    output_df = analysis(MM, dict_series_end_start, grid, args)
    complete_load(output_df)



if __name__ == "__main__":
    main()