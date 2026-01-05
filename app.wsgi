import sys
import site
import os

site.addsitedir('/var/www/itprosjekt/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/itprosjekt')

os.chdir('/var/www/itprosjekt')

os.environ['VIRTUAL_ENV'] = '/var/www/itprosjekt/env'
os.environ['PATH'] = '/var/www/itprosjekt/env/bin:' + os.environ['PATH']

from app import app as application
