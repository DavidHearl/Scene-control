// Fetch the data from the "scan_database.json"
fetch('../data/scan_database.json')
    .then(response => response.json())
    .then(data => {
        // Database search filters
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

        // Sort shipNames & company names alphabetically
        shipNames.sort();
        companyNames.sort();

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
            // Variables containing filter values
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

                // Check if the ship and company match the selected filters
                const shipMatched = !selectedShip || selectedShip === shipName;
                const companyMatched = !selectedCompany || selectedCompany === companyName;
                const numberMatched = !searchNumber || shipNumber.toLowerCase().includes(searchNumber);

                if (shipMatched && companyMatched && numberMatched) {
                    const areas = shipInfo.areas;

                    // Create a div/container for each ship
                    const shipElement = document.createElement('div');
                    shipElement.className = 'container ship-section';

                    // Create a row for ship name, number and area count
                    const shipRow = document.createElement('div');
                    shipRow.className = 'row ship-title';

                    // Create the title 
                    const shipNameElement = document.createElement('div');
                    shipNameElement.className = 'col-4';
                    const shipNameHeader = document.createElement('h3');
                    shipNameHeader.textContent = shipName;
                    shipNameElement.appendChild(shipNameHeader);
                    shipRow.appendChild(shipNameElement);

                    // Create the contract number
                    const shipNumberElement = document.createElement('div');
                    shipNumberElement.className = 'col';
                    const shipNumberHeader = document.createElement('h3');
                    shipNumberHeader.textContent = `CN: ${shipNumber}`;
                    shipNumberElement.appendChild(shipNumberHeader);
                    shipRow.appendChild(shipNumberElement);

                    // Create the area count
                    const areaCountElement = document.createElement('div');
                    areaCountElement.className = 'col';
                    const areaCountText = document.createElement('h3');
                    areaCountText.textContent = `Areas: ${Object.keys(areas).length}`;
                    areaCountElement.appendChild(areaCountText);
                    shipRow.appendChild(areaCountElement);

                    shipElement.appendChild(shipRow);

                    // Create an hr element under the title block
                    const titleUnderline = document.createElement('hr');
                    titleUnderline.className= 'title-underline';
                    shipElement.appendChild(titleUnderline);

                    for (const area in areas) {
                        const areaDetails = areas[area];
                        const subcategoryValues = Object.values(areaDetails);
                        const isAllSameValue = subcategoryValues.every(value => value === subcategoryValues[0]);

                        const areaElement = document.createElement('div');
                        areaElement.className = 'row area';

                        const areaNameElement = document.createElement('div');
                        areaNameElement.className = 'col-4 area-title';

                        const areaNameParagraph = document.createElement('p');
                        areaNameParagraph.className = 'area-name';
                        areaNameParagraph.textContent = area;
                        
                        areaNameElement.appendChild(areaNameParagraph);
                        areaElement.appendChild(areaNameElement);

                        if (isAllSameValue) {
                            const subcategoryElement = document.createElement('div');
                            subcategoryElement.className = 'col-8';
                            const status = subcategoryValues[0];
                            subcategoryElement.className = `col-8 area-box-large ${status === 'NoData' ? 'NoData' : status}`;
                            subcategoryElement.textContent = `All ${status}`;
                            areaElement.appendChild(subcategoryElement);
                        } else {
                            for (const subcategory in areaDetails) {
                                const subcategoryElement = document.createElement('div');
                                subcategoryElement.className = 'col-md-6 col-lg-1 progress-box';
                        
                                const subcategoryBox = document.createElement('div');
                        
                                const status = areaDetails[subcategory];
                        
                                // Set class based on status, use "NoData" for [No Data]
                                subcategoryBox.className = `area-box ${status === 'NoData' ? 'NoData' : status}`;
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
