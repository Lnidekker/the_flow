import sys, os, glob, shutil
from messages import Messages


class TclScrGen(Messages):

    def __init__(self,
                 step_dir,
                 step_table,
                 tf_run_dir_scripts,
                 tf_run_dir_work_tmp,
                 tf_tmp_file_steps_import,
                 tf_tmp_step_table,
                 flow_name,
                 tf_var_table,
                 tf_var_flow_table,
                 tf_var_common_table,
                 tf_var_mmmc_table,
                 mmmc_sdc_mode_table,
                 tf_run_dir_in_cfg
                 ):
        self.step_dir = step_dir
        self.step_table = step_table
        self.tf_run_dir_scripts = tf_run_dir_scripts
        self.tf_run_dir_work_tmp = tf_run_dir_work_tmp
        self.tf_tmp_file_steps_import = tf_tmp_file_steps_import
        self.tf_tmp_step_table = tf_tmp_step_table
        self.flow_name = flow_name
        self.tf_var_table = tf_var_table
        self.tf_var_flow_table = tf_var_flow_table
        self.tf_var_common_table = tf_var_common_table
        self.tf_var_mmmc_table = tf_var_mmmc_table
        self.mmmc_sdc_mode_table = mmmc_sdc_mode_table
        self.tf_run_dir_in_cfg = tf_run_dir_in_cfg

    def check_steps(self):

        step_file_list = {}
        step_dirs_list = {}
        step_file_list_flag = 0

        for i in range(len(self.step_dir)):
            sys.path.append(self.step_dir[i])
            os.chdir(self.step_dir[i])
            for j in glob.glob('tf*.py'):
                step_file_list[step_file_list_flag] = j
                step_dirs_list[step_file_list_flag] = self.step_dir[i]
                step_file_list_flag = step_file_list_flag + 1

        for i in range(len(step_file_list)):
            flag = 0
            for j in range(len(step_file_list)):
                if step_file_list[i] == step_file_list[j]:
                    flag = flag + 1
                if flag > 1:
                    self.tclscr_1(step_file_list[i], step_dirs_list[i] + '/' + step_file_list[i] + ' and ' +
                                  step_dirs_list[j] + '/' + step_file_list[j] + '.')

        for s in range(len(self.step_table)):
            name_counter = 0
            file_counter = {}
            for i in range(len(self.step_dir)):
                sys.path.append(self.step_dir[i])
                os.chdir(self.step_dir[i])
                for j in glob.glob('tf*.py'):
                    with open(j, 'r') as file:
                        for line_number, line in enumerate(file, start=1):
                            if self.step_table[s][1] + ' ' in line:
                                if self.step_table[s][1] != '' and \
                                        self.step_table[s][1][0] == 't' and \
                                        self.step_table[s][1][1] == 'f' and \
                                        self.step_table[s][1][2] == '_':
                                    file_counter[name_counter] = self.step_dir[i] + '/' + j
                                    name_counter = name_counter + 1
            if name_counter > 1:
                files = ''
                for i in range(len(file_counter)):
                    files = files + ', ' + file_counter[i]
                self.tclscr_2(self.step_table[s][1], files, str(name_counter))

    def create_tf_tmp_file_steps_import_file(self):

        original_stdout = sys.stdout
        with open(self.tf_tmp_file_steps_import, 'a') as f:
            sys.stdout = f
            for i in range(len(self.step_dir)):
                sys.path.append(self.step_dir[i])
                os.chdir(self.step_dir[i])
                for j in glob.glob('tf*.py'):
                    print('from ' + j + ' import *')
        sys.stdout = original_stdout

        with open(self.tf_tmp_file_steps_import, 'r') as f:
            data = f.read()
            data = data.replace('.py', '')
        with open(self.tf_tmp_file_steps_import, 'w') as f:
            f.write(data)

    def create_tf_tmp_step_table_file(self):

        original_stdout = sys.stdout

        with open(self.tf_tmp_step_table, 'a') as f:
            sys.stdout = f
            print('from tf_tmp_file_steps_import import *')
            print('')
            print('tf_tmp_step_table = (')
            n = 1
            for i in range(len(self.step_table)):
                if self.step_table[i][1] == '':
                    n = n + 1
            flag = 0
            for i in range(len(self.step_table)):
                if self.step_table[i][1] != '':
                    flag = flag + 1
                    if self.step_table[i][0] == 0:
                        print('    [0, \'' + self.step_table[i][1] + '\', ' + self.step_table[i][1] + '],')
                    elif i < int(len(self.step_table)) - n:
                        print('    [1, \'' + self.step_table[i][1] + '\', ' + self.step_table[i][1] + '],')
                    else:
                        print('    [1, \'' + self.step_table[i][1] + '\', ' + self.step_table[i][1] + ']')
            if flag < 2:
                print('    [1, \'\', \'\']')
            print(')')
        sys.stdout = original_stdout

    def create_tcl_scripts_for_each_step(self, step_name, previous_step_name, step_body):

        self.tf_info('(TFPrepareData.make_tcl_scripts_for_each_steps) start')

        original_stdout = sys.stdout
        tf_step_tcl_file = self.tf_run_dir_scripts + '/' + step_name + '.tcl'
        with open(tf_step_tcl_file, 'a') as f:

            sys.stdout = f
            print('# Steps')
            print('set STEP_NAME \"' + step_name + '\"')
            print('set PREVIOUS_STEP_NAME \"' + previous_step_name + '\"')
            print('')
            if self.flow_name == 'syn' or self.flow_name == 'impl' or self.flow_name == 'power':
                print('if {$PREVIOUS_STEP_NAME != \"\"} {read_db ../db/$PREVIOUS_STEP_NAME.db}')
            print('')
            print('source ../in/cfg/vars_config.tcl')
            print('')
            print('# STEP START')
            print(step_body)
            print('# STEP FINISH')
            print('')
            if self.flow_name == 'syn':
                print('write_db -all_root_attributes ../db/' + step_name + '.db')
            elif self.flow_name == 'impl':
                print('write_db -lib -sdc -def ../db/' + step_name + '.db')
            elif self.flow_name == 'power':
                print('write_db ../db/' + step_name + '.db')
            print('')
            print('exit')

        sys.stdout = original_stdout

        self.tf_info('(TFPrepareData.make_tcl_scripts_for_each_steps) finish')

    def create_vars_config(self):

        original_stdout = sys.stdout

        tf_vars_config_tcl_file = self.tf_run_dir_in_cfg + '/vars_config.tcl'

        if self.tf_file_exists_check(tf_vars_config_tcl_file) == 'True':
            os.remove(tf_vars_config_tcl_file)

        with open(tf_vars_config_tcl_file, 'a') as f:
            sys.stdout = f

            print('# Flow type')
            print('set FLOW \"' + self.flow_name + '\"')
            print('')

            print('# Variables from tf_var_common.tf_var_common_table')
            for i in range(len(self.tf_var_common_table)):
                list_ = ''
                for j in range(1, len(self.tf_var_common_table[i])):
                    if list_ == '':
                        list_ = self.tf_var_common_table[i][j]
                    else:
                        list_ = list_ + ' ' + self.tf_var_common_table[i][j]
                if self.tf_var_common_table[i][0] != '':
                    print('set ' + self.tf_var_common_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# Variables from tf_var.tf_var_table')
            for i in range(len(self.tf_var_table)):
                list_ = ''
                for j in range(1, len(self.tf_var_table[i])):
                    if list_ == '':
                        list_ = self.tf_var_table[i][j]
                    else:
                        list_ = list_ + ' ' + self.tf_var_table[i][j]
                if self.tf_var_table[i][0] != '':
                    print('set ' + self.tf_var_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# Variables from tf_var.tf_var_' + self.flow_name + '_table')
            if self.tf_var_flow_table != '':
                for i in range(len(self.tf_var_flow_table)):
                    list_ = ''
                    for j in range(1, len(self.tf_var_flow_table[i])):
                        if list_ == '':
                            list_ = self.tf_var_flow_table[i][j]
                        else:
                            list_ = list_ + ' ' + self.tf_var_flow_table[i][j]
                    if self.tf_var_flow_table[i][0] != '':
                        print('set ' + self.tf_var_flow_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# MMMC presets from tf_var.tf_var_mmmc_table')
            list_ = ''
            for i in range(0, len(self.tf_var_mmmc_table)):
                if list_ == '':
                    list_ = self.tf_var_mmmc_table[i]
                else:
                    list_ = list_ + ' ' + self.tf_var_mmmc_table[i]
            print('set MMMC_PRESETS \"' + list_ + '\"')
            print('')

            print('# MMMC sdc modes')
            list_ = ''
            for i in range(len(self.mmmc_sdc_mode_table)):
                if list_ == '':
                    list_ = self.mmmc_sdc_mode_table[i][0]
                else:
                    list_ = list_ + ' ' + self.mmmc_sdc_mode_table[i][0]
            print('set MMMC_SDC_MODES \"' + list_ + '\"')
            print('')

        sys.stdout = original_stdout

    def run(self):

        self.check_steps()

        shutil.rmtree(self.tf_run_dir_scripts)
        os.mkdir(self.tf_run_dir_scripts)

        shutil.rmtree(self.tf_run_dir_work_tmp)
        os.mkdir(self.tf_run_dir_work_tmp)

        self.create_tf_tmp_file_steps_import_file()

        sys.path.append(self.tf_run_dir_work_tmp)
        import tf_tmp_file_steps_import

        self.create_tf_tmp_step_table_file()
        import tf_tmp_step_table

        self.create_vars_config()

        for i in range(len(tf_tmp_step_table.tf_tmp_step_table)):  # Create tcl scr for all steps
            if tf_tmp_step_table.tf_tmp_step_table[i][0] == 0:
                self.create_tcl_scripts_for_each_step(
                    tf_tmp_step_table.tf_tmp_step_table[i][1],
                    '',
                    tf_tmp_step_table.tf_tmp_step_table[i][2])
            else:
                self.create_tcl_scripts_for_each_step(
                    tf_tmp_step_table.tf_tmp_step_table[i][1],
                    tf_tmp_step_table.tf_tmp_step_table[i - 1][1],
                    tf_tmp_step_table.tf_tmp_step_table[i][2])
