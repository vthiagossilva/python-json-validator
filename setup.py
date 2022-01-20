from setuptools import setup, find_packages


setup(
    name="json_validator",
    python_requires=">=3.6",
    version="0.0.2",
    license="MIT",
    description="Simples criador e validador de schema para JSON",
    author="Thiago Silva",
    author_email="valtemir.thiago@gmail.com",
    packages=find_packages(),
    package_data={"json_validator": ["py.typed"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
