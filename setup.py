import setuptools
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setuptools.setup(
    name="hexalattice-akorevaar",
    version="1.0.1",
    description="Compute and plot hexagonal grids",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akorevaar/hexalattice",
    author="Agnetha Korevaar",
    author_email="-",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=[
        "numpy",
        "matplotlib >= 3.1",
    ],
    setup_requires=[
        "numpy",
        "matplotlib >= 3.1",
    ],
)