from setuptools import setup, find_packages

setup(
    name="milsymbol-py",
    version="0.1.0",
    description="Python port of milsymbol library",
    packages=find_packages(),
    install_requires=[
        "cairosvg>=2.5.0",
    ],
    python_requires=">=3.6",
)
