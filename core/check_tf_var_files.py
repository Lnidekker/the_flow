import os
import global_tf_vars
from messages import Messages


def tf_var_finding(path):

    m = Messages()

    for element in os.scandir(path):
        try:
            e1 = element.is_file()
            e2 = element.name
        except PermissionError:
            m.init_8(element.path)
        else:
            if element.is_file() and element.name == 'tf_var.py':
                if global_tf_vars.tf_var_files == '':
                    global_tf_vars.tf_var_files = element.path
                else:
                    global_tf_vars.tf_var_files = global_tf_vars.tf_var_files + ' ' + element.path
            elif element.is_dir():
                tf_var_finding(element.path)


def run_check_tf_var_files():

    m = Messages()

    tf_var_finding(global_tf_vars.tf_start_dir)

    global_tf_vars.tf_var_files_split = global_tf_vars.tf_var_files.split()

    if len(global_tf_vars.tf_var_files_split) > 1:
        m.init_7(global_tf_vars.tf_var_files_split)
    else:
        global_tf_vars.tf_cfg_dir = global_tf_vars.tf_var_files.replace('/tf_var.py', '')
