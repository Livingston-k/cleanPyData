from setuptools import setup, find_packages

setup(
    name='cleanPyData',
    version='0.1.0',
    description='A package for data cleaning and preprocessing',
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
