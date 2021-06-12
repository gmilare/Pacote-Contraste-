"""Pacote Contraste - Aplicando contrastes em imagens Landsat8 por classes de uso e cobertura do solo de imagens classificadas do Mapbiomas."""

from setuptools import find_packages, setup

readme = open("README.rst").read()

history = open("CHANGES.rst").read()

tests_require = []

extras_require = {}

setup_requires = []

install_requires = ["rasterio>=1.1.0", "numpy>=1.20.0", "matplotlib>=3.3.0"]

packages = find_packages()

setup(
    name="contraste",
    version="1.0",
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    keywords=["Contraste", "Classes de Uso e Cobertura do Solo", "Landsat8", "Mapbiomas"],
    license="MIT",
    author="Diego Marcochi de Melo, Marielcio Lacerda, Gisele Milare",
    author_email="user@email.org",
    url="",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)