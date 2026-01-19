// Функция за автоматично отваряне на външни линкове в нов таб
document.addEventListener("DOMContentLoaded", function() {
    var links = document.links;
    for (var i = 0, linksLength = links.length; i < linksLength; i++) {
        if (links[i].hostname != window.location.hostname) {
            links[i].target = '_blank';
            links[i].rel = 'noopener'; // Добра практика за сигурност
        }
    }
});