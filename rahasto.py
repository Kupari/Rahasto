import re
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def importdata():
    """Tuo datan käytettäväksi"""
    #datalink = input('Syötä linkki tähän')
    
    if re.findall('xlsx$', datalink):   #varmistaa että linkki on xlsx muodossa.
        df = pd.read_excel(datalink)
    else:
        return 'Syötä tiedosto linkki xlsx-muodossa: '
    return df

def rivi1():
    return input('Syötä ensimmäinen rivi: ')


def rivi2():
    return input('Syötä toinen rivi: ')


class Rahasto:

    def __init__(self):
        self.data = importdata()
        self.dataisin = pd.read_excel(datalink,index_col='isin')
    

    def colcross(self):
        """Antaa tiedot kahdelta pystyriviltä"""
        cc = data[[rivi1(),rivi2()]]
        return cc


    def colinfo(self):
        """Näyttää kaikki pystyrivien otsikot"""
        print([col for col in data.columns])
        return [col for col in data.columns]


    def find_stats_isin(self,isin=None):
        """Pyytää käyttäjältä tilinumeron ja palauttaa sitä vastaavan yrityksen taloustiedot"""
        if isin: var = isin
        else: var = input('Kirjoita rahaston isin: ')
        if re.findall('^[A-Za-z][A-Za-z][0-9]{10}',var):    #Varmistaa että ISIN on oikeassa muodossa
            return dataisin.loc[var]
        else:
            return print('isin väärässä muodossa.')


    def top10(self,*args,plot=None):
        """Funktiolle voi ilmoittaa 2 parametria joista haluaa top10 tai antaa Terminaalin hoitaa "kysely" """
        def choice():
                x = input('Voit valita suodatuksen rahaston tai yrityksen mukaan\n(1)Rahasto\n(2)Yritys\nTai syötä oma suodatin: ')
                if x == '1': return 'fund_name_fi'
                elif x == '2': return 'company'
                elif x in self.colinfo(): return x
                else: 
                    raise ValueError('Syötä oikea suodatin')
                    choice()

        if len(args) != 2:
            y = input('Syötä kategoria jonka mukaan haluat top 10: ')
            ch = choice()
            datatop10 = data[[ch,y]].sort_values(by=y,ascending=False).head(10)
            #datatop10.index = ['|' for x in range(len(datatop10))]
            datatop10.set_index(data[ch])
            print(datatop10)

            if plot:
                tplot = datatop10
                names = [x for x in tplot[ch]]
                plt.bar(names,tplot[y])
                plt.ylabel(y)
                plt.xticks(rotation='vertical')
                plt.subplots_adjust(bottom=0.5)
                plt.show()

            return datatop10
        else: 
              #Program jumps here if arguments were given, sorting by the later value
            print(data[[args[1],args[0]]].sort_values(by=args[0],ascending=False).head(10))
            
            if plot:
                tplot = data[[args[1],args[0]]].sort_values(by=args[0],ascending=False).head(10)
                names = [x for x in tplot[args[1]]]
                plt.bar(names,tplot[args[0]])
                plt.ylabel(args[0])
                plt.xticks(rotation='vertical')
                plt.subplots_adjust(bottom=0.5)
                plt.show()
            return data[[args[1],args[0]]].sort_values(by=args[0],ascending=False).head(10)

        
                    
            

if __name__ == '__main__':
    datalink = str('http://taanila.fi/Rahastoraporttidata_201907.xlsx')
    a = Rahasto()
    data = a.data
    a.colinfo()
    a.top10()
    

'''
datalink = str('http://taanila.fi/Rahastoraporttidata_201907.xlsx') #str(input('Lisää linkki tähän (beta)'))
dataisin = pd.read_excel(datalink,index_col='isin')
data = importdata()
'''



