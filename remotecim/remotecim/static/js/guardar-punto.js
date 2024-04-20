// permite cerrar el popup del modal para guardar puntos
function cerrarModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}

const openModalButton = document.getElementById('open-modal');

const modal = document.getElementById('modal');

openModalButton.addEventListener('click', function() {
    modal.style.display = 'block';
});

modal.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

const openMoveModalButton = document.getElementById('open-move-modal');
const modalMove = document.getElementById('modal-move');

openMoveModalButton.addEventListener('click', function() {
    modalMove.style.display = 'block';
});

modalMove.addEventListener('click', function(event) {
    if (event.target === modalMove) {
        modalMove.style.display = 'none';
    }
});

// validación de los campos del formulario para guardar puntos
function validarFormulario() {
    var nombrePunto = document.getElementById("nombre_punto").value;
    var descripcion = document.getElementById("descripcion").value;

    if (nombrePunto.trim() === "" || descripcion.trim() === "") {
        alert("Por favor, completa todos los campos.");
        return false;
    }
    return true;
}