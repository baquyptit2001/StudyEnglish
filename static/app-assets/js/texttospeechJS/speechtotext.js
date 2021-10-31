

window.SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = true;
recognition.continuous = true;
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
    if(t.value==="YES"){
       recognition.stop();
       t.value="NO";
       $('#textscan').prop('disabled', false);
        document.getElementById("microphone-icon").className='{% static "fas fa-microphone" %}';
      //  document.getElementById('fa-microphone').setAttribute("style","color:black");
    }
    else if(t.value==="NO"){
        t.value="YES";
        recognition.start();
         $('#textscan').prop('disabled', true);
        document.getElementById("microphone-icon").className='{% static "fas fa-stop" %}';
        // document.getElementById('fas fa-stop').setAttribute("style","color:red");
    }
    
}