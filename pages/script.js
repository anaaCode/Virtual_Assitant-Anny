
   function button1Clicked(){
    alert("Ridirecting to virtual assitant page")
   }

   const button = document.getElementById('button1');

   button.addEventListener('click' ,() =>{
    executePython();

   })
  
    // Function to execute Python file
    function executePython() {
        fetch('/execute-python', {
            method: 'POST',
        })
        .then(response => response.text())
        .then(data => {
            alert(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    document.addEventListener("DOMContentLoaded" , function (){
        document.getElementById("button1").addEventListener("click", function(){
            alert("Button  Clicked");
        });
    })