# Author:  Adge Denkers | https://github.com/adgedenkers
# Created: Sun Mar 27 2022
# Updated: 
# Version: 0.1
# File:    main.py
# -----------------------------------------------------------------------------

# imports
from loguru import logger       # enterprise-grade logging
import pendulum as dt           # drop-in replacement for datetime
import pandas as pd             # data ETL
import numpy as np              # number functions
#import pyto_ui as ui

# main function
def main():

    now = dt.now("America/New York")
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.read_csv("medications.csv")
    print(df)

if __name__ == "__main__":
    main()