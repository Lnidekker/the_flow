from setuptools import setup

setup(
    name='the_flow',
    packages=['the_flow', 'the_flow.templates'],
    include_package_data=True,
    version='0.3.2',
    description='remove "Please, use [-update_run_dir [all] [cfg] [step_scripts] [input_data]] after [-ui_mode terminal]." check',
    author='Leonid Nidekker',
    author_email='leonidnidekker@gmail.com',
    license='MIT'
)
