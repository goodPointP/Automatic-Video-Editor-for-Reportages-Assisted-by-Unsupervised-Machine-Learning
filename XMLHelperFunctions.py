#funkcije za dobivanje xml boilerplate koda
def getHeader():
    return '<?xml version="1.0" encoding="UTF-8"?>          <!DOCTYPE xmeml> <xmeml version="4"> 	<sequence id="sequence-1" TL.SQAudioVisibleBase="0" TL.SQVideoVisibleBase="0" TL.SQVisibleBaseTime="0" TL.SQAVDividerPosition="0.5" TL.SQHideShyTracks="0" TL.SQHeaderWidth="236" Monitor.ProgramZoomOut="7305500160000" Monitor.ProgramZoomIn="0" TL.SQTimePerPixel="0.06198727824000002" MZ.EditLine="599477760000" MZ.Sequence.PreviewFrameSizeHeight="1080" MZ.Sequence.PreviewFrameSizeWidth="1920" MZ.Sequence.AudioTimeDisplayFormat="200" MZ.Sequence.PreviewRenderingClassID="1297106761" MZ.Sequence.VideoTimeDisplayFormat="101" MZ.WorkOutPoint="15240960000000" MZ.WorkInPoint="0" explodedTracks="true">		<uuid>121ee258-ca6a-49a4-913b-9b7e40547dcf</uuid><duration>'

def getSequenceInfo(sequenceName):
    return '</duration><rate><timebase>25</timebase><ntsc>FALSE</ntsc></rate><name>{sequenceName}</name><media>'.format(sequenceName = sequenceName)

def getFooter():
    return '</media><timecode> <rate><timebase>25</timebase><ntsc>FALSE</ntsc></rate><string>00:00:00:00</string><frame>0</frame><displayformat>NDF</displayformat></timecode><logginginfo><description></description><scene></scene><shottake></shottake><lognote></lognote><good></good><originalvideofilename></originalvideofilename>	<originalaudiofilename></originalaudiofilename></logginginfo>	</sequence></xmeml>'

def getVideoHeader():
    return '<video> <format> <samplecharacteristics>  <rate> <timebase>25</timebase><ntsc>FALSE</ntsc></rate>                     <codec>                         <name>Apple ProRes 422</name>                           <appspecificdata>                               <appname>Final Cut Pro</appname>                                <appmanufacturer>Apple Inc.</appmanufacturer>                               <appversion>7.0</appversion>                                <data>                                  <qtcodec>                                       <codecname>Apple ProRes 422</codecname>                                     <codectypename>Apple ProRes 422</codectypename>                                     <codectypecode>apcn</codectypecode>                                     <codecvendorcode>appl</codecvendorcode>                                     <spatialquality>1024</spatialquality>                                       <temporalquality>0</temporalquality>                                        <keyframerate>0</keyframerate>                                      <datarate>0</datarate>                                  </qtcodec>                              </data>                         </appspecificdata>                      </codec>                        <width>1920</width>                     <height>1080</height>                       <anamorphic>FALSE</anamorphic>                      <pixelaspectratio>square</pixelaspectratio> <fielddominance>none</fielddominance> <colordepth>24</colordepth>                 </samplecharacteristics>                </format><track TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1">'

def getVideoFooter():
    return '<enabled>TRUE</enabled><locked>FALSE</locked>   </track>   <track TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="0">					<enabled>TRUE</enabled>					<locked>FALSE</locked>				</track>				<track TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="0">					<enabled>TRUE</enabled>					<locked>FALSE</locked>				</track>			</video>'

def getAudioHeader():
    return '<audio>				<numOutputChannels>2</numOutputChannels>				<format>					<samplecharacteristics>						<depth>16</depth>						<samplerate>48000</samplerate>					</samplecharacteristics>				</format>				<outputs>					<group>						<index>1</index>						<numchannels>1</numchannels>						<downmix>0</downmix>						<channel>							<index>1</index>						</channel>					</group>					<group>						<index>2</index>						<numchannels>1</numchannels>						<downmix>0</downmix>						<channel>							<index>2</index>						</channel>					</group>				</outputs>'

def getAudioFooter():
    return '<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerStartKeyframe="-91445760000000000,0.5,0,0,0,0,0,0" PannerName="Balance" currentExplodedTrackIndex="0" totalExplodedTrackCount="2" premiereTrackType="Stereo">					<enabled>TRUE</enabled>					<locked>FALSE</locked>					<outputchannelindex>1</outputchannelindex>				</track>				<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerStartKeyframe="-91445760000000000,0.5,0,0,0,0,0,0" PannerName="Balance" currentExplodedTrackIndex="1" totalExplodedTrackCount="2" premiereTrackType="Stereo">					<enabled>TRUE</enabled>					<locked>FALSE</locked>					<outputchannelindex>2</outputchannelindex>				</track>				<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerStartKeyframe="-91445760000000000,0.5,0,0,0,0,0,0" PannerName="Balance" currentExplodedTrackIndex="0" totalExplodedTrackCount="2" premiereTrackType="Stereo">					<enabled>TRUE</enabled>					<locked>FALSE</locked>					<outputchannelindex>1</outputchannelindex>				</track>				<track TL.SQTrackAudioKeyframeStyle="0" TL.SQTrackShy="0" TL.SQTrackExpandedHeight="25" TL.SQTrackExpanded="0" MZ.TrackTargeted="1" PannerCurrentValue="0.5" PannerIsInverted="true" PannerStartKeyframe="-91445760000000000,0.5,0,0,0,0,0,0" PannerName="Balance" currentExplodedTrackIndex="1" totalExplodedTrackCount="2" premiereTrackType="Stereo">					<enabled>TRUE</enabled>					<locked>FALSE</locked>					<outputchannelindex>2</outputchannelindex>				</track>			</audio>'

#funkcija za konverziju zapisa u sekundama u zapis u frameovima za potrebe koristenja prema XML standardu
import math
def secondsToFPSConverter(seconds):
    return math.floor(float(seconds) * 25)

import re
#varijabla koja pamti na kojem frameu je zadnji klip stao
lastClipEndFrameVideo = 0
lastClipEndFrameAudioTrackOne = 0
lastClipEndFrameAudioTrackTwo = 0

#varijabla koja pamti definirane file-ove
definedClips = []

#funkcija za slaganje jednog unosa u track element
def getSingleVideoClipXML(clipItemId, filename, filepath, clipIN, clipOUT):
    global lastClipEndFrameVideo
    clipDuration = secondsToFPSConverter(clipOUT)-secondsToFPSConverter(clipIN)
    filenameNoExtension = re.split("\.(.*)", filename)[0]
    
    tagClipItemIdLine= '<clipitem id="clipitem-{clipId}">'.format(clipId = clipItemId)
    tagMasterClipId = '<masterclipid>masterclip-{clipName}</masterclipid>'.format(clipName = filenameNoExtension)
    tagName = '<name>{file}</name>'.format(file = filename)
    tagRate = '<enabled>TRUE</enabled><rate><timebase>25</timebase><ntsc>FALSE</ntsc></rate>'
    tagStart = '<start>{start}</start>'.format(start = lastClipEndFrameVideo+1)
    tagEnd = '<end>{end}</end>'.format(end = lastClipEndFrameVideo+1+clipDuration)
    tagIn = '<in>{clipIn}</in>'.format(clipIn = secondsToFPSConverter(clipIN))
    tagOut = '<out>{clipOut}</out>'.format(clipOut = secondsToFPSConverter(clipOUT))
    tagPproTicksIn = '<pproTicksIn>{pproIn}</pproTicksIn>'.format(pproIn = secondsToFPSConverter(clipIN) * 10160640000)
    tagPproTicksOut = '<pproTicksOut>{pproOut}</pproTicksOut>'.format(pproOut = secondsToFPSConverter(clipOUT) * 10160640000)
    tagAlphaPixelRatioAnamorhpic = '<alphatype>none</alphatype> <pixelaspectratio>square</pixelaspectratio> <anamorphic>FALSE</anamorphic>'
    if filename not in definedClips:
        tagFileHeader = '<file id="file-{clipName}">'.format(clipName = filenameNoExtension)
        tagFileName = '<name>{file}</name>'.format(file = filename)
        tagFilePath = '<pathurl>{filepath}</pathurl>'.format(filepath = filename)
        tagFileRate = '<rate> <timebase>25</timebase> <ntsc>FALSE</ntsc> </rate>'
        tagFileTimecode = '<timecode>	<rate>	<timebase>25</timebase>	<ntsc>FALSE</ntsc></rate><string>00:00:00:00</string><frame>0</frame>	<displayformat>NDF</displayformat></timecode>'
        tagFileMedia = '<media>	<video>	<samplecharacteristics>	<rate>	<timebase>25</timebase>	<ntsc>FALSE</ntsc></rate><width>1920</width><height>1080</height><anamorphic>FALSE</anamorphic>	<pixelaspectratio>square</pixelaspectratio><fielddominance>none</fielddominance></samplecharacteristics></video><audio>	<samplecharacteristics>	<depth>16</depth><samplerate>48000</samplerate>	</samplecharacteristics><channelcount>2</channelcount>	</audio></media></file>'
        tagFile = tagFileHeader + tagFileName + tagFilePath + tagFileRate + tagFileTimecode + tagFileMedia
    else:
        tagFile = '<file id="file-{clipName}"/>'.format(clipName = filenameNoExtension)
    tagLoggingColorLabels = '<logginginfo> <description></description> <scene></scene> <shottake></shottake> <lognote></lognote> <good></good> <originalvideofilename></originalvideofilename> <originalaudiofilename></originalaudiofilename> </logginginfo> <colorinfo> <lut></lut> <lut1></lut1> <asc_sop></asc_sop> <asc_sat></asc_sat> <lut2></lut2> </colorinfo> <labels> <label2>Iris</label2> </labels> </clipitem>'

    singleVideoClip = tagClipItemIdLine + tagMasterClipId + tagName + tagRate + tagStart + tagEnd + tagIn + tagOut + tagPproTicksIn + tagPproTicksOut + tagAlphaPixelRatioAnamorhpic + tagFile + tagLoggingColorLabels
    
    lastClipEndFrameVideo += clipDuration
    definedClips.append(filename)

    return singleVideoClip

def getSingleAudioTrackXML(clipItemId, filename, filepath, clipIN, clipOUT, trackMarker):
    global lastClipEndFrameAudioTrackOne
    global lastClipEndFrameAudioTrackTwo
    clipDuration = secondsToFPSConverter(clipOUT)-secondsToFPSConverter(clipIN)
    filenameNoExtension = re.split("\.(.*)", filename)[0]

    tagClipitem = '<clipitem id="clipitem-{clipId}" premiereChannelType="stereo">'.format(clipId = clipItemId)
    tagMasterclipid = '<masterclipid>masterclip-{clipName}</masterclipid>'.format(clipName = filenameNoExtension)
    tagName = '<name>{file}</name>'.format(file = filename)
    tagEnabled = '<enabled>TRUE</enabled>'
    tagRate = '<rate> 7 <rate> 8 <timebase>25</timebase> 8 <timebase>25</timebase> 9 <ntsc>FALSE</ntsc> 9 <ntsc>FALSE</ntsc> 10 </rate>'
    if (trackMarker == 1):
        tagRate = '<start>{start}</start>'.format(start = lastClipEndFrameAudioTrackOne+1)
        tagEnd = '<end>{end}</end>'.format(end = lastClipEndFrameAudioTrackOne+1+clipDuration)
    elif (trackMarker == 2):
        tagRate = '<start>{start}</start>'.format(start = lastClipEndFrameAudioTrackTwo+1)
        tagEnd = '<end>{end}</end>'.format(end = lastClipEndFrameAudioTrackTwo+1+clipDuration)
    tagIn = '<in>{clipIn}</in>'.format(clipIn = secondsToFPSConverter(clipIN))
    tagOut = '<out>{clipOut}</out>'.format(clipOut = secondsToFPSConverter(clipOUT))
    tagPproTicksIn = '<pproTicksIn>{pproIn}</pproTicksIn>'.format(pproIn = secondsToFPSConverter(clipIN) * 10160640000)
    tagPproTicksOut = '<pproTicksOut>{pproOut}</pproTicksOut>'.format(pproOut = secondsToFPSConverter(clipOUT) * 10160640000)
    tagFile = '<file id="file-{clipName}"/>'.format(clipName = filenameNoExtension)
    tagSourceTrack = '<sourcetrack><mediatype>audio</mediatype><trackindex>{trackIndex}</trackindex></sourcetrack>'.format(trackIndex = trackMarker)
    tagLoggingColorLabels = '<logginginfo> <description></description> <scene></scene> <shottake></shottake> <lognote></lognote> <good></good> <originalvideofilename></originalvideofilename> <originalaudiofilename></originalaudiofilename> </logginginfo> <colorinfo> <lut></lut> <lut1></lut1> <asc_sop></asc_sop> <asc_sat></asc_sat> <lut2></lut2> </colorinfo> <labels> <label2>Iris</label2> </labels> </clipitem>'

    singleAudioTrack = tagClipitem + tagMasterclipid + tagName + tagEnabled + tagRate + tagRate + tagEnd + tagIn + tagOut + tagPproTicksIn + tagPproTicksOut + tagFile + tagSourceTrack + tagLoggingColorLabels

    if (trackMarker == 1):
        lastClipEndFrameAudioTrackOne += clipDuration
    elif (trackMarker == 2):
        lastClipEndFrameAudioTrackTwo += clipDuration
        
    return singleAudioTrack
