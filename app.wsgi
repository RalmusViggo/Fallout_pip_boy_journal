import sys
import site
import os

site.addsitedir('/var/www/itprosjekt_js/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/itprosjekt_js')

os.chdir('/var/www/itprosjekt_js')

os.environ['VIRTUAL_ENV'] = '/var/www/itprosjekt_js/env'
os.environ['PATH'] = '/var/www/itprosjekt_js/env/bin:' + os.environ['PATH']

from app import app as application
