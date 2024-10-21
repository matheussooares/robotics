from setuptools import setup, find_packages
with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "robotics",
    version= "0.0.1",
    autor = "Matheus Soares",
    author_email="matheus.soares8890@gmail.com",
    description="Biblioteca de robótica de manipuladores",
    long_description = page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheussooares/robotics",
    packages= find_packages(),
    install_requires = requirements,
    python_requires = ">=3.13.0"
)