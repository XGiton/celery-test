#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    default_task.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-14
    :python version: 2.7
    
"""
from datetime import datetime
from default_celery import default_inst


@default_inst.task(name='default_test_a')
def test():
    print 'default test a: %s' % datetime.now().strftime('%Y-%m-%d %H:%M')
