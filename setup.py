import re
from setuptools import setup

# This file adapted from https://github.com/meejah/python-skeleton/blob/master/setup.py
# Accessed: 02/14/24


def pip_to_requirements(s):
    """
    Change a PIP-style requirements.txt string into one suitable for setup.py
    """

    if s.startswith("#"):
        return ""
    m = re.match("(.*)([>=]=[.0-9]*).*", s)
    if m:
        return "%s (%s)" % (m.group(1), m.group(2))
    return s.strip()


setup(
    name="mrnn",
    version=open("VERSION", "r").read().strip(),
    author="mmattb",
    author_email="mmattb@cs.washington.edu",
    license="GNU V3",
    url="https://github.com/mmattb/michaels_mrnn",
    install_requires=open("requirements.txt").readlines(),
    description="A PyTorch reference implementation of the modular RNN of Michaels et al. 2020",
    long_description=open("README.md", "r").read(),
    keywords=["python", "PyTorch"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["mrnn"],
    # data_files=[".", ("README.md",)],
)
