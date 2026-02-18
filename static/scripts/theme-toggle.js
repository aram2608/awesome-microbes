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
    const newCta = currentTheme === 'dark' ? 'light mode' : 'dark mode';
    const buttonText = `Switch to ${newCta}`;

    toggleButton.innerText = buttonText;
    toggleButton.setAttribute('aria-label', buttonText);
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme') && toggleButton) {
        const newSystemTheme = e.matches ? 'dark' : 'light';
        htmlElement.setAttribute('data-theme', newSystemTheme);
        updateButtonText(newSystemTheme);
    }
});
