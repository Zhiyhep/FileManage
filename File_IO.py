#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.dat','w+') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y年 %m月 %d日'))

with open('test.dat','r') as f:
    s = f.read()
    print('open for read...')
    print(s)