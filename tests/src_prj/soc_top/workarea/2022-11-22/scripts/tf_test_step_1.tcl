# Flow type
set FLOW "syn"

# Steps
set STEP_NAME "tf_test_step_1"
set PREVIOUS_STEP_NAME ""

# Variables from tf_var.tf_var_table
set cfg_common "/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/cfg"
set DESIGN_NAME "soc_top"
set EXP_NAME_SYN "2022-11-22"
set EXP_NAME_ATPG "testing_atpg"
set test_var "1 2"

# Variables from tf_var.tf_var_syn_table

# Variables from tf_var_common.tf_var_common_table

# MMMC presets from tf_var.tf_var_mmmc_table
set MMMC_PRESETS "test_lib tech_40"

# MMMC sdc modes
set MMMC_SDC_MODES "func scan"

if {$PREVIOUS_STEP_NAME != ""} {read_db ../db/$PREVIOUS_STEP_NAME.db}

# STEP START

    1

# STEP FINISH

write_db -all_root_attributes ../db/tf_test_step_1.db

exit
