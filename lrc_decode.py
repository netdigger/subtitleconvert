# -*- coding: utf-8 -*-

import re
from start_action import StartAction
from line_action import LineAction
from content_action import ContentAction
from end_action import EndAction

class LRCDecode:
    
    def __init__(self):
        self.pattern = re.compile("^\[(\d+):(\d+)\.(\d+)](.*)")

    def SetNextElement(self, out):
        self.out = out

    def Execute(self, action):
        if isinstance(action, StartAction):
            self._DoStart(action)
        elif isinstance(action, LineAction):
            self._Decode(action)
        elif isinstance(action, EndAction):
            self._DoEnd(action)

    def _DoStart(self, action):
        names = action.name.split(".")
        action.name = ".".join(names[:len(names) - 1])
        self.content = ContentAction() 
        self.first = True
        self.out.Execute(action)

    def _DoEnd(self, action):
        content = ContentAction()
        time = self.start + len(self.content) * 1000
        content.SetTime(self.start, time)
        content.SetContent(self.content)
        self.out.Execute(content)

        content = ContentAction()
        self.out.Execute(action)

    def _Decode(self, action):
        line = action.line.strip()
        rst = self.pattern.match(line)

        minutes = int(rst.group(1))
        seconds = int(rst.group(2))
        microsecond = int(rst.group(3))
        content = ContentAction()
        time = minutes * 60 * 1000 + seconds * 1000 + microsecond * 10
        if self.first:
            self.start = time
            self.content = rst.group(4)
            self.first = False
            return

        content.SetTime(self.start, time - 50)
        content.SetContent(self.content)
        self.out.Execute(content)

        self.start = time
        self.content = rst.group(4)

