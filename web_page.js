let blue_btn = document.getElementById('red_btn');
let red_btn = document.getElementById('red_btn');
let green_btn = document.getElementById('red_btn');
let content = document.getElementyById('content');

red_btn.addEventListner('click', () => {
    content.style.background='red';
})
blue_btn.addEventListner('click', () => {
    content.style.background='blue';
})
green_btn.addEventListner('click', () => {
    content.style.background='green';
})
