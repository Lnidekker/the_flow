"""
These functions are used for parsing tf_*_table.
"""
import os
import global_tf_vars
import common_func
from messages import messages


class prepare_tf_vars:

    def __init__(self, tf_dir_structure_table_, tf_var_table_):
        self.tf_dir_structure_table = tf_dir_structure_table_
        self.tf_var_table = tf_var_table_

    def parsing_tf_dir_structure_table(self):
        """
        Parsing tf_dir_structure_table.
        """

        for i in range(len(self.tf_dir_structure_table)):
            if self.tf_dir_structure_table[i][0] == 'sdc':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_sdc_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_sdc_dir[j-1]):
                        common_func.tf_info('tf_sdc_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_sdc_dir[j-1])
                    else:
                        messages.init_1(global_tf_vars.tf_sdc_dir[j-1], 'tf_dir_structure_table[sdc]')
            elif self.tf_dir_structure_table[i][0] == 'workarea_syn':
                global_tf_vars.tf_workarea_syn_dir = self.tf_dir_structure_table[i][1]
                if os.path.isdir(global_tf_vars.tf_workarea_syn_dir):
                    common_func.tf_info('tf_workarea_syn_dir variable is ' + global_tf_vars.tf_workarea_syn_dir)
                else:
                    messages.init_1(global_tf_vars.tf_workarea_syn_dir, 'tf_dir_structure_table[workarea_syn]')
            elif self.tf_dir_structure_table[i][0] == 'workarea_impl':
                global_tf_vars.tf_workarea_impl_dir = self.tf_dir_structure_table[i][1]
                if os.path.isdir(global_tf_vars.tf_workarea_impl_dir):
                    common_func.tf_info('tf_workarea_impl_dir variable is ' + global_tf_vars.tf_workarea_impl_dir)
                else:
                    messages.init_1(global_tf_vars.tf_workarea_impl_dir, 'tf_dir_structure_table[workarea_impl]')
            elif self.tf_dir_structure_table[i][0] == 'workarea_atpg':
                global_tf_vars.tf_workarea_atpg_dir = self.tf_dir_structure_table[i][1]
                if os.path.isdir(global_tf_vars.tf_workarea_atpg_dir):
                    common_func.tf_info('tf_workarea_atpg_dir variable is ' + global_tf_vars.tf_workarea_atpg_dir)
                else:
                    messages.init_1(global_tf_vars.tf_workarea_atpg_dir, 'tf_dir_structure_table[workarea_atpg]')
            elif self.tf_dir_structure_table[i][0] == 'syn_steps':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_syn_steps_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_syn_steps_dir[j-1]):
                        common_func.tf_info('tf_syn_steps_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_syn_steps_dir[j-1])
                    else:
                        messages.init_1(global_tf_vars.tf_syn_steps_dir[j-1], 'tf_dir_structure_table[syn_steps]')
            elif self.tf_dir_structure_table[i][0] == 'impl_steps':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_impl_steps_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_impl_steps_dir[j-1]):
                        common_func.tf_info('tf_impl_steps_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_impl_steps_dir[j-1])
                    else:
                        messages.init_1(global_tf_vars.tf_impl_steps_dir[j-1], 'tf_dir_structure_table[impl_steps]')
            elif self.tf_dir_structure_table[i][0] == 'atpg_steps':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_atpg_steps_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_atpg_steps_dir[j-1]):
                        common_func.tf_info('tf_atpg_steps_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_atpg_steps_dir[j-1])
                    else:
                        messages.init_1(global_tf_vars.tf_atpg_steps_dir[j-1], 'tf_dir_structure_table[atpg_steps]')
            elif self.tf_dir_structure_table[i][0] == 'rtl':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_rtl_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_rtl_dir[j-1]):
                        common_func.tf_info('tf_rtl_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_rtl_dir[j-1])
                    else:
                        messages.init_2(global_tf_vars.tf_rtl_dir[j-1], 'tf_dir_structure_table[rtl]')
            elif self.tf_dir_structure_table[i][0] == 'syn_src':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_syn_src_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_syn_src_dir[j-1]):
                        common_func.tf_info('tf_syn_src_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_syn_src_dir[j-1])
                    else:
                        messages.init_2(global_tf_vars.tf_syn_src_dir[j-1], 'tf_dir_structure_table[syn_src]')
            elif self.tf_dir_structure_table[i][0] == 'impl_src':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_impl_src_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_impl_src_dir[j-1]):
                        common_func.tf_info('tf_impl_src_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_impl_src_dir[j-1])
                    else:
                        messages.init_2(global_tf_vars.tf_impl_src_dir[j-1], 'tf_dir_structure_table[impl_src]')
            elif self.tf_dir_structure_table[i][0] == 'atpg_src':
                for j in range(1, len(self.tf_dir_structure_table[i])):
                    global_tf_vars.tf_atpg_src_dir[j-1] = self.tf_dir_structure_table[i][j]
                    if os.path.isdir(global_tf_vars.tf_atpg_src_dir[j-1]):
                        common_func.tf_info('tf_atpg_src_dir[' + str(j-1) + '] variable is ' +
                                            global_tf_vars.tf_atpg_src_dir[j-1])
                    else:
                        messages.init_2(global_tf_vars.tf_atpg_src_dir[j-1], 'tf_dir_structure_table[atpg_src]')
            else:
                messages.init_3(self.tf_dir_structure_table[i][0])

        if global_tf_vars.tf_sdc_dir == {}:
            if global_tf_vars.tf_is_syn == '1' or global_tf_vars.tf_is_impl == '1':
                messages.init_4('tf_dir_structure_table[sdc]')

        if global_tf_vars.tf_workarea_syn_dir == '' and global_tf_vars.tf_is_syn == '1':
            messages.init_4('tf_dir_structure_table[workarea_syn]')

        if global_tf_vars.tf_workarea_impl_dir == '' and global_tf_vars.tf_is_impl == '1':
            messages.init_4('tf_dir_structure_table[workarea_impl]')

        if global_tf_vars.tf_workarea_atpg_dir == '' and global_tf_vars.tf_is_atpg == '1':
            messages.init_4('tf_dir_structure_table[workarea_atpg]')

        if global_tf_vars.tf_syn_steps_dir == {} and global_tf_vars.tf_is_syn == '1':
            messages.init_4('tf_dir_structure_table[syn_steps]')

        if global_tf_vars.tf_impl_steps_dir == {} and global_tf_vars.tf_is_impl == '1':
            messages.init_4('tf_dir_structure_table[impl_steps]')

        if global_tf_vars.tf_atpg_steps_dir == {} and global_tf_vars.tf_is_atpg == '1':
            messages.init_4('tf_dir_structure_table[atpg_steps]')

    def parsing_tf_var_table(self):
        """
        Parsing tf_var_table.
        """

        for i in range(len(self.tf_var_table)):
            if self.tf_var_table[i][0] == 'DESIGN_NAME':
                global_tf_vars.tf_design_name = self.tf_var_table[i][1]
                common_func.tf_info('Design name is ' + global_tf_vars.tf_design_name + '.')
            elif self.tf_var_table[i][0] == 'EXP_NAME_SYN' and global_tf_vars.tf_is_syn == '1':
                global_tf_vars.tf_exp_name_syn = self.tf_var_table[i][1]
                common_func.tf_info('Synthesis experiment name is ' + global_tf_vars.tf_exp_name_syn + '.')
            elif self.tf_var_table[i][0] == 'EXP_NAME_IMPL' and global_tf_vars.tf_is_impl == '1':
                global_tf_vars.tf_exp_name_impl = self.tf_var_table[i][1]
                common_func.tf_info('Implementation experiment name is ' + global_tf_vars.tf_exp_name_impl + '.')
            elif self.tf_var_table[i][0] == 'EXP_NAME_ATPG' and global_tf_vars.tf_is_atpg == '1':
                global_tf_vars.tf_exp_name_atpg = self.tf_var_table[i][1]
                common_func.tf_info('ATPG experiment name is ' + global_tf_vars.tf_exp_name_atpg + '.')
            elif self.tf_var_table[i][0] == 'cfg_common':
                global_tf_vars.tf_cfg_common_dir = self.tf_var_table[i][1]
                if os.path.isdir(global_tf_vars.tf_cfg_common_dir):
                    common_func.tf_info('tf_cfg_common_dir variable is ' + global_tf_vars.tf_cfg_common_dir)
                else:
                    messages.init_1(global_tf_vars.tf_cfg_common_dir, 'tf_var_table[cfg_common]')

        if global_tf_vars.tf_cfg_common_dir == '':
            messages.init_4('tf_var_table[cfg_common]')

        if global_tf_vars.tf_design_name == '':
            messages.init_4('tf_var_table[DESIGN_NAME]')

        if global_tf_vars.tf_is_syn == '1' and global_tf_vars.tf_exp_name_syn == '':
            messages.init_4('tf_var_table[EXP_NAME_SYN]')

        if global_tf_vars.tf_is_impl == '1' and global_tf_vars.tf_exp_name_impl == '':
            messages.init_4('tf_var_table[EXP_NAME_IMPL]')

        if global_tf_vars.tf_is_atpg == '1' and global_tf_vars.tf_exp_name_atpg == '':
            messages.init_4('tf_var_table[EXP_NAME_ATPG]')
