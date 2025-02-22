# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import glob
import os

from setuptools import find_packages, setup
from setuptools.dist import Distribution

libs = list(glob.glob("./bitsandbytes/libbitsandbytes*.*"))
libs = [os.path.basename(p) for p in libs]
print("libs:", libs)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()


# Tested with wheel v0.29.0
class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(
    name="bitsandbytes",
    version="0.45.1.dev0",
    author="Tim Dettmers",
    author_email="dettmers@cs.washington.edu",
    description="k-bit optimizers and matrix multiplication routines.",
    license="MIT",
    keywords="gpu optimizers optimization 8-bit quantization compression",
    url="https://github.com/bitsandbytes-foundation/bitsandbytes",
    packages=find_packages(),
    package_data={"": libs},
    install_requires=["torch", "numpy", "typing_extensions>=4.8.0"],
    extras_require={
        "benchmark": ["pandas", "matplotlib"],
        "test": ["scipy", "lion_pytorch"],
    },
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    distclass=BinaryDistribution,
)
