"""
This file contains all global variables which are used in THE FLOW code.
"""
# Variables from tf_dir_structure_table
tf_cfg_common_dir = ''
tf_cfg_dir = ''
tf_sdc_dir = {}
tf_workarea_syn_dir = ''
tf_workarea_impl_dir = ''
tf_workarea_atpg_dir = ''
tf_workarea_power_dir = ''
tf_workarea_formal_dir = ''
tf_syn_steps_dir = {}
tf_impl_steps_dir = {}
tf_atpg_steps_dir = {}
tf_power_steps_dir = {}
tf_formal_steps_dir = {}
tf_rtl_dir = {}
tf_syn_src_dir = {}
tf_impl_src_dir = {}
tf_atpg_src_dir = {}
tf_power_src_dir = {}
tf_formal_src_dir = {}

# Variables from tf_var_table
tf_design_name = ''
tf_exp_name_syn = ''
tf_exp_name_impl = ''
tf_exp_name_atpg = ''
tf_exp_name_power = ''
tf_exp_name_formal = ''

# Run dir structure
tf_run_dir = ''
tf_run_dir_db = ''
tf_run_dir_in = ''
tf_run_dir_in_sdc = ''
tf_run_dir_in_rtl = ''
tf_run_dir_in_src = ''
tf_run_dir_in_cfg = ''
tf_run_dir_out = ''
tf_run_dir_scripts = ''
tf_run_dir_reports = ''
tf_run_dir_logs = ''
tf_run_dir_work = ''
tf_run_dir_work_tmp = ''

# Variables which contains arguments value of python3 command
tf_config = ''
tf_is_syn = 0
tf_is_impl = 0
tf_is_atpg = 0
tf_is_power = 0
tf_ux_ui_mode = ''
tf_update_run_dir = 0
tf_update_all = 0
tf_update_cfg = 0
tf_update_step_scripts = 0
tf_update_input_data = 0
tf_from_step = 0
tf_from_step_name = ''
tf_start_dir = ''
tf_to_step = 0
tf_to_step_name = ''
tf_only_step = 0
tf_only_step_name = ''
tf_is_formal = 0
tf_tmpdir = ''

# Variables to navigate THE FLOW script
tf_remove_run_dir = 0
tf_update_run_dir_in_cfg = 0
tf_update_run_dir_input_data = 0
tf_update_run_dir_scripts = 0
tf_start_eda_tool = 0
tf_use_xterm = 0
tf_q1_answer = 0
tf_q2_answer = 0
tf_q3_answer = 0
tf_q1_flag = ''
tf_q2_flag = ''
tf_q3_flag = ''
tf_delete_all_following_db = 0
tf_go_to_next_step = 0
tf_var_syn_table_exists = 1
tf_var_impl_table_exists = 1
tf_var_atpg_table_exists = 1
tf_var_power_table_exists = 1
tf_var_formal_table_exists = 1
tf_var_files = ''
tf_var_files_split = []
tf_var_mmmc_syn_table_exists = 1
tf_var_mmmc_impl_table_exists = 1
tf_var_mmmc_atpg_table_exists = 1
tf_var_mmmc_power_table_exists = 1
tf_var_mmmc_formal_table_exists = 1

# mmmc_gen variables
mmmc_analysis_view_table_sdc_mode = {}
mmmc_analysis_view_table_pvt_p = {}
mmmc_analysis_view_table_pvt_v = {}
mmmc_analysis_view_table_pvt_t = {}
mmmc_analysis_view_table_pvt = {}
mmmc_analysis_view_table_parasitic = {}
mmmc_analysis_view_table_mode = {}
mmmc_analysis_view_table_name = {}
mmmc_analysis_view_table_lib = {}
mmmc_analysis_view_table_lib_partitions = {}
mmmc_analysis_view_table_cdb = {}
mmmc_analysis_view_table_qrc = {}
mmmc_analysis_view_table_temperature = {}
mmmc_analysis_view_table_sdc_mode_file = {}
mmmc_analysis_view_table_lib_all = {}
mmmc_analysis_view_table_qrc_all = {}
mmmc_analysis_view_table_sdc_mode_file_all = {}

mmmc_ocv_p = {}
mmmc_ocv_v = {}
mmmc_ocv_t = {}
mmmc_ocv_qrc = {}
mmmc_ocv_mode = {}
mmmc_ocv_cd = {}
mmmc_ocv_cd_ = {}
mmmc_ocv_ce = {}
mmmc_ocv_ce_ = {}
mmmc_ocv_cl = {}
mmmc_ocv_cl_ = {}
mmmc_ocv_nd = {}
mmmc_ocv_nd_ = {}
mmmc_ocv_ne = {}
mmmc_ocv_ne_ = {}
mmmc_ocv_nl = {}
mmmc_ocv_nl_ = {}

tf_var_mmmc_table = {}
tf_partition_existing = 0

# Temporary files
tf_tmp_file_steps_import = ''
tf_tmp_step_table = {}
tf_tmpdir_name = ''

# phy_gen variables
phy_lef_files = ''
phy_verilog_files = ''
phy_cl_dirs = ''
phy_gds_files = ''
