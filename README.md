# Ofey Chan's Group Theory Module
This simple project is for Group Theory class of Fudan University 2020 Spring.

## Installation

```shell
git clone https://github.com/ofey404/ofgroup.git
cd ofgroup
```

Then in package dir:

```shell
pip install -r requirements.txt
python setup.py install --user
```

or on linux or OS X machine:

```shell
make install
```

## Test
After installation, run below in package's root directory.

```shell
make test
```

Some test titled `individualTest_*.py`, just run them in the `test/` dir. Like:

```shell
> pwd; python individualTest_S3Group.py 
# output:
# /Users/ofey/Code/GroupTheoryCode/Ofey'sGroupPackage/tests
# +-------+-------+-------+-------+-------+-------+-------+
# |   \   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
# +-------+-------+-------+-------+-------+-------+-------+
# |   e   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
# |  (12) |  (12) |   e   | (123) | (132) |  (23) |  (31) |
# |  (23) |  (23) | (132) |   e   | (123) |  (31) |  (12) |
# |  (31) |  (31) | (123) | (132) |   e   |  (12) |  (23) |
# | (123) | (123) |  (31) |  (12) |  (23) | (132) |   e   |
# | (132) | (132) |  (23) |  (31) |  (12) |   e   | (123) |
# +-------+-------+-------+-------+-------+-------+-------+
```

## INFO
Author: Ofey Chan, Department of Physics, Junior

Contact:
- 17307110121@fudan.edu.cn
- ofey206@gmail.com
