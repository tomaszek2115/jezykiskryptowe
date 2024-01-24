document.addEventListener('DOMContentLoaded', function () {
    var tbody = document.querySelector('#fileTable tbody');

    fetch('image_names.txt')
        .then(responseImage => responseImage.text())
        .then(dataImage => {
            var imageNames = dataImage.split('\n');

            imageNames = imageNames.filter(function(name) {
                return name.trim() !== '';
            });

            fetch('input.txt')
                .then(responseInput => responseInput.text())
                .then(dataInput => {
                    var fileNames = dataInput.split('\n');

                    fileNames = fileNames.filter(function(name) {
                        return name.trim() !== '';
                    });

                    var minLength = Math.min(imageNames.length, fileNames.length);

                    for (var index = 0; index < minLength; index++) {
                        var imageName = imageNames[index].trim();
                        var fileName = fileNames[index].trim();

                        var row = document.createElement('tr');

                        var fileNameCell = document.createElement('td');
                        fileNameCell.textContent = fileName;
                        row.appendChild(fileNameCell);

                        var imageCell = document.createElement('td');
                        var image = document.createElement('img');
                        image.src = 'output/' + imageName;
                        image.alt = 'Image ' + (index + 1);
                        image.width = 300;
                        image.height = 300;
                        imageCell.appendChild(image);
                        row.appendChild(imageCell);

                        tbody.appendChild(row);
                    }
                })
                .catch(error => console.error('Error fetching input.txt:', error));
        })
        .catch(error => console.error('Error fetching image_names.txt:', error));
});
