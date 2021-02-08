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