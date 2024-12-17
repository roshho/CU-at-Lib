document.addEventListener('DOMContentLoaded', function() {
    // Find all standard library blocks (excluding least occupied blocks)
    const libraryBlocks = document.querySelectorAll('.wp-block-library-occupancy:not([data-endpoint]), .wp-block-library-occupancy-detailed');
    
    // Find least occupied blocks separately
    const leastOccupiedBlocks = document.querySelectorAll('.least-occupied-block .wp-block-library-occupancy[data-endpoint]');
    
    // Handle regular library blocks
    libraryBlocks.forEach(block => {
        const libraryId = block.getAttribute('data-library-id');
        if (!libraryId) {
            console.error('No library ID found for block:', block);
            return;
        }

        // Show loading state
        block.querySelector('.library-content').innerHTML = '<div class="loading">Loading library information...</div>';

        // Fetch both library data and URL
        Promise.all([
            fetch(`http://localhost:5000/libraries/${libraryId}/occupancy`),
            fetch(`/wp-json/library-occupancy/v1/library-url/${libraryId}`)
        ])
        .then(([occupancyRes, urlRes]) => Promise.all([
            occupancyRes.json(),
            urlRes.json()
        ]))
        .then(([libraryData, urlData]) => {
            const isDetailed = block.classList.contains('wp-block-library-occupancy-detailed');
            const content = createBlockContent(libraryData, isDetailed);
            
            if (urlData.url) {
                const wrapper = document.createElement('a');
                wrapper.href = urlData.url;
                wrapper.className = `library-link ${isDetailed ? 'detailed-link' : ''}`;
                wrapper.innerHTML = content;
                block.innerHTML = '';
                block.appendChild(wrapper);
            } else {
                block.innerHTML = content;
            }
        })
        .catch(err => {
            console.error(`Error fetching data for library ${libraryId}:`, err);
            block.querySelector('.library-content').innerHTML = '<div class="error">Error loading library data</div>';
        });
    });

    // Handle least occupied blocks
    leastOccupiedBlocks.forEach(block => {
        const endpoint = block.getAttribute('data-endpoint');
        if (!endpoint) {
            console.error('No endpoint found for block:', block);
            return;
        }

        // Show loading state
        block.querySelector('.library-content').innerHTML = '<div class="loading">Loading library information...</div>';

        // Fetch library data from endpoint
        fetch(`http://localhost:5000/libraries/${endpoint}`)
            .then(res => res.json())
            .then(libraryData => {
                return Promise.all([
                    Promise.resolve(libraryData),
                    fetch(`/wp-json/library-occupancy/v1/library-url/${libraryData.id}`).then(res => res.json())
                ]);
            })
            .then(([libraryData, urlData]) => {
                const content = `
                    <div class="block-title" style="font-size: 14px; color: #6b7280; margin-bottom: 8px;">
                        ${getBlockTitle(endpoint)}
                    </div>
                    <div class="library-name">${libraryData.name}</div>
                    <div class="occupancy-section">
                        <div class="percentage">${parseFloat(libraryData.current_hour_occupancy.occupancyAvg)}% Full</div>
                        <div class="bar-container">
                            <div class="bar-fill" style="width: ${libraryData.current_hour_occupancy.occupancyAvg}%; 
                                background-color: ${getOccupancyColor(parseFloat(libraryData.current_hour_occupancy.occupancyAvg))};">
                            </div>
                        </div>
                        <div class="floor-info">
                            <span class="floor-number">${libraryData.current_hour_occupancy.mostFree}</span>
                            <span class="floor-text"> is most free</span>
                        </div>
                    </div>
                    <div class="hours">Hours: ${libraryData.hours}</div>
                `;
                
                if (urlData.url) {
                    const wrapper = document.createElement('a');
                    wrapper.href = urlData.url;
                    wrapper.className = 'library-link';
                    wrapper.innerHTML = content;
                    block.innerHTML = '';
                    block.appendChild(wrapper);
                } else {
                    block.innerHTML = content;
                }
            })
            .catch(err => {
                console.error(`Error fetching data for ${endpoint}:`, err);
                block.querySelector('.library-content').innerHTML = '<div class="error">Error loading library data</div>';
            });
    });
});

function createBlockContent(libraryData, isDetailed) {
    const occupancyAvg = parseFloat(libraryData.current_hour_occupancy.occupancyAvg);
    
    if (!isDetailed) {
        return `
            <div class="library-name">${libraryData.name}</div>
            <div class="occupancy-section">
                <div class="percentage">${occupancyAvg}% Full</div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: ${occupancyAvg}%; 
                        background-color: ${getOccupancyColor(occupancyAvg)};">
                    </div>
                </div>
                <div class="floor-info">
                    <span class="floor-number">${libraryData.current_hour_occupancy.mostFree}</span>
                    <span class="floor-text"> is most free</span>
                </div>
            </div>
            <div class="hours">Hours: ${libraryData.hours}</div>
        `;
    } else {
        const floorData = Object.entries(libraryData.current_hour_occupancy)
            .filter(([key]) => key.match(/^\d+F$/))
            .map(([floor, occupancy]) => {
                const floorNumber = floor.replace('F', '');
                return `
                    <tr>
                        <td>${floorNumber}${getOrdinalSuffix(floorNumber)} Floor</td>
                        <td>
                            <div class="occupancy-bar-container">
                                <div class="occupancy-progress ${getOccupancyClass(occupancy)}"
                                     style="width: ${occupancy}%;">
                                </div>
                                <div class="occupancy-text">${occupancy}% Full</div>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');

        return `
            <div class="library-content">
                <div class="library-name">${libraryData.name}</div>
                <div class="status-section">
                    <div class="status">Status: ${libraryData.current_hour_occupancy.status}</div>
                    <div class="overall-occupancy">Overall Occupancy: ${occupancyAvg}%</div>
                </div>
                <table class="occupancy-table">
                    <thead>
                        <tr>
                            <th>Each Floor</th>
                            <th>Seat Occupancy</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${floorData}
                    </tbody>
                </table>
                <div class="best-floor">
                    Best Floor: <span class="best-floor-value">${libraryData.current_hour_occupancy.mostFree}</span>
                </div>
                <div class="library-hours">Hours: ${libraryData.hours}</div>
            </div>
        `;
    }
}

function getBlockTitle(endpoint) {
    switch(endpoint) {
        case 'least-occupied':
            return 'Least Occupied Library';
        case 'second-least-occupied':
            return 'Second Least Occupied Library';
        case 'third-least-occupied':
            return 'Third Least Occupied Library';
        default:
            return '';
    }
}

function getOccupancyColor(occupancyAvg) {
    if (occupancyAvg >= 80) return '#ef4444'; // Red for high occupancy
    if (occupancyAvg >= 30) return '#fbbf24'; // Yellow for medium occupancy
    return '#10b981'; // Green for low occupancy
}

function getOccupancyClass(percentage) {
    percentage = parseFloat(percentage);
    if (percentage >= 70) return 'occupancy-high';
    if (percentage >= 40) return 'occupancy-medium';
    return 'occupancy-low';
}

function getOrdinalSuffix(number) {
    const j = number % 10,
          k = number % 100;
    if (j == 1 && k != 11) return "st";
    if (j == 2 && k != 12) return "nd";
    if (j == 3 && k != 13) return "rd";
    return "th";
}