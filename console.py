
"""
py shell
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Cmd class."""


    prompt = "(hbnb) "
    cls = {"BaseModel", "User", "Place", "City", "Amenity", "Review", "State"}

    def do_quit(self, arg):
        """Command quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True
        
    def emptyline(self):
        """ Empty line and do nothing."""
        pass

    def do_show(self, arg):
        """Pstring."""
        ar = arg.split()
        if not ar:
            print("** class name missing **")
        else:
            c_name = ar[0]
            if len(ar) == 0:
                print("** class name missing **")
            elif c_name not in HBNBCommand.cls:
                print("** class doesn't exist **")
            elif len(ar) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(c_name, ar[1])
                all_objs = storage.all()
                if obj_key in all_objs:
                    print(all_objs[obj_key])
                else:
                    print("** no instance found **")
                    
    def do_create(self, arg):
        """ fresh basemodel."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_inst = eval(arg)()
                new_inst.save()
                print(new_inst.id)
            except NameError:
                print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """ deletes an instance """
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = tuple(arg.split())
        if args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except Exception:
            print("** instance id missing **")
    
    def do_all(self, arg):
        res = []
        if len(arg) == 0:
            for obj in storage.all().values():
                res.append(obj)
            print(res)
            return
        if arg not in HBNBCommand.cls:
            print("** class doesn't exist **")
            return
        args = tuple(arg.split())
        if args[0] in HBNBCommand.cls:
            for key, obj in storage.all().items():
                if args[0] in key:
                    res.append(obj)
            print(res)
    
    def do_update(self, line):
        args = tuple(line.split())
        if len(args) >= 4:
            name = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            a = args[3].strip("'").strip('"')
            setattr(storage.all()[name], args[2], cast(a))
            storage.all()[name].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
