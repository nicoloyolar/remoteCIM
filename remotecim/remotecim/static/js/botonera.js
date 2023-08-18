function sendSerialMessage(data) {
    // Crear una instancia del objeto XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Configurar la solicitud para enviar datos al servidor
    var url = '/send_serial_message/'; // Cambia la URL según tu configuración
    var params = 'data=' + encodeURIComponent(data);
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    // Manejar la respuesta de la solicitud
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('Datos enviados correctamente a través de comunicación serial');
        }
    };

    // Enviar los datos
    xhr.send(params);
}


function changeInputValue(button) {
    var buttonValue = button.innerText;
    document.getElementById('screen-botonera').value = buttonValue;
    sendSerialMessage(buttonValue); // Llamar a la nueva función sendSerialMessage
}

function changeInputValue2(button) {
    var buttonName = button.innerText;
    var nombrePunto = document.querySelector('[name="nombre_punto"]').value;
    var valorPunto = document.querySelector('[name="valor_punto"]').value;

    var buttonValue = buttonName + ' ' + nombrePunto + valorPunto;

    document.getElementById('screen-botonera').value = buttonName;
    sendSerialMessage(buttonValue); // Llamar a la nueva función sendSerialMessage
}