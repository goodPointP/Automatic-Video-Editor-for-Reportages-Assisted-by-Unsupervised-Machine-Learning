import subprocess, math as m
import ntpath
import re

def konvertiranjeUWav(file, imeFileaBezEkstenzije):
    #procesiranje inputFilea
    print('file, kad ude u wav funkciju: '+file)
    print('imefileabezekstenzije, kad ude u wav funkciju: '+imeFileaBezEkstenzije)
    #print(re.split("\.(.*)", file)[1])
    if re.split("\.(.*)", file[1]) != ".wav":
        imeFileaBezExtenzije = re.split("\.(.*)", file)[0]
        outputFolderLocation = 'material\\'+imeFileaBezEkstenzije+'\\'+imeFileaBezEkstenzije+'.wav'
        #print(type(imeFileaBezExtenzije))
        print('outputFolderLocation: ' +outputFolderLocation)
        print('file prije subprocess calla: '+file)
        subprocess.call(["ffmpeg", "-i", file, outputFolderLocation])
        pathToConvertedFile = outputFolderLocation
        print('pathToConvertedFile: '+pathToConvertedFile)
        #print("trebao sam procesirati i sada izgleda ovako: "+file)
    else:
        pathToConvertedFile = file
        #print("nisam morao procesirati i sada izgleda ovako: "+file)
    print('uspjesno convertirao u wav')
    return pathToConvertedFile
