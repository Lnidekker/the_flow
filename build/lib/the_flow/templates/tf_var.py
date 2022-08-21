"""
This file contains mandatory THE FLOW tables.

Be careful:
    - Each table must have 2x2 minimum size:
        tf_<name>_table = (
            ['variable_1_name', 'variable_1_value_1', 'variable_1_value_2', ... , 'variable_1_value_N'],
            ['variable_2_name', 'variable_2_value_1', 'variable_2_value_2', ... , 'variable_2_value_N'],
            ... ,
            ['variable_M_name', 'variable_M_value_1', 'variable_M_value_2', ... , 'variable_M_value_N']
        )

Example of directories structure and mandatory tf_*.py files:

    project_home
    +-- common_data
    |   +-- cfg
    |   |   +-- tf_var_common.py
    |   +-- rtl
    +-- soc_top
    |   +-- data
    |   |   +-- atpg_steps
    |   |   |   +-- tf_atpg_step.py
    |   |   +-- atpg_src
    |   |   +-- cfg
    |   |   |   +-- tf_var.py
    |   |   +-- impl_src
    |   |   +-- impl_steps
    |   |   |   +-- tf_impl_step.py
    |   |   +-- sdc
    |   |   +-- syn_src
    |   |   +-- syn_steps
    |   |   |   +-- tf_syn_step.py
    |   +-- workarea
"""
import os

# Variables from tf_dir_structure_table describe a user directories structure.
# Be careful, you can't add other variables into tf_dir_structure_table.
tf_dir_structure_table = (
    # Mandatory variables
    ['sdc', ''],            # <list of dirs> example: project_home/soc_top/data/sdc
    ['workarea_syn', ''],   # <only one dir> example: project_home/soc_top/workarea
    ['workarea_impl', ''],  # <only one dir> example: project_home/soc_top/workarea
    ['workarea_atpg', ''],  # <only one dir> example: project_home/soc_top/workarea
    ['syn_steps', ''],      # <list of dirs> example: project_home/soc_top/data/syn_steps
    ['impl_steps', ''],     # <list of dirs> example: project_home/soc_top/data/impl_steps
    ['atpg_steps', ''],     # <list of dirs> example: project_home/soc_top/data/atpg_steps

    # Optional variables
    ['rtl', ''],       # <list of dirs> example: project_home/common_data/rtl
    ['syn_src', ''],   # <list of dirs> example: project_home/soc_top/data/syn_src
    ['impl_src', ''],  # <list of dirs> example: project_home/soc_top/data/impl_src
    ['atpg_src', '']   # <list of dirs> example: project_home/soc_top/data/atpg_src
)

# Variables from tf_var_table are used to automation step scripts.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script.
tf_var_table = (
    # Mandatory variables
    ['cfg_common', ''],     # Path to directory which contains tf_var_common.py file.
    ['DESIGN_NAME', ''],    # Top module name.
    ['EXP_NAME_SYN', ''],   # Synthesis experiment name.
    ['EXP_NAME_IMPL', ''],  # Implementation experiment name.
    ['EXP_NAME_ATPG', '']   # ATPG experiment name.

    # Optional
)

# tf_var_mmmc_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution.
tf_var_mmmc_table = (
    '',
    ''
)

# Variables from mmmc_sdc_mode_table are used to set constraint modes during mmmc_gen execution.
# Use the following mandatory template: ['<constraint mode name>', '<sdc file name>']
# SDC files will be searched in tf_dir_structure_table[sdc] directories.
mmmc_sdc_mode_table = (
    ['', ''],
    ['', '']
)

# Variables from mmmc_analysis_view_syn_table are used to set analysis views for synthesis during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
mmmc_analysis_view_syn_table = (
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
)

# tf_step_syn_table contains set of steps for synthesis.
tf_step_syn_table = (
    [0, 'step_name'],
    [1, 'step_name'],
    [1, 'step_name']
)

# Variables from mmmc_analysis_view_impl_table are used to set analysis views for implementation
# during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
mmmc_analysis_view_impl_table = (
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
)

# tf_step_impl_table contains set of steps for implementation.
tf_step_impl_table = (
    [0, 'step_name'],
    [1, 'step_name'],
    [1, 'step_name']
)

# tf_step_atpg_table contains set of steps for ATPG.
tf_step_atpg_table = (
    [0, 'step_name'],
    [1, 'step_name'],
    [1, 'step_name']
)
