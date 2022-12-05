import global_tf_vars
import common_func


def q3(step_name):
    if global_tf_vars.tf_q3_answer == 0:
        common_func.tf_info('Database of step ' + step_name + ' already exists.')
        global_tf_vars.tf_q3_flag = input(
            '[TF-Q3] What do you want to do?\n'
            '            1-Go to next step\n'
            '            2-Delete database and start THE FLOW execution from this step\n'
            '(1/2): '
        )
    elif global_tf_vars.tf_q3_answer == 1:
        if step_name == global_tf_vars.tf_from_step_name:
            global_tf_vars.tf_q3_flag = '2'
        else:
            common_func.tf_info('Database of step ' + step_name + ' already exists.')
            global_tf_vars.tf_q3_flag = '1'
            common_func.tf_info('Go to next step')
