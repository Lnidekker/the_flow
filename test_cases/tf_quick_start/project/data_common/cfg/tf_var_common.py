import os

# Variables from tf_var_common_table are used to automation step scripts.
# So, you can add every optional variables you want, because all of these
# will be automatically added to each .tcl step script.
tf_var_common_table = (
    # Optional
    ['global_var_1', 'value_1', 'value_2'],
    ['global_var_1', 'value_1', 'value_2']
)

# Variables from mmmc_pvt_p_table are used to set number of {{ process }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Process mandatory aliases are ss, tt, ff.
mmmc_pvt_p_table = (
    ['ss', 'ss_typical_max'],
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
    ['tttv25',  'tc'],
    ['tttv125', ''],
    ['sslvm40', 'wcl'],
    ['sslv0',   ''],
    ['sslv125', 'wc'],
    ['ffhvm40', 'lt'],
    ['ffhv0',   'bc'],
    ['ffhv125', 'ml']
)

# Variables from mmmc_pvt_qrc_table are used to set number of {{ extraction }} mmmc_gen parameter.
# Use the following mandatory template: ['<mandatory alias>', '<name_1>', '<name_2>', ... ]
# Extraction mandatory aliases are cb, cw, rcb, rcw, ct.
mmmc_pvt_qrc_table = (
    ['cb',  'cbest'],
    ['cw',  'cworst'],
    ['rcb', 'rcbest'],
    ['rcw', 'rcworst'],
    ['ct',  'typical']
)

# Variables from mmmc_lib_file_table are used to configurate library_set during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'lib_file_1', 'lib_file_2', ... ]
mmmc_lib_file_table = (
    ['std_lib', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lib/std_lib_hvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lib/std_lib_lvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lib/std_lib_rvt_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/mem/lib/memory_tc.lib'
     ],
    ['mem', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/mem/lib/memory_{{ process_voltage_temperature }}.lib'
     ],
    ['partitions', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/block/lib/block_{{ constraint_mode }}_{{ process }}{{ voltage }}{{ temperature }}{{ extraction }}_{{ analysis_mode }}.lib'
     ]
)

# Variables from mmmc_cdb_file_table are used to configurate library_set during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'cdb_file_1', 'cdb_file_2', ... ]
mmmc_cdb_file_table = (
    ['std_lib', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/celtic/std_lib_hvt_{{ process }}_{{ voltage }}_{{ temperature }}.cdb',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/celtic/std_lib_lvt_{{ process }}_{{ voltage }}_{{ temperature }}.cdb',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/celtic/std_lib_rvt_{{ process }}_{{ voltage }}_{{ temperature }}.cdb'
     ],
    ['', '']
)

# Variables from mmmc_qrc_file_table are used to configurate rc_corner during mmmc_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'qrcTech file']
mmmc_qrc_file_table = (
    ['tech', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/process/qrcTech/{{ extraction }}/qrcTechFile'],
    ['', '']
)

# mmmc_ocv_table contains number of ocv derate sets.
# Use the following mandatory template:
#   ['<process>', '<voltage>', '<temperature>', '<extraction>', '<type of analysis>',
#   <cell_data>, <cell_early>, <cell_late>, <net_data>, <net_early>, <net_late>]
mmmc_ocv_table = (
    ['ss', '*', '*', '*', 's', +0, -7, +0, +0, -7, +0],
    ['ss', '*', '*', '*', 'h', -9, -9, +0, -9, -9, +0],
    ['ff', '*', '*', '*', 'h', +0, +0, +9, +0, +0, +9]
)

# Variables from phy_lef_table are used to configurate lef_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'lef_file_1', 'lef_file_2', ... ]
phy_lef_table = (
    ['tech', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/process/techlef/tech.tlef'
     ],
    ['std_lib', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lef/std_lib_hvt.lef',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lef/std_lib_lvt.lef',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/lef/std_lib_rvt.lef'
     ],
    ['mem', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/mem/lef/memory.lef'
     ],
    ['partitions', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/project/block/lef/block.lef'
     ]
)

# Variables from phy_verilog_table are used to configurate verilog_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'verilog_file_1', 'verilog_file_2', ... ]
phy_verilog_table = (
    ['std_lib', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/verilog/std_lib_hvt.v',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/verilog/std_lib_lvt.v',
                os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/verilog/std_lib_rvt.v'
     ],
    ['mem', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/mem/verilog/memory.v'
     ]
)

# Variables from phy_cl_table are used to configurate cl_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'cl_dir_1', 'cl_dir_2', ... ]
phy_cl_table = (
    ['std_lib', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/std/cl_view/std_ml.cl'],
    ['mem', os.environ['TF_PATH'] + '/test_cases/tf_quick_start/src/mem/cl_view/mem_ml.cl']
)

# Variables from phy_gds_table are used to configurate gds_list during phy_gen execution.
# Use the following mandatory template: ['<mmmc_preset name>', 'gds_file_1', 'gds_file_2', ... ]
phy_gds_table = (
    ['', ''],
    ['', '']
)