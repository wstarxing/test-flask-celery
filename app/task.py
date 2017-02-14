# -*- coding: UTF-8 -*-
import random
import time
import os
from app import celery


@celery.task
def job1():
    dir_get = os.getcwd()
    print dir_get
    if os.path.exists(dir_get+'\\'+'testa') is False:
        os.mkdir(dir_get+'\\'+'testa')
        print 'mkdir'
    return 'ok'


@celery.task
def job2():
    return 'hello celery'


@celery.task(bind=True, max_retries=3)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))

        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}