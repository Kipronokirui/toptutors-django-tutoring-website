function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

// Working on the alert button with id of alertBtn starts 
let alertBtn = document.getElementById('alertBtn');
alertBtn.addEventListener('click', function(){
  alertBtn.parentElement.style.display = 'none';
});
// Working on the alert button with id of alertBtn ends