import common_func
import global_tf_vars


def q1():

    common_func.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' exists.')
    if global_tf_vars.tf_q1_answer == 0:
        global_tf_vars.tf_q1_flag = input('[TF_Q1] What do you want to do?\n'
                                          '            1-remove existing directory and continue THE FLOW execution\n'
                                          '            2-update cfg files and continue THE FLOW execution\n'
                                          '            3-update step .tcl scripts and continue THE FLOW execution\n'
                                          '            4-update input data and continue THE FLOW execution\n'
                                          '            5-just continue THE FLOW with existing directory and files\n'
                                          '            6-exit THE FLOW\n'
                                          '(1/2/3/4/5/6): ')
        if global_tf_vars.tf_q1_flag == '1':
            global_tf_vars.tf_remove_run_dir = 1
            global_tf_vars.tf_update_run_dir_in_cfg = 1
            global_tf_vars.tf_update_run_dir_input_data = 1
            global_tf_vars.tf_update_run_dir_scripts = 1
        elif global_tf_vars.tf_q1_flag == '2':
            global_tf_vars.tf_update_run_dir_in_cfg = 1
        elif global_tf_vars.tf_q1_flag == '3':
            global_tf_vars.tf_update_run_dir_scripts = 1
        elif global_tf_vars.tf_q1_flag == '4':
            global_tf_vars.tf_update_run_dir_input_data = 1
        elif global_tf_vars.tf_q1_flag == '5':
            empty_flag = 0
        elif global_tf_vars.tf_q1_flag == '6':
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
