document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('darkModeToggle');
    const body = document.body;
    const mainSection = document.getElementById('mainSection');
    const navbar = document.querySelector('nav');
    const footer = document.querySelector('footer'); // agar footer bo‘lsa

    // Oldingi holatni LocalStorage’dan o‘qish
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('bg-dark', 'text-light');
        body.classList.remove('bg-light', 'text-dark');

        if(mainSection) {
            mainSection.style.backgroundColor = '#121212';
            mainSection.style.color = '#ac7979ff';
        }

        if(navbar) {
            navbar.classList.add('navbar-dark', 'bg-dark');
            navbar.classList.remove('navbar-light', 'bg-light');
        }

        if(footer) {
            footer.classList.add('bg-dark', 'text-light');
        }

        toggleButton.textContent = '☀️ Light Mode';
    }

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('bg-dark');
        body.classList.toggle('bg-light');
        body.classList.toggle('text-light');
        body.classList.toggle('text-dark');

        if(mainSection) {
            if(body.classList.contains('bg-dark')) {
                mainSection.style.backgroundColor = '#121212';
                mainSection.style.color = '#f0f0f0';
            } else {
                mainSection.style.backgroundColor = '#ffffff';
                mainSection.style.color = '#000000';
            }
        }

        if(navbar) {
            navbar.classList.toggle('navbar-dark');
            navbar.classList.toggle('navbar-light');
            navbar.classList.toggle('bg-dark');
            navbar.classList.toggle('bg-light');
        }

        if(footer) {
            footer.classList.toggle('bg-dark');
            footer.classList.toggle('bg-light');
            footer.classList.toggle('text-light');
            footer.classList.toggle('text-dark');
        }

        // Toggle button text va LocalStorage
        if(body.classList.contains('bg-dark')) {
            toggleButton.textContent = '☀️ Light Mode';
            localStorage.setItem('theme', 'dark');
        } else {
            toggleButton.textContent = '🌙 Dark Mode';
            localStorage.setItem('theme', 'light');
        }
    });
});

