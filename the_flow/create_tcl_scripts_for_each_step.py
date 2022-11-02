"""
Create .tcl scripts for each steps from tf_step_*_table.
Each step contains the following information:
    - all variables from tf_var_table
    - all variables from tf_var_common_table
    - step body from some file in tf_dir_structure_table[*_steps]
"""
import sys
import os
import glob
import shutil
import common_func
import global_tf_vars
import tf_var
import tf_var_common
from messages import messages


def create_tcl_scripts_for_each_step(step_name, previous_step_name, step_body):
    """
    Creation of .tcl script.

    :param step_name: Step name from tf_step_*_table
    :param previous_step_name: Previous step name from tf_step_*_table
    :param step_body: Step body.
    :return: .tcl file.
    """
    common_func.tf_info('(TFPrepareData.make_tcl_scripts_for_each_steps) start')

    original_stdout = sys.stdout
    tf_step_tcl_file = global_tf_vars.tf_run_dir_scripts + '/' + step_name + '.tcl'
    with open(tf_step_tcl_file, 'a') as f:

        sys.stdout = f
        if global_tf_vars.tf_is_syn == 1:
            print('set FLOW \"syn\"')
        elif global_tf_vars.tf_is_impl == 1:
            print('set FLOW \"impl\"')
        elif global_tf_vars.tf_is_atpg == 1:
            print('set FLOW \"atpg\"')
        elif global_tf_vars.tf_is_power == 1:
            print('set FLOW \"power\"')
        print('')

        print('set STEP_NAME \"' + step_name + '\"')
        print('set PREVIOUS_STEP_NAME \"' + previous_step_name + '\"')
        print('')

        print('# Variables from tf_var.tf_var_table')
        for i in range(len(tf_var.tf_var_table)):
            list_ = ''
            for j in range(1, len(tf_var.tf_var_table[i])):
                if list_ == '':
                    list_ = tf_var.tf_var_table[i][j]
                else:
                    list_ = list_ + ' ' + tf_var.tf_var_table[i][j]
            if tf_var.tf_var_table[i][0] != '':
                print('set ' + tf_var.tf_var_table[i][0] + ' \"' + list_ + '\"')
        print('')

        print('# Variables from tf_var_common.tf_var_common_table')
        for i in range(len(tf_var_common.tf_var_common_table)):
            list_ = ''
            for j in range(1, len(tf_var_common.tf_var_common_table[i])):
                if list_ == '':
                    list_ = tf_var_common.tf_var_common_table[i][j]
                else:
                    list_ = list_ + ' ' + tf_var_common.tf_var_common_table[i][j]
            if tf_var_common.tf_var_common_table[i][0] != '':
                print('set ' + tf_var_common.tf_var_common_table[i][0] + ' \"' + list_ + '\"')
        print('')

        print('# MMMC presets from tf_var.tf_var_mmmc_table')
        list_ = ''
        for i in range(0, len(tf_var.tf_var_mmmc_table)):
            if list_ == '':
                list_ = tf_var.tf_var_mmmc_table[i]
            else:
                list_ = list_ + ' ' + tf_var.tf_var_mmmc_table[i]
        print('set MMMC_PRESETS \"' + list_ + '\"')
        print('')

        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            print('if {$PREVIOUS_STEP_NAME != \"\"} {read_db ../db/$PREVIOUS_STEP_NAME.db}')
        print('')
        print('# STEP START')
        print(step_body)
        print('# STEP FINISH')
        print('')
        if global_tf_vars.tf_is_syn == 1:
            print('write_db -all_root_attributes ../db/' + step_name + '.db')
        elif global_tf_vars.tf_is_impl == 1:
            print('write_db -lib -sdc -def ../db/' + step_name + '.db')
        elif global_tf_vars.tf_is_power == 1:
            print('write_db ../db/' + step_name + '.db')
        print('')
        print('exit')
        sys.stdout = original_stdout

    common_func.tf_info('(TFPrepareData.make_tcl_scripts_for_each_steps) finish')


def create_tf_tmp_file_steps_import_file(steps_dir):
    """
    Creation of temporary file which contains import function for all steps.
    It needs to load all steps body into python like variables.

    :param steps_dir: Dir path from tf_dir_structure_table[*_steps].
    :return: tf_tmp_file_steps_import.py file.
    """

    original_stdout = sys.stdout
    global_tf_vars.tf_tmp_file_steps_import = global_tf_vars.tf_run_dir_work_tmp + '/tf_tmp_file_steps_import.py'
    with open(global_tf_vars.tf_tmp_file_steps_import, 'a') as f:
        sys.stdout = f
        for i in range(len(steps_dir)):
            sys.path.append(steps_dir[i])
            os.chdir(steps_dir[i])
            for j in glob.glob('tf*.py'):
                print('from ' + j + ' import *')
    sys.stdout = original_stdout

    with open(global_tf_vars.tf_tmp_file_steps_import, 'r') as f:
        data = f.read()
        data = data.replace('.py', '')
    with open(global_tf_vars.tf_tmp_file_steps_import, 'w') as f:
        f.write(data)


def create_tf_tmp_step_table_file(steps_table):
    """
    Parsing tf_step_*_table into tf_tmp_step_table. It deeds to use create_tcl_scripts_for_each_step clearly.

    :param steps_table: tf_step_*_table from tf_var.py.
    :return: tf_tmp_step_table.py file.
    """
    original_stdout = sys.stdout
    global_tf_vars.tf_tmp_step_table = global_tf_vars.tf_run_dir_work_tmp + '/tf_tmp_step_table.py'

    with open(global_tf_vars.tf_tmp_step_table, 'a') as f:
        sys.stdout = f
        print('from tf_tmp_file_steps_import import *')
        print('')
        print('tf_tmp_step_table = (')
        for i in range(len(steps_table)):
            if steps_table[i][0] == 0:
                print('    [0, \'' + steps_table[i][1] + '\', ' +
                      steps_table[i][1] + '],')
            else:
                print('    [1, \'' + steps_table[i][1] + '\', ' +
                      steps_table[i][1] + '],')
        print('    [1, \'\', \'\']')
        print(')')
    sys.stdout = original_stdout


def check_steps():

    step_file_list = {}
    step_dirs_list = {}
    step_file_list_flag = 0

    if global_tf_vars.tf_is_syn == 1:
        step_dir = global_tf_vars.tf_syn_steps_dir
        step_table = tf_var.tf_step_syn_table
    elif global_tf_vars.tf_is_impl == 1:
        step_dir = global_tf_vars.tf_impl_steps_dir
        step_table = tf_var.tf_step_impl_table
    elif global_tf_vars.tf_is_atpg == 1:
        step_dir = global_tf_vars.tf_atpg_steps_dir
        step_table = tf_var.tf_step_atpg_table
    elif global_tf_vars.tf_is_power == 1:
        step_dir = global_tf_vars.tf_power_steps_dir
        step_table = tf_var.tf_step_power_table

    for i in range(len(step_dir)):
        sys.path.append(step_dir[i])
        os.chdir(step_dir[i])
        for j in glob.glob('tf*.py'):
            step_file_list[step_file_list_flag] = j
            step_dirs_list[step_file_list_flag] = step_dir[i]
            step_file_list_flag = step_file_list_flag + 1

    for i in range(len(step_file_list)):
        flag = 0
        for j in range(len(step_file_list)):
            if step_file_list[i] == step_file_list[j]:
                flag = flag + 1
            if flag > 1:
                messages.tclscr_1(step_file_list[i], step_dirs_list[i] + '/' + step_file_list[i] + ' and ' +
                                  step_dirs_list[j] + '/' + step_file_list[j] + '.')

    for s in range(len(step_table)):
        name_counter = 0
        file_counter = {}
        for i in range(len(step_dir)):
            sys.path.append(step_dir[i])
            os.chdir(step_dir[i])
            for j in glob.glob('tf*.py'):
                with open(j, 'r') as file:
                    for line_number, line in enumerate(file, start=1):
                        if step_table[s][1] + ' ' in line:
                            file_counter[name_counter] = step_dir[i] + '/' + j
                            name_counter = name_counter + 1
        if name_counter > 1:
            files = ''
            for i in range(len(file_counter)):
                files = files + ', ' + file_counter[i]
            messages.tclscr_2(step_table[s][1], files, str(name_counter))


def run_create_tcl_scripts_for_each_step():

    check_steps()

    shutil.rmtree(global_tf_vars.tf_run_dir_scripts)
    os.mkdir(global_tf_vars.tf_run_dir_scripts)
    if global_tf_vars.tf_is_syn == 1:
        create_tf_tmp_file_steps_import_file(global_tf_vars.tf_syn_steps_dir)
    elif global_tf_vars.tf_is_impl == 1:
        create_tf_tmp_file_steps_import_file(global_tf_vars.tf_impl_steps_dir)
    elif global_tf_vars.tf_is_atpg == 1:
        create_tf_tmp_file_steps_import_file(global_tf_vars.tf_atpg_steps_dir)
    elif global_tf_vars.tf_is_power == 1:
        create_tf_tmp_file_steps_import_file(global_tf_vars.tf_power_steps_dir)

    sys.path.append(global_tf_vars.tf_run_dir_work_tmp)
    import tf_tmp_file_steps_import

    if global_tf_vars.tf_is_syn == 1:
        create_tf_tmp_step_table_file(tf_var.tf_step_syn_table)
    elif global_tf_vars.tf_is_impl == 1:
        create_tf_tmp_step_table_file(tf_var.tf_step_impl_table)
    elif global_tf_vars.tf_is_atpg == 1:
        create_tf_tmp_step_table_file(tf_var.tf_step_atpg_table)
    elif global_tf_vars.tf_is_power == 1:
        create_tf_tmp_step_table_file(tf_var.tf_step_power_table)

    import tf_tmp_step_table

    for i in range(len(tf_tmp_step_table.tf_tmp_step_table)):  # Create tcl scr for all steps
        if tf_tmp_step_table.tf_tmp_step_table[i][0] == 0:
            create_tcl_scripts_for_each_step(
                tf_tmp_step_table.tf_tmp_step_table[i][1],
                '',
                tf_tmp_step_table.tf_tmp_step_table[i][2])
        else:
            create_tcl_scripts_for_each_step(
                tf_tmp_step_table.tf_tmp_step_table[i][1],
                tf_tmp_step_table.tf_tmp_step_table[i - 1][1],
                tf_tmp_step_table.tf_tmp_step_table[i][2])
