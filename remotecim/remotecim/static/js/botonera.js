function sendSocketMessage(buttonValue) {
    var xhr = new XMLHttpRequest();
    var url = '/send_message_validada/';
    var params = 'message=' + encodeURIComponent(buttonValue);
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('Mensaje enviado correctamente');
        }
    };
    xhr.send(params);
}

function changeInputValue(button) {
    var buttonValue = button.innerText;
    document.getElementById('screen-botonera').value = buttonValue;
    sendSocketMessage(buttonValue);
}

function changeInputValue2(button) {
    var buttonName = button.innerText;
    var nombrePunto = document.querySelector('[name="nombre_punto"]').value;
    var valorPunto = document.querySelector('[name="valor_punto"]').value;

    var buttonValue = buttonName + ' ' + nombrePunto + valorPunto;

    document.getElementById('screen-botonera').value = buttonName;
    sendSocketMessage(buttonValue);
}