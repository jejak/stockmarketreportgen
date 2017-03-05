from setuptools import setup, find_packages

setup(
    name="stockmarketreportgen",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.13.0'
    ],
    entry_points={
        'console_scripts': [
            'stockmarketreportgen = stockmarketreportgen.main:main',
        ],
    },
    data_files=[],
)
