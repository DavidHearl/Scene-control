fetch('../data/scan_database.json')
    .then(response => response.json())
    .then(data => {
        const shipDetailsDiv = document.getElementById('ship-details');
        const shipDropdown = document.getElementById('ship-dropdown');

        // Create the dropdown options for each ship
        for (const ship in data.ships) {
            const option = document.createElement('option');
            option.value = ship;
            option.textContent = `${ship} (Number: ${data.ships[ship].number})`;
            shipDropdown.appendChild(option);
        }

        // Function to update ship details when a ship is selected from the dropdown
        const updateShipDetails = () => {
            const selectedShip = shipDropdown.value;
            shipDetailsDiv.innerHTML = ''; // Clear previous ship details

            const shipInfo = data.ships[selectedShip];
            const shipName = selectedShip;
            const shipNumber = shipInfo.number;
            const areas = shipInfo.areas;

            const shipElement = document.createElement('div');
            shipElement.className = 'container-fluid ship-section mb-4';

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

                    // Set class based on status, use "No Data" for [No Data]
                    subcategoryBox.className = `area-box ${status === false ? 'No Data' : status}`;

                    subcategoryBox.textContent = subcategory; // Set the description as the text content

                    subcategoryElement.appendChild(subcategoryBox);

                    areaElement.appendChild(subcategoryElement);
                }

                shipElement.appendChild(areaElement);
            }

            shipDetailsDiv.appendChild(shipElement);
        };

        // Add event listener to the ship dropdown to update ship details
        shipDropdown.addEventListener('change', updateShipDetails);

        // Initial update of ship details for the default selected ship
        updateShipDetails();
    })
    .catch(error => console.error('Error fetching JSON:', error));
