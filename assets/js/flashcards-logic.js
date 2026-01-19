document.addEventListener("DOMContentLoaded", function() {
    // Намираме всички елементи с клас 'flashcard'
    const cards = document.querySelectorAll('.flashcard');

    cards.forEach(card => {
        // Добавяме слушател за клик на всяка карта
        card.addEventListener('click', function() {
            // Превключваме класа 'flipped'
            this.classList.toggle('flipped');
        });
    });

    // Поддръжка на клавиша Space за обръщане (за по-добра достъпност)
    document.addEventListener('keydown', function(event) {
        if (event.code === "Space") {
            const hoveredCard = document.querySelector('.flashcard:hover');
            if (hoveredCard) {
                event.preventDefault(); // Спира превъртането на страницата
                hoveredCard.classList.toggle('flipped');
            }
        }
    });
});