const searchIcon = document.querySelector('.search-icon');
const searchForm = document.querySelector('.search-form');
const cartIcon = document.querySelector('.cart-icon');
const cartContainer = document.querySelector('.cart-items-container');

searchIcon.addEventListener("click", () => {
    searchForm.classList.toggle("active");    
});

cartIcon.addEventListener('click', () => {
    cartContainer.classList.toggle('active');
});
