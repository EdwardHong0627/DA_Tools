import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

housing = pd.read_csv('data/housing.csv')
report = ProfileReport(housing)
report.to_file(output_file="report.html")
