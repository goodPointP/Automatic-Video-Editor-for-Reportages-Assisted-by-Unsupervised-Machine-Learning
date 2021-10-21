#GUI file
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import IntVar
from ControllerFile import programStart

root = tk.Tk()

root.resizable(width=False, height=False)
root.title('Vidya')
root.iconbitmap('vidya.ico')

canvas = tk.Canvas(root, height = '200', width = '600')
canvas.pack()

selectedInputFiles = []

frameImport = tk.Frame(root, bg = '#b1d5e5')
frameImport.place(relx=0.05, rely=0.05, relwidth = 0.9, relheight = 0.55)

def selectInputFiles():

    selectedFiles = tk.filedialog.askopenfilenames()
    if selectedFiles:
        global selectedInputFiles
        selectedInputFiles = list(selectedFiles)
        print(selectedInputFiles)
        print(type(selectedInputFiles))

lblDropFilesHere = tk.Button(frameImport, text='Browse for input files...', bg='#b1d5e5', command = selectInputFiles)
lblDropFilesHere.pack(pady=40)

frame = tk.Frame(root)
frame.place(relx=0.025, rely=0.65, relwidth = 0.95, relheight = 0.5)

#EXPORT LOCATION
#default export lokacija je direktorij iz kojeg smo pokrenuli program
exportLocation = os.getcwd()

inputFilename = tk.Entry(frame, width = '35', textvariable = exportLocation)
inputFilename.insert(0,string='My Reportage Name')
inputFilename.grid(row = 5, column = 0)

def selectExportLocation():
    selectedLocation = tk.filedialog.askdirectory()
    if selectedLocation:
        global exportLocation
        exportLocation = selectedLocation
        print(exportLocation)
        labelExportLocation.delete(0, 800)
        ExportLocation.insert(0,exportLocation)

btnExportLocation = tk.Button(frame, text = "Set export location...", command = selectExportLocation)
btnExportLocation.grid(row = 6, column = 0)

labelExportLocation = tk.Label(frame, text = exportLocation, width = '40')
labelExportLocation.grid(row = 6, column = 1, columnspan = 10)

var1 = IntVar()
check2 = tk.Checkbutton(frame, text=".mp4", variable=var1, onvalue=1, offvalue=0)
check2.grid(row = 5, column = 1)

var2 = IntVar()
check1=tk.Checkbutton(frame, text=".xml", variable=var2, onvalue=1, offvalue=0)
check1.grid(row = 5, column = 2)

##def ispisiState():
##    print('prvi checkbox je '+str(var1.get()))
##    print('drugi checkbox je '+str(var2.get()))

def sendStartSignal():
    checkBoxMp4 = var1.get()
    print(checkBoxMp4)
    checkBoxXml = var2.get()
    print(type(selectedInputFiles))
    print(type(exportLocation))
    print(type(checkBoxMp4))
    print(type(checkBoxXml))
    if (checkBoxMp4 or checkBoxXml) and len(selectedInputFiles) and len(exportLocation):
        finalnoIme = inputFilename.get()
        programStart(selectedInputFiles, exportLocation, checkBoxMp4, checkBoxXml, finalnoIme)
    elif not len(selectedInputFiles):
        print('Choose input files.')
    elif not len(exportLocation):
        print('Choose an export location.')
    elif checkBoxMp4 and checkBoxXml == 0:
        print('Choose at least one export option.')

btnExport = tk.Button(frame, text = "Export", command = sendStartSignal)
btnExport.grid(row = 5, rowspan = 4, column = 12, columnspan = 12, padx = '10', ipadx = '2')

root.mainloop()
