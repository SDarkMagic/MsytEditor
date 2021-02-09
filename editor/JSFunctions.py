import Util
# Creates a var called "element" from an elementId
def getElementById(elementId):
    return f"var {elementId} = document.getElementById('{elementId}')"

# Creates a function for changing the background color of an element in JS
def change_BG_Color(elementId, color):
    jsCode = f"""
    {getElementById(elementId)}
    {elementId}.style.backgroundColor = '{color}'
    """
    return jsCode

# Updates the entry list
def updateEntries(elementId, entries):
    htmlData = "<ul class='entryList_Text'>"
    for entry in entries['entries'].keys():
        htmlData =  f"""{htmlData}<li class="entryItem" onclick="updateEditor('{entry}')">{entry}</li>"""
    htmlData = f'{htmlData}</ul>'

    jsCode = f"""
    {getElementById(elementId)}
    {elementId}.innerHTML = `{htmlData}`
    """
    return jsCode

def updateEntryContent(elementId, entries, entryName):
    entryData = entries['entries'].get(entryName)
    entryContents = entryData['contents']
    try:
        entryAttributes = entryData['attributes']
    except:
        entryAttributes = None

    if entryAttributes != None:
        attributesSection = f"""
        {getElementById('attributes')}
        attributes.innerHTML = `<h2 class='Heading'>Attributes:</h2><form><input class='generalInput' id='attributesField' value='{entryAttributes}'></form>`
        """
    else:
        attributesSection = f"""
        {getElementById('attributes')}
        attributes.innerHTML = ``"""

    def getControlTextPairs(entry: list):
        entryHTML = str('')
        for component in entry:
            control, text = Util.checkDict_two(component, 'control', 'text')
            print(control, text)
            if control != None:
                entryHTML = f'{entryHTML}<h4>{control}</h4>'
            elif text != None:
                entryHTML = f'{entryHTML}<textarea class="entryText" id="EntryContentText">{text}</textarea>'
            else:
                print('An error occured: Both values were None')
        return entryHTML

    jsCode = f"""
    {getElementById('entryName')}
    entryName.innerText = `{entryName}`
    {attributesSection}
    {getElementById(elementId)}
    {elementId}.innerHTML = `{getControlTextPairs(entryContents)}`
    """
    return jsCode