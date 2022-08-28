"""
This file contains all usual use cases of THE FLOW.
"""
import sys
import os
import shutil
import time
import prepare_tf_vars
import create_run_dir
import copy_input_data
import global_tf_vars
import common_func

if __name__ == "__main__":

    # Set arguments value of python3 command to global_tf_vars
    global_tf_vars.tf_cfg_dir = sys.argv[1]
    global_tf_vars.tf_is_syn = int(sys.argv[2])
    global_tf_vars.tf_is_impl = int(sys.argv[3])
    global_tf_vars.tf_is_atpg = int(sys.argv[4])
    global_tf_vars.tf_ux_ui_mode = sys.argv[5]
    global_tf_vars.tf_update_run_dir = int(sys.argv[6])
    global_tf_vars.tf_update_all = int(sys.argv[7])
    global_tf_vars.tf_update_cfg = int(sys.argv[8])
    global_tf_vars.tf_update_step_scripts = int(sys.argv[9])
    global_tf_vars.tf_update_input_data = int(sys.argv[10])

    if global_tf_vars.tf_ux_ui_mode == 'interactive':
        global_tf_vars.tf_q1_answer = 0
        global_tf_vars.tf_q2_answer = 0
        global_tf_vars.tf_use_xterm = 1
        global_tf_vars.tf_start_eda_tool = 0
    elif global_tf_vars.tf_ux_ui_mode == 'terminal':
        global_tf_vars.tf_q1_answer = 1
        global_tf_vars.tf_q2_answer = 1
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
        common_func.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' exists.')
        if global_tf_vars.tf_q1_answer == 0:
            q1_flag = input('[TF_Q1] What do you want to do?\n'
                            '            1-remove existing directory and continue THE FLOW execution\n'
                            '            2-update cfg files and continue THE FLOW execution\n'
                            '            3-update step .tcl scripts and continue THE FLOW execution\n'
                            '            4-update input data and continue THE FLOW execution\n'
                            '            5-just continue THE FLOW with existing directory and files\n'
                            '            6-exit THE FLOW\n'
                            '(1/2/3/4/5/6): ')
            if q1_flag == '1':
                global_tf_vars.tf_remove_run_dir = 1
                global_tf_vars.tf_update_run_dir_in_cfg = 1
                global_tf_vars.tf_update_run_dir_input_data = 1
                global_tf_vars.tf_update_run_dir_scripts = 1
            elif q1_flag == '2':
                global_tf_vars.tf_update_run_dir_in_cfg = 1
            elif q1_flag == '3':
                global_tf_vars.tf_update_run_dir_scripts = 1
            elif q1_flag == '4':
                global_tf_vars.tf_update_run_dir_input_data = 1
            elif q1_flag == '5':
                empty_flag = 0
            elif q1_flag == '6':
                exit('Normal exit.')
        elif global_tf_vars.tf_q1_answer == 1:
            if global_tf_vars.tf_update_all == 1:
                global_tf_vars.tf_remove_run_dir = 1
            if global_tf_vars.tf_update_cfg == 1:
                global_tf_vars.tf_update_run_dir_in_cfg = 1
            if global_tf_vars.tf_update_step_scripts == 1:
                global_tf_vars.tf_update_run_dir_scripts = 1
            if global_tf_vars.tf_update_input_data == 1:
                global_tf_vars.tf_update_run_dir_input_data = 1
        else:
            exit('Unknown tf_ux_ui_mode value')

    # Delete run dir
    if os.path.isdir(global_tf_vars.tf_run_dir) and global_tf_vars.tf_remove_run_dir == 1:
        shutil.rmtree(global_tf_vars.tf_run_dir)
        common_func.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' has been deleted.')

    # Create run dir
    if global_tf_vars.tf_remove_run_dir == 1:
        create_run_dir.create_run_dir()

    # Copy input data to run dir
    if global_tf_vars.tf_update_run_dir_input_data:
        copy_input_data.copy_input_data()

    # Create mmmc_config.tcl and mmmc_derate.tcl
    import mmmc_gen
    import phy_gen

    if global_tf_vars.tf_update_run_dir_in_cfg:
        if global_tf_vars.tf_is_syn == 1:
            tf_mmmc_gen = mmmc_gen.mmmc_gen(tf_var.mmmc_analysis_view_syn_table,
                                            tf_var_common.mmmc_pvt_p_table,
                                            tf_var_common.mmmc_pvt_v_table,
                                            tf_var_common.mmmc_pvt_t_table,
                                            tf_var_common.mmmc_pvt_table,
                                            tf_var_common.mmmc_lib_file_table,
                                            tf_var_common.mmmc_cdb_file_table,
                                            tf_var_common.mmmc_pvt_qrc_table,
                                            tf_var_common.mmmc_qrc_file_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            tf_var_common.mmmc_ocv_table
                                            )
        elif global_tf_vars.tf_is_impl == 1:
            tf_mmmc_gen = mmmc_gen.mmmc_gen(tf_var.mmmc_analysis_view_impl_table,
                                            tf_var_common.mmmc_pvt_p_table,
                                            tf_var_common.mmmc_pvt_v_table,
                                            tf_var_common.mmmc_pvt_t_table,
                                            tf_var_common.mmmc_pvt_table,
                                            tf_var_common.mmmc_lib_file_table,
                                            tf_var_common.mmmc_cdb_file_table,
                                            tf_var_common.mmmc_pvt_qrc_table,
                                            tf_var_common.mmmc_qrc_file_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            tf_var_common.mmmc_ocv_table
                                            )

        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1:
            tf_mmmc_gen.parsing_analysis_view_table()
            tf_mmmc_gen.make_lib_files_list_for_each_view()
            tf_mmmc_gen.make_cdb_files_list_for_each_view()
            tf_mmmc_gen.make_qrc_files_list_for_each_view()
            tf_mmmc_gen.make_temperature_for_each_view()
            tf_mmmc_gen.make_sdc_files_for_each_view()
            tf_mmmc_gen.make_mmmc_config_file()
            tf_mmmc_gen.make_mmmc_derate_file()

        tf_phy_gen = phy_gen.phy_gen(tf_var_common.phy_lef_table, tf_var_common.phy_verilog_table)
        tf_phy_gen.make_lef_list()
        tf_phy_gen.make_verilog_list()
        tf_phy_gen.make_phy_config_file()

    # Create .tcl file for each step
    import create_tcl_scripts_for_each_step

    if global_tf_vars.tf_update_run_dir_scripts:
        shutil.rmtree(global_tf_vars.tf_run_dir_scripts)
        os.mkdir(global_tf_vars.tf_run_dir_scripts)
        if global_tf_vars.tf_is_syn == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_file_steps_import_file(global_tf_vars.tf_syn_steps_dir)
        elif global_tf_vars.tf_is_impl == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_file_steps_import_file(global_tf_vars.tf_impl_steps_dir)
        elif global_tf_vars.tf_is_atpg == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_file_steps_import_file(global_tf_vars.tf_atpg_steps_dir)

        sys.path.append(global_tf_vars.tf_run_dir_work_tmp)
        from tf_tmp_file_steps_import import *

        if global_tf_vars.tf_is_syn == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_step_table_file(tf_var.tf_step_syn_table)
        elif global_tf_vars.tf_is_impl == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_step_table_file(tf_var.tf_step_impl_table)
        elif global_tf_vars.tf_is_atpg == 1:
            create_tcl_scripts_for_each_step.create_tf_tmp_step_table_file(tf_var.tf_step_atpg_table)

        from tf_tmp_step_table import *

        for i in range(len(tf_tmp_step_table)):  # Create tcl scr for all steps
            if tf_tmp_step_table[i][0] == 0:
                create_tcl_scripts_for_each_step.create_tcl_scripts_for_each_step(
                    tf_tmp_step_table[i][1], '', tf_tmp_step_table[i][2])
            else:
                create_tcl_scripts_for_each_step.create_tcl_scripts_for_each_step(
                    tf_tmp_step_table[i][1], tf_tmp_step_table[i - 1][1], tf_tmp_step_table[i][2])

    # Go to work dir
    os.chdir(global_tf_vars.tf_run_dir_work)

    # Run to execute steps one by one
    if global_tf_vars.tf_q2_answer == 0:
        q2_flag = input(
            '[TF_Q2] Do you want to start EDA tool?\n'
            '            1-Yes\n'
            '            2-No\n'
            '(1/2): '
        )
    elif global_tf_vars.tf_q2_answer == 1:
        q2_flag = '1'

    if q2_flag == '1':
        if global_tf_vars.tf_is_syn == 1:
            for j in range(0, len(tf_var.tf_step_syn_table)):
                if tf_var.tf_step_syn_table[j][0] == 0:
                    common_func.tf_info('start to execute ' + tf_var.tf_step_syn_table[j][1] + ' step')
                    t = time.time()
                    if global_tf_vars.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm('genus -f ../scripts/' +
                                                                    tf_var.tf_step_syn_table[j][1] +
                                                                    '.tcl -log ../logs/' +
                                                                    tf_var.tf_step_syn_table[j][1] +
                                                                    '.log -overwrite'))
                    else:
                        os.system('genus -f ../scripts/' +
                                  tf_var.tf_step_syn_table[j][1] +
                                  '.tcl -log ../logs/' +
                                  tf_var.tf_step_syn_table[j][1] +
                                  '.log -overwrite')
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + tf_var.tf_step_syn_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                elif common_func.tf_file_exists_check('../db/' + tf_var.tf_step_syn_table[j - 1][1] + '.db') == \
                        'True':
                    common_func.tf_info('start to execute ' + tf_var.tf_step_syn_table[j][1] + ' step')
                    t = time.time()
                    if global_tf_vars.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm('genus -f ../scripts/' +
                                                                    tf_var.tf_step_syn_table[j][1] +
                                                                    '.tcl -log ../logs/' +
                                                                    tf_var.tf_step_syn_table[j][1] +
                                                                    '.log -overwrite'))
                    else:
                        os.system('genus -f ../scripts/' +
                                  tf_var.tf_step_syn_table[j][1] +
                                  '.tcl -log ../logs/' +
                                  tf_var.tf_step_syn_table[j][1] +
                                  '.log -overwrite')
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + tf_var.tf_step_syn_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                else:
                    common_func.tf_error('previous step db doesn\'t exist')
                    exit('exit with error')
        elif global_tf_vars.tf_is_impl == 1:
            for j in range(0, len(tf_var.tf_step_impl_table)):
                if tf_var.tf_step_impl_table[j][0] == 0:
                    common_func.tf_info('start to execute ' + tf_var.tf_step_impl_table[j][1] + ' step')
                    t = time.time()
                    if global_tf_vars.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm('innovus -stylus -file ../scripts/' +
                                                                    tf_var.tf_step_impl_table[j][1] +
                                                                    '.tcl -log ../logs/' +
                                                                    tf_var.tf_step_impl_table[j][1] +
                                                                    '.log -overwrite'))
                    else:
                        os.system('innovus -stylus -file ../scripts/' +
                                  tf_var.tf_step_impl_table[j][1] +
                                  '.tcl -log ../logs/' +
                                  tf_var.tf_step_impl_table[j][1] +
                                  '.log -overwrite')
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + tf_var.tf_step_impl_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                elif os.path.isdir('../db/' + tf_var.tf_step_impl_table[j - 1][1] + '.db'):
                    common_func.tf_info('start to execute ' + tf_var.tf_step_impl_table[j][1] + ' step')
                    t = time.time()
                    if global_tf_vars.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm('innovus -stylus -file ../scripts/' +
                                                                    tf_var.tf_step_impl_table[j][1] +
                                                                    '.tcl -log ../logs/' +
                                                                    tf_var.tf_step_impl_table[j][1] +
                                                                    '.log -overwrite'))
                    else:
                        os.system('innovus -stylus -file ../scripts/' +
                                  tf_var.tf_step_impl_table[j][1] +
                                  '.tcl -log ../logs/' +
                                  tf_var.tf_step_impl_table[j][1] +
                                  '.log -overwrite')
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + tf_var.tf_step_impl_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                else:
                    common_func.tf_error('previous step db doesn\'t exist')
                    exit('exit with error')
        elif global_tf_vars.tf_is_atpg == 1:
            for j in range(0, len(tf_var.tf_step_atpg_table)):
                common_func.tf_info('start to execute ' + tf_var.tf_step_atpg_table[j][1] + ' step')
                t = time.time()
                if global_tf_vars.tf_use_xterm == 1:
                    os.system(common_func.tf_run_eda_with_xterm('modus -f ../scripts/' +
                                                                tf_var.tf_step_atpg_table[j][1] +
                                                                '.tcl -log ../logs/' +
                                                                tf_var.tf_step_atpg_table[j][1] +
                                                                '.log'))
                else:
                    os.system('modus -f ../scripts/' +
                              tf_var.tf_step_atpg_table[j][1] +
                              '.tcl -log ../logs/' +
                              tf_var.tf_step_atpg_table[j][1] +
                              '.log')
                runtime = time.time() - t
                common_func.tf_info('finish to execute ' + tf_var.tf_step_atpg_table[j][1] +
                                    ' step. runtime: ' + str(runtime // 60) + ' min')
    elif q2_flag == '2':
        exit('Normal exit.')
