#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 李哲 Li Zhe (leftuestc) <lizheseven@gmail.com> 
# Released under GNU General Public License

# Use yum to install local rpm files 
# usage: rpminstall.py [FILES]

# @hide

import os, sys

n=len(sys.argv)
if n < 2:
    exit(1)

packages=sys.argv[1:]
print '正在嘗試安裝套件...'
os.system( 'yum localinstall -y %s' % ' '.join( packages ) )
