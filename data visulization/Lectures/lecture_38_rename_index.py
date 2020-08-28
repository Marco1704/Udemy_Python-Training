import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe= DataFrame(np.arange(12).reshape((3, 4)),
                 index=['NY', 'LA', 'SF'],
                 columns=['A', 'B', 'C', 'D'])


print(dframe)
# Just like a Series, axis indexes can also use map

#Let's use map to lowercase the city initials

dframe.index.map(str.lower)

dframe.index = dframe.index.map(str.lower)

print(dframe)

dframe1 = dframe.rename(index=str.title, columns=str.lower)

print(dframe1)