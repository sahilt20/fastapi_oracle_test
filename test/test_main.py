# import unittest
from os import sys,path
ROOT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

sys.path.append(ROOT_PATH)
#print(path.dirname(path.dirname(path.abspath(__file__))))
from app.main import handler


# class test_main(unittest.TestCase):
def test_main_f():
    print('hello world')
