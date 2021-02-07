#import pymsyt
import Util
import os
import pathlib
import webview
import threading

def startup(window):
    Util.Msyt(pathlib.Path('../tests/Test.msbt'))
    with open('assets/Main.js', 'rt') as readJSCode:
        JSCode = readJSCode.read()
    window.evaluate_js(JSCode)

window = webview.create_window('Botw Text Editor', './assets/MainWindow.html')
webview.start(startup, window)