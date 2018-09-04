<!DOCTYPE html>
<html>
 
<head>
	<title> Test </title>
<link href="https://fonts.googleapis.com/css?family=Bangers" rel="stylesheet">
	<style type="text/css">
		
		.loadersmall {
			border: 5px solid #f3f3f3;
			-webkit-animation: spin 1s linear infinite;
			animation: spin 1s linear infinite;
			border-top: 5px solid #555;
			border-radius: 50%;
			width: 50px;
			height: 50px;
		}



		@-webkit-keyframes spin {
		  0% { 
		    -webkit-transform: rotate(0deg);
		    -ms-transform: rotate(0deg);
		    transform: rotate(0deg);
		  }

		  100% {
		    -webkit-transform: rotate(360deg);
		    -ms-transform: rotate(360deg);
		    transform: rotate(360deg);
		  }
		}

		@keyframes spin {
		  0% { 
		    -webkit-transform: rotate(0deg);
		    -ms-transform: rotate(0deg);
		    transform: rotate(0deg);
		  }

		  100% {
		    -webkit-transform: rotate(360deg);
		    -ms-transform: rotate(360deg);
		    transform: rotate(360deg);
		  }
		}

	</style>

	<script type= "text/javascript">
		var loaded_bool = false;

		function sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		}

		function remove()
		{
			var element = document.getElementById("runRemove");
			element.parentNode.removeChild(element);

			element = document.getElementById("i_frame");
			element.height = "300";
			element.removeAttribute("style");
		}

		async function checkIframeLoaded() {
		    // Get a handle to the iframe element
		    var iframe = document.getElementById('i_frame');
		    var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

		    //alert("Got");
		    // Check if loading is complete
		    if (  iframeDoc.readyState  == 'complete' ) {
		        //iframe.contentWindow.alert("Hello");
		        /*
		        iframe.contentWindow.onload = function(){
		            alert("I am loaded");
		        };
		        */
		        // The loading is complete, call the function we want executed once the iframe is loaded
		        //afterLoading();
		        //return;
		        iframe.style.display = "none";

		        loaded_bool = true;
		        
		        var element = document.getElementById("content");
		        element.innerHTML = "Generating Report ...";

		        await sleep(1000);

		        remove();

		        element = document.getElementById("loader");
				element.parentNode.removeChild(element);

				element = document.getElementById("disp");
				element.parentNode.removeChild(element);

				element = document.getElementById("result");
				
				var i_frame = document.createElement("iframe");
				i_frame.setAttribute("frameborder", "0");
				i_frame.src = "result.html";
				i_frame.width = "98%";
				i_frame.height = "400";
				i_frame.style.float = "middle";

				element.appendChild(i_frame);
				return;
		    } 

		    // If we are here, it is not loaded. Set things up so we check   the status again in 100 milliseconds
		    window.setTimeout(checkIframeLoaded, 100);
		}

		function afterLoading(){
		    alert("I am here");
		}
	</script>

	<style>
		#myProgress {
		  width: 98%;
		  background-color: #ddd;
		}

		#myBar {
		  width: 0%;
		  height: 30px;
		  background-color: #4CAF50;
		  text-align: center;
		  line-height: 30px;
		  color: white;
		}
	</style>

</head>
 
<body onload= "checkIframeLoaded();" style= "background-image: url('http://pinet.org.uk/assets/images/desktop-background.png');">

	<div style= "margin-top: 5%; margin-left: 25%; margin-right: 25%; margin-bottom: 25%; background-color: white;">
		
		<div style= "margin-top: 10%; margin-left: 2%;">

			<br />

			<h1 align= 'center' style= 'font-family:Bangers; font-size:60px;'> No More #BUGS..! </h1> <br />

			<iframe id= "i_frame" frameborder= "0" src= "<?php echo '/cgi-bin/u_test.py?ip=' . $_POST['ip'];?>" width= "98%" height= "100" style= "float:middle" style= "opacity: 0;">
			</iframe>

			<div id= "runRemove">
				<p align= "center"> Running Scripts ... </p>
				<div id="myProgress">
			  		<div id="myBar">0%</div>
			  	</div>
			</div>

			<br>

			<script type= "text/javascript">
			async function move() {
			  var elem = document.getElementById("myBar");   
			  var width = 0;
			  var lapse = 20;
			  var lapvar = 0;
			  var chk = 60;
			  var id = setInterval(frame, 100);
			  
			  async function frame() {
			    
			    if (width >= chk) {
			    	if(chk == 100) {
			    		clearInterval(id);
			    	} else if(lapvar++ >= lapse) {
			    	  	chk += 20;
			    	  	lapvar = 0;
			      	}
			    } else {
			      width++; 
			      
			      if(loaded_bool == true)
			      {
			      	width = 100;
			      	//loaded_bool = false;
			      	chk = 100;
			      }
			      
			      elem.style.width = width + '%'; 
			      elem.innerHTML = width * 1  + '%';
			    }
			  }
			}

			move();

			</script>

			<br />
			<br />

			<div id= "result" style= "margin-left: 2%;">
				<div id= "disp">
					<p align= "center" id= "content"> Awaiting Results ... </p>
				</div>
				<div class= "loadersmall" id= "loader" style= "margin-left: 45%;"> 
				</div>
			</div>
			<br />
			<!--
			<iframe frameborder= "0" src= "result.html" width= "98%" height= "250" style= "float:middle">
			</iframe>
			-->

		</div>
	
	</div>

</body>
 
</html>
