"""Fill missing values"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from trd_utils import *

def test_run():
    """Function called by Test Run."""
    # Read data
    symbol_list = ["JAVA", "FAKE1", "FAKE2"]  # list of symbols
    start_date = "2005-12-31"
    end_date = "2014-12-07"
    dates = pd.date_range(start_date, end_date)  # date range as index
    df_data = get_data(symbol_list, dates)  # get data for each symbol

    # Fill missing values
    fill_missing_values(df_data)

    # Plot
    plot_data(df_data)


if __name__ == "__main__":
    test_run()
