import pandas as pa
import numpy as nu
from scipy import stats 

df_csuri = pa.read_csv('Finch.csv', sep=';', decimal=',')

df_beak = df_csuri['Beak_width']

atlag = nu.mean(df_beak)

stdev = nu.std (df_beak, ddof = 1)

t_stat = stats.ttest_1samp(df_beak, 6.07)

print atlag
print stdev
print t_stat
