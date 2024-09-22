"""
Create run directory for experiment in tf_dir_structure_table[workarea_*] according to tf_var_table[EXP_NAME_*].

Run directory structure:

    workarea
    +-- EXP_NAME_*
    |   +-- db
    |   +-- in
    |   |   +-- cdb
    |   |   +-- cfg
    |   |   +-- cl
    |   |   +-- lef
    |   |   +-- lib
    |   |   +-- rtl
    |   |   +-- sdc
    |   |   +-- src
    |   |   +-- vlg
    |   +-- logs
    |   +-- out
    |   +-- reports
    |   +-- scripts
    |   +-- work
"""
import os
import global_tf_vars
from common_func import CommonFunc


def run_dir_structure_is():
    """
    Define needed global_tf_vars for run dir creation.
    """

    if global_tf_vars.tf_is_syn == 1:
        global_tf_vars.tf_run_dir = global_tf_vars.tf_workarea_syn_dir + '/' + global_tf_vars.tf_exp_name_syn
    elif global_tf_vars.tf_is_impl == 1:
        global_tf_vars.tf_run_dir = global_tf_vars.tf_workarea_impl_dir + '/' + global_tf_vars.tf_exp_name_impl
    elif global_tf_vars.tf_is_atpg == 1:
        global_tf_vars.tf_run_dir = global_tf_vars.tf_workarea_atpg_dir + '/' + global_tf_vars.tf_exp_name_atpg
    elif global_tf_vars.tf_is_power == 1:
        global_tf_vars.tf_run_dir = global_tf_vars.tf_workarea_power_dir + '/' + global_tf_vars.tf_exp_name_power
    elif global_tf_vars.tf_is_formal == 1:
        global_tf_vars.tf_run_dir = global_tf_vars.tf_workarea_formal_dir + '/' + global_tf_vars.tf_exp_name_formal

    global_tf_vars.tf_run_dir_db = global_tf_vars.tf_run_dir + '/db'
    global_tf_vars.tf_run_dir_in = global_tf_vars.tf_run_dir + '/in'
    global_tf_vars.tf_run_dir_in_cdb = global_tf_vars.tf_run_dir_in + '/cdb'
    global_tf_vars.tf_run_dir_in_cfg = global_tf_vars.tf_run_dir_in + '/cfg'
    global_tf_vars.tf_run_dir_in_cl = global_tf_vars.tf_run_dir_in + '/cl'
    global_tf_vars.tf_run_dir_in_gds = global_tf_vars.tf_run_dir_in + '/gds'
    global_tf_vars.tf_run_dir_in_lef = global_tf_vars.tf_run_dir_in + '/lef'
    global_tf_vars.tf_run_dir_in_lib = global_tf_vars.tf_run_dir_in + '/lib'
    global_tf_vars.tf_run_dir_in_rtl = global_tf_vars.tf_run_dir_in + '/rtl'
    global_tf_vars.tf_run_dir_in_sdc = global_tf_vars.tf_run_dir_in + '/sdc'
    global_tf_vars.tf_run_dir_in_src = global_tf_vars.tf_run_dir_in + '/src'
    global_tf_vars.tf_run_dir_in_vlg = global_tf_vars.tf_run_dir_in + '/vlg'
    global_tf_vars.tf_run_dir_logs = global_tf_vars.tf_run_dir + '/logs'
    global_tf_vars.tf_run_dir_out = global_tf_vars.tf_run_dir + '/out'
    global_tf_vars.tf_run_dir_reports = global_tf_vars.tf_run_dir + '/reports'
    global_tf_vars.tf_run_dir_scripts = global_tf_vars.tf_run_dir + '/scripts'
    global_tf_vars.tf_run_dir_work = global_tf_vars.tf_run_dir + '/work'
    global_tf_vars.tf_run_dir_work_tmp = global_tf_vars.tf_run_dir_work + '/tmp'


def create_run_dir():
    """
    Run dir creation function.
    """

    run_dir_structure_is()

    for i in global_tf_vars.tf_run_dir, \
            global_tf_vars.tf_run_dir_db, \
            global_tf_vars.tf_run_dir_in, \
            global_tf_vars.tf_run_dir_in_cdb, \
            global_tf_vars.tf_run_dir_in_cfg, \
            global_tf_vars.tf_run_dir_in_cl, \
            global_tf_vars.tf_run_dir_in_gds, \
            global_tf_vars.tf_run_dir_in_lef, \
            global_tf_vars.tf_run_dir_in_lib, \
            global_tf_vars.tf_run_dir_in_rtl,\
            global_tf_vars.tf_run_dir_in_sdc, \
            global_tf_vars.tf_run_dir_in_src, \
            global_tf_vars.tf_run_dir_in_vlg, \
            global_tf_vars.tf_run_dir_logs, \
            global_tf_vars.tf_run_dir_out, \
            global_tf_vars.tf_run_dir_reports,\
            global_tf_vars.tf_run_dir_scripts, \
            global_tf_vars.tf_run_dir_work, \
            global_tf_vars.tf_run_dir_work_tmp:

        os.mkdir(i)
        CommonFunc.tf_info('Directory ' + i + ' has been created.')
