"""
This file contains all usual use cases of THE FLOW.
"""
import sys
import os
import shutil
from prepare_tf_vars import PrepareTfVars
import create_run_dir
import copy_input_data
import global_tf_vars
from common_func import CommonFunc
from questions import Questions
from messages import Messages
import check_tf_var_files
from questions import Questions
from run_eda_tools import RunEDATools

if __name__ == "__main__":

    '''
    Initialization
    '''

    # Set arguments value of python3 command to global_tf_vars
    global_tf_vars.tf_cfg_dir = str(sys.argv[1])
    global_tf_vars.tf_is_syn = int(sys.argv[2])
    global_tf_vars.tf_is_impl = int(sys.argv[3])
    global_tf_vars.tf_is_atpg = int(sys.argv[4])
    global_tf_vars.tf_is_power = int(sys.argv[5])
    global_tf_vars.tf_ux_ui_mode = str(sys.argv[6])
    global_tf_vars.tf_update_run_dir = int(sys.argv[7])
    global_tf_vars.tf_update_all = int(sys.argv[8])
    global_tf_vars.tf_update_cfg = int(sys.argv[9])
    global_tf_vars.tf_update_step_scripts = int(sys.argv[10])
    global_tf_vars.tf_update_input_data = int(sys.argv[11])
    global_tf_vars.tf_from_step = int(sys.argv[12])
    global_tf_vars.tf_from_step_name = str(sys.argv[13])
    global_tf_vars.tf_start_dir = str(sys.argv[14])

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

    if global_tf_vars.tf_cfg_dir == '':
        check_tf_var_files.run_check_tf_var_files()

    # Add global_tf_vars.tf_cfg_dir value to PYTHONPATH to see tf_var.py file
    # and import tf_var_table variable
    sys.path.append(global_tf_vars.tf_cfg_dir)
    import tf_var

    # Parsing tf_var_table
    try:
        tf_var.tf_var_table
    except AttributeError:
        Messages.init_5('tf_var_table', 'tf_var')

    tf = PrepareTfVars('', tf_var.tf_var_table)
    tf.parsing_tf_var_table()

    # Add global_tf_vars.tf_cfg_common_dir value to PYTHONPATH to see tf_var_common.py file
    # and import tf_dir_structure_table variable
    sys.path.append(global_tf_vars.tf_cfg_common_dir)
    import tf_var_common

    # Parsing tf_dir_structure_table
    try:
        tf_var.tf_dir_structure_table
    except AttributeError:
        Messages.init_5('tf_dir_structure_table', 'tf_var')

    tf = PrepareTfVars(tf_var.tf_dir_structure_table, tf_var.tf_var_table)
    tf.parsing_tf_dir_structure_table()

    # Check tables existing from tf_var and tf_var_common
    import check_tables

    from mmmc_gen import MmmcGen
    from phy_gen import PhyGen

    from tcl_scr_gen import TclScrGen

    import run_eda_tools

    '''
    Check input data
    '''

    check_tables.check_tables()

    '''
    Create experiment directory
    '''

    # Initialise global_ft_vars for run dir structure
    create_run_dir.run_dir_structure_is()

    # Set global_tf_vars to create_run_dir.create_run_dir
    if os.path.isdir(global_tf_vars.tf_run_dir):
        q = Questions()
        q.q1()

    # Delete run dir
    if os.path.isdir(global_tf_vars.tf_run_dir) and global_tf_vars.tf_remove_run_dir == 1:
        os.system('chmod 750 -R ' + global_tf_vars.tf_run_dir)
        shutil.rmtree(global_tf_vars.tf_run_dir)
        CommonFunc.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' has been deleted.')

    # Create run dir
    if not os.path.isdir(global_tf_vars.tf_run_dir):
        create_run_dir.create_run_dir()
        global_tf_vars.tf_update_run_dir_in_cfg = 1
        global_tf_vars.tf_update_run_dir_input_data = 1
        global_tf_vars.tf_update_run_dir_scripts = 1

    '''
    Copy input data into experiment directory
    '''

    # Copy input data to run dir
    if global_tf_vars.tf_update_run_dir_input_data == 1:
        copy_input_data.copy_input_data()

    '''
    MMMC and Phy Generators
    '''

    # Create mmmc_config.tcl and mmmc_derate.tcl

    def prepare_mmmc_presets():
        n = 0
        for k in range(len(tf_var.tf_var_mmmc_table)):
            if tf_var.tf_var_mmmc_table[k] != '':
                global_tf_vars.tf_var_mmmc_table[k] = tf_var.tf_var_mmmc_table[k]
                n = n + 1

        if global_tf_vars.tf_is_syn == 1 and global_tf_vars.tf_var_mmmc_syn_table_exists == 1:
            for k in range(len(tf_var.tf_var_mmmc_syn_table)):
                if tf_var.tf_var_mmmc_syn_table[k] != '':
                    global_tf_vars.tf_var_mmmc_table[n + k] = tf_var.tf_var_mmmc_syn_table[k]

        if global_tf_vars.tf_is_impl == 1 and global_tf_vars.tf_var_mmmc_impl_table_exists == 1:
            for k in range(len(tf_var.tf_var_mmmc_impl_table)):
                if tf_var.tf_var_mmmc_impl_table[k] != '':
                    global_tf_vars.tf_var_mmmc_table[n + k] = tf_var.tf_var_mmmc_impl_table[k]

        if global_tf_vars.tf_is_atpg == 1 and global_tf_vars.tf_var_mmmc_atpg_table_exists == 1:
            for k in range(len(tf_var.tf_var_mmmc_atpg_table)):
                if tf_var.tf_var_mmmc_atpg_table[k] != '':
                    global_tf_vars.tf_var_mmmc_table[n + k] = tf_var.tf_var_mmmc_atpg_table[k]

        if global_tf_vars.tf_is_power == 1 and global_tf_vars.tf_var_mmmc_power_table_exists == 1:
            for k in range(len(tf_var.tf_var_mmmc_power_table)):
                if tf_var.tf_var_mmmc_power_table[k] != '':
                    global_tf_vars.tf_var_mmmc_table[n + k] = tf_var.tf_var_mmmc_power_table[k]

    prepare_mmmc_presets()

    if global_tf_vars.tf_update_run_dir_in_cfg:
        for i in os.scandir(global_tf_vars.tf_run_dir_in_cfg):
            os.remove(i)
        MmmcGen.run_mmmc_gen()
        PhyGen.run_phy_gen()

    '''
    TCL_SCR Generator
    '''

    global_tf_vars.tf_tmp_file_steps_import = global_tf_vars.tf_run_dir_work_tmp + '/tf_tmp_file_steps_import.py'
    global_tf_vars.tf_tmp_step_table = global_tf_vars.tf_run_dir_work_tmp + '/tf_tmp_step_table.py'

    # Create .tcl file for each step

    if global_tf_vars.tf_update_run_dir_scripts:

        if global_tf_vars.tf_is_syn:
            if global_tf_vars.tf_var_syn_table_exists:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_syn_steps_dir,
                                            tf_var.tf_step_syn_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'syn',
                                            tf_var.tf_var_table,
                                            tf_var.tf_var_syn_table,
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)
            else:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_syn_steps_dir,
                                            tf_var.tf_step_syn_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'syn',
                                            tf_var.tf_var_table,
                                            '',
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)

        if global_tf_vars.tf_is_impl:
            if global_tf_vars.tf_var_impl_table_exists:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_impl_steps_dir,
                                            tf_var.tf_step_impl_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'impl',
                                            tf_var.tf_var_table,
                                            tf_var.tf_var_impl_table,
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)
            else:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_impl_steps_dir,
                                            tf_var.tf_step_impl_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'impl',
                                            tf_var.tf_var_table,
                                            '',
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)

        if global_tf_vars.tf_is_atpg:
            if global_tf_vars.tf_var_atpg_table_exists:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_atpg_steps_dir,
                                            tf_var.tf_step_atpg_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'atpg',
                                            tf_var.tf_var_table,
                                            tf_var.tf_var_atpg_table,
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)
            else:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_atpg_steps_dir,
                                            tf_var.tf_step_atpg_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'atpg',
                                            tf_var.tf_var_table,
                                            '',
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)

        if global_tf_vars.tf_is_power:
            if global_tf_vars.tf_var_power_table_exists:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_power_steps_dir,
                                            tf_var.tf_step_power_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'power',
                                            tf_var.tf_var_table,
                                            tf_var.tf_var_power_table,
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)
            else:
                run_tcl_scr_gen = TclScrGen(global_tf_vars.tf_power_steps_dir,
                                            tf_var.tf_step_power_table,
                                            global_tf_vars.tf_run_dir_scripts,
                                            global_tf_vars.tf_run_dir_work_tmp,
                                            global_tf_vars.tf_tmp_file_steps_import,
                                            global_tf_vars.tf_tmp_step_table,
                                            'power',
                                            tf_var.tf_var_table,
                                            '',
                                            tf_var_common.tf_var_common_table,
                                            tf_var.tf_var_mmmc_table,
                                            tf_var.mmmc_sdc_mode_table,
                                            global_tf_vars.tf_run_dir_in_cfg)

        run_tcl_scr_gen.run()

    '''
    Run EDA tools
    '''

    # Go to work dir
    os.chdir(global_tf_vars.tf_run_dir_work)

    # Run to execute steps one by one

    Questions.q2()

    if global_tf_vars.tf_q2_flag == '1':
        if global_tf_vars.tf_is_syn == 1:
            run = RunEDATools(global_tf_vars.tf_from_step,
                              global_tf_vars.tf_from_step_name,
                              global_tf_vars.tf_run_dir_db,
                              global_tf_vars.tf_q3_flag,
                              global_tf_vars.tf_use_xterm,
                              tf_var.tf_step_syn_table,
                              'syn')
        if global_tf_vars.tf_is_impl == 1:
            run = RunEDATools(global_tf_vars.tf_from_step,
                              global_tf_vars.tf_from_step_name,
                              global_tf_vars.tf_run_dir_db,
                              global_tf_vars.tf_q3_flag,
                              global_tf_vars.tf_use_xterm,
                              tf_var.tf_step_impl_table,
                              'impl')
        if global_tf_vars.tf_is_atpg == 1:
            run = RunEDATools(global_tf_vars.tf_from_step,
                              global_tf_vars.tf_from_step_name,
                              global_tf_vars.tf_run_dir_db,
                              global_tf_vars.tf_q3_flag,
                              global_tf_vars.tf_use_xterm,
                              tf_var.tf_step_atpg_table,
                              'atpg')
        if global_tf_vars.tf_is_power == 1:
            run = RunEDATools(global_tf_vars.tf_from_step,
                              global_tf_vars.tf_from_step_name,
                              global_tf_vars.tf_run_dir_db,
                              global_tf_vars.tf_q3_flag,
                              global_tf_vars.tf_use_xterm,
                              tf_var.tf_step_power_table,
                              'power')
        run.run()

    elif global_tf_vars.tf_q2_flag == '2':
        exit('Normal exit.')
