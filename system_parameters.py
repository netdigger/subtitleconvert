# -*- coding: utf-8 -*-

import getopt
import sys

class SystemParameters:

    def __init__(self):
        self._SetDefault()
        self._ReadFromCmdLine()

    def _SetDefault(self):
        self.source_dir= "./"
        self.output_dir = "./"

    def _ReadFromCmdLine(self):
        try:
            optlist, args = getopt.gnu_getopt(sys.argv[1:], 's:o:', 
                    ['src-dir=', 'output-dir='])
        except getopt.GetoptError as err:
            print(err)
            self._Usage()
            sys.exit(1)

        for opt, argv in optlist:
            if opt in ("-s", "--src-dir"):
                self.source_dir = argv
                if not argv.endswith("/"): self.source_dir += "/"
            elif opt in ("-o", "--output-dir"):
                self.output_dir= argv
                if not argv.endswith("/"): self.output_dir += "/"
    def _Usage(self):
        print("It is a tool for convert subtitle format.\n")
        print("Usage:\n")
        print("\t python main.py [command]\n")
        print("The commands are:\n")
        print("\t-s,--source-dir\t the directory with subtitle")
        print("\t-o,--output-dir\t the directory used to same new subtitle")
