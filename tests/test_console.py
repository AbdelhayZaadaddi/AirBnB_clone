#!/usr/bin/python3
"""Unit tests for the console command interpreter"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the console command interpreter"""

    def setUp(self):
        """Set up testing environment"""
        self.cli = HBNBCommand()

    def test_do_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_quit(None))

    def test_do_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_EOF(None))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.cli.emptyline())

    def test_do_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_show("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_destroy("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_all("")
            self.assertEqual(str(storage.all()) + "\n", f.getvalue())

    def test_do_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_update("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_create_valid(self):
        """Test create command with valid input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_do_show_invalid_class(self):
        """Test show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_show("NotAClass 1234-1234-1234")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_do_destroy_invalid_class(self):
        """Test destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_destroy("NotAClass 1234-1234-1234")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_do_update_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_update("NotAClass 1234-1234-1234 attr value")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_counter(self):
        """Test counter method"""
        count = self.cli.counter("BaseModel")
        self.assertEqual(count, len([obj for obj in storage.all().values() if type(obj).__name__ == "BaseModel"]))

    def test_default_invalid_command(self):
        """Test default method with invalid command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.default("NotAClass.not_a_method()")
            self.assertEqual("", f.getvalue())


if __name__ == '__main__':
    """Main entry point for script"""
    unittest.main()
