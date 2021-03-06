#! python3
# -*- coding: utf-8 -*-
from commands8 import *
class Git:
    @classmethod
    def add(cls, what):
        Process.start("git", "add", what)

    @classmethod
    def commit(cls, message=None):
        commands = ["git", "commit"]
        if message:
            commands.append("-m")
            commands.append(Bash.argument_escape(message))
        Process.start(commands)

    @classmethod
    def push(cls, path, upstream=False):
        commands = ["git", "push"]
        if upstream:
            commands.append("-u")
        commands.append(path)
        Process.start(commands)


    @classmethod
    def update(cls, message, path="github"):
        cls.add(".")
        cls.commit(message)
        cls.push(path, upstream=True)


arguments = list(sys.argv)
arguments.pop(0)
string = "small update (default message)"
try:
    arguments[0]
    string = ""
    for arg in arguments:
        string += arg + " "
    string = string.rstrip(" ")
except IndexError:
    input_string = input("Enter a description or press Enter to defaul message: ")
    if input_string:
        string = input_string
Git.update(string)
