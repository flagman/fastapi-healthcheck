import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi-healthcheck-flagman",
    version="0.0.3",
    author="Pavel Malay",
    author_email="flagmansupport@gmail.com",
    description="A small healthcheck package for adding /healthcheck routes to FastAPI projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flagman/fastapi-healthcheck",
    packages=setuptools.find_packages(),
    install_requires=[
        'aioredis'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
