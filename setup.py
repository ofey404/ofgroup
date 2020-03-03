# -*- coding: utf-8 -*-

'''
@Author: Ofey Chan
@Date: 2020-03-03 16:57:09
@LastEditors: Ofey Chan
@LastEditTime: 2020-03-03 20:13:36
@Description: 
@Reference: 
'''

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="ofgroup",
    version="0.0.1",
    description="Ofey Chan's Group Theory Module for class of Fudan University 2020 Spring.",
    long_description=readme,
    author="Ofey Chan",
    author_email="ofey206@gmail.com",
    license=license,
    packages=["ofgroup"]
)