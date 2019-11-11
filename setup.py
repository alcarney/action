import os

from setuptools import find_packages, setup

info = {}
version = os.path.join("action", "_version.py")

with open(version) as f:
    exec(f.read(), info)

setup(
    name="action",
    version=info["__version__"],
    description="A nothing package",
    author="Alex Carney",
    author_email="alcarneyme@gmail.com",
    license="MIT",
    packages=find_packages(".", exclude=["tests"]),
    python_requires=">=3.6",
)
