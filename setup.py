from setuptools import setup, find_packages

setup(
    name="webdata",         # This will be your pip install name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Murphy Sheppard",
    author_email="sheppardmurphy@gmail.com",
    description="WebData is an application that collects user information and stores it into a database for law enforcement and for educational purposes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NoSleepWebDeveloper/WebData",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'webdata=webdata:main',   # so users can run `webdata` command after install
        ],
    },
)
