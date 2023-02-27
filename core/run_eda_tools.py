import os
import time
import global_tf_vars
from questions import Questions
from jinja2 import Template


class RunEDATools(Questions):

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
                self.tf_error('Step name "' + self.tf_from_step_name + '" from [-from_step] option doesn\'t exist.')
                self.tf_exit_with_error()

        for j in range(0, len(self.tf_step_table)):
            tf_go_to_next_step = 0
            if self.tf_dir_exists_check(self.tf_run_dir_db + '/' + self.tf_step_table[j][1] + '.db'):
                self.q3(self.tf_step_table[j][1])
                if global_tf_vars.tf_q3_flag == '1':
                    tf_go_to_next_step = 1
                elif global_tf_vars.tf_q3_flag == '2':
                    for k in range(j, len(self.tf_step_table)):
                        if self.tf_dir_exists_check(self.tf_run_dir_db + '/' + self.tf_step_table[k][1] + '.db'):
                            os.remove(self.tf_run_dir_db + '/' + self.tf_step_table[k][1] + '.db')
            if tf_go_to_next_step == 0:
                if self.tf_step_table[j][0] == 0:
                    self.tf_info('start to execute ' + self.tf_step_table[j][1] + ' step')
                    t = time.time()
                    if self.tf_use_xterm == 1:
                        os.system(self.tf_run_eda_with_xterm(self.eda_tool_run_command(self.tf_step_table[j][1])))
                    else:
                        os.system(self.eda_tool_run_command(self.tf_step_table[j][1]))
                    runtime = time.time() - t
                    runtime_h = str(int(runtime // 3600))
                    runtime_m = str(int((runtime % 3600) // 60))
                    runtime_s = str(int((runtime % 60)))
                    self.tf_info('finish to execute ' + self.tf_step_table[j][1] +
                                 ' step. runtime: ' + runtime_h + ':' + runtime_m + ':' + runtime_s)
                elif self.tf_dir_exists_check('../db/' + self.tf_step_table[j - 1][1] + '.db'):
                    self.tf_info('start to execute ' + self.tf_step_table[j][1] + ' step')
                    t = time.time()
                    if self.tf_use_xterm == 1:
                        os.system(self.tf_run_eda_with_xterm(
                            self.eda_tool_run_command(self.tf_step_table[j][1])))
                    else:
                        os.system(self.eda_tool_run_command(self.tf_step_table[j][1]))
                    runtime = time.time() - t
                    runtime_h = str(int(runtime // 3600))
                    runtime_m = str(int((runtime % 3600) // 60))
                    runtime_s = str(int((runtime % 60)))
                    self.tf_info('finish to execute ' + self.tf_step_table[j][1] +
                                 ' step. runtime: ' + runtime_h + ':' + runtime_m + ':' + runtime_s)
                else:
                    self.tf_error('previous step db doesn\'t exist')
                    self.tf_exit_with_error()
