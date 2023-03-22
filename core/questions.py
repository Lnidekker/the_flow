from common_func import CommonFunc
import global_tf_vars


class Questions(CommonFunc):

    def q1(self):

        self.tf_info('Directory ' + global_tf_vars.tf_run_dir + ' exists.')
        if global_tf_vars.tf_q1_answer == 0:
            global_tf_vars.tf_q1_flag = input('[TF-Q1] What do you want to do?\n'
                                              '            1-remove existing directory and continue THE FLOW execution\n'
                                              '            2-update cfg files and continue THE FLOW execution\n'
                                              '            3-update step .tcl scripts and continue THE FLOW execution\n'
                                              '            4-update input data and continue THE FLOW execution\n'
                                              '            5-just continue THE FLOW with existing directory and files\n'
                                              '            6-exit THE FLOW\n'
                                              '(1/2/3/4/5/6): ')
            if global_tf_vars.tf_q1_flag == '1':
                global_tf_vars.tf_remove_run_dir = 1
                global_tf_vars.tf_update_run_dir_in_cfg = 1
                global_tf_vars.tf_update_run_dir_input_data = 1
                global_tf_vars.tf_update_run_dir_scripts = 1
            elif global_tf_vars.tf_q1_flag == '2':
                global_tf_vars.tf_update_run_dir_in_cfg = 1
            elif global_tf_vars.tf_q1_flag == '3':
                global_tf_vars.tf_update_run_dir_scripts = 1
            elif global_tf_vars.tf_q1_flag == '4':
                global_tf_vars.tf_update_run_dir_input_data = 1
            elif global_tf_vars.tf_q1_flag == '5':
                empty_flag = 0
            elif global_tf_vars.tf_q1_flag == '6':
                exit('Normal exit.')
        elif global_tf_vars.tf_q1_answer == 1:
            if global_tf_vars.tf_update_all == 1:
                global_tf_vars.tf_remove_run_dir = 1
            if global_tf_vars.tf_update_cfg == 1:
                global_tf_vars.tf_update_run_dir_in_cfg = 1
            if global_tf_vars.tf_update_step_scripts == 1:
                global_tf_vars.tf_update_run_dir_scripts = 1
            if global_tf_vars.tf_update_input_data == 1:
                global_tf_vars.tf_update_run_dir_input_data = 1
        else:
            exit('Unknown tf_ux_ui_mode value')

    @staticmethod
    def q2():
        if global_tf_vars.tf_q2_answer == 0:
            global_tf_vars.tf_q2_flag = input(
                '[TF-Q2] Do you want to start EDA tool?\n'
                '            1-Yes\n'
                '            2-No\n'
                '(1/2): '
            )
        elif global_tf_vars.tf_q2_answer == 1:
            global_tf_vars.tf_q2_flag = '1'

    def q3(self, step_name):
        if global_tf_vars.tf_q3_answer == 0:
            self.tf_info('Database of step ' + step_name + ' already exists.')
            global_tf_vars.tf_q3_flag = input(
                '[TF-Q3] What do you want to do?\n'
                '            1-Go to next step\n'
                '            2-Delete database and start THE FLOW execution from this step\n'
                '(1/2): '
            )
        elif global_tf_vars.tf_q3_answer == 1:
            if step_name == global_tf_vars.tf_from_step_name or step_name == global_tf_vars.tf_only_step_name:
                global_tf_vars.tf_q3_flag = '2'
            else:
                self.tf_info('Database of step ' + step_name + ' already exists.')
                global_tf_vars.tf_q3_flag = '1'
                self.tf_info('Go to next step')
