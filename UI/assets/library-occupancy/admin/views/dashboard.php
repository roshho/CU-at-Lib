<?php
if (!defined('ABSPATH')) exit;
?>

<div class="wrap">
    <h1>Library Occupancy Dashboard</h1>
    
    <div class="dashboard-grid">
        <?php
        $libraries = fetch_library_data(); // From your functions.php
        if ($libraries && is_array($libraries)): 
            foreach ($libraries as $library): 
                $occupancy = $library['current_hour_occupancy'];
                $status = $occupancy['status'];
        ?>
            <div class="library-card">
                <div class="library-header">
                    <h2><?php echo esc_html($library['name']); ?></h2>
                    <span class="status-badge <?php echo strtolower($status); ?>">
                        <?php echo esc_html($status); ?>
                    </span>
                </div>

                <div class="occupancy-info">
                    <div class="occupancy-bar">
                        <div class="occupancy-fill" 
                             style="width: <?php echo esc_attr($occupancy['occupancyAvg']); ?>%">
                            <?php echo esc_html($occupancy['occupancyAvg']); ?>% Occupied
                        </div>
                    </div>
                </div>

                <div class="library-details">
                    <p>Most Available: <?php echo esc_html($occupancy['mostFree']); ?></p>
                </div>
            </div>
        <?php 
            endforeach;
        else:
        ?>
            <p>No library data available at the moment.</p>
        <?php endif; ?>
    </div>
</div>