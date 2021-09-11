import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="termux-api", 
    version="1.2.2",
    author="drshajul",
    author_email="drshajul@gmail.com",
    description="A package for accessing termux-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shajul/termux-api.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
