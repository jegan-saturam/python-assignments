var max_attempts = 5; 

function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "jegan_chaela" && password == "jegan1011"){
alert ("Login successfully");
window.location = "success2.html"; 
return false;
}
else{
max_attempts --;// Decrementing by one.
alert("You have left "+max_attempts+" attempts only;");

if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}
