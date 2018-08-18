#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from input_element import InputElement
from lrc_decode import LRCDecode 
from srt_encode import SRTEncode 
from output_element import OutputElement
from system_parameters import SystemParameters

def main():
    params = SystemParameters()
    if params.input_type == "lrc":
        in_node = InputElement(params.input_dir, "lrc")
        decode_node = LRCDecode()
    else:
        print("current not support decode " + params.input_type + " format")
        sys.exit(1)

    if params.output_type == "srt":
        encode_node = SRTEncode()
    else:
        print("current not support encode " + params.output_type + " format")
        sys.exit(1)


    out_node = OutputElement(params.output_dir)

    in_node.SetNextElement(decode_node)
    decode_node.SetNextElement(encode_node)
    encode_node.SetNextElement(out_node)

    in_node.Start()

if __name__ == "__main__":
    main()
