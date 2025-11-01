// OpenAlgo MVP - Main JavaScript

// Theme management
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

// Clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'success');
    }).catch(err => {
        showNotification('Failed to copy', 'error');
    });
}

// Notification system
function showNotification(message, type = 'info') {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} fixed top-4 right-4 w-96 z-50 fade-in`;
    alert.innerHTML = `<span>${message}</span>`;
    
    document.body.appendChild(alert);
    
    setTimeout(() => {
        alert.remove();
    }, 3000);
}

// Auto-refresh functionality for dashboard
function setupAutoRefresh(interval = 30000) {
    if (window.location.pathname.includes('/dashboard')) {
        setInterval(() => {
            location.reload();
        }, interval);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    
    // Add event listeners for theme selectors
    const themeSelectors = document.querySelectorAll('[data-theme-selector]');
    themeSelectors.forEach(selector => {
        selector.addEventListener('change', (e) => {
            setTheme(e.target.value);
        });
    });
});

// Export functions for global use
window.openalgo = {
    setTheme,
    copyToClipboard,
    showNotification
};
