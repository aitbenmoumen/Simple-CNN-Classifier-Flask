// DOM Elements
const uploadForm = document.getElementById('uploadForm');
const fileInput = document. getElementById('fileInput');
const fileName = document.getElementById('fileName');
const imagePreview = document.getElementById('imagePreview');
const preview = document.getElementById('preview');
const predictBtn = document.getElementById('predictBtn');
const loading = document.getElementById('loading');
const results = document.getElementById('results');
const errorDiv = document.getElementById('error');
const errorMessage = document.getElementById('errorMessage');
const tryAgainBtn = document.getElementById('tryAgain');
const dismissErrorBtn = document.getElementById('dismissError');

// File input change event
fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    
    if (file) {
        // Update file name
        fileName.textContent = file.name;
        
        // Show image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            imagePreview.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
        
        // Enable predict button
        predictBtn.disabled = false;
    }
});

// Form submit event
uploadForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Hide previous results and errors
    results.classList.add('hidden');
    errorDiv.classList.add('hidden');
    
    // Show loading
    loading.classList.remove('hidden');
    
    // Prepare form data
    const formData = new FormData();
    formData.append('file', fileInput. files[0]);
    
    try {
        // Send prediction request
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        // Hide loading
        loading.classList.add('hidden');
        
        if (response.ok) {
            // Display results
            displayResults(data);
        } else {
            // Display error
            showError(data.error || 'An error occurred during prediction');
        }
    } catch (error) {
        loading.classList.add('hidden');
        showError('Network error: ' + error.message);
    }
});

// Display prediction results
function displayResults(data) {
    // Set predicted class and confidence
    document.getElementById('predictedClass').textContent = data.predicted_class;
    document.getElementById('confidence'). textContent = data.confidence + '%';
    
    // Display all predictions
    const allPredictionsDiv = document.getElementById('allPredictions');
    allPredictionsDiv.innerHTML = '';
    
    // Sort predictions by confidence
    const sortedPredictions = Object.entries(data.all_predictions)
        .sort((a, b) => b[1] - a[1]);
    
    sortedPredictions.forEach(([className, percentage]) => {
        const item = document.createElement('div');
        item.className = 'prediction-item';
        item.innerHTML = `
            <div>
                <div class="name">${className}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${percentage}%"></div>
                </div>
            </div>
            <div class="percentage">${percentage. toFixed(2)}%</div>
        `;
        allPredictionsDiv.appendChild(item);
    });
    
    // Show results
    results.classList.remove('hidden');
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorDiv. classList.remove('hidden');
}

// Try again button
tryAgainBtn.addEventListener('click', function() {
    // Reset form
    uploadForm.reset();
    fileName.textContent = 'Choose an image...';
    imagePreview.classList.add('hidden');
    results.classList.add('hidden');
    predictBtn.disabled = true;
});

// Dismiss error button
dismissErrorBtn.addEventListener('click', function() {
    errorDiv.classList.add('hidden');
});