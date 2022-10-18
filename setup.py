from setuptools import setup

setup(
    name='the_flow',
    packages=['the_flow', 'the_flow.templates'],
    include_package_data=True,
    version='0.4.12',
    description='add db exists check before deleting; tested',
    author='Leonid Nidekker',
    author_email='leonidnidekker@gmail.com',
    license='MIT'
)
