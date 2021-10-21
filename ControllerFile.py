#master file
#ova datoteka poziva sve funkcije i kontrolira izvodenje cijelog programa
#author: Leo Vitasovic, Croatia 2020.
import time
start_time = time.time()

import os
import shutil
import ntpath
import csv
import re
import pandas as pd
from konverzija import konvertiranjeUWav
from pathlib import Path
from prepoznavanjePauzi import otkrijpauze
from prepoznavanjeTeksta import transkriptiranjeKlipa
from micanjePrazneTranskripcije import makniRedovePrazneTranskripcije
from topicModelling import getTopics
from topicsSorter import sortTopics
from export import *
from nltk import *

def programStart(selectedInputFiles, exportLocation, checkBoxMp4, checkBoxXml, finalnoIme):
    #saznati koji je root folder
    path = os.getcwd()
    pathToMaterial = path+'\\material\\'
    
    #odabir fileova
    #
    #files = ["LeoFavouriteColorSimple2.wav", "Katarina-FavouriteColorSimple2.wav"]
    files = ['MVI_2394.MP4','MVI_2395.MP4','MVI_2396.MP4','MVI_2397.MP4']
    #files = ['Katarina-FavouriteColorSimple.mp4','Leo-FavouriteColorSimple.mp4']
    files = selectedInputFiles
    # "PiotrSound.wav","womanSound.wav"
    #namjestanje jezika
    language = "en"


    #pocetno otvaranje csv filea
    with open('project.csv', 'w') as fileZaPisanje:
        fileZaPisanje.write("OriginalFileName,Ime klipa,Lokacija,In point,Out point,Trajanje\n")
    #varijabla za prebrojavanje sugovornika
    talkingHeadNumber = 1
        
    ### ZA SVAKI ODABRANI FILE START: ###
    for file in files:

    #kopirati odabrane fileove u root folder
        print('file: '+file)
        imeFilea = ntpath.basename(file)
        imeFileaBezEkstenzije = re.split("\.(.*)", ntpath.basename(imeFilea))[0]
        print('imeFilea: '+imeFilea)
        print('path to material: '+pathToMaterial)
        print('path+imeFilea:' +path+'\\'+imeFilea)
        #pathToFile = pathToMaterial+imeFilea
        shutil.copyfile(file, path+'\\'+imeFilea)
    
    #napraviti folder s nazivom fileova koje analiziramo
        pathToFile = pathToMaterial+imeFileaBezEkstenzije+'\\'
        if os.path.exists(pathToFile):
            shutil.rmtree(pathToFile)
        if not os.path.exists('material'):
            os.mkdir('material')
        os.mkdir(pathToFile)
        
    #convertiranje u wav
        zaWav = path+'\\'+imeFilea
        pathToWav = konvertiranjeUWav(zaWav, imeFileaBezEkstenzije)
        
    #prepoznavanje pauzi, vracanje popisa dijelova filea u kojem ima govora, splitanje filea prema pauzama, stvaranje novih kratkih klipova samo sa zvukom
        otkrijpauze(file, pathToWav, talkingHeadNumber, checkBoxMp4)
        talkingHeadNumber += 1
        
    ### ZA SVAKI ODABRANI FILE END ###

    # speech to text analiza svih klipova, nadopisivanje njihovog sadrzaja (izgovorenih rijeci, imena originalnog filea,
    # ime pojedinacnih klipova, vrijeme pocetka klipa u originalnom fileu i trajanje) u 'project.csv' file

    #ZA SVAKI UNOS U project.csv START

    with open('project.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        listaTranskripcija = []
        for row in reader:
            print(f'row:{row}')
            jedanRed = list(row)
            lokacijaKlipa = jedanRed[2]
            transkripcijaKlipa = transkriptiranjeKlipa(lokacijaKlipa)
            print (f'transkripcija jednog Klipa:{transkripcijaKlipa}')
            listaTranskripcija.append(transkripcijaKlipa)
            print(listaTranskripcija)
    
    #konkatenacija novonapravljene kolumne
    lst = pd.read_csv("project.csv")
    df=lst
    df2 = pd.DataFrame(listaTranskripcija)
    df.insert(5,"Transkripcija",df2)        
    df.to_csv('project.csv', index=False)        

        
    #ZA SVAKI UNOS U project.csv END

    #maknuti redove sa praznom transkripcijom
    makniRedovePrazneTranskripcije()

    #slanje csv file-a na topic modelling, dodavanje teme u novi stupac za svaki klip svakog filea
    getTopics()

    #sortiranje tema
    sortTopics()

    #eksport videa
    if checkBoxMp4:
        print('detektirao sam check za eksportiranje videa')
        exportVidea(files, finalnoIme)

    #stvaranje .xml filea
    if checkBoxXml:
        exportXML(finalnoIme)

    print("--- %s seconds ---" % (time.time() - start_time))