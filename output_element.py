# -*- coding: utf-8 -*-

import os
from start_action import StartAction
from line_action import LineAction
from end_action import EndAction


class OutputElement:

    def __init__(self, path):
        self.path = path

    def Execute(self, action):
        if isinstance(action, StartAction):
            self._OpenFile(action)
        elif isinstance(action, LineAction):
            self._WriteLine(action)
        elif isinstance(action, EndAction):
            self._CloseFile(action)

    def _OpenFile(self, action):
        path = self.path + action.path
        try:
            if not os.path.exists(path): os.makedirs(path)
        except Exception as e:
            print(e)
            os._exit(1)

        self.f = open(path + action.name, "w")

    def _CloseFile(self, action):
        self.f.close()

    def _WriteLine(self, action):
        self.f.write(action.line)
