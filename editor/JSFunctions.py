# Creates a var called "element" from an elementId
def getElementById(elementId):
    return f"var element = document.getElementById('{elementId}')"

# Creates a function for changing the background color of an element in JS
def change_BG_Color(elementId, color):
    jsCode = f"""
    {getElementById(elementId)}
    element.style.backgroundColor = '{color}'
    """
    return jsCode

# Updates the entry list
def updateEntries(elementId, entries):
    jsCode = f"""
    {getElementById(elementId)}
    element.innerHTML = "<h1>{entries.keys()}</h1>"
    """
    return jsCode