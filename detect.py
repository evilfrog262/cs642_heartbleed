#! /usr/bin/env python

import sys, struct, socket

ip_addr = '';

def get_args() :
        args = sys.argv
        if (len(args) != 2) :
                print "Usage: detect.py <IP address>"
        ip_addr = args[1]
        print(ip_addr)

if __name__ == "__main__" :
        print "running main woo"
        get_args()
