#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        print()
        return True
    
    def emptyline(self):
        pass


    def create():
        pass

    def show():
        pass

    def destroy():
        pass

    def all():
        pass

    def update():
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()