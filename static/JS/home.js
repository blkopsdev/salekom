function ImgRotateScale() {
  var x = document.getElementsByTagName("img");
  var y = document.getElementsByClassName("Category");
  var i;
  for (x[i]=y[i]; i <= y.length;){
    x[i].style.transform = "rotate(-5deg)";
    x[i].style.transition = "transform 0.8s ease";
  }
}
