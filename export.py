import pandas as pd
from XMLHelperFunctions import *

def exportVidea(files, finalnoIme):
    import csv, subprocess, re
    #citanje project.csv filea
    with open('project.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data.pop(0)
        #print(data)
        #otvaranje filea za pisanje
        filePisanje = open('listaZaExportVidea.txt', 'w+')
        ispis = []
        for line in data:
            imeKlipa = line[3]
            imeKlipa = re.split("\.(.*)", imeKlipa)[0]
            imeKlipa += '.mp4'
            #print(imeKlipa)
            ispis.append("file '"+imeKlipa+"'\n")
        print(ispis)
        filePisanje.writelines(ispis)
        #zatvaranje filea s popisom klipova za montazu
        filePisanje.close()

    subprocess.call('ffmpeg -f concat -safe 0 -i listaZaExportVidea.txt -c copy "{ime}".mp4'.format(ime=finalnoIme), shell=True)
    print('exportirao sam video')
    

def exportXML(finalnoIme = 'montiraniVideo'):
    #dohvacanje podataka iz project.csv
    data = pd.read_csv('project.csv', index_col=False)
    allLines = data.values.tolist()

    clipsXMLDataVideo = ''
    clipsXMLDataAudioTrackOne = '<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerName="Balance" currentExplodedTrackIndex="0" totalExplodedTrackCount="2" premiereTrackType="Stereo">'
    clipsXMLDataAudioTrackTwo = '<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerName="Balance" currentExplodedTrackIndex="1" totalExplodedTrackCount="2" premiereTrackType="Stereo">'
    
    clipItemId = 1
    #za svaki klip START
    for line in allLines:
    
        filename = line[1]
        filepath = line[3]
        clipIN = line[4]
        clipOUT = line[5]

        #video track
        clipsXMLDataVideo += getSingleVideoClipXML(clipItemId, filename, filepath, clipIN, clipOUT)
        clipItemId += 1

        #audio track 1
        trackMarker = 1
        clipsXMLDataAudioTrackOne += getSingleAudioTrackXML(clipItemId, filename, filepath, clipIN, clipOUT, trackMarker)
        clipItemId += 1

        #audio track 2
        trackMarker = 2
        clipsXMLDataAudioTrackTwo += getSingleAudioTrackXML(clipItemId, filename, filepath, clipIN, clipOUT, trackMarker)
        clipItemId += 1
        
    #za svaki klip END

    #spajanje dvije audio tracke
    clipsXMLDataAudioTrackOne += '</track>'
    clipsXMLDataAudioTrackTwo += '</track>'
    clipsXMLDataAudio = clipsXMLDataAudioTrackOne + clipsXMLDataAudioTrackTwo

    #dodavanja video i audio headera i footera
    clipsXMLDataVideo = getVideoHeader() + clipsXMLDataVideo + getVideoFooter()
    clipsXMLDataAudio = getAudioHeader() + clipsXMLDataAudio + getAudioFooter()
    
    clipsXMLFinalData = clipsXMLDataVideo + clipsXMLDataAudio
    
    cijeliXML = getHeader() + str(lastClipEndFrameVideo) + getSequenceInfo(finalnoIme) + clipsXMLFinalData + getFooter()
    print (cijeliXML)
    xml_file = open('{ime}.xml'.format(ime = finalnoIme),'w+')
    xml_file.write(cijeliXML)
    xml_file.close()
    print('exportirao sam XML')
    #ocisti varijable
    clipsXMLDataVideo = clipsXMLDataAudioTrackOne = clipsXMLDataAudioTrackTwo = ''

#exportXML()


