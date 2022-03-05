import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ui",
    version="0.1.0",
    description="Ui designign library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Andre-cmd-rgb/Py-ui-library",
    author="Andre-Cmd-Rgb",
    author_email="andreavigolini@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["ui"],
    include_package_data=True,
    install_requires=["os", "tkinter"],
)
