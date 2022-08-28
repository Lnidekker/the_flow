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
import common_func
import global_tf_vars
import tf_var
import tf_var_common


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
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1:
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
