#!/usr/bin/python3
# -*- coding: utf-8 -*-

from input_element import InputElement
from lrc_decode import LRCDecode 
from srt_encode import SRTEncode 
from output_element import OutputElement

def main():
    in_node = InputElement("./", "lrc")
    decode_node = LRCDecode()
    encode_node = SRTEncode()
    out_node = OutputElement()

    in_node.SetNextElement(decode_node)
    decode_node.SetNextElement(encode_node)
    encode_node.SetNextElement(out_node)

    in_node.Start()
    

if __name__ == "__main__":
    x = 1
    print(format(1, "02d"))
    main()
