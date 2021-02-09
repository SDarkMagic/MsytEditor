#import pymsyt
import Util
import os
import pathlib
import webview
import threading
import json
import JSFunctions as js
import FileHandling

class ApiFunctions:
    window: webview.Window

    def __init__(self):
        self.Config = Util.config()

    def openFile(self):
        file = FileHandling.openFile(self.window)
        data = Util.Msyt(pathlib.Path(file))
        self.openData = data.msbtDict
        jsCode = js.updateEntries('EntryList', self.openData)
        self.window.evaluate_js(jsCode)

    def getEntry(self, entryName):
        jsCode = js.updateEntryContent('EntryContentText', self.openData, entryName)
        self.window.evaluate_js(jsCode)

    def startup(self):
        with open('editor/assets/Main.js', 'rt') as readJSCode:
            JSCode = readJSCode.read()
        self.window.evaluate_js(JSCode)

    def getConfigData(self):
        configData = self.Config.getConfigData()
        configJson = json.dumps(configData)
        return configJson

    def reloadWindow(self):
        self.window.load_url('assets/MainWindow.html')
        self.startup()

def main():
    api = ApiFunctions()
    api.window = webview.create_window('Botw Text Editor', 'assets/MainWindow.html', js_api=api)
    webview.start(debug=True, gui='cef', func=api.startup)

if __name__ == '__main__':
    main()