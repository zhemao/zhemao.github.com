function slideOut(dist, direction, width, url){
  $("body").css("margin-left",direction*dist);
  console.log("dist: "+dist);
  if(dist<width){
    dist+=10;
    setTimeout("slideOut("+dist+", "+direction+", "+width+", '"+url+"')",1);
  }
  else{
    window.location=url;
  }
}

function slideIn(dist, direction, stop){
  $("body").css("margin-left",direction*dist);
  console.log("dist: "+dist);
  if(dist>stop){
    dist-=10;
    setTimeout("slideOut("+dist+", "+direction+", "+stop+")",1);
  }
}
