from setuptools import setup

setup(
    name='the_flow',
    packages=['the_flow', 'the_flow.templates'],
    include_package_data=True,
    version='0.3.0',
    description='don\'t use -si option in create_library_set if mmmc_cdb_file_table is empty',
    author='Leonid Nidekker',
    author_email='leonidnidekker@gmail.com',
    license='MIT'
)
