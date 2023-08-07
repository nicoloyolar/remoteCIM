function cerrarModal2() {
    var modal = document.getElementById("modal2");
    modal.style.display = "none";
}

const openModalButton = document.getElementById('open-modal2');

const modal = document.getElementById('modal2');

openModalButton.addEventListener('click', function() {
    modal.style.display = 'block';
});

modal.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});