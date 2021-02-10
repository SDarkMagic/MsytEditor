# Program for recursively obtaining the different control types from msbt files
import pathlib
import pymsyt
import sys
import json
import numpy as np


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
        print(file.name)
        if file.is_dir():
            genControlTypeList(file, controlList)
        else:
            controlList.extend(handleFile(file))
    return controlList

def genControlValueList(dirIn: pathlib.Path, controlType, listIn=None):
    if listIn == None:
        controlDict = {}
    else:
        controlDict = listIn

    def extendNestedList(dictInA: dict, dictInB: dict):
        dictC = {}
        print(cleanList(list(np.append(list(dictInA.keys()), list(dictInB.keys())))))
        keys = list(np.append(list(dictInA.keys()), list(dictInB.keys())))
        if dictInA == dictInB:
            dictC.update(dictInA)
        else:
            for key in keys:
                if key in dictInB.keys() and key in dictInB.keys():
                    currentObjA = dictInA[key]
                    currentObjB = dictInB[key]
                    print(currentObjA, currentObjB)
                    if isinstance(currentObjA, list) and isinstance(currentObjB, list):
                        currentObjA.extend(currentObjB)
                        dictC.update({key: currentObjA})
                    else:
                        print('Error: dict values are not lists')
                        if currentObjA == currentObjB:
                            dictC.update({key: currentObjA})
                        else:
                            dictC.update({key: [currentObjA, currentObjB]})
                elif key in dictInA.keys() and key not in dictInB.keys():
                    print('Key in A')
                    dictC.update({key: dictInA[key]})
                elif key in dictInB.keys() and key not in dictInA.keys():
                    print('key in B')
                    dictC.update({key: dictInB[key]})
                else:
                    print('how did you get here? the key had to have been in one of the two dicts...')
                    continue
        print(dictC)
        return dictC

    def handleFile(file):
        controlDict = {}
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
                                if kind == controlType:
                                    keyTypes = list(piece['control'].keys())
                                    keyTypes.remove('kind')
                                    for key in keyTypes:
                                        tempDict = {key: piece['control'].get(key)}
                                        if key in controlDict:
                                            controlDict.update(tempDict)
                                        else:
                                            controlDict.update(tempDict)
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
        return controlDict

    for file in dirIn.iterdir():
        if file.is_dir():
            print(file.name)
            genControlValueList(file, controlType, controlDict)
        else:
            controlDict.update(handleFile(file))
    return controlDict

def cleanList(listIn):
    finalList =[]
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
    for i in cleansedList:
        vals = genControlValueList(pathlib.Path(sys.argv[1]), i)
        print(vals)
    #jsonDict.update({'control': cleansedList})
    #print(jsonDict)
    #with open('assets/options.json', 'wt') as writeJson:
        #writeJson.write(json.dumps(jsonDict, indent=2))

if __name__ == '__main__':
    main()