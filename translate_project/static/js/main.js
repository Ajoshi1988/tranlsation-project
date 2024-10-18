var socket= new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage=function(e){

    var djangoData=JSON.parse(e.data);
    console.log(djangoData);

    var translate_button = document.getElementById('translate_button');
    var download_button = document.getElementById('download_button');
    


    // Disable the buttons and link
    translate_button.disabled = true;
    download_button.disabled = true;
    document.getElementById('download_file_link').setAttribute('href', '#');


    

    


    // document.querySelector('#app').innerText= djangoData.value;

   if(djangoData.value==3.142){

    var paragraph = document.getElementById('no_file_id');
    paragraph.textContent = "Translation aborted, Please upload the file to submit the task";
    paragraph.className = "p-3 text-center fw-bold bg-light border border-danger rounded rounded-2 text-danger";


    translate_button.disabled = false;
    download_button.disabled = false;
    document.getElementById('download_file_link').setAttribute('href', "http://localhost:8000/download/");
    




   } else if(djangoData.value==3.1425){


    var paragraph = document.getElementById('no_file_id');
    paragraph.textContent = "Translation aborted, Wrong file uploaded, Only .XLSX files are allowed";
    paragraph.className = "p-3 text-center fw-bold bg-light border border-danger rounded rounded-2 text-danger";

    translate_button.disabled = false;
    download_button.disabled = false;
    document.getElementById('download_file_link').setAttribute('href', "http://localhost:8000/download/");
    
   }else if(djangoData.value==3.14256){


    translate_button.disabled = false;
    download_button.disabled = false;
    document.getElementById('download_file_link').setAttribute('href', "http://localhost:8000/download/");
   

   }  
   else {


    


    var progressBar = document.getElementById('progress_bar');
    
   
    // Update the width and text content of the progress bar
    progressBar.style.width = djangoData.value + '%';
    progressBar.setAttribute('aria-valuenow', djangoData.value);
    progressBar.textContent = djangoData.value + '%';



    if(djangoData.value==100){

                var paragraph = document.getElementById('no_file_id');
                paragraph.textContent = "Translation Completed, Click on the download button to download the file";
                paragraph.className = "p-3 text-center fw-bold bg-lightgreen border border-success rounded rounded-2 text-success";


                // Enable the buttons, once transaltion is complete
                

                setTimeout(function() {
                    paragraph.textContent = "";
                    paragraph.className = "";
                    
                    // Clear the content
                }, 8000);


                

    }


    
    


   }







}




