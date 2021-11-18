
window.SpeechRecognition =
window.SpeechRecognition ||
 window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.interimResults = true;
recognition.continuous = true;
var langopt=$('#select1').val();
 recognition.lang=langopt;
var textarea=$("#textscan");
recognition.addEventListener("result", (e) => {
const text = Array.from(e.results)
  .map((result) => result[0])
  .map((result) => result.transcript)
   .join("");
    textarea.val(text)
});

var t = document.getElementById("recognize-btn");
 function micro() {
   recognition.lang=String($('#select1').val());
    if(t.value==="YES"){
       recognition.stop();
       t.value="NO";
       $('#textscan').prop('disabled', false);
       $('#select1').prop('disabled', false);
        document.getElementById('recognize-btn').setAttribute("style","color:black");
        
    }
    else if(t.value==="NO"){
        t.value="YES";
        recognition.start();
         $('#textscan').prop('disabled', true);
       $('#select1').prop('disabled', true);
        document.getElementById('textscan').setAttribute("style","background-color:#F8F8F8;")
        document.getElementById('recognize-btn').setAttribute("style","color:red");
    }
    
}
