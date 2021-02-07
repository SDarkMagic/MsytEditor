#import pymsyt
import Util
import os
import pathlib
import webview
import threading

Util.Msyt(pathlib.Path('../tests/Test.msbt'))
webview.create_window('Botw Text Editor', './assets/MainWindow.html')
windowThread = threading.Thread(webview.start())
windowThread.start()
print('e')