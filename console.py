#!/usr/bin/python3

"""
A command line interpreter for our AirBnB clone project
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Airbnb_clone console"""

    intro = 'Hi there! Bienvenue to the AirBnB-clone console Type ? or shout help for help'
    prompt = '(hbnb) '

        def __init__(self, completekey='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

    def do_EOF(self, line):
        """End of The File"""

        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""

        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""

        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""

        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""

        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        if args == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[args]
                resp = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)."""

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
