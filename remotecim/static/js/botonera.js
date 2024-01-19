function changeInputValue(button) {
    var buttonValue = button.innerText;
    document.getElementById('screen-botonera').value = buttonValue;
    sendCOM(buttonValue);
}

function sendCOM(buttonValue) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/serial_communication/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onload = function() {
        if (xhr.status == 200) {
            var respuesta = JSON.parse(xhr.responseText);
            console.log(respuesta.resultado);

        }
    };

    xhr.send("buttonValue=" + encodeURIComponent(buttonValue));
}
