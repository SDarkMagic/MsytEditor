# Script for converting an msbt file to a json file
import pymsyt
import sys
import pathlib
import json

def main(fileIn):
  filePath = pathlib.Path(fileIn)
  with open(filePath, 'rb') as readData:
    rawData = readData.read()
    convertedData = pymsyt.Msbt.from_binary(rawData)
    data = convertedData.to_dict()
  writePath = pathlib.Path(f'{filePath.parents[0]}/Test.json')
  writePath.write_text(json.dumps(data, indent=2))
  
  
if __name__ == '__main__':
  main(sys.argv[1])