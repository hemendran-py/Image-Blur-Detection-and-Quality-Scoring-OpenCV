document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('imageInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select an image file.');
        return;
    }

    // Preview the image
    const reader = new FileReader();
    reader.onload = function (e) {
        const preview = document.getElementById('preview');
        preview.innerHTML = '<img src="' + e.target.result + '" alt="Image Preview">';
    };
    reader.readAsDataURL(file);

    // Send the image to the backend
    const formData = new FormData();
    formData.append('image', file);

    fetch('http://localhost:5000/score', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            const result = document.getElementById('result');
            if (data.error) {
                result.innerHTML = '<p class="error">Error: ' + data.error + '</p>';
            } else {
                result.innerHTML = '<p class="success">Score: ' + data.score.toFixed(2) + '<br>Category: ' + data.category + '</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const result = document.getElementById('result');
            result.innerHTML = '<p class="error">Error: Unable to process the image. Please try again.</p>';
        });
});