#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    default_celery.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-14
    :python version: 2.7
    
"""
from celery_config import create_celery_instance, DefaultCeleryConfig


default_inst = create_celery_instance('schedule_celery', DefaultCeleryConfig)