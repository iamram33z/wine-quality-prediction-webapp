"""
Folder Package Installation
"""

# Import Required Libraries
import setuptools

# Set up project details in README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Set up project details
__version__ = "0.1.0"

REPO_NAME = "wine-quality-prediction-webapp"
AUTHOR = "Rameez M Rassdeen"
AUTHOR_EMAIL = "iamrameez97@gmail.com"
AUTHOR_USERNAME = "iamram33z"
DESCRIPTION = "Wine Quality Prediction Web Application"
SOURCE_REPO = "Wine-Quality-Prediction"

# Set up project details
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "source"},
    packages=setuptools.find_packages(where="source"),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "start=main:main",
        ],
    },
    include_package_data=True,
)