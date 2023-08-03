fetch('../data/scan_database.json')
    .then(response => response.json())
    .then(data => {
        const shipDetailsDiv = document.getElementById('ship-details');

        for (const ship in data.ships) {
            const shipInfo = data.ships[ship];
            const shipName = ship;
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
                    subcategoryBox.className = `area-box ${areaDetails[subcategory]}`;
                    subcategoryBox.textContent = subcategory; // Set the description as the text content

                    subcategoryElement.appendChild(subcategoryBox);

                    areaElement.appendChild(subcategoryElement);
                }

                shipElement.appendChild(areaElement);
            }

            shipDetailsDiv.appendChild(shipElement);
        }
    })
    .catch(error => console.error('Error fetching JSON:', error));
