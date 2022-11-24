from setuptools import setup

setup(
    name='the_flow',
    packages=['the_flow', 'the_flow.templates'],
    include_package_data=True,
    version='0.7.1',
    description='fix delay_corner name in mmmc_derate.tcl',
    author='Leonid Nidekker',
    author_email='leonidnidekker@gmail.com',
    license='MIT'
)
