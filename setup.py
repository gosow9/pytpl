from setuptools import setup, find_packages

setup(
    name='pytpl',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pytpl': ['templates/*.j2'],
    },
    install_requires=[
        'click',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'pytpl=pytpl.cli:create_project',
        ],
    },
)
