<?php
// Add these at the top of your functions.php
if (!defined('ABSPATH')) exit;

// Debug function
function debug_to_console($data) {
    $output = json_encode($data);
    error_log($output);
}

// Register REST API endpoints
add_action('rest_api_init', function () {
    register_rest_route('library-occupancy/v1', '/libraries/occupancy', array(
        'methods' => 'GET',
        'callback' => 'get_libraries_occupancy',
        'permission_callback' => '__return_true'
    ));
});

function get_libraries_occupancy(WP_REST_Request $request) {
    $mock_data = array(
        array(
            'id' => 1,
            'name' => 'Avery Library',
            'floors' => 3,
            'current_hour_occupancy' => array(
                'status' => 'Open',
                'occupancyAvg' => 65,
                '1F' => 70,
                '2F' => 60,
                '3F' => 65,
                'mostFree' => '2F'
            )
        ),
        array(
            'id' => 2,
            'name' => 'Barnard Library',
            'floors' => 6,
            'current_hour_occupancy' => array(
                'status' => 'Open',
                'occupancyAvg' => 75,
                '1F' => 80,
                '2F' => 75,
                'mostFree' => '2F'
            )
        )
    );

    debug_to_console($mock_data); // Debug the data

    return rest_ensure_response($mock_data);
}

function enqueue_library_occupancy_block() {
    wp_enqueue_script(
        'library-occupancy-block',
        get_template_directory_uri() . '/path/to/block.js',
        array('wp-blocks', 'wp-element', 'react')
    );

    wp_enqueue_style(
        'library-occupancy-styles',
        get_template_directory_uri() . '/path/to/style.css'
    );
}
add_action('enqueue_block_editor_assets', 'enqueue_library_occupancy_block');