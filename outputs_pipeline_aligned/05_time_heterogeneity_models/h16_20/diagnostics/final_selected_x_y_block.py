Y_COL = 'speed_kmh'
Y_TRANSFORM = 'raw'
ROW_QUERY = 'speed_kmh <= 40 and start_hour_local >= 16 and start_hour_local < 20'

X_SELECTED_RAW = [
    'onhand_order_count_start',
    'time_pressure_min',
    'is_weekend_local',
    'rider_avg_orders_per_active_day',
    'full_time',
    'rider_mean_segment_distance_m',
    'road_class_share_levelThreeRoad_lenw_mean',
    'road_class_share_secondaryRoad_lenw_mean',
    'road_class_share_nationalRoad_lenw_mean',
    'road_class_share_provincialRoad_lenw_mean',
    'curvature_deg_per_m_lenw_mean',
    'intersection_density_per_km_300m_lenw_mean',
    'betweenness_log1p_z_mean_end_lenw_mean',
    'closeness_per_km_z_mean_end_lenw_mean',
    'poi_count_30m_lenw_mean',
    'poi_mix_entropy_norm_30m_lenw_mean',
]

X_SELECTED_MODEL = [
    'onhand_order_count_start',
    'time_pressure_min',
    'is_weekend_local',
    'rider_avg_orders_per_active_day',
    'full_time',
    'div1000_rider_mean_segment_distance_m',
    'road_class_share_levelThreeRoad_lenw_mean',
    'road_class_share_secondaryRoad_lenw_mean',
    'road_class_share_nationalRoad_lenw_mean',
    'road_class_share_provincialRoad_lenw_mean',
    'curvature_deg_per_m_lenw_mean',
    'intersection_density_per_km_300m_lenw_mean',
    'betweenness_log1p_z_mean_end_lenw_mean',
    'closeness_per_km_z_mean_end_lenw_mean',
    'ln1p_poi_count_30m_lenw_mean',
    'poi_mix_entropy_norm_30m_lenw_mean',
]