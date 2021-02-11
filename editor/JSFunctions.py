import Util
import json
import pathlib

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

class form:
    def __init__(self, elementId, entries, entryName):
        self.entries = entries
        self.setupJS = self.updateEntryContent(elementId, entries, entryName)
        self.js = self.updateEntryContent(elementId, entries, entryName)
        self.entry = entries['entries'][entryName]

    def updateEntryContent(self, elementId, entries, entryName):
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
            controlOption = '<option value="{control}"{isSelected}>{control}</option>'
            for component in entry:
                i = 0
                control, text = Util.checkDict_two(component, 'control', 'text')
                if control != None:
                    controlOptions = Util.getOptionsData()
                    for option in controlOptions['control']:
                        if i == 0:
                            entryHTML = f'{entryHTML}<div class="controlContainer"><h4 class="controlHeading">Controls:</h4><select class="controlType" id="control" name="controlType">'
                        else:
                            pass
                        if option == control['kind']:
                            entryHTML = f'{entryHTML}{controlOption.format(control=option, isSelected=" selected")}'
                        else:
                            entryHTML = f'{entryHTML}{controlOption.format(control=option, isSelected="")}'
                        i += 1
                        if i == len(controlOptions['control']):
                            entryHTML = f'{entryHTML}</select></div>'
                        else:
                            pass
                elif text != None:
                    entryHTML = f'{entryHTML}<textarea class="entryText" id="text">{text}</textarea>'
                else:
                    print('An error occured: Both values were None')
            return entryHTML

        jsCode = f"""
        {getElementById('entryName')}
        entryName.innerText = `{entryName}`
        {attributesSection}
        {getElementById(elementId)}
        {elementId}.innerHTML = `{getControlTextPairs(entryContents)}`
        function updateEntry_JS(){r'{'}
            var form = document.forms['entryContentForm']
            var updatedEntryArray = []

            for(var element in form.elements){r'{'}
                element = form.elements[element];
                let entrySubData = {r'{}'};
                if(element.id == 'control'){r'{'}
                    entrySubData['control'] = element.value
                {r'}'}
                else if(element.id == 'text'){r'{'}
                    entrySubData['text'] = element.value
                {r'}'}
                else{r'{'}
                    continue
                {r'}'}
                updatedEntryArray.push(entrySubData)
            {r'}'}
            console.warn(updatedEntryArray)
            return updatedEntryArray
        {r'}'}
        {getElementById('submit')}
        submit.addEventListener('click', async function(){r'{'}let updatedEntry = updateEntry_JS(); await pywebview.api.updateEntry('{entryName}', updatedEntry){r'}'})

        """
        return jsCode
"""
    def saveEntryData(self):
        jsCode = f
        function updateEntry(){r'{'}
            var form = document.forms['entryContentForm']
            var updatedEntryArray = []

            for(var element in form.elements){r'{'}
                element = form.elements[element];
                let entrySubData = {r'{}'};
                if(element.id == 'control'){r'{'}
                    entrySubData['control'] = element.value
                {r'}'}
                else if(element.id == 'text'){r'{'}
                    entrySubData['text'] = element.value
                {r'}'}
                else{r'{'}
                    continue
                {r'}'}
                updatedEntryArray.push(entrySubData)
            {r'}'}
            console.warn(updatedEntryArray)
        {r'}'}

        return jsCode
"""