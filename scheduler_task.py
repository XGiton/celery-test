#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    scheduler_task.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-14
    :python version: 2.7
    
"""
from datetime import datetime
from scheduler_celery import scheduler_inst


@scheduler_inst.task(name='scheduler_test_a')
def test():
    print 'scheduler test a: %s' % datetime.now().strftime('%Y-%m-%d %H:%M')
