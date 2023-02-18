"""
Copy input data to according directories in tf_run_dir.
Be careful, command also copied all attached files and directories.
"""
import os
import shutil
import glob
import global_tf_vars
from common_func import CommonFunc


def copy_input_data():
    """
    Copy data from tf_sdc_dir to tf_run_dir_in_sdc.
    Copy data from tf_rtl_dir to tf_run_dir_in_rtl.
    Copy data from tf_syn_src_dir to tf_run_dir_in_src.
    Copy data from tf_impl_src_dir to tf_run_dir_in_src.
    """

    if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
        for i in range(len(global_tf_vars.tf_sdc_dir)):
            for j in glob.glob(global_tf_vars.tf_sdc_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_sdc, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_sdc)

    if global_tf_vars.tf_is_syn == 1:
        for i in range(len(global_tf_vars.tf_rtl_dir)):
            for j in glob.glob(global_tf_vars.tf_rtl_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_rtl, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_rtl)

    if global_tf_vars.tf_is_syn == 1:
        for i in range(len(global_tf_vars.tf_syn_src_dir)):
            for j in glob.glob(global_tf_vars.tf_syn_src_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_src, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_src)

    if global_tf_vars.tf_is_impl == 1:
        for i in range(len(global_tf_vars.tf_impl_src_dir)):
            for j in glob.glob(global_tf_vars.tf_impl_src_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_src, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_src)

    if global_tf_vars.tf_is_atpg == 1:
        for i in range(len(global_tf_vars.tf_atpg_src_dir)):
            for j in glob.glob(global_tf_vars.tf_atpg_src_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_src, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_src)

    if global_tf_vars.tf_is_power == 1:
        for i in range(len(global_tf_vars.tf_power_src_dir)):
            for j in glob.glob(global_tf_vars.tf_power_src_dir[i], recursive=True):
                shutil.copytree(j, global_tf_vars.tf_run_dir_in_src, dirs_exist_ok=True)
                CommonFunc.tf_info('Directory ' + j + ' has been copied to ' + global_tf_vars.tf_run_dir_in_src)

    os.system('chmod 750 -R ' + global_tf_vars.tf_run_dir)
