from setuptools import setup, find_packages
setup(
    name = 'transaction_pipeline',
    version = '1.0',
    packages = find_packages(include = ('transaction_pipeline*', )) + ['prophecy_config_instances.transaction_pipeline'],
    package_dir = {'prophecy_config_instances.transaction_pipeline' : 'configs/resources/transaction_pipeline'},
    package_data = {'prophecy_config_instances.transaction_pipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.49'],
    entry_points = {
'console_scripts' : [
'main = transaction_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
