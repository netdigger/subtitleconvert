# -*- coding: utf-8 -*-

from start_action import StartAction
from content_action import ContentAction
from line_action import LineAction
from end_action import EndAction


class SRTEncode:

    def SetNextElement(self, out):
        self.out = out

    def Execute(self, action):
        if isinstance(action, StartAction):
            self._SetName(action)
        elif isinstance(action, ContentAction):
            self._Encode(action)
        elif isinstance(action, EndAction):
            self.out.Execute(action)

    def _SetName(self, action):
        action.name = action.name + ".srt"
        self.index = 1
        self.out.Execute(action)

    def _Encode(self, action):
        line = str(self.index) + "\n" \
                + self._GetTime(action.start) + " --> " \
                + self._GetTime(action.end) + "\n" \
                + action.content + "\n\n"
        self.out.Execute(LineAction(line))
        self.index = self.index + 1

    def _GetTime(self, time):
        micro = format(time % 1000, "03d")
        time = time / 1000
        second = format(time % 60, "02d")
        time = time / 60
        minute = format(time % 60, "02d")
        hour = format(time / 60, "02d")
        return hour + ":" + minute + ":" + second + "," + micro
