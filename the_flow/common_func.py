"""
Common functions are used in THE FLOW code.
"""

from jinja2 import Template
from os import close
from shutil import move
from tempfile import mkstemp


def tf_info(text):
    """
    This function returns information text message.
    It's used to inform user about current stage of THE FLOW.

    :param text: Text message.
    :type text: str

    :return: Text message.
    """

    t = Template('\033[33mTF_INFO    : {{ tt }}\033[0m')
    print(t.render(tt=text))


def tf_error(text):
    """
    This function returns error text message.
    It's used to inform user about some problem during THE FLOW execution.

    :param text: Text message.
    :type text: str

    :return: Text message.
    """

    t = Template('\033[31mTF_ERROR   : {{ tt }}\033[0m')
    print(t.render(tt=text))


def tf_warning(text):
    """
    This function returns warning text message.
    It's used to inform user about some problem during THE FLOW execution.

    :param text: Text message.
    :type text: str

    :return: Text message.
    """

    t = Template('\033[34mTF_WARNING : {{ tt }}\033[0m')
    print(t.render(tt=text))


def tf_file_exists_check(file):
    """
    This function is used to check file existing.

    :param file: File name
    :type file: str

    :return: 'True' or 'False'
    """

    try:
        f = open(file, 'r')
        f.close()
    except IOError:
        return 'False'
    return 'True'


def tf_remove_double_lines(file):
    """
    This function is used to delete double lines in file.

    :param file: File name.
    :type file: str

    :return: Updated file with the same name.
    """

    ft, temp = mkstemp()
    lines = []
    with open(temp, 'w', encoding='utf-8') as t, open(file) as f:
        for line in f:
            if line not in lines:
                lines.append(line)
                t.write(line)
    close(ft)
    move(temp, file)


def tf_run_eda_with_xterm(body):
    """
    This function is used to run EDA tools into xterm emulator.

    :param body: Command which need to execute.
    :type body: str

    :return: Xterm command.
    """
    t = Template('xterm -geometry 150x35 -fs 12 -bg white -fg black -e {{ b }}')
    return t.render(b=body)


def tf_exit_with_error():
    """
    This function is used to exit from THE FLOW execution with some message.
    """

    exit('\033[31mExit with error.\033[0m')
