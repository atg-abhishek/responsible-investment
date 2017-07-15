/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunctiongeographic() {
    document.getElementById("myGeographicDropdown").classList.toggle("showGeography");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.geographicDropbtn')) {

    var dropdowns = document.getElementsByClassName("geographicDropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('showGeography')) {
        openDropdown.classList.remove('showGeography');
      }
    }
  }
}