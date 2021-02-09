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

    jsCode = f"""
    {getElementById('entryName')}
    entryName.innerText = `{entryName}`
    {attributesSection}
    {getElementById(elementId)}
    {elementId}.innerText = `{entryContents}`
    """
    return jsCode