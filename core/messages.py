"""
This file contains list of ERROR and WARNING messages and solutions which are used during THE FLOW execution.
Type of messages:
    [INIT-*]   - initialization part of THE FLOW
    [PHYGEN-*] - phy_gen messages
"""
from common_func import CommonFunc


class Messages(CommonFunc):

    def init_1(self, dir_name, var_name):
        """
        ERROR : Directory * in * doesn't exist.

        :param dir_name: Directory name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_error('[INIT-1] Directory "' + dir_name + '" in ' + var_name + ' doesn\'t exist.')
        self.tf_exit_with_error()

    def init_2(self, dir_name, var_name):
        """
        WARNING : Directory * in * doesn't exist.

        :param dir_name: Directory name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_warning('[INIT-2] Directory "' + dir_name + '" in ' + var_name + ' doesn\'t exist.')

    def init_3(self, var_name):
        """
        ERROR : * variable name is invalid. Please, use variable names from template file.

        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_error('[INIT-3] ' + var_name +
                      ' variable name is invalid. Please, use variable names from template file.')
        self.tf_exit_with_error()

    def init_4(self, var_name):
        """
        ERROR : * doesn't define.

        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_error('[INIT-4] ' + var_name + ' doesn\'t define.')
        self.tf_exit_with_error()

    def init_5(self, table_name, file_name):
        """
        ERROR : *_table from * doesn't exist.

        :param table_name: Table name.
        :param file_name: File name.
        :return: Text message into terminal window.
        """

        self.tf_error('[INIT-5] ' + table_name + ' table from ' + file_name + ' doesn\'t exist.')
        self.tf_exit_with_error()

    def init_6(self, table_name, file_name):
        """
        WARNING : *_table from * doesn't exist.

        :param table_name: Table name.
        :param file_name: File name.
        :return: Text message into terminal window.
        """

        self.tf_warning('[INIT-6] ' + table_name + ' table from ' + file_name + ' doesn\'t exist.')

    def init_7(self, files):
        """
        ERROR : There are several tf_var.py files.

        :param files: List of tf_var.py files.
        :return: Text message into terminal window.
        """

        self.tf_error('[INIT-7] There are several tf_var.py files. These files are: ' + str(files))
        self.tf_exit_with_error()

    def init_8(self, file):
        """
        WARNING : File couldn't be read while tf_var.py searching.

        :param file: File.
        :return: Text message into terminal window.
        """

        self.tf_warning('[INIT-8] File ' + file + ' couldn\'t be read while tf_var.py searching.')

    def phygen_1(self, file_name, var_name):
        """
        ERROR : File or dir * from * doesn't exist.

        :param file_name: File or dir name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_error('[PHYGEN-1] File or dir ' + file_name + ' from ' + var_name + ' doesn\'t exist.')
        self.tf_exit_with_error()

    def mmmcgen_1(self, file_name, var_name):
        """
        ERROR : Files * from * doesn't exist.

        :param file_name: File name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        self.tf_error('[MMMCGEN-1] File ' + file_name + ' from ' + var_name + ' doesn\'t exist.')
        self.tf_exit_with_error()

    def mmmcgen_2(self, file, pvt):
        """
        ERROR : File * doesn't exists for * pvt set.

        :param file: .lib file.
        :param pvt: Combination of pvt aliases.
        :return: Text message into terminal window.
        """

        self.tf_error('[MMMCGEN-2] File ' + file + ' doesn\'t exists for ' + pvt + ' pvt set.')
        self.tf_exit_with_error()

    def mmmcgen_3(self, alias, table):
        """
        ERROR : Alias * from table * are used twice. Please, remove repeating aliases.

        :param alias: Alias from table.
        :param table: Table name.
        :return: Text message into terminal window.
        """

        self.tf_error('[MMMCGEN-3] Alias "' + alias + '" from table "' + table +
                      '" are used twice. Please, remove repeating aliases.')
        self.tf_exit_with_error()

    def tclscr_1(self, file_name, files):
        """
        ERROR : There are several step files * with the same names.

        :param file_name: File name.
        :param files: List of files with the same names.
        :return: Text message into terminal window.
        """

        self.tf_error('[TCLSCR-1] There are several step files with ' + file_name + ' name. This files are ' + files)
        self.tf_exit_with_error()

    def tclscr_2(self, step_name, files, number):
        """
        ERROR : There are several steps with the same names.

        :param step_name: Step name.
        :param files: List of files witch contain recurring steps.
        :param number: Number of repetitions.
        :return: Text message into terminal window.
        """

        self.tf_error('[TCLSCR-2] There are ' + number + ' steps with \"' + step_name +
                      '\" name. These steps from following files: ' + files)
        self.tf_exit_with_error()
