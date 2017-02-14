# -*- coding: UTF-8 -*-

from . import main
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import *
from app.task import long_task


@main.route('/', methods=[u'GET'])
def index():
    return render_template('index.html')


@main.route('/longtask', methods=[u'POST'])
def task():
    # task = long_task.apply_async()
    task = long_task.delay()
    return jsonify({}), 202, {'Location': url_for('main.taskstatus', task_id=task.id)}


@main.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    print task.state
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
