let root = document.documentElement
var openButton = document.getElementById('openFile')
var reloadButton = document.getElementById('reload')
var cleanConsoleButton = document.getElementById('cleanConsole')

openButton.addEventListener('click', async function (){
    await pywebview.api.openFile()
})

reloadButton.addEventListener('click', async function (){
    await pywebview.api.reloadWindow()
})

cleanConsoleButton.addEventListener('click', async function (){
    await pywebview.api.cleanConsole()
})

async function updateConfig() {
    var rawConfigData = await pywebview.api.getConfigData()
    var configData = JSON.parse(rawConfigData)
    for(var configItem in Object.keys(configData)){
        let configKey = Object.keys(configData).find(configItem => configData[configItem] === configData[configItem])
        root.style.setProperty(`--${configKey}`, configData[configKey])
    }
};

async function updateEditor(entryName){
    console.log(entryName)
    await pywebview.api.getEntry(entryName)
}