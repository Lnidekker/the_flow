import tf_var_common
import tf_var
from messages import messages


def check_tables():

    try:
        tf_var_common.mmmc_pvt_p_table
    except AttributeError:
        messages.init_5('mmmc_pvt_p_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_pvt_v_table
    except AttributeError:
        messages.init_5('mmmc_pvt_v_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_pvt_t_table
    except AttributeError:
        messages.init_5('mmmc_pvt_t_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_pvt_table
    except AttributeError:
        messages.init_5('mmmc_pvt_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_pvt_qrc_table
    except AttributeError:
        messages.init_5('mmmc_pvt_qrc_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_lib_file_table
    except AttributeError:
        messages.init_5('mmmc_lib_file_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_cdb_file_table
    except AttributeError:
        messages.init_5('mmmc_cdb_file_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_qrc_file_table
    except AttributeError:
        messages.init_5('mmmc_qrc_file_table', 'tf_var_common')

    try:
        tf_var_common.mmmc_ocv_table
    except AttributeError:
        messages.init_5('mmmc_ocv_table', 'tf_var_common')

    try:
        tf_var.mmmc_sdc_mode_table
    except AttributeError:
        messages.init_5('mmmc_sdc_mode_table', 'tf_var')

    try:
        tf_var.tf_var_mmmc_table
    except AttributeError:
        messages.init_5('tf_var_mmmc_table', 'tf_var')

    try:
        tf_var.mmmc_analysis_view_syn_table
    except AttributeError:
        messages.init_5('mmmc_analysis_view_syn_table', 'tf_var')

    try:
        tf_var.mmmc_analysis_view_impl_table
    except AttributeError:
        messages.init_5('mmmc_analysis_view_impl_table', 'tf_var')

    try:
        tf_var.mmmc_analysis_view_power_table
    except AttributeError:
        messages.init_5('mmmc_analysis_view_power_table', 'tf_var')

    try:
        tf_var_common.tf_var_common_table
    except AttributeError:
        messages.init_5('tf_var_common_table', 'tf_var_common')

    try:
        tf_var.tf_step_syn_table
    except AttributeError:
        messages.init_5('tf_step_syn_table', 'tf_var')

    try:
        tf_var.tf_step_impl_table
    except AttributeError:
        messages.init_5('tf_step_impl_table', 'tf_var')

    try:
        tf_var.tf_step_atpg_table
    except AttributeError:
        messages.init_5('tf_step_atpg_table', 'tf_var')

    try:
        tf_var.tf_step_power_table
    except AttributeError:
        messages.init_5('tf_step_power_table', 'tf_var')

    try:
        tf_var_common.phy_lef_table
    except AttributeError:
        messages.init_5('phy_lef_table', 'tf_var_common')

    try:
        tf_var_common.phy_verilog_table
    except AttributeError:
        messages.init_5('phy_verilog_table', 'tf_var_common')

    try:
        tf_var_common.phy_cl_table
    except AttributeError:
        messages.init_5('phy_cl_table', 'tf_var_common')
