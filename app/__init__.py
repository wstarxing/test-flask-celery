# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from celery import Celery,platforms
# from flask_apscheduler import APScheduler



celery = Celery(__name__, broker=config['development'].CELERY_BROKER_URL)
#apscheduler = APScheduler()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    celery.conf.update(app.config)
    # TaskBase = celery.Task

    #apscheduler.init_app(app)

    # class ContextTask(TaskBase):
    #     abstract = True
    #
    #     def __call__(self, *args, **kwargs):
    #         with app.app_context():
    #             return TaskBase.__call__(self, *args, **kwargs)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # celery.Task = ContextTask
    platforms.C_FORCE_ROOT = True

    return app
