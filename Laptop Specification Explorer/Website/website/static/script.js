function fetchLaptops() {
    const brandId = document.getElementById('brand').value;
    const processorId = document.getElementById('processor').value;
    const gpuId = document.getElementById('gpu').value;
    const categoryId = document.getElementById('category').value;

    const url = `/get_laptops?brand_id=${brandId}&processor_id=${processorId}&gpu_id=${gpuId}&category_id=${categoryId}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const laptopList = document.getElementById('laptop-list');
            laptopList.innerHTML = ''; // Clear previous results
            data.forEach(laptop => {
                const laptopItem = document.createElement('div');
                laptopItem.innerHTML = `
                    <h3>${laptop[1]} (${laptop[2]})</h3>
                    <p>GPU: ${laptop[3]}</p>
                    <p>Category: ${laptop[4]}</p>
                `;
                laptopList.appendChild(laptopItem);
            });
        })
        .catch(error => console.error('Error fetching laptops:', error));
}

// Function to populate dropdowns for brands, processors, GPUs, and categories
function populateDropdowns() {
    fetch('/get_brands')
        .then(response => response.json())
        .then(data => {
            const brandSelect = document.getElementById('brand');
            data.forEach(brand => {
                const option = document.createElement('option');
                option.value = brand[0]; // Assuming brand_id is the first column
                option.textContent = brand[1]; // Assuming brand_name is the second column
                brandSelect.appendChild(option);
            });
        });

    fetch('/get_processors')
        .then(response => response.json())
        .then(data => {
            const processorSelect = document.getElementById('processor');
            data.forEach(processor => {
                const option = document.createElement('option');
                option.value = processor[0]; // Assuming processor_id is the first column
                option.textContent = processor[1]; // Assuming processor_name is the second column
                processorSelect.appendChild(option);
            });
        });

    fetch('/get_gpus')
        .then(response => response.json())
        .then(data => {
            const gpuSelect = document.getElementById('gpu');
            data.forEach(gpu => {
                const option = document.createElement('option');
                option.value = gpu[0]; // Assuming gpu_id is the first column
                option.textContent = gpu[1]; // Assuming gpu_brand is the second column
                gpuSelect.appendChild(option);
            });
        });

    fetch('/get_categories')
        .then(response => response.json())
        .then(data => {
            const categorySelect = document.getElementById('category');
            data.forEach(category => {
                const option = document.createElement('option');
                option.value = category[0]; // Assuming category_id is the first column
                option.textContent = category[1]; // Assuming category_name is the second column
                categorySelect.appendChild(option);
            });
        });
}

// Call populateDropdowns on page load
window.onload = populateDropdowns;