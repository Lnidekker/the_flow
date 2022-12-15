import os

# Variables from tf_dir_structure_table describe a user directories structure.
# Be careful, you can't add other variables into tf_dir_structure_table.
tf_dir_structure_table = (
    # Mandatory variables
    ['sdc',            os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/sdc',
                       os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/sdc/io'
     ],  # <list of dirs>
    ['workarea_syn',   os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/workarea'],  # <only one dir>
    ['workarea_impl',  os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/workarea'],  # <only one dir>
    ['workarea_atpg',  os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/workarea'],  # <only one dir>
    ['workarea_power', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/workarea'],  # <only one dir>
    ['syn_steps',      os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/data_common/steps'],  # <list of dirs>
    ['impl_steps',     os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/data_common/steps'],  # <list of dirs>
    ['atpg_steps',     os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/data_common/steps'],  # <list of dirs>
    ['power_steps',    os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/data_common/steps'],  # <list of dirs>

    # Optional variables
    ['rtl',       os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/rtl'],  # <list of dirs>
    ['syn_src',   os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/src'],  # <list of dirs>
    ['impl_src',  os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/src'],  # <list of dirs>
    ['atpg_src',  os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/src'],  # <list of dirs>
    ['power_src', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/asic_top/data/src']   # <list of dirs>
)

# Variables from tf_var_table are used to automation step scripts.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script.
tf_var_table = (
    # Mandatory variables
    ['cfg_common',     os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/data_common/cfg'],     # Path to directory which contains tf_var_common.py file
    ['DESIGN_NAME',    'asic_top'],    # Design module name
    ['EXP_NAME_SYN',   'syn_v0'],   # Synthesis experiment name
    ['EXP_NAME_IMPL',  'impl_v0'],  # Implementation experiment name
    ['EXP_NAME_ATPG',  'atpg_v0'],  # ATPG experiment name
    ['EXP_NAME_POWER', 'power_v0'], # Power analysis experiment name

    # Optional
    ['local_var_1', 'value_1', 'value_2'],
    ['local_var_2', 'value_1', 'value_2']
)

# Variables from tf_var_syn_table are used to automation step scripts during [-syn] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-syn] flow.
tf_var_syn_table = (
    ['syn_var_1', 'value_1', 'value_2'],
    ['syn_var_2', 'value_1', 'value_2']
)

# Variables from tf_var_impl_table are used to automation step scripts during [-impl] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-impl] flow.
tf_var_impl_table = (
    ['impl_var_1', 'value_1', 'value_2'],
    ['impl_var_2', 'value_1', 'value_2']
)

# Variables from tf_var_atpg_table are used to automation step scripts during [-atpg] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-atpg] flow.
tf_var_atpg_table = (
    ['atpg_var_1', 'value_1', 'value_2'],
    ['atpg_var_2', 'value_1', 'value_2']
)

# Variables from tf_var_power_table are used to automation step scripts during [-power] flow.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script during [-power] flow.
tf_var_power_table = (
    ['power_var_1', 'value_1', 'value_2'],
    ['power_var_2', 'value_1', 'value_2']
)

# tf_var_mmmc_table contains number of mmmc_preset which are used during mmmc_gen and phy_gen execution.
tf_var_mmmc_table = (
    'tech',
    'std_lib',
    'mem'
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
    'partitions',
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
    ['func', 'func_clocks.sdc',
             'func_io.sdc'
     ],
    ['scan_capture', 'scan_capture_clocks.sdc',
                     'scan_capture_io.sdc'
     ],
    ['scan_shift', 'scan_shift_clocks.sdc',
                   'scan_shift_io.sdc'
     ]
)

# Variables from mmmc_analysis_view_syn_table are used to set analysis views for synthesis during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
mmmc_analysis_view_syn_table = (
    ['func scan_capture scan_shift', 'ss', 'lv', '125', 'cw', 's h'],
    ['', '', '', '', '', '']
)

# tf_step_syn_table contains set of steps for synthesis.
tf_step_syn_table = (
    [0, 'tf_syn_step_1'],
    [1, 'tf_syn_step_2'],
    [1, 'tf_syn_step_3']
)

# Variables from mmmc_analysis_view_impl_table are used to set analysis views for implementation
# during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
mmmc_analysis_view_impl_table = (
    ['func scan_capture scan_shift', 'ss', 'lv', '125', 'cw', 's'],
    ['func scan_capture scan_shift', 'ff', 'hv', '0', 'cb', 'h']
)

# tf_step_impl_table contains set of steps for implementation.
tf_step_impl_table = (
    [0, 'tf_impl_step_1'],
    [1, 'tf_impl_step_2'],
    [1, 'tf_impl_step_3']
)

# tf_step_atpg_table contains set of steps for ATPG.
tf_step_atpg_table = (
    [0, 'tf_atpg_step_1'],
    [1, 'tf_atpg_step_2'],
    [1, 'tf_atpg_step_3']
)

# Variables from mmmc_analysis_view_power_table are used to set analysis views for power analysis
# during mmmc_gen execution.
# Use the following mandatory template:
#   ['<constraint mode>', '<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>']
# Types of analysis: s - setup; h - hold.
mmmc_analysis_view_power_table = (
    ['func', 'ff', 'hv', '0', 'cb', 's h'],
    ['', '', '', '', '', '']
)

# tf_step_power_table contains set of steps for power analysis
tf_step_power_table = (
    [0, 'tf_power_step_1'],
    [1, 'tf_power_step_1'],
    [1, 'tf_power_step_1']
)
