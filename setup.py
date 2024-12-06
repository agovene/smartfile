from setuptools import setup, find_packages

# Read the contents of the README file for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Read the contents of the requirements.txt file
def parse_requirements(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Get the dependencies from requirements.txt
requirements = parse_requirements('requirements.txt')

setup(
    name="smartfile", 
    version="0.1.0",  
    author="Arnaldo Govene", 
    author_email="arnaldo.govene@outlook.com", 
    description="A Python package for file management, renaming, and previews",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/agovene/smartfile",
    packages=find_packages(),  # Automatically find all sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=requirements,  # Load dependencies from requirements.txt
    entry_points={ 
        'console_scripts': [
            'smartfile-cli=smartfile.cli:main', 
        ],
    },
)