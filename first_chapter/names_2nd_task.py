import csv
import pandas as pd
import numpy as np

input_file_boys = open("boys.csv","rb")
input_file_girls = open("girls.csv","rb")

boys_fname = r'boys.csv'
girls_fname = r'girls.csv'

boys_data = pd.read_csv(boys_fname, sep=';', encoding='cp1251')
girls_data = pd.read_csv(girls_fname, sep=';', encoding='cp1251')

def getStatsForName(name, names_data):
    list_of_frequences = []
    for row in names_data.itertuples():
        if (name == row.Name):
            list_of_frequences.append(row.NumberOfPersons)
    list_of_frequences.sort()
    first_quartile = np.percentile(list_of_frequences, 25)
    second_quartile = np.percentile(list_of_frequences, 50)
    third_quartile = np.percentile(list_of_frequences, 75)
    iqr = third_quartile - first_quartile
    isOutlier = False
    for element in list_of_frequences:
        if (element < (first_quartile - 1.5 * iqr)):
            #print("Выброс перед первым квартилем - ", element)
            isOutlier = True
        if (element > (third_quartile + 1.5 * iqr)):
            #print("Выброс после третьего квартиля - ", element)
            isOutlier = True
    #print(list_of_frequences)
    #print(first_quartile, second_quartile, third_quartile)
    print(name, "Есть выбросы  - ", isOutlier)
# Виктория, Вадим, Ольга, Владислав, Полина, Алексей, Марианна 

getStatsForName('Виктория', girls_data)
getStatsForName('Вадим', boys_data)
getStatsForName('Ольга', girls_data)
getStatsForName('Владислав', boys_data)
getStatsForName('Полина', girls_data)
getStatsForName('Алексей', boys_data)
getStatsForName('Марианна', girls_data)