#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    scheduler_and_default_task.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-14
    :python version: 2.7
    
"""
from datetime import datetime
from scheduler_celery import scheduler_inst
from default_celery import default_inst


@default_inst.task(name='default_test_b')
def test():
    print 'default test b: %s' % datetime.now().strftime('%Y-%m-%d %H:%M')


@scheduler_inst.task(name='scheduler_test_b')
def test():
    print 'scheduler test b: %s' % datetime.now().strftime('%Y-%m-%d %H:%M')
