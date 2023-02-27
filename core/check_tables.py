import tf_var_common
import tf_var
from messages import Messages
import global_tf_vars


def check_tables():

    m = Messages()

    try:
        tf_var_common.mmmc_pvt_p_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_pvt_p_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_pvt_p_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_pvt_v_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_pvt_v_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_pvt_v_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_pvt_t_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_pvt_t_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_pvt_t_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_pvt_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_pvt_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_pvt_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_pvt_qrc_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_pvt_qrc_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_pvt_qrc_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_lib_file_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_lib_file_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_lib_file_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_cdb_file_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_cdb_file_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_cdb_file_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_qrc_file_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_qrc_file_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_qrc_file_table', 'tf_var_common.py')

    try:
        tf_var_common.mmmc_ocv_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_ocv_table', 'tf_var_common.py')
        else:
            m.init_6('mmmc_ocv_table', 'tf_var_common.py')

    try:
        tf_var.mmmc_sdc_mode_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_sdc_mode_table', 'tf_var.py')
        else:
            m.init_6('mmmc_sdc_mode_table', 'tf_var.py')

    try:
        tf_var.tf_var_mmmc_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('tf_var_mmmc_table', 'tf_var.py')
        else:
            m.init_6('tf_var_mmmc_table', 'tf_var.py')

    try:
        tf_var.tf_var_mmmc_syn_table
    except AttributeError:
        m.init_6('tf_var_mmmc_syn_table', 'tf_var.py')
        global_tf_vars.tf_var_mmmc_syn_table_exists = 0

    try:
        tf_var.tf_var_mmmc_impl_table
    except AttributeError:
        m.init_6('tf_var_mmmc_impl_table', 'tf_var.py')
        global_tf_vars.tf_var_mmmc_impl_table_exists = 0

    try:
        tf_var.tf_var_mmmc_atpg_table
    except AttributeError:
        m.init_6('tf_var_mmmc_atpg_table', 'tf_var.py')
        global_tf_vars.tf_var_mmmc_atpg_table_exists = 0

    try:
        tf_var.tf_var_mmmc_power_table
    except AttributeError:
        m.init_6('tf_var_mmmc_power_table', 'tf_var.py')
        global_tf_vars.tf_var_mmmc_power_table_exists = 0

    try:
        tf_var.mmmc_analysis_view_syn_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1:
            m.init_5('mmmc_analysis_view_syn_table', 'tf_var.py')
        else:
            m.init_6('mmmc_analysis_view_syn_table', 'tf_var.py')

    try:
        tf_var.mmmc_analysis_view_impl_table
    except AttributeError:
        if global_tf_vars.tf_is_impl == 1:
            m.init_5('mmmc_analysis_view_impl_table', 'tf_var.py')
        else:
            m.init_6('mmmc_analysis_view_impl_table', 'tf_var.py')

    try:
        tf_var.mmmc_analysis_view_power_table
    except AttributeError:
        if global_tf_vars.tf_is_power == 1:
            m.init_5('mmmc_analysis_view_power_table', 'tf_var.py')
        else:
            m.init_6('mmmc_analysis_view_power_table', 'tf_var.py')

    try:
        tf_var_common.tf_var_common_table
    except AttributeError:
        m.init_5('tf_var_common_table', 'tf_var_common.py')

    try:
        tf_var.tf_step_syn_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1:
            m.init_5('tf_step_syn_table', 'tf_var.py')
        else:
            m.init_6('tf_step_syn_table', 'tf_var.py')

    try:
        tf_var.tf_step_impl_table
    except AttributeError:
        if global_tf_vars.tf_is_impl == 1:
            m.init_5('tf_step_impl_table', 'tf_var.py')
        else:
            m.init_6('tf_step_impl_table', 'tf_var.py')

    try:
        tf_var.tf_step_atpg_table
    except AttributeError:
        if global_tf_vars.tf_is_atpg == 1:
            m.init_5('tf_step_atpg_table', 'tf_var.py')
        else:
            m.init_6('tf_step_atpg_table', 'tf_var.py')

    try:
        tf_var.tf_step_power_table
    except AttributeError:
        if global_tf_vars.tf_is_power == 1:
            m.init_5('tf_step_power_table', 'tf_var.py')
        else:
            m.init_6('tf_step_power_table', 'tf_var.py')

    try:
        tf_var_common.phy_lef_table
    except AttributeError:
        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:
            m.init_5('phy_lef_table', 'tf_var_common.py')
        else:
            m.init_6('phy_lef_table', 'tf_var_common.py')

    try:
        tf_var_common.phy_verilog_table
    except AttributeError:
        if global_tf_vars.tf_is_atpg == 1:
            m.init_5('phy_verilog_table', 'tf_var_common.py')
        else:
            m.init_6('phy_verilog_table', 'tf_var_common.py')

    try:
        tf_var_common.phy_cl_table
    except AttributeError:
        if global_tf_vars.tf_is_power == 1:
            m.init_5('phy_cl_table', 'tf_var_common.py')
        else:
            m.init_6('phy_cl_table', 'tf_var_common.py')

    try:
        tf_var.tf_var_syn_table
    except AttributeError:
        m.init_6('tf_var_syn_table', 'tf_var.py')
        global_tf_vars.tf_var_syn_table_exists = 0

    try:
        tf_var.tf_var_impl_table
    except AttributeError:
        m.init_6('tf_var_impl_table', 'tf_var.py')
        global_tf_vars.tf_var_impl_table_exists = 0

    try:
        tf_var.tf_var_atpg_table
    except AttributeError:
        m.init_6('tf_var_atpg_table', 'tf_var.py')
        global_tf_vars.tf_var_atpg_table_exists = 0

    try:
        tf_var.tf_var_power_table
    except AttributeError:
        m.init_6('tf_var_power_table', 'tf_var.py')
        global_tf_vars.tf_var_power_table_exists = 0
