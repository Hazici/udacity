import numpy as nu
from scipy import stats

lista = [5, 19, 11, 23, 12, 7, 3, 21]

t_stat = stats.ttest_1samp(lista, 10)

print t_stat