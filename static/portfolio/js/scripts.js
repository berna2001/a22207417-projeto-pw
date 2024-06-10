document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;

    darkModeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
    });

    function updateDateTime() {
        const now = new Date();
        const datetimeElement = document.getElementById('datetime');
        datetimeElement.textContent = now.toLocaleString();
    }

    setInterval(updateDateTime, 1000);
    updateDateTime();
});