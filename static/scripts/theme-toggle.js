const toggleButton = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;
const storedTheme = localStorage.getItem('theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initialTheme = storedTheme || (prefersDark ? 'dark' : 'light');

if (initialTheme && toggleButton) {
    htmlElement.setAttribute('data-theme', initialTheme);
    updateButtonText(initialTheme);
}

if (toggleButton) {
    toggleButton.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const targetTheme = currentTheme === 'light' ? 'dark' : 'light';

        htmlElement.setAttribute('data-theme', targetTheme);
        localStorage.setItem('theme', targetTheme);
        updateButtonText(targetTheme);
    });
}

function updateButtonText(currentTheme) {
    const newCta = currentTheme === 'dark' ? 'Light mode' : 'Dark mode';
    const icon = currentTheme === 'dark' ? 'Sun' : 'Moon';

    toggleButton.innerText = `${icon} - ${newCta}`;
    toggleButton.setAttribute('aria-label', `Switch to ${newCta}`);
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme') && toggleButton) {
        const newSystemTheme = e.matches ? 'dark' : 'light';
        htmlElement.setAttribute('data-theme', newSystemTheme);
        updateButtonText(newSystemTheme);
    }
});
