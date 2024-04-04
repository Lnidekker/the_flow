"""
Physical data generator.
"""
import sys
from jinja2 import Template
import tf_var_common
import global_tf_vars
from messages import Messages


class PhyGen(Messages):

    def __init__(self, phy_lef_table_, phy_verilog_table_, phy_cl_table_, phy_gds_table_):
        self.phy_lef_table = phy_lef_table_
        self.phy_verilog_table = phy_verilog_table_
        self.phy_cl_table = phy_cl_table_
        self.phy_gds_table = phy_gds_table_

    def make_lef_list(self):
        """
        Define global_tf_vars.phy_lef_files variable.
        """

        for i in range(len(self.phy_lef_table)):
            for j in range(len(global_tf_vars.tf_var_mmmc_table)):
                if self.phy_lef_table[i][0] == global_tf_vars.tf_var_mmmc_table[j]:
                    for n in range(1, len(self.phy_lef_table[i])):
                        if self.tf_file_exists_check(self.phy_lef_table[i][n]) == 'True':
                            global_tf_vars.phy_lef_files = global_tf_vars.phy_lef_files + ' \\\n    ' + \
                                                           self.phy_lef_table[i][n]
                        elif self.tf_file_exists_check(self.phy_lef_table[i][n]) == 'False':
                            self.phygen_1(self.phy_lef_table[i][n], 'phy_lef_table')

    @staticmethod
    def create_lef_list_template(phy_lef_files):
        """
        Template for .tcl script.

        :param phy_lef_files: global_tf_vars.phy_lef_files variable.
        :return: set lef_list "{{ phy_lef_files }}"
        """
        t = Template('set lef_list "{{ n }}"')
        return t.render(n=phy_lef_files)

    def make_verilog_list(self):
        """
        Define global_tf_vars.phy_verilog_files variable.
        """

        for i in range(len(self.phy_verilog_table)):
            for j in range(len(global_tf_vars.tf_var_mmmc_table)):
                if self.phy_verilog_table[i][0] == global_tf_vars.tf_var_mmmc_table[j]:
                    for n in range(1, len(self.phy_verilog_table[i])):
                        if self.tf_file_exists_check(self.phy_verilog_table[i][n]) == 'True':
                            global_tf_vars.phy_verilog_files = global_tf_vars.phy_verilog_files + ' \\\n    ' + \
                                                           self.phy_verilog_table[i][n]
                        elif self.tf_file_exists_check(self.phy_verilog_table[i][n]) == 'False':
                            self.phygen_1(self.phy_verilog_table[i][n], 'phy_verilog_table')

    @staticmethod
    def create_verilog_list_template(phy_verilog_files):
        """
        Template for .tcl script.

        :param phy_verilog_files: global_tf_vars.phy_verilog_files variable.
        :return: set verilog_list "{{ phy_verilog_files }}"
        """
        t = Template('set verilog_list "{{ n }}"')
        return t.render(n=phy_verilog_files)

    def make_cl_list(self):
        """
        Define global_tf_vars.phy_cl_files variable.
        """

        for i in range(len(self.phy_cl_table)):
            for j in range(len(global_tf_vars.tf_var_mmmc_table)):
                if self.phy_cl_table[i][0] == global_tf_vars.tf_var_mmmc_table[j]:
                    for n in range(1, len(self.phy_cl_table[i])):
                        if self.tf_dir_exists_check(self.phy_cl_table[i][n]):
                            global_tf_vars.phy_cl_dirs = global_tf_vars.phy_cl_dirs + ' \\\n    ' + \
                                                           self.phy_cl_table[i][n]
                        else:
                            self.phygen_1(self.phy_cl_table[i][n], 'phy_cl_table')

    @staticmethod
    def create_cl_list_template(phy_cl_dirs):
        """
        Template for .tcl script.

        :param phy_cl_dirs: global_tf_vars.phy_cl_dirs variable.
        :return: set cl_list "{{ phy_cl_dirs }}"
        """
        t = Template('set cl_list "{{ n }}"')
        return t.render(n=phy_cl_dirs)

    def make_gds_list(self):
        """
        Define global_tf_vars.phy_gds_files variable.
        """

        for i in range(len(self.phy_gds_table)):
            for j in range(len(global_tf_vars.tf_var_mmmc_table)):
                if self.phy_gds_table[i][0] == global_tf_vars.tf_var_mmmc_table[j]:
                    for n in range(1, len(self.phy_gds_table[i])):
                        if self.tf_file_exists_check(self.phy_gds_table[i][n]) == 'True':
                            global_tf_vars.phy_gds_files = global_tf_vars.phy_gds_files + ' \\\n    ' + \
                                                           self.phy_gds_table[i][n]
                        elif self.tf_file_exists_check(self.phy_gds_table[i][n]) == 'False':
                            self.phygen_1(self.phy_gds_table[i][n], 'phy_gds_table')

    @staticmethod
    def create_gds_list_template(phy_gds_files):
        """
        Template for .tcl script.

        :param phy_gds_files: global_tf_vars.phy_gds_files variable.
        :return: set gds_list "{{ phy_gds_files }}"
        """
        t = Template('set gds_list "{{ n }}"')
        return t.render(n=phy_gds_files)

    @staticmethod
    def make_phy_config_file():
        """
        Create phy_config.tcl file.
        """

        original_stdout = sys.stdout
        phy_config_file = global_tf_vars.tf_run_dir_in_cfg + '/phy_config.tcl'
        with open(phy_config_file, 'a') as f:
            sys.stdout = f
            print(PhyGen.create_lef_list_template(global_tf_vars.phy_lef_files))
            print('')
            print(PhyGen.create_verilog_list_template(global_tf_vars.phy_verilog_files))
            print('')
            print(PhyGen.create_cl_list_template(global_tf_vars.phy_cl_dirs))
            print('')
            print(PhyGen.create_gds_list_template(global_tf_vars.phy_gds_files))
        sys.stdout = original_stdout

    @staticmethod
    def run_phy_gen():

        tf_phy_gen = PhyGen(tf_var_common.phy_lef_table, tf_var_common.phy_verilog_table, tf_var_common.phy_cl_table,
                            tf_var_common.phy_gds_table)
        tf_phy_gen.make_lef_list()
        tf_phy_gen.make_verilog_list()
        tf_phy_gen.make_cl_list()
        tf_phy_gen.make_gds_list()
        tf_phy_gen.make_phy_config_file()
