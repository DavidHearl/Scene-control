// Fetch the data and populate the ships and companies filter dropdowns
fetch('../data/scan_database.json')
    .then(response => response.json())
    .then(data => {
        const shipFilter = document.getElementById('ship-filter');
        const companyFilter = document.getElementById('company-filter');
        const numberSearch = document.getElementById('number-search');

        // Initialize arrays to store unique ship names and company names
        const shipNames = [];
        const companyNames = [];

        // Loop through the data and extract ship and company names
        for (const ship in data.ships) {
            const shipInfo = data.ships[ship];
            const shipName = ship;
            const companyName = shipInfo.company;

            // Add ship and company names to arrays if not already present
            if (!shipNames.includes(shipName)) {
                shipNames.push(shipName);
            }

            if (!companyNames.includes(companyName)) {
                companyNames.push(companyName);
            }
        }

        // Sort shipNames alphabetically
        shipNames.sort();

        // Populate ship filter dropdown options
        for (const shipName of shipNames) {
            const option = document.createElement('option');
            option.textContent = shipName;
            shipFilter.appendChild(option);
        }

        // Populate company filter dropdown options
        for (const companyName of companyNames) {
            const option = document.createElement('option');
            option.textContent = companyName;
            companyFilter.appendChild(option);
        }

        // Add event listeners for ship and company filters
        shipFilter.addEventListener('change', applyFilters);
        companyFilter.addEventListener('change', applyFilters);
        numberSearch.addEventListener('input', applyFilters);

        // Apply the filters on initial page load
        applyFilters();

        function applyFilters() {
            const selectedShip = shipFilter.value;
            const selectedCompany = companyFilter.value;
            const searchNumber = numberSearch.value.toLowerCase();

            const shipDetailsDiv = document.getElementById('ship-details');
            shipDetailsDiv.innerHTML = '';

            for (const ship in data.ships) {
                const shipInfo = data.ships[ship];
                const shipName = ship;
                const shipNumber = shipInfo.number;
                const companyName = shipInfo.company;
                const areas = shipInfo.areas;

                // Check if the ship and company match the selected filters
                const shipMatched = !selectedShip || selectedShip === shipName;
                const companyMatched = !selectedCompany || selectedCompany === companyName;
                const numberMatched = !searchNumber || shipNumber.toLowerCase().includes(searchNumber);

                if (shipMatched && companyMatched && numberMatched) {
                    const areas = shipInfo.areas;

                    const shipElement = document.createElement('div');
                    shipElement.className = 'container-fluid ship-section mb-4';

                    // Create a row for ship name and number
                    const shipRow = document.createElement('div');
                    shipRow.className = 'row mb-2';

                    const shipNameElement = document.createElement('div');
                    shipNameElement.className = 'col';
                    const shipNameHeader = document.createElement('h3');
                    shipNameHeader.textContent = shipName;
                    shipNameElement.appendChild(shipNameHeader);
                    shipRow.appendChild(shipNameElement);

                    const shipNumberElement = document.createElement('div');
                    shipNumberElement.className = 'col';
                    const shipNumberHeader = document.createElement('h3');
                    shipNumberHeader.textContent = `CN: ${shipNumber}`;
                    shipNumberElement.appendChild(shipNumberHeader);
                    shipRow.appendChild(shipNumberElement);

                    const areaCountElement = document.createElement('div');
                    areaCountElement.className = 'col';
                    const areaCountText = document.createElement('h3');
                    areaCountText.textContent = `Areas: ${Object.keys(areas).length}`;
                    areaCountElement.appendChild(areaCountText);
                    shipRow.appendChild(areaCountElement);

                    shipElement.appendChild(shipRow);

                    for (const area in areas) {
                        const areaDetails = areas[area];
                        const subcategoryValues = Object.values(areaDetails);
                        const isAllSameValue = subcategoryValues.every(value => value === subcategoryValues[0]);
        
                        const areaElement = document.createElement('div');
                        areaElement.className = 'area row mb-2';
        
                        const areaNameElement = document.createElement('div');
                        areaNameElement.className = 'col-lg-4';
        
                        const areaNameList = document.createElement('ul');
                        areaNameList.className = '';
        
                        const areaNameListItem = document.createElement('li');
                        areaNameList.className = 'area-name';
                        areaNameListItem.textContent = area;
        
                        areaNameList.appendChild(areaNameListItem);
                        areaNameElement.appendChild(areaNameList);
                        areaElement.appendChild(areaNameElement);
        
                        if (isAllSameValue) {
                            const subcategoryElement = document.createElement('div');
                            subcategoryElement.className = 'col-lg-8 area-subcategory';
                            const status = subcategoryValues[0];
                            const statusClass = status.replace(/\s/g, ''); // Remove spaces from status for class name
                            subcategoryElement.className = `col-lg-8 area-box ${status === 'No Data' ? 'NoData' : statusClass}`;
                            subcategoryElement.textContent = `All ${status}`;
                            areaElement.appendChild(subcategoryElement);
                        } else {
                            for (const subcategory in areaDetails) {
                                const subcategoryElement = document.createElement('div');
                                subcategoryElement.className = 'col-md-6 col-lg-1 area-subcategory';

                                const subcategoryBox = document.createElement('div');

                                const status = areaDetails[subcategory];
                                const statusClass = status.replace(/\s/g, ''); // Remove spaces from status for class name

                                // Set class based on status, use "NoData" for [No Data]
                                subcategoryBox.className = `area-box ${status === 'No Data' ? 'NoData' : statusClass}`;
                                subcategoryBox.textContent = subcategory; // Set the description as the text content

                                subcategoryElement.appendChild(subcategoryBox);

                                areaElement.appendChild(subcategoryElement);
                            }
                        }

                        shipElement.appendChild(areaElement);
                    }

                    shipDetailsDiv.appendChild(shipElement);
                }
            }
        }

    })
    .catch(error => console.error('Error fetching JSON:', error));
