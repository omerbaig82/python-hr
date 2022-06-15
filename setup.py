from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup (
    name='hr',
    version='1.0.0',
    author='Omer Baig',
    author_email='omer.baig@email.com',
    description='A utility for exporting users information.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/omerbaig/hr',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main'
            ],
    }
)
