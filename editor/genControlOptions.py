# Program for recursively obtaining the different control types from msbt files
import pathlib
import pymsyt
import sys
import json
import numpy as np

valDict = {}

def genControlTypeList(dirIn: pathlib.Path, listIn=None):
    if listIn == None:
        controlList = []
    else:
        controlList = listIn

    def handleFile(file):
        controlList =[]
        with open(file, 'rb') as readData:
            msytData = pymsyt.Msbt.from_binary(readData.read())
            data = msytData.to_dict()
        #print(data)
        entries = data['entries']

        for part in entries.keys():
            if isinstance(entries[part], dict):
                if 'contents' in entries[part].keys():
                    contents = entries[part]['contents']
                    for piece in contents:
                        if isinstance(piece, dict):
                            if 'control' in piece.keys():
                                kind = piece['control'].get('kind')
                                #print(kind)
                                controlList.append(kind)
                            else:
                                continue
                        else:
                            print(f'not a dict {piece}')
                            continue
                else:
                    continue
            else:
                print(f'Not a dict {part}')
                continue
        return controlList

    for file in dirIn.iterdir():
        if file.is_dir():
            genControlTypeList(file, controlList)
        else:
            controlList.extend(handleFile(file))
    return controlList

def genControlValueList(dirIn: pathlib.Path):
    def handleFile(file):
        with open(file, 'rb') as readData:
            msytData = pymsyt.Msbt.from_binary(readData.read())
            data = msytData.to_dict()
        entries = data['entries']

        for part in entries.keys():
            if isinstance(entries[part], dict):
                if 'contents' in entries[part].keys():
                    contents = entries[part]['contents']
                    for content in contents:
                        if ('control') in content.keys():
                            control = content['control']
                            kind = control['kind']
                            # Checks if the kind is in the dictionary, and if not, adds it
                            if kind in valDict.keys():
                                pass
                            else:
                                valDict.update({kind: {}})

                            subValDict = valDict[kind]

                            for entry in control.keys():
                                entryVal = control[entry]
                                #print('entry:', entry, entryVal)
                                if entry == 'kind':
                                    continue
                                else:
                                    if entry in subValDict.keys():
                                        optionList = subValDict.get(entry)
                                    else:
                                        optionList = []

                                    if isinstance(entryVal, list):
                                        optionList.extend(entryVal)
                                    else:
                                        optionList.append(entryVal)
                                    optionList = cleanList(optionList)
                                subValDict.update({entry: optionList})
                            valDict.update({kind: subValDict})
                        else:
                            continue
                else:
                    continue
            else:
                print(f'Not a dict {part}')
                continue
        return

    for file in dirIn.iterdir():
        if file.is_dir():
            #print(file.name)
            genControlValueList(file)
        else:
            handleFile(file)
    #return controlDict

def cleanList(listIn):
    finalList =[]
    listIn = list(listIn)
    for i in listIn:
        if i not in finalList:
            finalList.append(i)
        else:
            continue
    return finalList

def main():
    with open('assets/options.json', 'rt') as readJson:
        jsonDict = json.loads(readJson.read())
    listOut = genControlTypeList(pathlib.Path(sys.argv[1]))
    cleansedList = cleanList(listOut)
    genControlValueList(pathlib.Path(sys.argv[1]))
    #print('vals:', valDict)
    jsonDict.update({'control': cleansedList})
    jsonDict.update(valDict)
    #print(jsonDict)
    with open('assets/options.json', 'wt') as writeJson:
        writeJson.write(json.dumps(jsonDict, indent=2))

if __name__ == '__main__':
    main()