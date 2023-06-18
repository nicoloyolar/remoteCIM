function handleMediaStream(stream) {
    const videoElements = document.querySelectorAll('.monitor-video');
    videoElements.forEach(function(videoElement) {
        videoElement.srcObject = stream;
    });
}

function handleMediaStreamError(error) {
    console.log('Error accessing media devices:', error);
}

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(handleMediaStream)
        .catch(handleMediaStreamError);
} else {
    console.log('getUserMedia is not supported');
}