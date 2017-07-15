/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunctionGeo() {
    document.getElementById("myGeoDropdown").classList.toggle("showGeo");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.geoDropbtn')) {

    var dropdowns = document.getElementsByClassName("geoDropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('showGeo')) {
        debugger;
        openDropdown.classList.remove('showGeo');
      }
    }
  }
}