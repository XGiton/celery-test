#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    celery_config.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2016-10-14
    :python version: 2.7
    
"""
from celery import Celery, platforms
from celery.schedules import crontab


class BaseCeleryConfig(object):
    """Base configuration for celery.
    Each celery instance configs class will extend from this class
    """
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERYD_CONCURRENCY = 4
    CELERY_ACKS_LATE = True
    CELERY_IGNORE_RESULT = True
    CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERY_EVENT_QUEUE_EXPIRES = 7200
    CELERY_TIMEZONE = 'UTC'


class DefaultCeleryConfig(BaseCeleryConfig):
    """"""
    pass


class ScheduleCeleryConfig(BaseCeleryConfig):
    """ Schedule celery configuration for this project"""
    CELERY_ENABLE_UTC = False
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_IMPORTS = (
        'scheduler_and_default_task',  # if comment this line, schedule works well
        'scheduler_task'
    )
    CELERYBEAT_SCHEDULE = {
        'scheduler_test_a': {
            'task': 'scheduler_test_a',
            'schedule': crontab(minute='*', hour='12',
                                day_of_month=14),
        },
        'scheduler_test_b': {
            'task': 'scheduler_test_b',
            'schedule': crontab(minute='*', hour='12',
                                day_of_month=14),
        },
    }


def create_celery_instance(name, config, broker='redis://localhost:6379/1'):
    """
    Create Celery instance

    Args:
        name: celery name
        config: celery config
        broker: celery broker

    Returns:
        celery_instance: celery instance

    """
    inst = Celery(name, broker=broker)
    inst.config_from_object(config)
    platforms.C_FORCE_ROOT = True  # running celery worker by rooter
    return inst



