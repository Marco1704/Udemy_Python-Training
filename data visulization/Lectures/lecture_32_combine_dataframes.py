import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''ser1 = Series ( [2, np.nan, 4, np.nan, 6, np.nan],
                index=['Q', 'R', 'S', 'T', 'U', 'V'] )

print ( ser1 )

ser2 = Series ( np.arange ( len ( ser1 ) ), dtype=np.float64,
                index=['Q', 'R', 'S', 'T', 'U', 'V'] )

print ( ser2 )

ser3=Series( np.where( pd.isnull ( ser1 ), ser2, ser1), index=ser1.index)

print(ser3)

ser4 = ser1.combine_first(ser2)

print(ser4)

nan = np.nan

dframe_odds = DataFrame({'X':[1.,nan,3.,nan],
                         'Y':[nan,5.,nan,7.],
                         'Z':[nan,9.,nan,11]})

dframe_evens = DataFrame({'X':[2.,4.,nan,6.,8.],
                          'Y':[nan,10., 12.,14.,16.]})

print(dframe_odds)
print(dframe_evens)

dframe_comb = dframe_odds.combine_first(dframe_evens)

print(dframe_comb)'''
#########################################################

dframe1 = DataFrame(np.arange(8).reshape(2,4), index=pd.Index(['LA','SF'], name='city'),
                    columns=pd.Index(['A','B','C','D'],name='letter'))

print(dframe1)

dframe_st = dframe1.stack()

print(dframe_st)#stack a datafrema by using .stack method. To redo the dataframe use the .unstack method




