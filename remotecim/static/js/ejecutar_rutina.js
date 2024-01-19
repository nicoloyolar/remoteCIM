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

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function ejecutarRutina() {
    var table = document.getElementById("myTable");
    var rows = table.getElementsByTagName("tr");
    var rutina = [];

    for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var selectComando = row.querySelector("select[name='comando']").value;
        var selectPunto = row.querySelector("select[name='punto']").value;

        if (selectComando === 'move' || selectComando === 'movel') {
            rutina.push({ comando: selectComando, punto: selectPunto });
        } else {
            // Agrega solo el valor del comando
            rutina.push({ comando: selectComando });
        }
    }

    for (var j = 0; j < rutina.length; j++) {
        var comando = rutina[j].comando;
        var punto = rutina[j].punto || ''; // Si no hay punto, asigna una cadena vacía
        // Aquí puedes usar los valores comando y punto como desees
        sendSocketMessage(comando + " " + punto);
        await sleep(5000);
    }
}