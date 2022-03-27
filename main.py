# Author:  Adge Denkers | https://github.com/adgedenkers
# Created: Sun Mar 27 2022
# Updated: 
# Version: 0.1
# File:    main.py
# -----------------------------------------------------------------------------

# imports
import datetime
import pandas as pd
import numpy as np
#import pyto_ui as ui

# main function
def main():

    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.read_csv("medications.csv")
    print(df)

if __name__ == "__main__":
    main()