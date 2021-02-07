#import pymsyt
import Util
import os
import pathlib
import webview
import threading
import time
import JSFunctions as js
import FileHandling

class ApiFunctions:
    window: webview.Window

    def openFile(self):
        FileHandling.openFile(self.window)

    def startup(self):
        data = Util.Msyt(pathlib.Path('tests/Test.msbt'))
        with open('editor/assets/Main.js', 'rt') as readJSCode:
            JSCode = readJSCode.read()
        self.window.evaluate_js(JSCode)
        self.window.evaluate_js(js.updateEntries('EntryList', data.msbtDict))


def main():
    api = ApiFunctions()
    api.window = webview.create_window('Botw Text Editor', 'assets/MainWindow.html', js_api=api)
    webview.start(debug=True, gui='cef', func=api.startup)

if __name__ == '__main__':
    main()