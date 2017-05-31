import pandas
import numpy

df = pandas.read_csv('Engagement.csv', sep=';', decimal=',')

#print numpy.mean(df['Engagement'])
print (8.3 - numpy.mean(df['Engagement'])) / (numpy.std(df['Engagement']) / 30**(.5))
