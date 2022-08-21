set STEP_NAME ""
set PREVIOUS_STEP_NAME "tf_test_step_2"

# Variables from tf_var.tf_var_table
set cfg_common "/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/cfg"
set DESIGN_NAME "soc_top"
set EXP_NAME_SYN "testing_1"
set EXP_NAME_ATPG "testing_atpg"
set test_var "1 2"

# Variables from tf_var_common.tf_var_common_table

if {$PREVIOUS_STEP_NAME != ""} {read_db ../db/$PREVIOUS_STEP_NAME.db}

# STEP START

# STEP FINISH

write_db -all_root_attributes ../db/.db

exit
