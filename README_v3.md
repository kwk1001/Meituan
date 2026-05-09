# trip_road_v3

This folder contains the v3 rewrite of the two notebooks / scripts:

- `segment_variables_v3_trip_road.ipynb`
- `model_analysis_v3_trip_road.ipynb`
- script versions with the same names and `.py` suffix

## What changed in v3

### segment_variables_v3
- Trip table layout is now controlled and ordered as:
  - IDs
  - X variables
  - Y variables (`overspeed_20`, `speed_kmh`)
  - aux / process / time columns
- All `mid_*` columns are removed from the trip big table.
- Road outputs now include both:
  - overspeed rate by time window
  - mean speed by time window
- New road outputs:
  - `road_model_table_long_v3.csv.gz` (model-ready long table)
  - `road_model_table_wide_v3.csv.gz` (mapping / join wide table)
  - `road_pass_table_v3.csv.gz` (pass-level table)
- Spatial exports added:
  - trip lines
  - road network lines
  - junction node points
- Each SHP export comes with a field map CSV because SHP field names are limited.
- Full field names are preserved in GPKG exports.

### model_analysis_v3
- Variable selection is now controlled in one place at the top of the file:
  - X groups to use
  - extra X variables
  - X variables to drop
  - X variables to log-transform
  - Y variables to log-transform
- Distribution plots are exported for selected trip / road variables.
- Road models now use the road long table and support per-scope `min_passes` thresholds.
- Logistic fitting now:
  - removes exact alias columns before estimation
  - can estimate on standardized continuous X
  - exports both original-scale and estimation-scale coefficients
- Combined comparison tables are exported so time-window model coefficients can be compared side by side.

## Recommended run order

1. Run `segment_variables_v3_trip_road.ipynb`
2. Run `model_analysis_v3_trip_road.ipynb`

## Main output folders

### segment outputs
`outputs/segment_variables_v3/`

Key files:
- `segments/trip_model_table_v3.csv.gz`
- `roads/road_model_table_long_v3.csv.gz`
- `roads/road_model_table_wide_v3.csv.gz`
- `roads/road_pass_table_v3.csv.gz`
- `spatial/trip_lines_full_v3.*`
- `spatial/road_network_full_v3.*`
- `spatial/junction_nodes_full_v3.*`

### model outputs
`outputs/model_analysis_v3/`

Key files:
- `all_models_coef_long.csv`
- `all_models_fit_info.csv`
- `all_models_prep_info.csv`
- `comparison_tables/*.csv`
- `distribution_plots/*`
- `diagnostics/*`

## Notes on SHP exports

SHP has strict field-name and text-length limits.
To keep joins easy:
- IDs such as `seg_id`, `conedge_id`, and `node_id` are kept in the SHP exports
- a `*_shp_field_map.csv` file is exported next to each SHP
- GPKG exports keep the full original field names
