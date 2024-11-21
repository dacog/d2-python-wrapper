from setuptools import setup, find_packages

setup(
    name="d2-python",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        "d2_python": [
            "bin/linux/*",
            "bin/win32/*",
            "bin/darwin/*"
        ]
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
