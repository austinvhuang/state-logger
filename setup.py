import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="state_logger",
    version="0.0.1",
    author="Austin Huang",
    description="Minimal logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/austinvhuang/state-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
