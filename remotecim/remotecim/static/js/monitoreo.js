function handleMediaStream(stream, videoElementId) {
    const videoElement = document.getElementById(videoElementId);
    if (videoElement) {
        videoElement.srcObject = stream;
    }
}

function handleMediaStreamError(error) {
    console.log('Error accessing media devices:', error);
}

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: { deviceId: '1daf9f733de26a770431bc64d6fda4aabd0c0679e19e9b8ce5d19db6c75f4dbf' } })
        .then(stream => handleMediaStream(stream, 'video1'))
        .catch(handleMediaStreamError);

    navigator.mediaDevices.getUserMedia({ video: { deviceId: '1f88cc771b6fb2dcc724ea3137f00297964779ad895f3291751f3960628a634e' } })
        .then(stream => handleMediaStream(stream, 'video2'))
        .catch(handleMediaStreamError);

    navigator.mediaDevices.getUserMedia({ video: { deviceId: '01d938008bbfe315751355d44391c0ce8e53075de559227f5211974ac94b0462' } })
        .then(stream => handleMediaStream(stream, 'video3'))
        .catch(handleMediaStreamError);
} else {
    console.log('getUserMedia is not supported');
}