import os
import time
import common_func
import q3
from jinja2 import Template


class RunEDATools:

    def __init__(self,
                 tf_from_step,
                 tf_from_step_name,
                 tf_run_dir_db,
                 tf_q3_flag,
                 tf_use_xterm,
                 tf_step_table,
                 flow_name):
        self.tf_from_step = tf_from_step
        self.tf_from_step_name = tf_from_step_name
        self.tf_run_dir_db = tf_run_dir_db
        self.tf_q3_flag = tf_q3_flag
        self.tf_use_xterm = tf_use_xterm
        self.tf_step_table = tf_step_table
        self.flow_name = flow_name

    def eda_tool_run_command(self, step_name):
        if self.flow_name == 'syn':
            t = Template(
                'genus -f ../scripts/{{ step_name }}.tcl -log ../logs/{{ step_name }}.log -overwrite')
            return t.render(step_name=step_name)
        if self.flow_name == 'impl':
            t = Template(
                'innovus -stylus -file ../scripts/{{ step_name }}.tcl -log ../logs/{{ step_name }}.log -overwrite')
            return t.render(step_name=step_name)
        if self.flow_name == 'atpg':
            t = Template(
                'modus -f ../scripts/{{ step_name }}.tcl -log ../logs/{{ step_name }}.log')
            return t.render(step_name=step_name)
        if self.flow_name == 'power':
            t = Template(
                'voltus -stylus -file ../scripts/{{ step_name }}.tcl -log ../logs/{{ step_name }}.log -overwrite')
            return t.render(step_name=step_name)

    def run(self):

        if self.tf_from_step == 1:
            flag = 0
            for i in range(0, len(self.tf_step_table)):
                if self.tf_step_table[i][1] == self.tf_from_step_name:
                    flag = 1
            if flag == 0:
                common_func.tf_error('Step name "' + self.tf_from_step_name +
                                     '" from [-from_step] option doesn\'t exist.')
                common_func.tf_exit_with_error()

        for j in range(0, len(self.tf_step_table)):
            tf_go_to_next_step = 0
            if common_func.tf_dir_exists_check(self.tf_run_dir_db + '/' + self.tf_step_table[j][1] + '.db'):
                q3.q3(self.tf_step_table[j][1])
                if self.tf_q3_flag == '1':
                    tf_go_to_next_step = 1
                elif self.tf_q3_flag == '2':
                    for k in range(j, len(self.tf_step_table)):
                        if common_func.tf_dir_exists_check(self.tf_run_dir_db + '/' + self.tf_step_table[k][1] + '.db'):
                            os.remove(self.tf_run_dir_db + '/' + self.tf_step_table[k][1] + '.db')
            if tf_go_to_next_step == 0:
                if self.tf_step_table[j][0] == 0:
                    common_func.tf_info('start to execute ' + self.tf_step_table[j][1] + ' step')
                    t = time.time()
                    if self.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm(self.eda_tool_run_command(self.tf_step_table[j][1])))
                    else:
                        os.system(self.eda_tool_run_command(self.tf_step_table[j][1]))
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + self.tf_step_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                elif common_func.tf_dir_exists_check('../db/' + self.tf_step_table[j - 1][1] + '.db') == 'True':
                    common_func.tf_info('start to execute ' + self.tf_step_table[j][1] + ' step')
                    t = time.time()
                    if self.tf_use_xterm == 1:
                        os.system(common_func.tf_run_eda_with_xterm(self.eda_tool_run_command(self.tf_step_table[j][1])))
                    else:
                        os.system(self.eda_tool_run_command(self.tf_step_table[j][1]))
                    runtime = time.time() - t
                    common_func.tf_info('finish to execute ' + self.tf_step_table[j][1] +
                                        ' step. runtime: ' + str(runtime // 60) + ' min')
                else:
                    common_func.tf_error('previous step db doesn\'t exist')
                    common_func.tf_exit_with_error()
