# -*- coding: UTF-8 -*-
from celery.schedules import timedelta


class Config:
    # celery
    CELERY_BROKER_URL = 'redis://192.168.0.203:6379/5'
    CELERY_RESULT_BACKEND = 'redis://192.168.0.203:6379/5'

    CELERYBEAT_SCHEDULE = {
        # 'job1': {
        #     'task': 'app.task.job1',
        #     'schedule': timedelta(seconds=10),
        #     'args': (),  # 参数
        # },
        'job2': {
            'task': 'app.task.job2',
            'schedule': timedelta(seconds=10),
            'args': (),  # 参数
        }
    }

    CELERY_TIMEZONE = 'Asia/Shanghai'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    #  'heroku': HerokuConfig,
    #  'unix': UnixConfig,

    'default': DevelopmentConfig
}