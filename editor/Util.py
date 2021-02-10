import pymsyt
import pathlib
import oead
import json
import os
from platform import system

defaultConfig = {'bgColor': 'red'}

def getMsbtAsDict(pathIn):
  fileLoc = pathlib.Path(pathIn)
  with open(fileLoc, 'rb') as readData:
    msyt = pymsyt.Msbt.from_binary(readData)
  return msyt.to_dict()

# Obtain the system's local directory to determine where data should be stored
def get_data_dir():
    if system() == "Windows":
        data_dir = pathlib.Path(os.path.expandvars("%LOCALAPPDATA%")) / "botw_text_editor"
    else:
        data_dir = pathlib.Path.home() / ".config" / "botw_text_editor"
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    return(data_dir)

# Checks if a directory exists and makes it if not
def findMKDir(checkDir):
    if isinstance(checkDir, pathlib.Path):
        checkDir = checkDir
    else:
        try:
            checkDir = pathlib.Path(checkDir)
        except:
            print('Failed to make the pathlib instance :(')
            return
    if checkDir.exists():
        return checkDir
    else:
        checkDir.mkdir(parents=True, exist_ok=True)
        return checkDir

class Msyt:
  def __init__(self, filePathIn):
    with open(pathlib.Path(filePathIn), 'rb') as readFile:
      self.msbtDict = pymsyt.Msbt.from_binary(readFile.read()).to_dict()

class config:
  def __init__(self):
    self.configDirPath = findMKDir(get_data_dir() / 'Config')
    self.configFile = self.configDirPath / 'config.json'
    if self.configFile.exists():
      pass
    else:
      with open(self.configFile, 'wt') as initConfig:
        initConfig.write(json.dumps(defaultConfig, indent=2))

  def getConfigData(self):
    with open(self.configFile, 'rt') as readConfig:
      return json.loads(readConfig.read())

  def updateConfig(self, configData: dict):
    with open(self.configFile, 'wt') as writeConfig:
      writeConfig.write(json.dumps(configData))

def checkDict_two(dictIn: dict, valA, valB):
  try:
    returnValA = dictIn[valA]
  except:
    returnValA = None
  try:
    returnValB = dictIn[valB]
  except:
    returnValB = None
  return(returnValA, returnValB)

def getOptionsData():
  with open(pathlib.Path('editor/assets/options.json'), 'rt') as readOptions:
    options = json.loads(readOptions.read())
  return options