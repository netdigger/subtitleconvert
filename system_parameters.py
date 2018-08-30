# -*- coding: utf-8 -*-

import getopt
import sys


class SystemParameters:

    def __init__(self):
        self._SetDefault()
        self._ReadFromCmdLine()

    def _SetDefault(self):
        self.input_dir = "./"
        self.output_dir = "./"
        self.input_type = "lrc"
        self.output_type = "rst"

    def _ReadFromCmdLine(self):
        try:
            optlist, args = getopt.gnu_getopt(
                sys.argv[1:], 'I:O:i:o:',
                ['input-type=', 'output-type=', 'input-dir=', 'output-dir='])
        except getopt.GetoptError as err:
            print(err)
            self._Usage()
            sys.exit(1)

        for opt, argv in optlist:
            if opt in ("-I", "--input-type"):
                self.input_type = argv.lower()
            elif opt in ("-O", "--output-type"):
                self.output_type = argv.lower()
            elif opt in ("-i", "--input-dir"):
                self.input_dir = argv
                if not argv.endswith("/"): self.input_dir += "/"
            elif opt in ("-o", "--output-dir"):
                self.output_dir = argv
                if not argv.endswith("/"): self.output_dir += "/"

    def _Usage(self):
        print("It is a tool for convert subtitle format.\n")
        print("Usage:\n")
        print("\t python " + sys.argv[0] + " [command]\n")
        print("The commands are:\n")
        print("\t-I,--Input-type\t the type of source subtitle")
        print("\t-O,--Output-type\t the type of new subtitle")
        print("\t-i,--input-dir\t the directory with subtitle")
        print("\t-o,--output-dir\t the directory used to same new subtitle")
