from setuptools import setup, find_packages
import sys
import os

pkg_name = "qobuz-dl"


def read_file(fname):
    with open(fname, "r") as f:
        return f.read()


requirements = read_file("requirements.txt").strip().split()
if os.name == "nt" or "win" in sys.platform:
    requirements.append("windows-curses")

setup(
    name=pkg_name,
    version="0.5.4.1",
    author="Vitiko",
    author_email="vhnz98@gmail.com",
    description="The complete Lossless and Hi-Res music downloader for Qobuz",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/vitiko98/Qobuz-DL",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "qobuz-dl = qobuz_dl:main",
            "qdl = qobuz_dl:main",
        ],
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

# python3 setup.py sdist bdist_wheel
# rm -f dist/*
# twine upload dist/*
