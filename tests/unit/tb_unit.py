import sys
import os
import shutil

sys.path.append('/Users/leonidnidekker/Dropbox/python/the_flow')

from the_flow import prepare_tf_vars
from the_flow import create_run_dir
from the_flow import global_tf_vars
from the_flow import copy_input_data


if __name__ == "__main__":
    tb = prepare_tf_vars.prepare_tf_vars(tb_tf_dir_structure_table, tb_tf_var_table)

    tb.parsing_tf_dir_structure_table()
    tb.parsing_tf_var_table()

    create_run_dir.run_dir_structure_is()

    if os.path.exists(global_tf_vars.tf_run_dir):
        shutil.rmtree(global_tf_vars.tf_run_dir)
        create_run_dir.create_run_dir()
    else:
        create_run_dir.create_run_dir()

    copy_input_data.copy_input_data()
