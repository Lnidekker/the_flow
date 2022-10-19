"""
This file contains all usual use cases of THE FLOW.
"""
import sys
import os
import shutil
import prepare_tf_vars
import create_run_dir
import copy_input_data
import global_tf_vars
import common_func
import q1
import q2

if __name__ == "__main__":

    # Set arguments value of python3 command to global_tf_vars
    global_tf_vars.tf_cfg_dir = str(sys.argv[1])
    global_tf_vars.tf_is_syn = int(sys.argv[2])
    global_tf_vars.tf_is_impl = int(sys.argv[3])
    global_tf_vars.tf_is_atpg = int(sys.argv[4])
    global_tf_vars.tf_ux_ui_mode = str(sys.argv[5])
    global_tf_vars.tf_update_run_dir = int(sys.argv[6])
    global_tf_vars.tf_update_all = int(sys.argv[7])
    global_tf_vars.tf_update_cfg = int(sys.argv[8])
    global_tf_vars.tf_update_step_scripts = int(sys.argv[9])
    global_tf_vars.tf_update_input_data = int(sys.argv[10])
    global_tf_vars.tf_from_step = int(sys.argv[11])
    global_tf_vars.tf_from_step_name = str(sys.argv[12])

    if global_tf_vars.tf_ux_ui_mode == 'interactive':
        global_tf_vars.tf_q1_answer = 0
        global_tf_vars.tf_q2_answer = 0
        global_tf_vars.tf_q3_answer = 0
        global_tf_vars.tf_use_xterm = 1
        global_tf_vars.tf_start_eda_tool = 0
    elif global_tf_vars.tf_ux_ui_mode == 'terminal':
        global_tf_vars.tf_q1_answer = 1
        global_tf_vars.tf_q2_answer = 1
        global_tf_vars.tf_q3_answer = 1
        global_tf_vars.tf_use_xterm = 0
        global_tf_vars.tf_start_eda_tool = 1

    # Add global_tf_vars.tf_cfg_dir value to PYTHONPATH to see tf_var.py file
    # and import tf_var_table variable
    sys.path.append(global_tf_vars.tf_cfg_dir)
    import tf_var

    # Parsing tf_var_table
    tf = prepare_tf_vars.prepare_tf_vars('', tf_var.tf_var_table)
    tf.parsing_tf_var_table()

    # Add global_tf_vars.tf_cfg_common_dir value to PYTHONPATH to see tf_var_common.py file
    # and import tf_dir_structure_table variable
    sys.path.append(global_tf_vars.tf_cfg_common_dir)
    import tf_var_common

    # Parsing tf_dir_structure_table
    tf = prepare_tf_vars.prepare_tf_vars(tf_var.tf_dir_structure_table, tf_var.tf_var_table)
    tf.parsing_tf_dir_structure_table()

    # Initialise global_ft_vars for run dir structure
    create_run_dir.run_dir_structure_is()

    # Set global_tf_vars to create_run_dir.create_run_dir
    if os.path.isdir(global_tf_vars.tf_run_dir):
        q1.q1()

    # Delete run dir
    if os.path.isdir(global_tf_vars.tf_run_dir) and global_tf_vars.tf_remove_run_dir == 1:
        os.system('chmod 750 -R ' + global_tf_vars.tf_run_dir)
        shutil.rmtree(global_tf_vars.tf_run_dir)
        common_func.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' has been deleted.')

    # Create run dir
    if not os.path.isdir(global_tf_vars.tf_run_dir):
        create_run_dir.create_run_dir()
        global_tf_vars.tf_update_run_dir_in_cfg = 1
        global_tf_vars.tf_update_run_dir_input_data = 1
        global_tf_vars.tf_update_run_dir_scripts = 1

    # Copy input data to run dir
    if global_tf_vars.tf_update_run_dir_input_data == 1:
        copy_input_data.copy_input_data()

    # Create mmmc_config.tcl and mmmc_derate.tcl
    import mmmc_gen
    import phy_gen

    if global_tf_vars.tf_update_run_dir_in_cfg:
        mmmc_gen.mmmc_gen.run_mmmc_gen()
        phy_gen.phy_gen.run_phy_gen()

    # Create .tcl file for each step
    import create_tcl_scripts_for_each_step

    if global_tf_vars.tf_update_run_dir_scripts:
        create_tcl_scripts_for_each_step.run_create_tcl_scripts_for_each_step()

    # Go to work dir
    os.chdir(global_tf_vars.tf_run_dir_work)

    # Run to execute steps one by one
    q2.q2()

    import run_eda_tools

    if global_tf_vars.tf_q2_flag == '1':
        run_eda_tools.run_eda_tools()
    elif global_tf_vars.tf_q2_flag == '2':
        exit('Normal exit.')
