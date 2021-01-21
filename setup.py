from setuptools import setup, find_packages


setup(
    name='dependency_visualizer',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click'],
    tests_require=['pytest-cov', 'mypy', 'pytest', 'flake8'],
    extras_require={
        'tests': ['pytest-cov', 'mypy', 'pytest', 'flake8'],
    },
    entry_points={
        'console_scripts': ['dependency_visualizer = dependency_visualizer.main:main']
    },
)
