$(document).ready(function() {
    $('.upload-btn-wrapper input[type=file]').change(function() {
        var filename = $(this).val().split('\\').pop();
        $('.upload-btn-wrapper .btn').html(filename);
    });
});

function analyzeAudio() {
    const audioInput = document.getElementById('audioInput');
    const resultDiv = document.getElementById('result');

    const formData = new FormData();
    formData.append('audio', audioInput.files[0]);

    $.ajax({
        type: 'POST',
        url: '/analyze_audio',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
            if (data.error) {
                resultDiv.innerHTML = `Error: ${data.error}`;
            } else {
                resultDiv.innerHTML = `Text: ${data.text}`;
            }
        },
        error: function () {
            resultDiv.innerHTML = 'Error analyzing audio.';
        }
    });
}
