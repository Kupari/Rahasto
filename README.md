import re
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def importdata():
    """Tuo datan käytettäväksi"""
    if re.findall('xlsx$', datalink):   #varmistaa että linkki on xlsx muodossa.
        df = pd.read_excel(datalink)
    else:
        return 'Syötä tiedosto linkki xlsx-muodossa: '
    return df    

def rivi1():
    return input('Syötä ensimmäinen rivi: ')


def rivi2():
    return input('Syötä toinen rivi: ')


def colcross():
    """Printtaa tiedot kahdelta pystyriviltä"""
    ct = data[rivi1()] +'   '+ data[rivi2()]
    return ct

def colinfo():
    """Näyttää kaikki pystyrivien otsikot"""
    return [col for col in data.columns]

def find_stats_isin():
    """Pyytää käyttäjältä tilinumeron ja palauttaa sitä vastaavan yrityksen taloustiedot"""
    
    var = input('Kirjoita rahaston isin: ')
    if re.findall('^[A-Za-z][A-Za-z][0-9]{10}',var):    #Varmistaa että ISIN on oikeassa muodossa
        return dataisin.loc[var]
    else:
        return print('isin väärässä muodossa.')

def top10():
    def valinta():
        x = input('Voit valita suodatuksen rahaston tai yrityksen mukaan\n(1)Rahasto\n(2)Yritys\n')
        if x == '1': return 'fund_name_fi'
        if x == '2': return 'company'
    y = input('Syötä kategoria jonka mukaan haluat top 10: ')
    datatop10 = data[[valinta(),y]].sort_values(by=y,ascending=False).head(10)
    return datatop10

def plottop10():
    return top10()[''].plt

if __name__ == '__main__':
    datalink = str(input('Lisää linkki tähän (beta)'))
    dataisin = pd.read_excel(datalink,index_col='isin')
    data = importdata()
    print(colinfo())
    print(plottop10())
    #print(find_stats_isin())
    #print(colcross())
    #http://taanila.fi/Rahastoraporttidata_201907.xlsx
    #FI0008800016
