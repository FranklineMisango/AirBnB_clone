#!/usr/bin/python3

"""
A command line interpreter for our AirBnB clone project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb_clone console"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        'Quit command to exit the program'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'an empty line + ENTER shouldn’t execute anything'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
