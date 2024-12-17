<?php
/*
Plugin Name: Library Occupancy
Description: Display real-time library occupancy information
Version: 1.0
Author: Your Name
*/

if (!defined('ABSPATH')) exit;

// Load required files
require_once plugin_dir_path(__FILE__) . 'includes/functions.php';
require_once plugin_dir_path(__FILE__) . 'admin/admin.php';

function library_occupancy_init() {
    // Register individual library blocks
    $library_ids = range(1, 8);
    
    foreach ($library_ids as $id) {
        // Register small block for each library
        register_block_type("library-occupancy/library-$id", array(
            'editor_script' => 'library-occupancy-editor-script',
            'editor_style'  => 'library-occupancy-editor-style',
            'style'         => 'library-occupancy-style',
            'render_callback' => 'render_library_occupancy_block',
            'attributes' => array(
                'align' => array(
                    'type' => 'string',
                    'default' => 'center'
                )
            )
        ));

        // Register detailed block for each library
        register_block_type("library-occupancy/library-$id-detailed", array(
            'editor_script' => 'library-occupancy-detailed-script',
            'editor_style'  => 'library-occupancy-editor-style',
            'style'         => 'library-occupancy-style',
            'render_callback' => 'render_library_occupancy_detailed_block',
            'attributes' => array(
                'align' => array(
                    'type' => 'string',
                    'default' => 'wide'
                )
            )
        ));
    }

    // Register least occupied library blocks
    $least_occupied_blocks = array(
        'least-occupied' => 'Least Occupied Library',
        'second-least-occupied' => 'Second Least Occupied Library',
        'third-least-occupied' => 'Third Least Occupied Library'
    );

    foreach ($least_occupied_blocks as $block_name => $title) {
        register_block_type("library-occupancy/$block_name", array(
            'editor_script' => 'library-occupancy-editor-script',
            'editor_style'  => 'library-occupancy-editor-style',
            'style'         => 'library-occupancy-style',
            'render_callback' => 'render_library_occupancy_least_occupied_block',
            'attributes' => array(
                'align' => array(
                    'type' => 'string',
                    'default' => 'center'
                )
            )
        ));
    }
}
add_action('init', 'library_occupancy_init');

function library_occupancy_register_assets() {
    // Register block editor scripts
    wp_register_script(
        'library-occupancy-editor-script',
        plugins_url('public/js/block.js', __FILE__),
        array('wp-blocks', 'wp-element', 'wp-editor', 'wp-components'),
        '1.0.0',
        true
    );

    // Register detailed block script
    wp_register_script(
        'library-occupancy-detailed-script',
        plugins_url('public/js/detailed-block.js', __FILE__),
        array('wp-blocks', 'wp-element', 'wp-editor', 'wp-components', 'react'),
        '1.0.0',
        true
    );

    // Register frontend script
    wp_register_script(
        'library-occupancy-frontend',
        plugins_url('public/js/frontend.js', __FILE__),
        array(),
        '1.0.0',
        true
    );

    // Register styles
    wp_register_style(
        'library-occupancy-editor-style',
        plugins_url('public/css/block-style.css', __FILE__),
        array()
    );

    wp_register_style(
        'library-occupancy-style',
        plugins_url('public/css/block-style.css', __FILE__),
        array()
    );

    // Enqueue block editor assets (in admin only)
    if (is_admin()) {
        wp_enqueue_script('library-occupancy-editor-script');
        wp_enqueue_script('library-occupancy-detailed-script');
        wp_enqueue_style('library-occupancy-editor-style');
    }

    // Always enqueue the frontend script and styles on the frontend
    if (!is_admin()) {
        wp_enqueue_script('library-occupancy-frontend');
        wp_enqueue_script('library-occupancy-detailed-script');
        wp_enqueue_style('library-occupancy-style');
    }
}
add_action('init', 'library_occupancy_register_assets');

// Render callback for regular library blocks
function render_library_occupancy_block($attributes, $content, $block) {
    preg_match('/library-(\d+)$/', $block->name, $matches);
    $library_id = isset($matches[1]) ? $matches[1] : '';
    
    // Get saved URLs
    $library_urls = get_option('library_occupancy_urls', array());
    $library_url = isset($library_urls[$library_id]) ? $library_urls[$library_id] : '#';
    
    // Get alignment class
    $align_class = isset($attributes['align']) ? 'align' . $attributes['align'] : 'aligncenter';
    
    ob_start();
    ?>
    <div class="wp-block-library-occupancy-wrapper <?php echo esc_attr($align_class); ?>">
        <div class="wp-block-library-occupancy" data-library-id="<?php echo esc_attr($library_id); ?>">
            <div class="library-content">
                <div class="loading">Loading library information...</div>
            </div>
        </div>
    </div>
    <?php
    return ob_get_clean();
}

// Render callback for detailed blocks
function render_library_occupancy_detailed_block($attributes, $content, $block) {
    preg_match('/library-(\d+)-detailed$/', $block->name, $matches);
    $library_id = isset($matches[1]) ? $matches[1] : '';
    
    // Get saved URLs
    $library_urls = get_option('library_occupancy_urls', array());
    $library_url = isset($library_urls[$library_id]) ? $library_urls[$library_id] : '#';
    
    // Get alignment class
    $align_class = isset($attributes['align']) ? 'align' . $attributes['align'] : 'alignwide';
    
    ob_start();
    ?>
    <div class="wp-block-library-occupancy-detailed-wrapper <?php echo esc_attr($align_class); ?>">
        <div class="wp-block-library-occupancy-detailed" data-library-id="<?php echo esc_attr($library_id); ?>">
            <div class="library-content">
                <div class="loading">Loading detailed library information...</div>
            </div>
        </div>
    </div>
    <?php
    return ob_get_clean();
}

// Render callback for least occupied blocks
function render_library_occupancy_least_occupied_block($attributes, $content, $block) {
    $block_name = $block->name;
    $endpoint = str_replace('library-occupancy/', '', $block_name);
    
    // Get alignment class
    $align_class = isset($attributes['align']) ? 'align' . $attributes['align'] : 'aligncenter';
    
    ob_start();
    ?>
    <div class="wp-block-library-occupancy-wrapper least-occupied-block <?php echo esc_attr($align_class); ?>">
        <div class="wp-block-library-occupancy" data-endpoint="<?php echo esc_attr($endpoint); ?>">
            <div class="library-content">
                <div class="loading">Loading library information...</div>
            </div>
        </div>
    </div>
    <?php
    return ob_get_clean();
}

// Register REST API endpoints
function library_occupancy_register_rest_routes() {
    register_rest_route('library-occupancy/v1', '/library-url/(?P<id>\d+)', array(
        'methods' => 'GET',
        'callback' => 'get_library_url',
        'permission_callback' => '__return_true',
        'args' => array(
            'id' => array(
                'validate_callback' => function($param) {
                    return is_numeric($param) && $param > 0 && $param <= 8;
                }
            )
        )
    ));
}
add_action('rest_api_init', 'library_occupancy_register_rest_routes');

function get_library_url($request) {
    $id = $request['id'];
    $urls = get_option('library_occupancy_urls', array());
    
    return new WP_REST_Response(array(
        'url' => isset($urls[$id]) ? $urls[$id] : ''
    ), 200);
}

// Add version to prevent caching during development
function library_occupancy_add_version($src) {
    if (strpos($src, 'block.js') !== false || 
        strpos($src, 'detailed-block.js') !== false || 
        strpos($src, 'block-style.css') !== false ||
        strpos($src, 'frontend.js') !== false) {
        $src = add_query_arg('ver', time(), $src);
    }
    return $src;
}
add_filter('script_loader_src', 'library_occupancy_add_version', 99, 1);
add_filter('style_loader_src', 'library_occupancy_add_version', 99, 1);