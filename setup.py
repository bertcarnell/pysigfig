import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysigfig", # Replace with your own username
    version="0.0.1",
    author="Rob Carnell",
    author_email="bertcarnell@gmail.com",
    description="A package for creating and manipulating floating point numbers accounting for significant figures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bertcarnell/pysigfig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
