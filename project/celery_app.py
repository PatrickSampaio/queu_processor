from __future__ import absolute_import, unicode_literals
from celery import Celery

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
import queu_processor

app = Celery('celery_app',
             broker='amqp://',
             backend='amqp://',
             include=['queu_processor.project.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
