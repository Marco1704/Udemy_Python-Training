import numpy as np
import pandas as pd

import webbrowser

website='https://en.wikipedia.org/wiki/List_of_all-time_NFL_win-loss_records'
#webbrowser.open(website)

nfl_frame = pd.read_clipboard()

print(nfl_frame.columns)

