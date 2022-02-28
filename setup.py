import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Shrinking-Overpotential-Method",
    version="1.0",
    author="Becca Segel",
    author_email="becca.segel@pitt.edu",
    description="Electrochemical method toolkit to analyze kinetics of a three electrode cell ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsegel/Shrinking-Overpotential-Method",
    packages=setuptools.find_packages()
)
