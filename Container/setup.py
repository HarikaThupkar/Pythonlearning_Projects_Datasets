import setuptools

with open("README.me","r") as fh:
    long_description = fh.read(

setuptools.setup(
    name="TinyMath",
    version="0.0.1",
    author="Harika Thupkar",
    author_email="hthupkar@gmail.com",
    description="A small mathematics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
