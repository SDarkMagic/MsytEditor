import pymsyt
import pathlib
import oead

def getMsbtAsDict(pathIn):
  fileLoc = pathlib.Path(pathIn)
  with open(fileLoc, 'rb') as readData:
    msyt = pymsyt.Msbt.from_binary(readData)
  return msyt.to_dict()

class Msyt:
  def __init__(self, filePathIn):
    with open(pathlib.Path(filePathIn), 'rb') as readFile:
      self.msbtDict = pymsyt.Msbt.from_binary(readFile.read()).to_dict()
