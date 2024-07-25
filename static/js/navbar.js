document.addEventListener('DOMContentLoaded', (event) => {
    const searchButton = document.querySelector('[data-collapse-toggle="navbar-search"]');
    const searchInput = document.getElementById('navbar-search');

    searchButton.addEventListener('click', () => {
        searchInput.classList.toggle('hidden');
    });
});
