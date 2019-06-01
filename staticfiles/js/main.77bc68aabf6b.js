const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();
setTimeout(() => {
  $("#messages").fadeOut("slow");
}, 3000);

setTimeout(function() {
  $(".messages").fadeOut("slow");
}, 3000);

$(document).ready(function() {
  console.log("App connected to JS");
});
