const { registerBlockType } = wp.blocks;
const { useState, useEffect } = wp.element;
const { Placeholder, Spinner } = wp.components;

document.addEventListener('DOMContentLoaded', function() {
    const libraryIds = [1, 2, 3, 4, 5, 6, 7, 8];
    const libraryNames = {
        1: 'Avery Library',
        2: 'Barnard Library', 
        3: 'Burke Library',
        4: 'Business Library',
        5: 'Butler Library',
        6: 'Lehman Library',
        7: 'Science Library', 
        8: 'Teachers Library'
    };

    libraryIds.forEach(id => {
        const blockName = `library-occupancy/library-${id}-detailed`;

        registerBlockType(blockName, {
            title: `${libraryNames[id]} Detailed View`,
            icon: 'building',
            category: 'widgets',
            supports: {
                align: ['wide', 'full']
            },
            attributes: {
                align: {
                    type: 'string',
                    default: 'wide'
                },
                libraryUrl: {
                    type: 'string',
                    default: ''
                }
            },

            edit: function(props) {
                const [libraryData, setLibraryData] = React.useState(null);
                const [loading, setLoading] = React.useState(true);
                const [libraryUrl, setLibraryUrl] = React.useState('');

                React.useEffect(() => {
                    // Fetch both library data and URL
                    Promise.all([
                        fetch(`http://localhost:5000/libraries/${id}/occupancy`),
                        fetch(`/wp-json/library-occupancy/v1/library-url/${id}`)
                    ])
                    .then(([occupancyRes, urlRes]) => Promise.all([
                        occupancyRes.json(),
                        urlRes.json()
                    ]))
                    .then(([occupancyData, urlData]) => {
                        setLibraryData(occupancyData);
                        setLibraryUrl(urlData.url);
                        props.setAttributes({ libraryUrl: urlData.url });
                        setLoading(false);
                    })
                    .catch(err => {
                        console.error('Error fetching data:', err);
                        setLoading(false);
                    });
                }, []);

                if (loading) {
                    return wp.element.createElement('div', { className: 'loading' }, 'Loading...');
                }

                if (!libraryData) {
                    return wp.element.createElement('div', { className: 'error' }, 'Error loading library data');
                }

                const currentOccupancy = libraryData.current_hour_occupancy;
                
                const getOccupancyClass = (percentage) => {
                    percentage = parseFloat(percentage);
                    if (percentage >= 70) return 'occupancy-high';
                    if (percentage >= 40) return 'occupancy-medium';
                    return 'occupancy-low';
                };

                function getOrdinalSuffix(number) {
                    const j = number % 10,
                          k = number % 100;
                    if (j == 1 && k != 11) return "st";
                    if (j == 2 && k != 12) return "nd";
                    if (j == 3 && k != 13) return "rd";
                    return "th";
                }

                const floorRows = Object.entries(currentOccupancy)
                    .filter(([key]) => key.match(/^\d+F$/))
                    .map(([floor, occupancy], index) => {
                        const floorNumber = floor.replace('F', '');
                        return wp.element.createElement('tr', { key: `floor-row-${index}` }, [
                            wp.element.createElement('td', { key: `floor-name-${index}` }, 
                                `${floorNumber}${getOrdinalSuffix(floorNumber)} Floor`
                            ),
                            wp.element.createElement('td', { key: `floor-occupancy-${index}` },
                                wp.element.createElement('div', { 
                                    className: 'occupancy-bar-container',
                                    key: `bar-container-${index}`
                                }, [
                                    wp.element.createElement('div', {
                                        className: `occupancy-progress ${getOccupancyClass(occupancy)}`,
                                        key: `bar-progress-${index}`,
                                        style: {
                                            width: `${occupancy}%`
                                        }
                                    }),
                                    wp.element.createElement('div', {
                                        className: 'occupancy-text',
                                        key: `bar-text-${index}`
                                    }, `${occupancy}% Full`)
                                ])
                            )
                        ]);
                    });

                const blockContent = wp.element.createElement(
                    'div',
                    { 
                        className: 'wp-block-library-occupancy-detailed',
                        'data-library-id': id
                    },
                    [
                        wp.element.createElement('table', {
                            className: 'occupancy-table',
                            key: 'table'
                        }, [
                            wp.element.createElement('thead', { key: 'thead' },
                                wp.element.createElement('tr', { key: 'thead-row'}, [
                                    wp.element.createElement('th', { key: 'header-floor' }, 'Each Floor'),
                                    wp.element.createElement('th', { key: 'header-occupancy' }, 'Seat Occupancy')
                                ])
                                ),
                                wp.element.createElement('tbody', { key: 'tbody' }, floorRows)
                            ]),
    
                            wp.element.createElement('div', {
                                className: 'best-floor',
                                key: 'best-floor'
                            }, [
                                'Best Floor: ',
                                wp.element.createElement('span', {
                                    className: 'best-floor-value',
                                    key: 'best-floor-value'
                                }, `${currentOccupancy.mostFree}`)
                            ]),
    
                            wp.element.createElement('div', {
                                className: 'library-hours',
                                key: 'hours'
                            }, `Hours: ${libraryData.hours}`)
                        ]
                    );
    
                    return libraryUrl ? 
                        wp.element.createElement(
                            'a',
                            { 
                                href: libraryUrl,
                                className: 'wp-block-library-occupancy-detailed-wrapper library-link'
                            },
                            blockContent
                        ) : blockContent;
                },
    
                save: function() {
                    return null;
                }
            });
        });
    });