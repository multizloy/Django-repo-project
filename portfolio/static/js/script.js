let flipCards = document.querySelectorAll(‘.flip-card’);
flipCards.forEach((flipCard) => {
flipCard.addEventListener(‘click’, () => {
flipCard.classList.toggle(‘flipped’);
});
});