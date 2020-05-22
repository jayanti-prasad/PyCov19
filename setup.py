import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCov19", # Replace with your own username
    version="1.0.0",
    author="Jayanti Prasad",
    author_email="prasad.jayanti@gmail.com",
    description="A python package for Covid-19 data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayanti-prasad/PyCov19",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
