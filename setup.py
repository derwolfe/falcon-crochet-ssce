from setuptools import setup, find_packages

setup(
    name='ssce',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'serve = ssce.server:run_with_twisted'
        ]
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=[]),
    install_requires=[
        'falcon',
        'twisted',
        'crochet',
        'requests'
    ],
)
