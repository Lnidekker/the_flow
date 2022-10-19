import os
import time
import global_tf_vars
import common_func
import tf_var
import q3


def run_eda_tools():

    if global_tf_vars.tf_is_syn == 1:

        if global_tf_vars.tf_from_step == 1:
            flag = 0
            for i in range(0, len(tf_var.tf_step_syn_table)):
                if tf_var.tf_step_syn_table[i][1] == global_tf_vars.tf_from_step_name:
                    flag = 1
            if flag == 0:
                common_func.tf_error('Step name "' + global_tf_vars.tf_from_step_name +
                                     '" from [-from_step] option doesn\'t exist.')
                common_func.tf_exit_with_error()

        for j in range(0, len(tf_var.tf_step_syn_table)):
            global_tf_vars.tf_go_to_next_step = 0
            if common_func.tf_dir_exists_check(global_tf_vars.tf_run_dir_db + '/' +
                                               tf_var.tf_step_syn_table[j][1] + '.db'):
                q3.q3(tf_var.tf_step_syn_table[j][1])
                if global_tf_vars.tf_q3_flag == '1':
                    global_tf_vars.tf_go_to_next_step = 1
                elif global_tf_vars.tf_q3_flag == '2':
                    for k in range(j, len(tf_var.tf_step_syn_table)):
                        if common_func.tf_dir_exists_check(
                                global_tf_vars.tf_run_dir_db + '/' + tf_var.tf_step_syn_table[k][1] + '.db'):
                            os.remove(global_tf_vars.tf_run_dir_db + '/' + tf_var.tf_step_syn_table[k][1] + '.db')
            if global_tf_vars.tf_go_to_next_step == 0:
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

        if global_tf_vars.tf_from_step == 1:
            flag = 0
            for i in range(0, len(tf_var.tf_step_impl_table)):
                if tf_var.tf_step_impl_table[i][1] == global_tf_vars.tf_from_step_name:
                    flag = 1
            if flag == 0:
                common_func.tf_error('Step name "' + global_tf_vars.tf_from_step_name +
                                     '" from [-from_step] option doesn\'t exist.')
                common_func.tf_exit_with_error()

        for j in range(0, len(tf_var.tf_step_impl_table)):
            global_tf_vars.tf_go_to_next_step = 0
            if common_func.tf_dir_exists_check(global_tf_vars.tf_run_dir_db + '/' +
                                               tf_var.tf_step_syn_table[j][1] + '.db'):
                q3.q3(tf_var.tf_step_syn_table[j][1])
                if global_tf_vars.tf_q3_flag == '1':
                    global_tf_vars.tf_go_to_next_step = 1
                elif global_tf_vars.tf_q3_flag == '2':
                    for k in range(j, len(tf_var.tf_step_syn_table)):
                        if common_func.tf_dir_exists_check(
                                global_tf_vars.tf_run_dir_db + '/' + tf_var.tf_step_syn_table[k][1] + '.db'):
                            os.remove(global_tf_vars.tf_run_dir_db + '/' + tf_var.tf_step_syn_table[k][1] + '.db')
            if global_tf_vars.tf_go_to_next_step == 0:
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
