# -*- coding: utf-8 -*-

import os
from start_action import StartAction
from line_action import LineAction
from end_action import EndAction

class InputElement:

    def __init__(self, directory, ext):
        self.dir = directory
        self.ext = ext


    def SetNextElement(self, out):
        self.out = out

    def Start(self):
        if not os.path.exists(self.dir):
            print(self.dir, " not exist")
            return

        for dirpath, dirnames, filenames in os.walk(self.dir):
            #print(dirpath, dirnames, filenames)
            for name in filenames:
                if name.endswith(self.ext):
                    self._Read(dirpath, name)

    def _Read(self, dirpath, name):
        print("Convert " + dirpath + name + " ...")
        with open(dirpath + name) as fp:
            start = StartAction(dirpath, name)
            self.out.Execute(start)
            for line in fp:
                self.out.Execute(LineAction(line))
            self.out.Execute(EndAction())

