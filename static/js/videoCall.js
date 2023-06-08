var x ="loading js file." 

let username;

var screenTrack = null;
var recodedChunks = [];
const audioTrack = null;
var videoStream
let mediaRecorder;
var interScreen

var remote_video = document.getElementById("remote-video")
var local_video = document.getElementById("local-video")


function test(){
    console.log(x)
}

const constraints = {
    "audio" : true,
    "video": {
        "width": 1280,
        "height": 720

    }
}

function muteAudio(){
    audioTrack = videoStream.getAudioTrack()
    
    if(!audioTrack){
        return;
    }
    else if (audioTrack.enabled == false){
        audioTrack.enabled = true;
        $(this).text("Mute")
    }
    else{
        audioTrack.enabled = false;
        $(this).text("unmute");
    }
}

async function sharebtn(){
    var share = document.getElementById("share");
    if (share.innerHTML == "Stop Share"){
        screenTrack.stop();
        screenTrack = null;
        share.innerHTML="Screen Share"
        var local_video = document.getElementById("local-video")
        var remote_video = document.getElementById("remote-video")
        remote_video.srcObject = videoStream;
        local_video.srcObject = null

    }
    else{
        try{
            var local_video = document.getElementById("local-video")
            var sc_stream = await navigator.mediaDevices.getDisplayMedia(constraints);
            var remote_video = document.getElementById("remote-video")
            local_video.srcObject = videoStream;   

            // remote_video.srcObject = new MediaStream(sc_stream);
    
            // var sc_stream = await navigator.mediaDevices.getDisplayMedia(constraints);
            // if (sc_stream && sc_stream.getVideoTracks().length>0){
    
            //     screenTrack = sc_stream.getVideoTracks()[0];
            //     remote_video.srcObject = new MediaStream(screenTrack);
            // }
            if (sc_stream && sc_stream.getVideoTracks().length > 0) {
                screenTrack = sc_stream.getVideoTracks()[0];
                remote_video.srcObject = new MediaStream([screenTrack]);
                interScreen = sc_stream;
                share.innerHTML="Stop Share"
                
            }
            screenStream = sc_stream;
            
        } catch(e){
            console.log(e)
        }
    }
}

function startCall(){   
        document.getElementById("video-call-div").style.display = "inline"
    
        var remote_video = document.getElementById("remote-video")
        var local_video = document.getElementById("local-video")

        
        navigator.mediaDevices.getUserMedia(constraints).then(stream =>{
            var options = { mimeType: "video/webm; codecs=vp8,opus" };
            if (screenTrack && screenTrack.readyState === "live") {
                stream.addTrack(screenTrack);
             }
            mediaRecorder = new MediaRecorder(stream, options);
            videoStream = stream;
            remote_video.srcObject = stream;
        })
        .catch(error =>{
            console.log('Error Accessing Media devides',error)
        })
    }


//     // Start Recording


    let recordedBlobs;
    let downloadButton = document.getElementById("downBtn")
    const codecPreferences = document.querySelector('#codecPreferences');
    const recordButton = document.getElementById("record");
    function record(){
        let downloadButton = document.getElementById("downBtn")
        console.log("recording")
        const recordButton = document.getElementById("record");
      if (recordButton.textContent === 'Start Recording') {
        
        startRecording();
        console.log(recordButton.textContent)
      } else {
        stopRecording();
        recordButton.textContent = 'Start Recording';
        downloadButton.disabled = false;
      }
    };

function startRecording() {
    recordedBlobs = [];
    try {
            

            mediaRecorder.ondataavailable = handleDataAvailable;
            mediaRecorder.start();
        
    } catch (e) {
        console.error('Exception while creating MediaRecorder:', e);
        return;
    }
    
    
    const recordButton = document.getElementById("record");
    recordButton.innerHTML = 'Stop Recording';
    
    downloadButton.disabled = false;
    mediaRecorder.onstop = (event) => {
        console.log('Recorder stopped: ', event);
        console.log('Recorded Blobs: ', recordedBlobs);
    };
    mediaRecorder.ondataavailable = handleDataAvailable;
    // mediaRecorder.start();
    console.log('MediaRecorder started', mediaRecorder);
    }

function stopRecording() {
    mediaRecorder.stop();
    }


function handleDataAvailable(event) {
    console.log('handleDataAvailable', event);
    if (event.data && event.data.size > 0) {
      recordedBlobs.push(event.data);
    }
  }


  
  function downBtn(){
    const blob = new Blob(recordedBlobs, {type: 'video/webm'});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'test.webm';
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    }, 100);
  };