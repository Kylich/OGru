# -*- coding: utf-8 -*-
import sys, os
sys.path.append('/Flask') # указываем директорию с проектом
f = open('/tmp/restart.txt', 'w')
f.close()
from Flask import app as application # когда Flask стартует, он ищет application. Если не указать 'as application', сайт не заработает
from werkzeug.debug import DebuggedApplication # Опционально: подключение модуля отладки
application.wsgi_app = DebuggedApplication(application.wsgi_app, True) # Опционально: включение модуля отадки
application.debug = True  # Опционально: True/False устанавливается по необходимости в отладке