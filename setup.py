import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyducers-furiel",
    version="0.0.1",
    author="furiel",
    author_email="antal.nemes@gmail.com",
    description="Transducer library for python inspired by clojure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/furiel/pyducers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
