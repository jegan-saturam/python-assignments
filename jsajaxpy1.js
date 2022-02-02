function UpdateRecord()  
	{  
	var username = document.getElementsByName("username");
	var password = document.getElementsByName("password");
	var email = document.getElementsByName("email");
	resultsContainer.style.display = "block";
	
	var server_data = [
		{"username": username},
		{"password": password},
		{"email": email}
 	]; 
 	
 	$.ajax({
   	type: "POST",
   	url: "/process_qtc",
   	data: JSON.stringify(server_data),
   	contentType: "application/json",
   	dataType: 'json',
   	success: function(result) {
     	numRows.innerHTML = result.rows; 
   } 
 });
}
	}
    
