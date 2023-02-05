console.log("this is a message")
var dt = new Date();
dt1 = dt.toLocaleDateString().split("/");
var newDate = new Date( dt1[2], dt1[0]-1, dt1[1]-1);
document.getElementById('date-time').innerHTML='• '+ newDate.toLocaleString();