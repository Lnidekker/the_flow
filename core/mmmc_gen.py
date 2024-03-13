"""
MMMC analysis views generator for Cadence tools in Common_UI mode
"""
import sys
from jinja2 import Template
from itertools import product
import global_tf_vars
import tf_var_tmp
import tf_var_common
from messages import Messages


class MmmcGen(Messages):
    def __init__(self,
                 mmmc_analysis_view_table_,
                 mmmc_pvt_p_table_,
                 mmmc_pvt_v_table_,
                 mmmc_pvt_t_table_,
                 mmmc_pvt_table_,
                 mmmc_lib_file_table_,
                 mmmc_cdb_file_table_,
                 mmmc_pvt_qrc_table_,
                 mmmc_qrc_file_table_,
                 mmmc_sdc_mode_table_,
                 mmmc_ocv_table_
                 ):
        self.mmmc_analysis_view_table = mmmc_analysis_view_table_
        self.mmmc_pvt_p_table = mmmc_pvt_p_table_
        self.mmmc_pvt_v_table = mmmc_pvt_v_table_
        self.mmmc_pvt_t_table = mmmc_pvt_t_table_
        self.mmmc_pvt_table = mmmc_pvt_table_
        self.mmmc_lib_file_table = mmmc_lib_file_table_
        self.mmmc_cdb_file_table = mmmc_cdb_file_table_
        self.mmmc_pvt_qrc_table = mmmc_pvt_qrc_table_
        self.mmmc_qrc_file_table = mmmc_qrc_file_table_
        self.mmmc_sdc_mode_table = mmmc_sdc_mode_table_
        self.mmmc_ocv_table = mmmc_ocv_table_

    def check_pvtq_table_for_repeating_aliases(self, table, table_name):
        for i in range(len(table)):
            for j in range(len(table[i])):
                for k in range(len(table[i])):
                    if table[i][j] == table[i][k] and j != k:
                        self.mmmcgen_3(table[i][j], table_name)

    @staticmethod
    def create_lib_cdb_file_template(sdc_mode, pvt_p, pvt_v, pvt_t, pvt, qrc, mode, template_body):
        t = Template(template_body)
        return t.render(constraint_mode=sdc_mode,
                        process=pvt_p,
                        voltage=pvt_v,
                        temperature=pvt_t,
                        process_voltage_temperature=pvt,
                        extraction=qrc,
                        analysis_mode=mode)

    @staticmethod
    def create_qrc_file_template(pvt_qrc, template_body):
        t = Template(template_body)
        return t.render(extraction=pvt_qrc)

    def parsing_analysis_view_table(self):
        self.tf_info('(TFMmmcGen.parsing_analysis_view_table) start')
        n = 0
        for i in range(len(self.mmmc_analysis_view_table)):
            for mix in product(self.mmmc_analysis_view_table[i][0].split(),
                               self.mmmc_analysis_view_table[i][1].split(),
                               self.mmmc_analysis_view_table[i][2].split(),
                               self.mmmc_analysis_view_table[i][3].split(),
                               self.mmmc_analysis_view_table[i][4].split(),
                               self.mmmc_analysis_view_table[i][5].split()
                               ):
                global_tf_vars.mmmc_analysis_view_table_sdc_mode[n] = mix[0]
                global_tf_vars.mmmc_analysis_view_table_pvt_p[n] = mix[1]
                global_tf_vars.mmmc_analysis_view_table_pvt_v[n] = mix[2]
                global_tf_vars.mmmc_analysis_view_table_pvt_t[n] = mix[3]
                global_tf_vars.mmmc_analysis_view_table_pvt[n] = mix[1] + mix[2] + mix[3]
                global_tf_vars.mmmc_analysis_view_table_parasitic[n] = mix[4]
                global_tf_vars.mmmc_analysis_view_table_mode[n] = mix[5]
                global_tf_vars.mmmc_analysis_view_table_name[n] = mix[0] + '_' + mix[1] + mix[2] + mix[3] + mix[4] + \
                    '_' + mix[5]
                global_tf_vars.mmmc_analysis_view_table_lib[n] = ''
                global_tf_vars.mmmc_analysis_view_table_lib_partitions[n] = ''
                global_tf_vars.mmmc_analysis_view_table_cdb[n] = ''
                global_tf_vars.mmmc_analysis_view_table_qrc[n] = ''
                global_tf_vars.mmmc_analysis_view_table_temperature[n] = ''
                global_tf_vars.mmmc_analysis_view_table_sdc_mode_file[n] = ''
                n = n + 1

        self.tf_info('(TFMmmcGen.parsing_analysis_view_table) finish')

    def make_lib_files_list_for_each_view(self):
        self.tf_info('(TFMmmcGen.make_lib_files_list_for_each_view) start')
        for lib in range(len(self.mmmc_lib_file_table)):
            for preset in range(len(global_tf_vars.tf_var_mmmc_table)):
                if global_tf_vars.tf_var_mmmc_table[preset] == self.mmmc_lib_file_table[lib][0]:
                    for lib_file in range(1, len(tf_var_common.mmmc_lib_file_table[lib])):

                        temp_type_flag_1 = 0
                        temp_type_flag_2 = 0
                        temp_type_flag_3 = 0

                        if '{{ process_voltage_temperature }}' in self.mmmc_lib_file_table[lib][lib_file]:
                            temp_type_flag_2 = 1
                        elif '{{ analysis_mode }}' in self.mmmc_lib_file_table[lib][lib_file]:
                            temp_type_flag_3 = 1
                        else:
                            temp_type_flag_1 = 1

                        existing_flag = 0

                        if temp_type_flag_1 == 1:
                            for p in range(len(self.mmmc_pvt_p_table)):
                                for v in range(len(self.mmmc_pvt_v_table)):
                                    for t in range(len(self.mmmc_pvt_t_table)):
                                        for m in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                                            if self.mmmc_pvt_p_table[p][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_p[m] and \
                                                    self.mmmc_pvt_v_table[v][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_v[m] and \
                                                    self.mmmc_pvt_t_table[t][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_t[m]:
                                                existing_flag = 0
                                                for pvt_pvt in product(self.mmmc_pvt_p_table[p],
                                                                       self.mmmc_pvt_v_table[v],
                                                                       self.mmmc_pvt_t_table[t]):
                                                    answer = self.tf_file_exists_check(
                                                        self.create_lib_cdb_file_template(
                                                            '',
                                                            pvt_pvt[0],
                                                            pvt_pvt[1],
                                                            pvt_pvt[2],
                                                            '',
                                                            '',
                                                            '',
                                                            self.mmmc_lib_file_table[lib][lib_file]))
                                                    if answer == 'True':
                                                        existing_flag = 1
                                                        global_tf_vars.mmmc_analysis_view_table_lib[m] = \
                                                            global_tf_vars.mmmc_analysis_view_table_lib[m] + \
                                                            ' perehod_na_novuy_stroku ' + \
                                                            self.create_lib_cdb_file_template(
                                                                '',
                                                                pvt_pvt[0],
                                                                pvt_pvt[1],
                                                                pvt_pvt[2],
                                                                '',
                                                                '',
                                                                '',
                                                                self.mmmc_lib_file_table[lib][lib_file])

                                                if existing_flag == 0:
                                                    self.mmmcgen_2(
                                                        self.mmmc_lib_file_table[lib][lib_file],
                                                        self.mmmc_pvt_p_table[p][0] +
                                                        self.mmmc_pvt_v_table[v][0] +
                                                        self.mmmc_pvt_t_table[t][0],
                                                        self.mmmc_lib_file_table[lib][0]
                                                    )

                        if temp_type_flag_2 == 1:
                            for i in range(len(self.mmmc_pvt_table)):
                                for view in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
                                    if global_tf_vars.mmmc_analysis_view_table_pvt[view] == self.mmmc_pvt_table[i][0]:
                                        existing_flag = 0
                                        for j in range(len(self.mmmc_pvt_table[i])):
                                            answer = self.tf_file_exists_check(
                                                self.create_lib_cdb_file_template(
                                                    '',
                                                    '',
                                                    '',
                                                    '',
                                                    self.mmmc_pvt_table[i][j],
                                                    '',
                                                    '',
                                                    self.mmmc_lib_file_table[lib][lib_file]))
                                            if answer == 'True':
                                                existing_flag = 1
                                                global_tf_vars.mmmc_analysis_view_table_lib[view] = \
                                                    global_tf_vars.mmmc_analysis_view_table_lib[
                                                        view] + ' perehod_na_novuy_stroku ' + \
                                                    self.create_lib_cdb_file_template(
                                                        '',
                                                        '',
                                                        '',
                                                        '',
                                                        self.mmmc_pvt_table[i][j],
                                                        '',
                                                        '',
                                                        self.mmmc_lib_file_table[lib][lib_file])
                                        if existing_flag == 0:
                                            self.mmmcgen_2(
                                                self.mmmc_lib_file_table[lib][lib_file],
                                                self.mmmc_pvt_table[i][0],
                                                self.mmmc_lib_file_table[lib][0]
                                            )

                        if temp_type_flag_3 == 1:
                            for p in range(len(self.mmmc_pvt_p_table)):
                                for v in range(len(self.mmmc_pvt_v_table)):
                                    for t in range(len(self.mmmc_pvt_t_table)):
                                        for c in range(len(self.mmmc_pvt_qrc_table)):
                                            for m in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                                                if self.mmmc_pvt_p_table[p][0] == \
                                                        global_tf_vars.mmmc_analysis_view_table_pvt_p[m] and \
                                                        self.mmmc_pvt_v_table[v][0] == \
                                                        global_tf_vars.mmmc_analysis_view_table_pvt_v[m] and \
                                                        self.mmmc_pvt_t_table[t][0] == \
                                                        global_tf_vars.mmmc_analysis_view_table_pvt_t[m] and \
                                                        self.mmmc_pvt_qrc_table[c][0] == \
                                                        global_tf_vars.mmmc_analysis_view_table_parasitic[m]:
                                                    existing_flag = 0
                                                    for pvt_pvt in product(
                                                            self.mmmc_pvt_p_table[p],
                                                            self.mmmc_pvt_v_table[v],
                                                            self.mmmc_pvt_t_table[t],
                                                            self.mmmc_pvt_qrc_table[c]):
                                                        answer = self.tf_file_exists_check(
                                                            self.create_lib_cdb_file_template(
                                                                global_tf_vars.mmmc_analysis_view_table_sdc_mode[m],
                                                                pvt_pvt[0],
                                                                pvt_pvt[1],
                                                                pvt_pvt[2],
                                                                '',
                                                                pvt_pvt[3],
                                                                global_tf_vars.mmmc_analysis_view_table_mode[m],
                                                                self.mmmc_lib_file_table[lib][lib_file]))
                                                        if answer == 'True':
                                                            existing_flag = 1
                                                            global_tf_vars.tf_partition_existing = 1
                                                            global_tf_vars.mmmc_analysis_view_table_lib_partitions[m] = \
                                                                global_tf_vars.mmmc_analysis_view_table_lib_partitions[m] + \
                                                                ' perehod_na_novuy_stroku ' + \
                                                                self.create_lib_cdb_file_template(
                                                                    global_tf_vars.mmmc_analysis_view_table_sdc_mode[m],
                                                                    pvt_pvt[0],
                                                                    pvt_pvt[1],
                                                                    pvt_pvt[2],
                                                                    '',
                                                                    pvt_pvt[3],
                                                                    global_tf_vars.mmmc_analysis_view_table_mode[m],
                                                                    self.mmmc_lib_file_table[lib][lib_file])
                                                    if existing_flag == 0:
                                                        self.mmmcgen_2(
                                                            self.mmmc_lib_file_table[lib][lib_file],
                                                            global_tf_vars.mmmc_analysis_view_table_sdc_mode[m] +
                                                            '_' +
                                                            self.mmmc_pvt_p_table[p][0] +
                                                            self.mmmc_pvt_v_table[v][0] +
                                                            self.mmmc_pvt_t_table[t][0] +
                                                            self.mmmc_pvt_qrc_table[c][0] +
                                                            '_' +
                                                            global_tf_vars.mmmc_analysis_view_table_mode[m],
                                                            self.mmmc_lib_file_table[lib][0]
                                                        )

                        if existing_flag == 0:
                            self.mmmcgen_1(self.mmmc_lib_file_table[lib][lib_file], 'mmmc_lib_file_table[' +
                                           global_tf_vars.tf_var_mmmc_table[preset] + ']')

        self.tf_info('(TFMmmcGen.make_lib_files_list_for_each_view) finish')

    def make_cdb_files_list_for_each_view(self):
        self.tf_info('(TFMmmcGen.make_cdb_files_list_for_each_view) start')
        for cdb in range(len(self.mmmc_cdb_file_table)):
            for preset in range(len(global_tf_vars.tf_var_mmmc_table)):
                if global_tf_vars.tf_var_mmmc_table[preset] == self.mmmc_cdb_file_table[cdb][0]:
                    for cdb_file in range(1, len(tf_var_common.mmmc_cdb_file_table[cdb])):

                        temp_type_flag_1 = 0
                        temp_type_flag_2 = 0

                        if '{{ process_voltage_temperature }}' in self.mmmc_cdb_file_table[cdb][cdb_file]:
                            temp_type_flag_2 = 1
                        else:
                            temp_type_flag_1 = 1

                        existing_flag = 0

                        if temp_type_flag_1 == 1:
                            for p in range(len(self.mmmc_pvt_p_table)):
                                for v in range(len(self.mmmc_pvt_v_table)):
                                    for t in range(len(self.mmmc_pvt_t_table)):
                                        for m in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                                            if self.mmmc_pvt_p_table[p][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_p[m] and \
                                                    self.mmmc_pvt_v_table[v][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_v[m] and \
                                                    self.mmmc_pvt_t_table[t][0] == \
                                                    global_tf_vars.mmmc_analysis_view_table_pvt_t[m]:
                                                existing_flag = 0
                                                for pvt in product(self.mmmc_pvt_p_table[p],
                                                                   self.mmmc_pvt_v_table[v],
                                                                   self.mmmc_pvt_t_table[t]):
                                                    answer = self.tf_file_exists_check(
                                                        self.create_lib_cdb_file_template(
                                                            '',
                                                            pvt[0],
                                                            pvt[1],
                                                            pvt[2],
                                                            '',
                                                            '',
                                                            '',
                                                            self.mmmc_cdb_file_table[cdb][cdb_file]))
                                                    if answer == 'True':
                                                        existing_flag = 1
                                                        global_tf_vars.mmmc_analysis_view_table_cdb[m] = \
                                                            global_tf_vars.mmmc_analysis_view_table_cdb[m] + \
                                                            ' perehod_na_novuy_stroku ' + \
                                                            self.create_lib_cdb_file_template(
                                                                '',
                                                                pvt[0],
                                                                pvt[1],
                                                                pvt[2],
                                                                '',
                                                                '',
                                                                '',
                                                                self.mmmc_cdb_file_table[cdb][cdb_file])
                                                if existing_flag == 0:
                                                    self.mmmcgen_2(
                                                        self.mmmc_cdb_file_table[cdb][cdb_file],
                                                        self.mmmc_pvt_p_table[p][0] +
                                                        self.mmmc_pvt_v_table[v][0] +
                                                        self.mmmc_pvt_t_table[t][0],
                                                        self.mmmc_lib_file_table[cdb][0]
                                                    )

                        if temp_type_flag_2 == 1:
                            for i in range(len(self.mmmc_pvt_table)):
                                for view in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
                                    if global_tf_vars.mmmc_analysis_view_table_pvt[view] == self.mmmc_pvt_table[i][0]:
                                        existing_flag = 0
                                        for j in range(len(self.mmmc_pvt_table[i])):
                                            answer = self.tf_file_exists_check(
                                                self.create_lib_cdb_file_template(
                                                    '',
                                                    '',
                                                    '',
                                                    '',
                                                    self.mmmc_pvt_table[i][j],
                                                    '',
                                                    '',
                                                    self.mmmc_cdb_file_table[cdb][cdb_file]))
                                            if answer == 'True':
                                                existing_flag = 1
                                                global_tf_vars.mmmc_analysis_view_table_cdb[view] = \
                                                    global_tf_vars.mmmc_analysis_view_table_cdb[view] + \
                                                    ' perehod_na_novuy_stroku ' + \
                                                    self.create_lib_cdb_file_template(
                                                        '',
                                                        '',
                                                        '',
                                                        '',
                                                        self.mmmc_pvt_table[i][j],
                                                        '',
                                                        '',
                                                        self.mmmc_cdb_file_table[cdb][cdb_file])
                                        if existing_flag == 0:
                                            self.mmmcgen_2(
                                                self.mmmc_cdb_file_table[cdb][cdb_file],
                                                self.mmmc_pvt_table[i][0],
                                                self.mmmc_lib_file_table[cdb][0]
                                            )

                        if existing_flag == 0:
                            self.mmmcgen_1(self.mmmc_cdb_file_table[cdb][cdb_file], 'mmmc_cdb_file_table[' +
                                           global_tf_vars.tf_var_mmmc_table[preset] + ']')

        self.tf_info('(TFMmmcGen.make_cdb_files_list_for_each_view) finish')

    def make_qrc_files_list_for_each_view(self):
        self.tf_info('(TFMmmcGen.make_qrc_files_list_for_each_view) start')
        f = 0
        for n in range(len(self.mmmc_qrc_file_table)):
            for preset in range(len(global_tf_vars.tf_var_mmmc_table)):
                if global_tf_vars.tf_var_mmmc_table[preset] == self.mmmc_qrc_file_table[n][0]:
                    existing_flag = 0
                    for i in range(len(self.mmmc_pvt_qrc_table)):
                        for j in range(len(self.mmmc_pvt_qrc_table[i])):
                            answer = self.tf_file_exists_check(
                                self.create_qrc_file_template(
                                    self.mmmc_pvt_qrc_table[i][j], self.mmmc_qrc_file_table[n][1]))
                            if answer == 'True':
                                existing_flag = 1
                                global_tf_vars.mmmc_analysis_view_table_qrc_all[self.mmmc_pvt_qrc_table[f][0]] = \
                                    self.create_qrc_file_template(
                                        self.mmmc_pvt_qrc_table[i][j], self.mmmc_qrc_file_table[n][1])
                                f = f + 1
                    if existing_flag == 0:
                        self.mmmcgen_1(self.mmmc_qrc_file_table[n][1], 'mmmc_qrc_file_table[' +
                                       global_tf_vars.tf_var_mmmc_table[preset] + ']')

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_qrc)):
            global_tf_vars.mmmc_analysis_view_table_qrc[i] = \
                global_tf_vars.mmmc_analysis_view_table_qrc_all[global_tf_vars.mmmc_analysis_view_table_parasitic[i]]

        self.tf_info('(TFMmmcGen.make_qrc_files_list_for_each_view) finish')

    def make_temperature_for_each_view(self):
        self.tf_info('(TFMmmcGen.make_temperature_for_each_view) start')
        for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_t)):
            if global_tf_vars.mmmc_analysis_view_table_pvt_t[i] == 'm40':
                global_tf_vars.mmmc_analysis_view_table_temperature[i] = '-40'
            else:
                global_tf_vars.mmmc_analysis_view_table_temperature[i] = \
                    global_tf_vars.mmmc_analysis_view_table_pvt_t[i]

        self.tf_info('(TFMmmcGen.make_temperature_for_each_view) finish')

    def make_sdc_files_for_each_view(self):
        self.tf_info('(TFMmmcGen.make_sdc_files_for_each_view) start')

        for i in range(len(self.mmmc_sdc_mode_table)):
            list_ = ''
            for j in range(1, len(self.mmmc_sdc_mode_table[i])):
                if self.tf_file_exists_check(global_tf_vars.tf_run_dir_in_sdc + '/' +
                                             self.mmmc_sdc_mode_table[i][j]) == 'True':
                    if list_ == '':
                        list_ = '../in/sdc/' + self.mmmc_sdc_mode_table[i][j]
                    else:
                        list_ = list_ + ' ' + '../in/sdc/' + self.mmmc_sdc_mode_table[i][j]
                elif self.mmmc_sdc_mode_table[i][j] != '' or self.mmmc_sdc_mode_table[i][0] != '':
                    self.mmmcgen_1(global_tf_vars.tf_run_dir_in_sdc + '/' + self.mmmc_sdc_mode_table[i][j],
                                   'mmmc_sdc_mode_table[' + self.mmmc_sdc_mode_table[i][0] + ']')
            global_tf_vars.mmmc_analysis_view_table_sdc_mode_file_all[self.mmmc_sdc_mode_table[i][0]] = list_

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
            global_tf_vars.mmmc_analysis_view_table_sdc_mode_file[i] = \
                global_tf_vars.mmmc_analysis_view_table_sdc_mode_file_all[
                    global_tf_vars.mmmc_analysis_view_table_sdc_mode[i]]

        self.tf_info('(TFMmmcGen.make_sdc_files_for_each_view) finish')

    @staticmethod
    def make_analysis_view_setup():
        mmmc_analysis_view_setup = ''

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
            if global_tf_vars.mmmc_analysis_view_table_mode[i] == 's':
                mmmc_analysis_view_setup = mmmc_analysis_view_setup + ' ' + \
                                           global_tf_vars.mmmc_analysis_view_table_name[i]

        return mmmc_analysis_view_setup

    @staticmethod
    def make_analysis_view_hold():
        mmmc_analysis_view_hold = ''

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
            if global_tf_vars.mmmc_analysis_view_table_mode[i] == 'h':
                mmmc_analysis_view_hold = mmmc_analysis_view_hold + ' ' + \
                                          global_tf_vars.mmmc_analysis_view_table_name[i]

        return mmmc_analysis_view_hold

    @staticmethod
    def make_analysis_view_power():
        mmmc_analysis_view_power = ''

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_sdc_mode)):
            if global_tf_vars.mmmc_analysis_view_table_mode[i] == 'p':
                mmmc_analysis_view_power = mmmc_analysis_view_power + ' ' + \
                                           global_tf_vars.mmmc_analysis_view_table_name[i]

        return mmmc_analysis_view_power

    @staticmethod
    def create_library_set_template(name, lib_files, cdb_files):
        if cdb_files == "":
            t = Template('create_library_set -name {{ n }} -timing \"{{ lib }}\"')
        else:
            t = Template('create_library_set -name {{ n }} -timing \"{{ lib }}\" -si \"{{ cdb }}\"')
        return t.render(n=name, lib=lib_files, cdb=cdb_files)

    @staticmethod
    def create_timing_condition_template(name, lib_sets):
        t = Template('create_timing_condition -name {{ n }} -library_sets \"{{ libs }}\"')
        return t.render(n=name, libs=lib_sets)

    @staticmethod
    def create_rc_corner_template(name, temperature, qrc_tech):
        t = Template('create_rc_corner -name {{ n }} -temperature {{ te }} -qrc_tech {{ q_t }}')
        return t.render(n=name, te=temperature, q_t=qrc_tech)

    @staticmethod
    def create_delay_corner_template(name, timing_condition, rc_corner):
        t = Template('create_delay_corner -name {{ n }} -timing_condition {{ t_c }} -rc_corner {{ rc_c }}')
        return t.render(n=name, t_c=timing_condition, rc_c=rc_corner)

    @staticmethod
    def create_constraint_mode_template(name, sdc_files):
        t = Template('create_constraint_mode -name {{ n }} -sdc_files \"{{ s_f }}\"')
        return t.render(n=name, s_f=sdc_files)

    @staticmethod
    def create_analysis_view_template(name, constraint_mode, delay_corner):
        t = Template('create_analysis_view -name {{ n }} -constraint_mode {{ c_m }} -delay_corner {{ d_c }}')
        return t.render(n=name, c_m=constraint_mode, d_c=delay_corner)

    @staticmethod
    def set_analysis_view_template(setup, hold):
        t = Template('set_analysis_view -setup \"{{ s }}\" -hold \"{{ h }}\"')
        return t.render(s=setup, h=hold)

    def make_mmmc_config_file(self):
        self.tf_info('(TFMmmcGen.make_mmmc_config_file) start')

        for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
            if global_tf_vars.mmmc_analysis_view_table_lib[i] == '':
                self.tf_error('(MMMC_GEN) lib file set ' +
                              global_tf_vars.mmmc_analysis_view_table_pvt_p[i] +
                              global_tf_vars.mmmc_analysis_view_table_pvt_v[i] +
                              global_tf_vars.mmmc_analysis_view_table_pvt_t[i] + ' for analysis view ' +
                              global_tf_vars.mmmc_analysis_view_table_name[i] + ' is empty')
                exit('exit with error')

        original_stdout = sys.stdout
        mmmc_config_file = global_tf_vars.tf_run_dir_in_cfg + '/mmmc_config.tcl'
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                print(self.create_library_set_template(
                    global_tf_vars.mmmc_analysis_view_table_pvt_p[i] +
                    global_tf_vars.mmmc_analysis_view_table_pvt_v[i] +
                    global_tf_vars.mmmc_analysis_view_table_pvt_t[i],
                    global_tf_vars.mmmc_analysis_view_table_lib[i],
                    global_tf_vars.mmmc_analysis_view_table_cdb[i]
                ))
            if global_tf_vars.tf_partition_existing == 1:
                for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                    print(self.create_library_set_template(
                        global_tf_vars.mmmc_analysis_view_table_name[i],
                        global_tf_vars.mmmc_analysis_view_table_lib_partitions[i],
                        ''
                    ))
            print('#')
        sys.stdout = original_stdout
        self.tf_remove_double_lines(mmmc_config_file)

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            if global_tf_vars.tf_partition_existing == 0:
                for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                    print(self.create_timing_condition_template(
                        global_tf_vars.mmmc_analysis_view_table_name[i],
                        global_tf_vars.mmmc_analysis_view_table_pvt_p[i] +
                        global_tf_vars.mmmc_analysis_view_table_pvt_v[i] +
                        global_tf_vars.mmmc_analysis_view_table_pvt_t[i]
                    ))
            else:
                for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                    print(self.create_timing_condition_template(
                        global_tf_vars.mmmc_analysis_view_table_name[i],
                        global_tf_vars.mmmc_analysis_view_table_pvt_p[i] +
                        global_tf_vars.mmmc_analysis_view_table_pvt_v[i] +
                        global_tf_vars.mmmc_analysis_view_table_pvt_t[i] +
                        ' ' +
                        global_tf_vars.mmmc_analysis_view_table_name[i]
                    ))
            print('##')
        sys.stdout = original_stdout

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                print(self.create_rc_corner_template(
                    global_tf_vars.mmmc_analysis_view_table_parasitic[i] + '_' +
                    global_tf_vars.mmmc_analysis_view_table_pvt_t[i],
                    global_tf_vars.mmmc_analysis_view_table_temperature[i],
                    global_tf_vars.mmmc_analysis_view_table_qrc[i]
                ))
            print('###')
        sys.stdout = original_stdout
        self.tf_remove_double_lines(mmmc_config_file)

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                print(self.create_delay_corner_template(
                    global_tf_vars.mmmc_analysis_view_table_name[i],
                    global_tf_vars.mmmc_analysis_view_table_name[i],
                    global_tf_vars.mmmc_analysis_view_table_parasitic[i] + '_' +
                    global_tf_vars.mmmc_analysis_view_table_pvt_t[i]
                ))
            print('####')
        sys.stdout = original_stdout

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                print(self.create_constraint_mode_template(
                    global_tf_vars.mmmc_analysis_view_table_sdc_mode[i],
                    global_tf_vars.mmmc_analysis_view_table_sdc_mode_file[i]
                ))
            print('#####')
        sys.stdout = original_stdout
        self.tf_remove_double_lines(mmmc_config_file)

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                print(self.create_analysis_view_template(
                    global_tf_vars.mmmc_analysis_view_table_name[i],
                    global_tf_vars.mmmc_analysis_view_table_sdc_mode[i],
                    global_tf_vars.mmmc_analysis_view_table_name[i]
                ))
            print('######')
        sys.stdout = original_stdout

        original_stdout = sys.stdout
        with open(mmmc_config_file, 'a') as f:
            sys.stdout = f
            print(self.set_analysis_view_template(
                self.make_analysis_view_setup() + ' ' + self.make_analysis_view_power(),
                self.make_analysis_view_setup() + ' ' +
                self.make_analysis_view_hold() + ' ' +
                self.make_analysis_view_power()
            ))
        sys.stdout = original_stdout

        with open(mmmc_config_file, 'r') as f:
            data = f.read()
            data = data.replace('#', '')
            data = data.replace('perehod_na_novuy_stroku', '\\\n       ')
            data = data.replace('-name', '\\\n    -name')
            data = data.replace('-timing', '\\\n    -timing')
            data = data.replace('-library_sets', '\\\n    -library_sets')
            data = data.replace('-si', '\\\n    -si')
            data = data.replace('-temperature', '\\\n    -temperature')
            data = data.replace('-qrc_tech', '\\\n    -qrc_tech')
            data = data.replace('-rc_corner', '\\\n    -rc_corner')
            data = data.replace('-sdc_files', '\\\n    -sdc_files')
            data = data.replace('-constraint_mode', '\\\n    -constraint_mode')
            data = data.replace('-delay_corner', '\\\n    -delay_corner')
        with open(mmmc_config_file, 'w') as f:
            f.write(data)

        self.tf_info('(TFMmmcGen.make_mmmc_config_file) finish')

    @staticmethod
    def create_derate_template(delay_corner, cell_dly_data, cell_dly_clk_late, cell_dly_clk_early, net_dly_data,
                               net_dly_clk_late, net_dly_clk_early):
        t = Template('set_timing_derate -delay_corner {{ dc }} -cell_delay -data {{ cdd }}\n'
                     'set_timing_derate -delay_corner {{ dc }} -cell_delay -clock -late {{ cdcl }}\n'
                     'set_timing_derate -delay_corner {{ dc }} -cell_delay -clock -early {{ cdce }}\n'
                     'set_timing_derate -delay_corner {{ dc }} -net_delay -data {{ ndd }}\n'
                     'set_timing_derate -delay_corner {{ dc }} -net_delay -clock -late {{ ndcl }}\n'
                     'set_timing_derate -delay_corner {{ dc }} -net_delay -clock -early {{ ndce }}\n')
        return t.render(dc=delay_corner, cdd=cell_dly_data, cdcl=cell_dly_clk_late, cdce=cell_dly_clk_early,
                        ndd=net_dly_data, ndcl=net_dly_clk_late, ndce=net_dly_clk_early)

    def make_mmmc_derate_file(self):
        self.tf_info('(TFMmmcGen.make_mmmc_derate_file) start')

        for i in range(len(self.mmmc_ocv_table)):
            for j in range(len(self.mmmc_ocv_table[i])):
                if self.mmmc_ocv_table[i][j] == '*':
                    self.mmmc_ocv_table[i][j] = ''
                    for n in range(len(self.mmmc_analysis_view_table)):
                        self.mmmc_ocv_table[i][j] = self.mmmc_ocv_table[i][j] + ' ' + \
                                                    self.mmmc_analysis_view_table[n][j + 1]

        n = 0

        for i in range(len(self.mmmc_ocv_table)):
            for mix in product(
                    self.mmmc_ocv_table[i][0].split(),
                    self.mmmc_ocv_table[i][1].split(),
                    self.mmmc_ocv_table[i][2].split(),
                    self.mmmc_ocv_table[i][3].split(),
                    self.mmmc_ocv_table[i][4].split()
            ):
                global_tf_vars.mmmc_ocv_p[n] = mix[0]
                global_tf_vars.mmmc_ocv_v[n] = mix[1]
                global_tf_vars.mmmc_ocv_t[n] = mix[2]
                global_tf_vars.mmmc_ocv_qrc[n] = mix[3]
                global_tf_vars.mmmc_ocv_mode[n] = mix[4]
                global_tf_vars.mmmc_ocv_cd[n] = tf_var_common.mmmc_ocv_table[i][5]
                global_tf_vars.mmmc_ocv_ce[n] = tf_var_common.mmmc_ocv_table[i][6]
                global_tf_vars.mmmc_ocv_cl[n] = tf_var_common.mmmc_ocv_table[i][7]
                global_tf_vars.mmmc_ocv_nd[n] = tf_var_common.mmmc_ocv_table[i][8]
                global_tf_vars.mmmc_ocv_ne[n] = tf_var_common.mmmc_ocv_table[i][9]
                global_tf_vars.mmmc_ocv_nl[n] = tf_var_common.mmmc_ocv_table[i][10]
                n = n + 1

        original_stdout = sys.stdout
        mmmc_derate_file = global_tf_vars.tf_run_dir_in_cfg + '/mmmc_derate.tcl'
        with open(mmmc_derate_file, 'a') as f:
            sys.stdout = f
            for i in range(len(global_tf_vars.mmmc_ocv_p)):
                for j in range(len(global_tf_vars.mmmc_analysis_view_table_pvt_p)):
                    if global_tf_vars.mmmc_analysis_view_table_pvt_p[j] + \
                            global_tf_vars.mmmc_analysis_view_table_pvt_v[j] + \
                            global_tf_vars.mmmc_analysis_view_table_pvt_t[j] + \
                            global_tf_vars.mmmc_analysis_view_table_parasitic[j] + '_' + \
                            global_tf_vars.mmmc_analysis_view_table_mode[j] == \
                            global_tf_vars.mmmc_ocv_p[i] + \
                            global_tf_vars.mmmc_ocv_v[i] + \
                            global_tf_vars.mmmc_ocv_t[i] + \
                            global_tf_vars.mmmc_ocv_qrc[i] + '_' + \
                            global_tf_vars.mmmc_ocv_mode[i]:
                        print(self.create_derate_template(
                            global_tf_vars.mmmc_analysis_view_table_name[j],
                            1 + global_tf_vars.mmmc_ocv_cd[i] / 100,
                            1 + global_tf_vars.mmmc_ocv_cl[i] / 100,
                            1 + global_tf_vars.mmmc_ocv_ce[i] / 100,
                            1 + global_tf_vars.mmmc_ocv_nd[i] / 100,
                            1 + global_tf_vars.mmmc_ocv_nl[i] / 100,
                            1 + global_tf_vars.mmmc_ocv_ne[i] / 100
                        ))
        sys.stdout = original_stdout
        self.tf_remove_double_lines(mmmc_derate_file)

        self.tf_info('(TFMmmcGen.make_mmmc_derate_file) finish')

    @staticmethod
    def run_mmmc_gen():

        if global_tf_vars.tf_is_syn == 1:
            tf_mmmc_gen = MmmcGen(tf_var_tmp.mmmc_analysis_view_syn_table,
                                  tf_var_common.mmmc_pvt_p_table,
                                  tf_var_common.mmmc_pvt_v_table,
                                  tf_var_common.mmmc_pvt_t_table,
                                  tf_var_common.mmmc_pvt_table,
                                  tf_var_common.mmmc_lib_file_table,
                                  tf_var_common.mmmc_cdb_file_table,
                                  tf_var_common.mmmc_pvt_qrc_table,
                                  tf_var_common.mmmc_qrc_file_table,
                                  tf_var_tmp.mmmc_sdc_mode_table,
                                  tf_var_common.mmmc_ocv_table
                                  )
        elif global_tf_vars.tf_is_impl == 1:
            tf_mmmc_gen = MmmcGen(tf_var_tmp.mmmc_analysis_view_impl_table,
                                  tf_var_common.mmmc_pvt_p_table,
                                  tf_var_common.mmmc_pvt_v_table,
                                  tf_var_common.mmmc_pvt_t_table,
                                  tf_var_common.mmmc_pvt_table,
                                  tf_var_common.mmmc_lib_file_table,
                                  tf_var_common.mmmc_cdb_file_table,
                                  tf_var_common.mmmc_pvt_qrc_table,
                                  tf_var_common.mmmc_qrc_file_table,
                                  tf_var_tmp.mmmc_sdc_mode_table,
                                  tf_var_common.mmmc_ocv_table
                                  )
        elif global_tf_vars.tf_is_power == 1:
            tf_mmmc_gen = MmmcGen(tf_var_tmp.mmmc_analysis_view_power_table,
                                  tf_var_common.mmmc_pvt_p_table,
                                  tf_var_common.mmmc_pvt_v_table,
                                  tf_var_common.mmmc_pvt_t_table,
                                  tf_var_common.mmmc_pvt_table,
                                  tf_var_common.mmmc_lib_file_table,
                                  tf_var_common.mmmc_cdb_file_table,
                                  tf_var_common.mmmc_pvt_qrc_table,
                                  tf_var_common.mmmc_qrc_file_table,
                                  tf_var_tmp.mmmc_sdc_mode_table,
                                  tf_var_common.mmmc_ocv_table
                                  )

        if global_tf_vars.tf_is_syn == 1 or global_tf_vars.tf_is_impl == 1 or global_tf_vars.tf_is_power == 1:

            tf_mmmc_gen.check_pvtq_table_for_repeating_aliases(tf_var_common.mmmc_pvt_p_table, 'mmmc_pvt_p_table')
            tf_mmmc_gen.check_pvtq_table_for_repeating_aliases(tf_var_common.mmmc_pvt_v_table, 'mmmc_pvt_v_table')
            tf_mmmc_gen.check_pvtq_table_for_repeating_aliases(tf_var_common.mmmc_pvt_t_table, 'mmmc_pvt_t_table')
            tf_mmmc_gen.check_pvtq_table_for_repeating_aliases(tf_var_common.mmmc_pvt_table, 'mmmc_pvt_table')
            tf_mmmc_gen.check_pvtq_table_for_repeating_aliases(tf_var_common.mmmc_pvt_qrc_table, 'mmmc_pvt_qrc_table')

            tf_mmmc_gen.parsing_analysis_view_table()
            tf_mmmc_gen.make_lib_files_list_for_each_view()
            tf_mmmc_gen.make_cdb_files_list_for_each_view()
            tf_mmmc_gen.make_qrc_files_list_for_each_view()
            tf_mmmc_gen.make_temperature_for_each_view()
            tf_mmmc_gen.make_sdc_files_for_each_view()
            tf_mmmc_gen.make_mmmc_config_file()
            tf_mmmc_gen.make_mmmc_derate_file()
