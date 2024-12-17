<?php
// Add menu item under Settings
function library_occupancy_add_admin_menu() {
    add_options_page(
        'Library Occupancy Settings',
        'Library Occupancy',
        'manage_options',
        'library-occupancy',
        'library_occupancy_settings_page'
    );
}
add_action('admin_menu', 'library_occupancy_add_admin_menu');

// Register settings
function library_occupancy_settings_init() {
    register_setting('library_occupancy', 'library_occupancy_urls');
}
add_action('admin_init', 'library_occupancy_settings_init');

// Settings page content
function library_occupancy_settings_page() {
    // Get saved URLs or initialize empty array
    $library_urls = get_option('library_occupancy_urls', array());
    
    // Libraries data
    $libraries = array(
        1 => 'Avery Library',
        2 => 'Barnard Library',
        3 => 'Burke Library',
        4 => 'Business Library',
        5 => 'Butler Library',
        6 => 'Lehman Library',
        7 => 'Science Library',
        8 => 'Teachers Library'
    );
    
    // Handle form submission
    if (isset($_POST['submit'])) {
        check_admin_referer('library_occupancy_update');
        
        $new_urls = array();
        foreach ($libraries as $id => $name) {
            $new_urls[$id] = sanitize_url($_POST['library_url_' . $id]);
        }
        
        update_option('library_occupancy_urls', $new_urls);
        echo '<div class="updated"><p>Settings saved successfully.</p></div>';
        
        // Update stored URLs
        $library_urls = $new_urls;
    }
    ?>
    <div class="wrap">
        <h1>Library Occupancy Settings</h1>
        <form method="post" action="">
            <?php wp_nonce_field('library_occupancy_update'); ?>
            <table class="form-table">
                <?php foreach ($libraries as $id => $name): ?>
                    <tr>
                        <th scope="row">
                            <label for="library_url_<?php echo esc_attr($id); ?>">
                                <?php echo esc_html($name); ?> URL
                            </label>
                        </th>
                        <td>
                            <input type="url" 
                                   name="library_url_<?php echo esc_attr($id); ?>" 
                                   id="library_url_<?php echo esc_attr($id); ?>" 
                                   value="<?php echo esc_url($library_urls[$id] ?? ''); ?>" 
                                   class="regular-text">
                        </td>
                    </tr>
                <?php endforeach; ?>
            </table>
            <p class="submit">
                <input type="submit" name="submit" id="submit" class="button button-primary" value="Save Changes">
            </p>
        </form>
    </div>
    <?php
}