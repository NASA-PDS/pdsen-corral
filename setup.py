import re
import setuptools

with open("./pdsen_corral/__init__.py") as fi:
    result = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fi.read())
version = result.group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdsen_corral", # Replace with your own package name
    version=version,
    license="apache-2.0",
    author="thomas loubrieu",
    author_email="loubrieu@jpl.nasa.gov",
    description="pds engineering node system release",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NASA-PDS/pdsen-corral",
    packages=setuptools.find_packages(),
    keywords=['github', 'action', 'github action', 'snapshot', 'release', 'maven', 'version'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'github3.py',
        'beautifulsoup4',
        'packaging',
        'mdutils',
        'requests'
    ],
    entry_points={
        'console_scripts': ['summary=pdsen_corral.cmd:main'],
    },


)