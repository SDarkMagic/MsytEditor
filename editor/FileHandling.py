from pathlib import Path
import webview

def openFile(window):
    fileTypes = ('MSBT files (*.msbt)', 'Pack files (*.pack)', 'All files (*.*)')
    result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False, file_types=fileTypes)
    print(result)
    return result