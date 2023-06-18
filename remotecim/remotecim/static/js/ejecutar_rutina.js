function sendSocketMessage(buttonValue) {
    var xhr = new XMLHttpRequest();
    var url = '/send_message/';
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
        var select = row.getElementsByTagName("select")[0];
        var comando = select.value;
        rutina.push(comando);
    }

    for (var j = 0; j < rutina.length; j++) {
        var comando = rutina[j];
        sendSocketMessage(comando + "\n");
        await sleep(2000);
    }
}