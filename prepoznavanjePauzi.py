from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import subprocess, math as m
import re
import csv
import ntpath

def otkrijpauze(fileName, pathToWav, talkingHeadNumber, checkBoxMp4):
    #inputFile filea
    fileName = ntpath.basename(fileName)
    inputFile = fileName
    #inputFile = "/home/leo/Desktop/ZavrsniLinux/material/Rachel Dolezalobradenarucno.wav"
    nazivOriginalnogFilea = re.split("\.(.*)", fileName)[0]
    extenzijaOriginalnogFilea = re.split("\.(.*)", fileName)[1]
    fileNameWithoutExtension = re.split("\.(.*)", fileName)[0]
    

    #citanje i analiza file-a
    #pathToWav = 'joe.wav'
    [Fs, x] = aIO.read_audio_file(pathToWav)
    #print('tu sam')
    #print(Fs)
    #print(x)
    segments = aS.silence_removal(x, Fs, 0.02, 0.002, weight = 0.2, smooth_window = 1, plot = False)
    #print('tu sam2')
    #return 1
    #print(segments)
    #segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, plot = True)

    #ffmpeg konverzija
    #print('length of segments: ')
    #print(len(segments))

    ##PRIVREMENO SAMO ZA RACHEL TESTIRANJE
    
    #inputFile = "LeoFavouriteColorSimple2.wav"
    
    brojKlipa = 0
    segmentsZaPisanje = []
    
    for i in segments:
        print('segment broj;{0} pocinje'.format(brojKlipa))
        trajanje = i[1]-i[0]
        if trajanje > 1:
            
            #napraviti novu listu segmenata samo sa segmentima koji odgovaraju
            segmentsZaPisanje.append(i)
            

            imeNovogKlipaSaLokacijom='material\\'+fileNameWithoutExtension+"\\interviewee{numHead}-clip{numClip}.wav".format(numHead=talkingHeadNumber, numClip=brojKlipa)
            imeNovogVideoKlipaSaLokacijom='material\\'+fileNameWithoutExtension+"\\interviewee{numHead}-clip{numClip}.mp4".format(numHead=talkingHeadNumber, numClip=brojKlipa)
            print('tu')
            subprocess.call(["ffmpeg", "-i", pathToWav, "-ss", "{0}".format(m.ceil(i[0])), "-t", "{0}".format(trajanje) ,imeNovogKlipaSaLokacijom])
            #izrada video klipa
            if checkBoxMp4:
                subprocess.call(["ffmpeg", "-i", fileName, "-ss", "{0}".format(m.ceil(i[0])), "-t", "{0}".format(trajanje),imeNovogVideoKlipaSaLokacijom])
            segmentsZaPisanje[brojKlipa].insert(0,"{file}".format(file = fileName))
            segmentsZaPisanje[brojKlipa].insert(1,"interviewee{numHead}-clip{numClip}.wav".format(numHead=talkingHeadNumber, numClip=brojKlipa))
            segmentsZaPisanje[brojKlipa].insert(2,imeNovogKlipaSaLokacijom)
            segmentsZaPisanje[brojKlipa].insert(6,trajanje)
            brojKlipa += 1
            print('segment broj; zavrsava')
    with open('project.csv', 'a', newline='') as fileZaPisanje:
        writer = csv.writer(fileZaPisanje)
        writer.writerows(segmentsZaPisanje)

    print('gotov sa prepoznavanjem pauzi i splittanjem filea')

#otkrijpauze('asa.das', 1, 1)