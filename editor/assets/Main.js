var button = document.getElementById('openFile')

button.addEventListener('click', async function (){
    console.warn('openFile Called')
    button.innerText = 'Hi'
    var file = await pywebview.api.openFile()
})
