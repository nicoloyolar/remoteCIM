function addRow() {
    var table = document.getElementById("myTable");
    var tbody = table.getElementsByTagName("tbody")[0]; // Obtener el elemento <tbody>

    // Obtener la primera fila de la tabla (fila por defecto)
    var defaultRow = tbody.getElementsByTagName("tr")[0];

    // Clonar la primera fila para crear una nueva fila
    var newRow = defaultRow.cloneNode(true);

    // Reiniciar los valores seleccionados de los menús desplegables en la nueva fila
    var selects = newRow.getElementsByTagName("select");
    for (var i = 0; i < selects.length; i++) {
        selects[i].selectedIndex = 0;
    }

    // Agregar la nueva fila al <tbody> de la tabla
    tbody.appendChild(newRow);
}

function deleteRow(row) {
    var table = document.getElementById("myTable");
    var rowIndex = row.parentNode.parentNode.rowIndex; // Obtener el índice de fila

    // Eliminar la fila de la tabla
    table.deleteRow(rowIndex);
}