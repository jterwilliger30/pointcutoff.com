// Onclick of the button
document.querySelector("login").onclick = function () {
  // Call python's random_python function
  eel.parse()(function(number){
    // Update the div with a random number returned by python
    document.querySelector(".retstring").innerHTML = number;
  })
}