function showSection(sectionId) {
    var botoneraSection = document.getElementById('section-botonera');
    var rutinasSection = document.getElementById('section-rutinas');

    if (sectionId === 'botonera') {
        botoneraSection.style.display = 'block';
        rutinasSection.style.display = 'none';
    } else if (sectionId === 'rutinas') {
        botoneraSection.style.display = 'none';
        rutinasSection.style.display = 'block';
    }
}