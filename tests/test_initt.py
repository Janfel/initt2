'''
Tests for initt.py
'''
import unittest
import subprocess
from pathlib import Path
from shutil import rmtree
import initt


class NormalUsageTestCase(unittest.TestCase):
    '''
    Tests the program in normal use
    '''

    def test_help(self):
        '''Tests the help message'''
        subprocess.run(['python', 'initt.py', '-h'], check=True)

    def test_templates(self):
        '''Tests every module'''
        root = Path('./,test-temp')
        if root.exists():
            rmtree(root)
        root.mkdir()
        for module in initt.templates():
            with self.subTest(module=module):
                subprocess.run(['python', 'initt.py', '-n',
                                module, module], check=True)
