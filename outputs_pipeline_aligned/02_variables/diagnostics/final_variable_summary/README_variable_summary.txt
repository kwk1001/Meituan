Final variable diagnostics generated after building all variables.

Main files:
all_variable_summary.csv: all columns with missingness, uniqueness, percentiles, skewness, top values, and optional definitions.
numeric_variable_summary.csv: numeric variables only.
categorical_variable_summary.csv: categorical and string variables only.
high_missing_variables.csv: variables with missing_share >= 0.20.
near_constant_variables.csv: variables with very low variation.
skewed_numeric_variables.csv: numeric variables with absolute skew >= 2.
correlation_with_speed.csv: numeric variables ranked by correlation with speed_kmh when speed_kmh exists.

Plots:
/Users/kwk1001/Desktop/Meituan/outputs_pipeline_aligned/02_variables/diagnostics/final_variable_summary/plots/numeric_variable_distributions_page_01.png
/Users/kwk1001/Desktop/Meituan/outputs_pipeline_aligned/02_variables/diagnostics/final_variable_summary/plots/numeric_variable_distributions_page_02.png
/Users/kwk1001/Desktop/Meituan/outputs_pipeline_aligned/02_variables/diagnostics/final_variable_summary/plots/numeric_variable_distributions_page_03.png
/Users/kwk1001/Desktop/Meituan/outputs_pipeline_aligned/02_variables/diagnostics/final_variable_summary/plots/numeric_variable_distributions_page_04.png
/Users/kwk1001/Desktop/Meituan/outputs_pipeline_aligned/02_variables/diagnostics/final_variable_summary/plots/numeric_variable_distributions_page_05.png