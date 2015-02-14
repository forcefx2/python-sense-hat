import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Astro Pi HAT",
    version="0.0.2",
    author="Dave Honess",
    author_email="dave@raspberrypi.org",
    description="Astro Pi sensor board for the Raspberry Pi",
    license="BSD",
    keywords=[
        "raspberrypi",
        "astro pi",
        "astro pi hat",
        "sense hat",
    ],
    url="https://github.com/astro-pi/astro-pi-hat",
    packages=[
        "astro_pi",
    ],
    package_data={"txt": ['astro_pi_text.txt'], "png": ['astro_pi_text.png']},
    include_package_data=True,
    install_requires=[
        "RPi.GPIO",
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: BSD License",
    ],
)
