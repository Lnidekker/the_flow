import os
import datetime

tf_dir_structure_table = (
    # Recommended to use absolute directory path.
    # If you want to use relative path, you have to make corresponding variable in tf_var_table and use syntax like:
    # '/dir1/dir2/' + VAR + '/dir3'

    # Mandatory variables
    ['sdc',           '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/sdc',
                      '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/sdc_'],     # <list of dirs> sdc files
    ['workarea_syn',  '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/workarea'],      # <only one dir> experiments
    ['workarea_impl', '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/workarea'],      # <only one dir> experiments
    ['workarea_atpg', '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/workarea'],
    ['syn_steps',     '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/syn_steps'],
#                      '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/syn_steps_'],   # <only one dir> scripts for synthesis
    ['impl_steps',    '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/impl_steps'],  # <only one dir> scripts for implementation

    # Optional variables
    ['rtl',      '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/rtl',
                 '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/rtl_'],       # <list of dirs> rtl files
    ['syn_src',  '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/syn_src',
                 '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/syn_src_'],  # <list of dirs> source files for synthesis
    ['impl_src', '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/impl_src',
                 '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/soc_top/data/impl_src_']  # <list of dirs> source files for implementation
)

tf_var_table = (
    # All variables in tf_var_table use to automation tcl step scripts. So, you can add every variable you want.
    # All these variables will be automatically added to each step tcl script.

    # Mandatory variables
    ['cfg_common',   '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/cfg'],
    ['DESIGN_NAME',  'soc_top'],   # Name of top or partition module.
    ['EXP_NAME_SYN', str(datetime.date.today())],  # Name of current experiment. This name used like directory name created in workarea.
    ['EXP_NAME_ATPG', 'testing_atpg'],

    # Optional
    ['test_var', '1', '2']
)

# Available sdc modes (mode name | sdc file name)
# SDC files MUST places in the_flow.py/design_name/frontend/sdc
mmmc_sdc_mode_table = (
    ['func', './sdc_dir/sdc_dir_file.sdc', 'constraint_1.sdc', 'constraint_2.sdc'],
    ['scan', 'constraint_3.sdc', 'constraint_4.sdc']
)

tf_var_mmmc_table = (
    'test_lib',
    'tech_40'
)

'''
Synthesis
'''

# Analysis views table
mmmc_analysis_view_syn_table = (
    ['func scan', 'ss', 'lv', 'm40', 'cw', 's h'],
    ['scan',      'ff', 'hv', '0',   'cb', 'h']
)

tf_step_syn_table = (
    [0, 'tf_test_step_1', 'main'],
    [1, 'tf_test_step_2', 'main']
)

'''
Implementation
'''

# Analysis views table
mmmc_analysis_view_impl_table = (
    ['func scan', 'ss', 'lv', 'm40', 'cw', 's h'],
    ['scan',      'ff', 'hv', '0',   'cb', 'h']
)

tf_step_impl_table = (
    [0, 'syn_step_0', 'main', ''],
    [1, 'syn_step_1', 'main', ''],
    [1, 'syn_step_1_1', 'incr', ''],
    [2, 'syn_step_2', 'main', '']
)

tf_step_atpg_table = (
    [0, 'step_name'],
    [1, 'step_name'],
    [1, 'step_name']
)
mmmc_analysis_view_power_table = (
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
)

# tf_step_power_table contains set of steps for power analysis
tf_step_power_table = (
    [0, 'step_name'],
    [1, 'step_name'],
    [1, 'step_name']
)