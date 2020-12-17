$(document).ready(function(){
  $('.sidenav').sidenav(); // jQuery for side menu on mobile devices
  $('.modal').modal();     // jQuery to initate modal pop ups
  $('.tooltipped').tooltip(); // jQuery to tooltip on edit review page reminding user to add rating. 
});

/* 
Button appears on home page allowing user to scroll back to the top of the page. 
Code adapted from: 
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
*/

var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}