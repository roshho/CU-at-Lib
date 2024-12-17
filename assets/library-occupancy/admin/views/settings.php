<?php
// admin/admin.php
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

function library_occupancy_settings_page() {
    $library_urls = get_option('library_occupancy_urls', array());
    
    if (isset($_POST['submit'])) {
        check_admin_referer('library_occupancy_update');
        
        $library_urls = array();
        for ($i = 1; $i <= 8; $i++) {
            $library_urls[$i] = sanitize_url($_POST['library_url_' . $i]);
        }
        update_option('library_occupancy_urls', $library_urls);
        echo '<div class="updated"><p>Settings saved.</p></div>';
    }
    
    ?>
    <div class="wrap">
        <h1>Library Occupancy Settings</h1>
        <form method="post" action="">
            <?php wp_nonce_field('library_occupancy_update'); ?>
            <table class="form-table">
                <?php
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
                
                foreach ($libraries as $id => $name) {
                    $url = isset($library_urls[$id]) ? $library_urls[$id] : '';
                    ?>
                    <tr>
                        <th scope="row"><label for="library_url_<?php echo $id; ?>"><?php echo esc_html($name); ?> URL</label></th>
                        <td>
                            <input type="url" 
                                   name="library_url_<?php echo $id; ?>" 
                                   id="library_url_<?php echo $id; ?>" 
                                   value="<?php echo esc_url($url); ?>" 
                                   class="regular-text">
                        </td>
                    </tr>
                    <?php
                }
                ?>
            </table>
            <p class="submit">
                <input type="submit" name="submit" id="submit" class="button button-primary" value="Save Changes">
            </p>
        </form>
    </div>
    <?php
}