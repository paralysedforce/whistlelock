var recorder, audioContext;

function setup(){
    audioContext = new AudioContext();
    audioContext.sampleRate = 44100;

    navigator.mediaDevices.getUserMedia({'audio': true}).then(function(stream){
        var input = audioContext.createMediaStreamSource(stream);
        recorder = new Recorder(input);
    }).catch(function(err){ console.log(err) });
}

function startRecording(button){
    recorder && recorder.record();
    button.disabled = true;
    button.nextElementSibling.disabled = false;
}

function stopRecording(button){
    recorder && recorder.stop();
    button.disabled = true;
    button.previousElementSibling.disabled = false;

    sendWAVToServer();
    recorder.clear();
}

function sendWAVToServer(){
    recorder && recorder.exportWAV(function(blob){
        /* Process this blob somehow */
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function(){
            if (xhr.readyState == 4 && xhr.status == 200){
                alert("everything worked!");
                var resp = JSON.parse(xhr.responseText);
                console.log("Certainty: " + resp.certainty.toString());
            }
        };

        var username = document.getElementById('username').value;
        var whistle;

        var fd = new FormData();
        fd.append('fname', 'test.wav');
        fd.append('data', blob);
        xhr.send(fd);


        /*
        var reader = new FileReader();
        reader.addEventListener("loadend", function(e){
            whistle = reader.result;
            data = {'data': whistle, 'username': username};
            xhr.send(JSON.stringify(data));
        });

        reader.readAsArrayBuffer(blob);
        */
    });
}


window.onload = setup;
