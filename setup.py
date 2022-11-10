from setuptools import setup

setup(
    name='the_flow',
    packages=['the_flow', 'the_flow.templates'],
    include_package_data=True,
    version='0.6.6',
    description='fix error when step into table have '' name ; make tcl scripts creator more stable but from now '
                'step name must start from tf_*',
    author='Leonid Nidekker',
    author_email='leonidnidekker@gmail.com',
    license='MIT'
)
