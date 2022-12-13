import os

# Variables from tf_dir_structure_table describe a user directories structure.
# Be careful, you can't add other variables into tf_dir_structure_table.
tf_dir_structure_table = (
    # Mandatory variables
    ['sdc',            ''],  # <list of dirs>
    ['workarea_syn',   ''],  # <only one dir>
    ['workarea_impl',  ''],  # <only one dir>
    ['workarea_atpg',  ''],  # <only one dir>
    ['workarea_power', ''],  # <only one dir>
    ['syn_steps',      ''],  # <list of dirs>
    ['impl_steps',     ''],  # <list of dirs>
    ['atpg_steps',     ''],  # <list of dirs>
    ['power_steps',    ''],  # <list of dirs>

    # Optional variables
    ['rtl',       ''],  # <list of dirs>
    ['syn_src',   ''],  # <list of dirs>
    ['impl_src',  ''],  # <list of dirs>
    ['atpg_src',  ''],  # <list of dirs>
    ['power_src', '']   # <list of dirs>
)

# Variables from tf_var_table are used to automation step scripts.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script.
tf_var_table = (
    # Mandatory variables
    ['cfg_common', ''],     # Path to directory which contains tf_var_common.py file
    ['DESIGN_NAME', ''],    # Design module name
    ['EXP_NAME_SYN', ''],   # Synthesis experiment name
    ['EXP_NAME_IMPL', ''],  # Implementation experiment name
    ['EXP_NAME_ATPG', ''],  # ATPG experiment name
    ['EXP_NAME_POWER', '']  # Power analysis experiment name

    # Optional
)

# Variables from tf_var_syn_table are used to automation step scripts during [-syn] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-syn] flow.
tf_var_syn_table = (
    ['', ''],
    ['', '']
)

# Variables from tf_var_impl_table are used to automation step scripts during [-impl] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-impl] flow.
tf_var_impl_table = (
    ['', ''],
    ['', '']
)

# Variables from tf_var_atpg_table are used to automation step scripts during [-atpg] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-atpg] flow.
tf_var_atpg_table = (
    ['', ''],
    ['', '']
)

# Variables from tf_var_power_table are used to automation step scripts during [-power] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-power] flow.
tf_var_power_table = (
    ['', ''],
    ['', '']
)

# tf_var_mmmc_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution.
tf_var_mmmc_table = (
    '',
    ''
)

# tf_var_mmmc_syn_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution
# only for [-syn] flow.
tf_var_mmmc_syn_table = (
    '',
    ''
)

# tf_var_mmmc_syn_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution
# only for [-impl] flow.
tf_var_mmmc_impl_table = (
    '',
    ''
)

# tf_var_mmmc_syn_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution
# only for [-atpg] flow.
tf_var_mmmc_atpg_table = (
    '',
    ''
)

# tf_var_mmmc_syn_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution
# only for [-power] flow.
tf_var_mmmc_power_table = (
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


# Variables from mmmc_analysis_view_power_table are used to set analysis views for power analysis
# during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
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
