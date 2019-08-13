# -*- coding: utf-8 -*-
import sys, os
sys.path.append('/home/f/f950220q/open-gamer.ru/Flask') # указываем директорию с проектом
sys.path.append('/home/f/f950220q/.local/lib/python3.6/site-packages') # указываем директорию с библиотеками, куда поставили Flask
f = open('/home/f/f950220q/open-gamer.ru/tmp/restart.txt', 'w')
f.close()
from Flask import app as application # когда Flask стартует, он ищет application. Если не указать 'as application', сайт не заработает
from werkzeug.debug import DebuggedApplication # Опционально: подключение модуля отладки
application.wsgi_app = DebuggedApplication(application.wsgi_app, True) # Опционально: включение модуля отадки
application.debug = True  # Опционально: True/False устанавливается по необходимости в отладке