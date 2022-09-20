import global_tf_vars


def q2():
    if global_tf_vars.tf_q2_answer == 0:
        global_tf_vars.tf_q2_flag = input(
            '[TF_Q2] Do you want to start EDA tool?\n'
            '            1-Yes\n'
            '            2-No\n'
            '(1/2): '
        )
    elif global_tf_vars.tf_q2_answer == 1:
        global_tf_vars.tf_q2_flag = '1'
