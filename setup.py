from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dialectic",
    version="0.3.2",
    description="Mathematical Logic Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alisoltanirad/dialectic",
    author="Ali Soltanirad",
    author_email="soltaniradali@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.11"
)