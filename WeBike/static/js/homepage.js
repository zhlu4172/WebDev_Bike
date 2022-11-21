
var jump_to_top_button = document.getElementById("jump_to_top_btn");

window.onscroll = function() {scrollFunction()}

const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const carousel_width = document.querySelector(".track").offsetWidth;
const track = document.querySelector('.track');

var section_index = 0;

function scrollFunction(){
    if(document.body.scrollTop > 800 || document.documentElement.scrollTop > 800){
        jump_to_top_button.style.display = "block";
    }
    else{
        jump_to_top_button.style.display = "none";
    }
}

//Moves to the top of the screen
function topFunction(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

//Moves to second banner
function slideDownFunction(){
    document.body.scrollTop = 900;
    document.documentElement.scrollTop = 900;
}

function shiftRight(){
    section_index = (section_index < 3) ? section_index + 1 : 3;
    track.style.transform = `translateX(${-carousel_width/4 * section_index}px)`;
    console.log(section_index)
}
function shiftLeft(){
    section_index = (section_index > 0) ? section_index - 1 : 0;
    track.style.transform = `translateX(${-carousel_width/4 * section_index }px)`;
    console.log(section_index)
}