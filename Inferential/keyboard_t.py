import pandas as pa
import numpy as nu
from scipy import stats

df_keyb = pa.read_csv('Keyboard.csv', sep=';', decimal=',')

df_querty = df_keyb['QUERTY']
df_abc = df_keyb['ABC']

#point estimate
pe = nu.mean(df_querty)-nu.mean(df_abc)

#Difference
S = nu.std(df_querty-df_abc, ddof = 1) 
