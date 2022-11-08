tf_var_common_table = (
    # All variables in tf_var_common_table use to automation tcl step scripts. So, you can add every variable you want.
    # All these variables will be automatically added to each step tcl script.

    ['', ''],
    ['', '']
)

# Available process names (names in first column mast be like in mmmc_analysis_view_table)
mmmc_pvt_p_table = (
    ['ss', 'ssg', 'ss_typical_max'],
    ['tt',        'tt_typical_max'],
    ['ff', 'ffg', 'ff_typical_min']
)

# Available voltage names (names in first column mast be like in mmmc_analysis_view_table)
mmmc_pvt_v_table = (
    ['lv', '0p81v'],
    ['tv', '0p90v'],
    ['hv', '0p99v']
)

# Available temperature names (names in first column mast be like in mmmc_analysis_view_table)
mmmc_pvt_t_table = (
    ['m40', 'm40c'],
    ['0',   '0c'],
    ['25',  '25c'],
    ['85',  '85c'],
    ['125', '125c']
)

# Available pvt combination names (must contain all pvt for all views)
mmmc_pvt_table = (
    ['sslvm40', 'worst_case'],
    ['ffhv0',   'best_case']
)

# Available qrcTech names (names in first column mast be like in mmmc_analysis_view_table)
mmmc_pvt_qrc_table = (
    ['cb',  'cbest'],
    ['cw',  'cworst'],
    ['rcb', 'rcbest'],
    ['rcw', 'rcworst'],
    ['ct',  'typical']
)

# Available lib files
mmmc_lib_file_table = (
    ['test_lib', '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_{{ process }}_{{ voltage }}_{{ temperature }}.lib',
                 '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_{{ process_voltage_temperature }}.lib'
     ],
    ['', '']
)

# Available cdb files
mmmc_cdb_file_table = (
    ['test_lib', '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_{{ process }}_{{ voltage }}_{{ temperature }}.cdb',
                 '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_{{ process_voltage_temperature }}.cdb'
     ],
    ['', '']
)

# Available qrcTech files (technology name | qrcTech file)
mmmc_qrc_file_table = (
    ['tech_40', '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.{{ extraction }}'],
    ['', '']
)

# Available derate for each delay corners
# cell_data | cell_early | cell_late | net_data | net_early | net_late
mmmc_ocv_table = (
    ['ss', '*', '*', '*', 's', +1, -2, +3, -4, +5, -6],
    ['ff', '*', '*', '*', 'h', 7, 8, 9, 10, 11, 12]
)

"""
Mandatory variables for phy_gen
"""

phy_lef_table = (
    ['tech_40', '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lef/technology.techlef',
                '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lef/tech_2.techlef'],
    ['test_lib', '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lef/test_file.lef',
                 '/Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lef/test_file_1.lef']
)

phy_verilog_table = (
    ['test_lib', '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/verilog/test_lib_file_1.v',
                 '/Users/leonidnidekker/Dropbox/python/the_flow/tests/src_prj/common_data/verilog/test_lib_file_2.v'],
    ['', '']
)

phy_cl_table = ()
