Y_COL = 'speed_kmh_minus_service_time'
Y_TRANSFORM = 'raw'
ROW_QUERY = 'speed_kmh_minus_service_time <= 40'

X_SELECTED_RAW = [
    'onhand_order_count_start',
    'time_pressure_min',
    'is_weekend_local',
    'time_midday_peak_10_14',
    'time_evening_peak_16_20',
    'time_midnight_2_6',
    'rider_avg_orders_per_active_day',
    'rider_mean_segment_distance_m',
    'road_class_share_levelThreeRoad_lenw_mean',
    'road_class_share_secondaryRoad_lenw_mean',
    'road_class_share_nationalRoad_lenw_mean',
    'road_class_share_provincialRoad_lenw_mean',
    'curvature_deg_per_m_lenw_mean',
    'intersection_density_per_km_300m_lenw_mean',
    'betweenness_log1p_z_mean_end_lenw_mean',
    'closeness_per_km_z_mean_end_lenw_mean',
    'restaurant_shp_count_30m_lenw_mean',
    'poi_count_30m_lenw_mean',
    'poi_mix_entropy_norm_30m_lenw_mean',
]

X_SELECTED_MODEL = [
    'onhand_order_count_start',
    'time_pressure_min',
    'is_weekend_local',
    'time_midday_peak_10_14',
    'time_evening_peak_16_20',
    'time_midnight_2_6',
    'rider_avg_orders_per_active_day',
    'div1000_rider_mean_segment_distance_m',
    'road_class_share_levelThreeRoad_lenw_mean',
    'road_class_share_secondaryRoad_lenw_mean',
    'road_class_share_nationalRoad_lenw_mean',
    'road_class_share_provincialRoad_lenw_mean',
    'curvature_deg_per_m_lenw_mean',
    'intersection_density_per_km_300m_lenw_mean',
    'betweenness_log1p_z_mean_end_lenw_mean',
    'closeness_per_km_z_mean_end_lenw_mean',
    'ln1p_restaurant_shp_count_30m_lenw_mean',
    'ln1p_poi_count_30m_lenw_mean',
    'poi_mix_entropy_norm_30m_lenw_mean',
]