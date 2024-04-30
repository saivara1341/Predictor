// script.js

document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const form = document.querySelector('form');

    // Display selected file name
    fileInput.addEventListener('change', function() {
        const fileName = this.files[0].name;
        const fileInfo = document.createElement('p');
        fileInfo.textContent = `Selected file: ${fileName}`;
        form.appendChild(fileInfo);
    });

    // Highlight selected plot type
    const plotTypeSelect = document.querySelector('#plot_type');
    plotTypeSelect.addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex].textContent;
        console.log(selectedOption);
    });
});
