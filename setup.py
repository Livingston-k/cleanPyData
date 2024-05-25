from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cleanPyData',
    version='0.1.2',
    description='A package for data cleaning and preprocessing',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    author='Kaddu Livingstone',
    author_email='kaddulivingston@gmail.com',
    url='https://github.com/Livingston-k/cleanPyData',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0',
        'scikit-learn>=0.24'
    ],
    tests_require=[
        'pytest>=6.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
