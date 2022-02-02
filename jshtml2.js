function ShowAll()  
	{  
	const { Client } = require('pg')
	const client = new Client({
  		user: 'myuser',
  		host: 'localhost',
  		database: 'mydatabase',
  		password: 'mypass',
  		port: 5432,
		})
	client.connect(function(err) {
  	if (err) throw err;
  		console.log("Connected!");
	});
	var query = client.query("SELECT username,email from accounts");    
	var span = document.createElement("span");  
	span.style.color = "Blue";  
	span.innerText = " username " + " password " + " email ";  
	document.body.appendChild(span);  
	while (!rs.eof) {  
		var span = document.createElement("span");  
		span.style.color = "green";  
		span.innerText = "\n " + rs.fields(0) + " |  " + rs.fields(1) + " |  " + rs.fields(2);  
		document.body.appendChild(span);  
		client.MoveNext();  
        	}   
        }  
       
function UpdateRecord()  
        {    
        var username = document.getElementById('username').value;  
        var password = document.getElementById('password').value;  
        if (username.length != 0 && password.length != 0) {  
        	const { Client } = require('pg')
		const client = new Client({
  			user: 'myuser',
  			host: 'localhost',
  			database: 'mydatabase',
  			password: 'mypass',
  			port: 5432,
			})
		client.connect(function(err) {
  		if (err) throw err;
  			console.log("Connected!");
	});	
        	var query = "delete from accounts where username = " + username ;
        	client.query(query);
        	alert("Update Record Successfuly");  
        	username.value = " ";     
        	}  
         else  
         	{  
                alert("Please textbox's value");  
                }  
       
         }  
    
