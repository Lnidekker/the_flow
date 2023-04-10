import os
import global_tf_vars
from messages import Messages


def tf_var_finding(path, file_name):

    m = Messages()

    for element in os.scandir(path):
        try:
            e1 = element.is_file()
            e2 = element.name
        except PermissionError:
            m.init_8(element.path)
        else:
            if element.is_file() and element.name == file_name:
                if global_tf_vars.tf_var_files == '':
                    global_tf_vars.tf_var_files = element.path
                else:
                    global_tf_vars.tf_var_files = global_tf_vars.tf_var_files + ' ' + element.path
            elif element.is_dir():
                tf_var_finding(element.path, file_name)


def run_check_tf_var_files():

    m = Messages()

    tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var.py')

    if global_tf_vars.tf_is_syn:
        tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var_syn.py')
    if global_tf_vars.tf_is_impl:
        tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var_impl.py')
    if global_tf_vars.tf_is_atpg:
        tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var_atpg.py')
    if global_tf_vars.tf_is_power:
        tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var_power.py')
    if global_tf_vars.tf_is_formal:
        tf_var_finding(global_tf_vars.tf_start_dir, 'tf_var_formal.py')

    global_tf_vars.tf_var_files_split = global_tf_vars.tf_var_files.split()

    if len(global_tf_vars.tf_var_files_split) > 1:
        m.init_7(global_tf_vars.tf_var_files_split)
    else:
        global_tf_vars.tf_config = global_tf_vars.tf_var_files
