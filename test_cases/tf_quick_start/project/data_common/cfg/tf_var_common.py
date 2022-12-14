import os

# Variables from tf_var_common_table are used to automation step scripts.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script.
tf_var_common_table = (
    # Optional
    ['', ''],
    ['', '']
)

# Variables from mmmc_pvt_p_table are used to set number of {{ process }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Process mandatory aliases are ss, tt, ff.
mmmc_pvt_p_table = (
    ['ss', 'ss_typical_min'],
    ['tt', 'tt_typical_max'],
    ['ff', 'ff_typical_min']
)

# Variables from mmmc_pvt_v_table are used to set number of {{ voltage }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Voltage mandatory aliases are lv, tv, hv.
mmmc_pvt_v_table = (
    ['lv', '0p81v'],
    ['tv', '0p90v'],
    ['hv', '0p99v']
)

# Variables from mmmc_pvt_t_table are used to set number of {{ temperature }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Temperature mandatory aliases are m40, 0, 25, 85, 125.
mmmc_pvt_t_table = (
    ['m40', 'm40c'],
    ['0',   '0c'],
    ['25',  '25c'],
    ['85',  ''],
    ['125', '125c']
)

# Variables from mmmc_pvt_table are used to set number of {{ process_voltage_temperature }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# pvt mandatory aliases are tttv25, tttv125, sslvm40, sslv0, sslv125, ffhvm40, ffhv0, ffhv125.
mmmc_pvt_table = (
    ['tttv25',  ''],
    ['tttv125', ''],
    ['sslvm40', ''],
    ['sslv0',   ''],
    ['sslv125', ''],
    ['ffhvm40', ''],
    ['ffhv0',   ''],
    ['ffhv125', '']
)

# Variables from mmmc_pvt_qrc_table are used to set number of {{ extraction }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Extraction mandatory aliases are cb, cw, rcb, rcw, ct.
mmmc_pvt_qrc_table = (
    ['cb',  ''],
    ['cw',  ''],
    ['rcb', ''],
    ['rcw', ''],
    ['ct',  '']
)

# Variables from mmmc_lib_file_table are used to configurate library_set during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'lib_file_1', 'lib_file_2', ... ]
mmmc_lib_file_table = (
    ['std_lib', '../../../../src/std/lib/std_lib_hvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                '../../../../src/std/lib/std_lib_lvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                '../../../../src/std/lib/std_lib_rvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib'],
    ['', '']
)

# Variables from mmmc_cdb_file_table are used to configurate library_set during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'cdb_file_1', 'cdb_file_2', ... ]
mmmc_cdb_file_table = (
    ['', ''],
    ['', '']
)

# Variables from mmmc_qrc_file_table are used to configurate rc_corner during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'qrcTech file']
mmmc_qrc_file_table = (
    ['', ''],
    ['', '']
)

# mmmc_ocv_table contains number of ocv derate sets.
# Use the following mandatory template:
#   ['<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>',
#   <cell_data>, <cell_early>, <cell_late>, <net_data>, <net_early>, <net_late>]
mmmc_ocv_table = (
    ['ss', '*', '*', '*', 's', 0, 0, 0, 0, 0, 0],
    ['ff', '*', '*', '*', 'h', 0, 0, 0, 0, 0, 0]
)

# Variables from phy_lef_table are used to configurate lef_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'lef_file_1', 'lef_file_2', ... ]
phy_lef_table = (
    ['', ''],
    ['', '']
)

# Variables from phy_verilog_table are used to configurate verilog_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'verilog_file_1', 'verilog_file_2', ... ]
phy_verilog_table = (
    ['', ''],
    ['', '']
)

# Variables from phy_cl_table are used to configurate cl_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'cl_dir_1', 'cl_dir_2', ... ]
phy_cl_table = (
    ['', ''],
    ['', '']
)
