let root = document.documentElement
var button = document.getElementById('openFile')

button.addEventListener('click', async function (){
    await pywebview.api.openFile()
})

async function updateConfig() {
    var rawConfigData = await pywebview.api.getConfigData()
    var configData = JSON.parse(rawConfigData)
    for(var configItem in Object.keys(configData)){
        let configKey = Object.keys(configData).find(configItem => configData[configItem] === configData[configItem])
        root.style.setProperty(`--${configKey}`, configData[configKey])
    }
};

function updateEditor(entryName){
    console.warn(entryName)
}

/*
button.addEventListener('mouseover', async function (){
    await updateConfig()
})
*/