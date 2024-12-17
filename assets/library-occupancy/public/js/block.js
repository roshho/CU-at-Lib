document.addEventListener('DOMContentLoaded', function() {
    const libraryIds = [1, 2, 3, 4, 5, 6, 7, 8];

    // Regular library blocks
    libraryIds.forEach(id => {
        const blockName = `library-occupancy/library-${id}`;
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

        wp.blocks.registerBlockType(blockName, {
            title: libraryNames[id],
            icon: 'building',
            category: 'widgets',
            supports: {
                align: ['wide', 'full']
            },
            attributes: {
                align: {
                    type: 'string',
                    default: 'wide'
                }
            },

            edit: function(props) {
                const [libraryData, setLibraryData] = React.useState(null);
                const [loading, setLoading] = React.useState(true);
                const [libraryUrl, setLibraryUrl] = React.useState('');

                React.useEffect(() => {
                    // Fetch both occupancy data and URL
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

                const occupancyAvg = parseFloat(libraryData.current_hour_occupancy.occupancyAvg);
                const getOccupancyColor = () => {
                    if (occupancyAvg >= 70) return '#ef4444';
                    if (occupancyAvg >= 30) return '#fbbf24';
                    return '#10b981';
                };

                const blockContent = wp.element.createElement(
                    'div',
                    { 
                        className: 'wp-block-library-occupancy',
                        key: `library-${id}`,
                        'data-library-id': id
                    },
                    [
                        // Library Name
                        wp.element.createElement('div', {
                            className: 'library-name',
                            key: 'library-name'
                        }, libraryData.name),
            
                        // Occupancy Information Section
                        wp.element.createElement('div', {
                            className: 'occupancy-section',
                            key: 'occupancy-section'
                        }, [
                            // Percentage
                            wp.element.createElement('div', {
                                className: 'percentage',
                                key: 'percentage'
                            }, `${occupancyAvg}% Full`),
            
                            // Bar
                            wp.element.createElement('div', {
                                className: 'bar-container',
                                key: 'bar-container'
                            }, 
                            wp.element.createElement('div', {
                                className: 'bar-fill',
                                key: 'bar-fill',
                                style: {
                                    width: `${occupancyAvg}%`,
                                    backgroundColor: getOccupancyColor()
                                }
                            })),
            
                            // Most Free Floor
                            wp.element.createElement('div', {
                                className: 'floor-info',
                                key: 'floor-info'
                            }, [
                                wp.element.createElement('span', {
                                    className: 'floor-number',
                                    key: 'floor-number'
                                }, libraryData.current_hour_occupancy.mostFree),
                                wp.element.createElement('span', {
                                    className: 'floor-text',
                                    key: 'floor-text'
                                }, ' is most free')
                            ])
                        ]),
            
                        // Hours
                        wp.element.createElement('div', {
                            className: 'hours',
                            key: 'hours'
                        }, `Hours: ${libraryData.hours}`)
                    ]
                );

                return libraryUrl ? 
                    wp.element.createElement(
                        'a',
                        { 
                            href: libraryUrl,
                            className: 'wp-block-library-occupancy-wrapper library-link'
                        },
                        blockContent
                    ) : blockContent;
            },

            save: function() {
                return null;
            }
        });
    });

    // Least Occupied Library Blocks
    [
        { name: 'least-occupied', title: 'Least Occupied Library' },
        { name: 'second-least-occupied', title: 'Second Least Occupied Library' },
        { name: 'third-least-occupied', title: 'Third Least Occupied Library' }
    ].forEach(blockConfig => {
        wp.blocks.registerBlockType(`library-occupancy/${blockConfig.name}`, {
            title: blockConfig.title,
            icon: 'chart-line',
            category: 'widgets',
            supports: {
                align: ['wide', 'full', 'center'],
                alignment: true
            },
            attributes: {
                align: {
                    type: 'string',
                    default: 'center'
                }
            },

            edit: function(props) {
                const [libraryData, setLibraryData] = React.useState(null);
                const [loading, setLoading] = React.useState(true);
                const [libraryUrl, setLibraryUrl] = React.useState('');

                React.useEffect(() => {
                    fetch(`http://localhost:5000/libraries/${blockConfig.name}`)
                        .then(res => res.json())
                        .then(data => {
                            setLibraryData(data);
                            return fetch(`/wp-json/library-occupancy/v1/library-url/${data.id}`)
                                .then(res => res.json())
                                .then(urlData => {
                                    setLibraryUrl(urlData.url);
                                    setLoading(false);
                                });
                        })
                        .catch(err => {
                            console.error(`Error fetching data for ${blockConfig.title}:`, err);
                            setLoading(false);
                        });
                }, []);

                if (loading) {
                    return wp.element.createElement('div', { className: 'loading' }, 'Loading...');
                }

                if (!libraryData) {
                    return wp.element.createElement('div', { className: 'error' }, 'Error loading library data');
                }

                const occupancyAvg = parseFloat(libraryData.current_hour_occupancy.occupancyAvg);
                const getOccupancyColor = () => {
                    if (occupancyAvg >= 70) return '#ef4444';
                    if (occupancyAvg >= 30) return '#fbbf24';
                    return '#10b981';
                };

                const blockContent = wp.element.createElement(
                    'div',
                    { 
                        className: 'wp-block-library-occupancy',
                        'data-library-id': libraryData.id
                    },
                    [
                        // Block Title
                        wp.element.createElement('div', {
                            className: 'block-title',
                            key: 'block-title',
                            style: { 
                                fontSize: '14px',
                                color: '#6b7280',
                                marginBottom: '8px'
                            }
                        }, blockConfig.title),

                        // Library Name
                        wp.element.createElement('div', {
                            className: 'library-name',
                            key: 'library-name'
                        }, libraryData.name),
        
                        // Occupancy Information Section
                        wp.element.createElement('div', {
                            className: 'occupancy-section',
                            key: 'occupancy-section'
                        }, [
                            wp.element.createElement('div', {
                                className: 'percentage',
                                key: 'percentage'
                            }, `${occupancyAvg}% Full`),
        
                            wp.element.createElement('div', {
                                className: 'bar-container',
                                key: 'bar-container'
                            }, 
                            wp.element.createElement('div', {
                                className: 'bar-fill',
                                key: 'bar-fill',
                                style: {
                                    width: `${occupancyAvg}%`,
                                    backgroundColor: getOccupancyColor()
                                }
                            })),
        
                            wp.element.createElement('div', {
                                className: 'floor-info',
                                key: 'floor-info'
                            }, [
                                wp.element.createElement('span', {
                                    className: 'floor-number',
                                    key: 'floor-number'
                                }, libraryData.current_hour_occupancy.mostFree),
                                wp.element.createElement('span', {
                                    className: 'floor-text',
                                    key: 'floor-text'
                                }, ' is most free')
                            ])
                        ]),
        
                        // Hours
                        wp.element.createElement('div', {
                            className: 'hours',
                            key: 'hours'
                        }, `Hours: ${libraryData.hours}`)
                    ]
                );

                return libraryUrl ? 
                    wp.element.createElement(
                        'a',
                        { 
                            href: libraryUrl,
                            className: 'wp-block-library-occupancy-wrapper library-link'
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