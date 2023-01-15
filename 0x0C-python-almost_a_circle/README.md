# 0x0C. Python - Almost a circle
Project done during Software Engineering program at ALX.
It aims to learn about `args` and `kwargs`, serialization/deserialization, JSON and unit testing in **Python**.

## Learning Objectives
Learning points in this project include:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Technologies
* Python Scripts are written with Python 3
* Tested on Ubuntu 20.04 LTS

## Files

Inside `models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `base.py` | Base class of geometrical instances |
| `rectangle.py` | Class that inherits attributes references from `Base` class |
| `square.py` | Class that inherits attributes references from `Square` class |

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.

Inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `test_base.py` | Module that contains unittests to `Base` class |
| `test_rectangle.py` | Module that contains unittests to `Rectangle` class |
| `test_square.py` | Module that contains unittests to `Square` class |
