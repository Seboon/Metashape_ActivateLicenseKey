import Metashape

from PySide2 import QtCore,QtWidgets
from pathlib import Path
import glob
import os


path = QtCore.QDir.currentPath()
global appFile
appFile = [f.as_posix() for f in list (Path(path).glob('Metashape.exe'))]


global licenses
licenses = [Path(f) for f in list (Path(path).glob('*.lic')) if Path(f).stem != 'rlm_roam']
for licence in licenses:
    os.remove(licence.as_posix())

global app
app = QtCore.QCoreApplication.instance()
global key

key = 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX'

if Metashape.app.activated == False:
    locale = QtCore.QLocale.system().name().split('_')[0]
    if locale =='fr':
        print("Activation de la clé de licence...")
    else:
        print(" Activating License Key...")
    Metashape.License().activate(key)

def removeLicense():   
    Metashape.License().deactivate(key)
    for licence in licenses:
        os.remove(licence.as_posix())   


app.aboutToQuit.connect(removeLicense)
