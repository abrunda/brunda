 

 var btn = document.getElementById("btn")
 var container = document.getElementById("ourcontainer")
 var url = "http://ec2-3-13-112-64.us-east-2.compute.amazonaws.com/SI/getmoisturedata.php?h_id=1100"
 btn.addEventListener("click", function(){
 	var ourRequest = new XMLHttpRequest();
 	ourRequest.open("GET", url);
 	ourRequest.onload = function() {
 		console.log(ourRequest.responseText);
 		var ourData = JSON.parse(ourRequest.responseText);
 		console.log(ourData);
 	}
 	ourRequest.send();
 })