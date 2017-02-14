# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from app import create_app
from app.task import celery

app = create_app('default')
app.app_context().push()


if __name__ == '__main__':
    app.run(debug=True)
