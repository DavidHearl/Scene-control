fetch('../data/scan_database.json')
    .then(response => response.json())
    .then(data => {
        const shipDetailsDiv = document.getElementById('ship-details');
        const shipDropdown = document.getElementById('ship-dropdown');

        // Create an option for showing all ships
        const allShipsOption = document.createElement('option');
        allShipsOption.value = '';
        allShipsOption.textContent = 'Show All Ships';
        shipDropdown.appendChild(allShipsOption);

        for (const ship in data.ships) {
            const shipInfo = data.ships[ship];
            const shipName = ship;
            const shipNumber = shipInfo.number;
            const areas = shipInfo.areas;

            const shipElement = document.createElement('div');
            shipElement.className = 'container-fluid ship-section mb-4';
            shipElement.id = ship; // Set the ID to the ship name for easier selection

            // Create a row for ship name and number
            const shipRow = document.createElement('div');
            shipRow.className = 'row mb-2';

            const shipNameElement = document.createElement('strong');
            shipNameElement.className = 'col';
            shipNameElement.textContent = `${shipName} (Number: ${shipNumber})`;
            shipRow.appendChild(shipNameElement);

            shipElement.appendChild(shipRow);

            for (const area in areas) {
                const areaDetails = areas[area];

                const areaElement = document.createElement('div');
                areaElement.className = 'area row mb-2'; // Use row class for area

                const areaNameElement = document.createElement('strong');
                areaNameElement.className = 'col-lg-4'; // Use col class for area name
                areaNameElement.textContent = area;
                areaElement.appendChild(areaNameElement);

                for (const subcategory in areaDetails) {
                    const subcategoryElement = document.createElement('div');
                    subcategoryElement.className = 'col-md-6 col-lg-1 area-subcategory'; // Use col-2 class for subcategory

                    const subcategoryBox = document.createElement('div');

                    const status = areaDetails[subcategory];

                    // Set class based on status, use "NoData" for [No Data]
                    subcategoryBox.className = `area-box ${status === 'No Data' ? 'NoData' : status}`;

                    subcategoryBox.textContent = subcategory; // Set the description as the text content

                    subcategoryElement.appendChild(subcategoryBox);

                    areaElement.appendChild(subcategoryElement);
                }

                shipElement.appendChild(areaElement);
            }

            // Add an option for each ship to the dropdown list
            const shipOption = document.createElement('option');
            shipOption.value = ship;
            shipOption.textContent = `${shipName} (Number: ${shipNumber})`;
            shipDropdown.appendChild(shipOption);

            shipDetailsDiv.appendChild(shipElement);
        }

        // Event listener for the dropdown list
        shipDropdown.addEventListener('change', function () {
            const selectedShip = shipDropdown.value;
            const shipSections = document.getElementsByClassName('ship-section');

            for (const shipSection of shipSections) {
                shipSection.style.display = shipSection.id === selectedShip || selectedShip === '' ? 'block' : 'none';
            }
        });
    })
    .catch(error => console.error('Error fetching JSON:', error));
