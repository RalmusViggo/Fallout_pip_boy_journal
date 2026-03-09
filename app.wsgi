import sys
import site
import os

site.addsitedir('/var/www/Fallout_pip_boy_journal-main/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/Fallout_pip_boy_journal-main')

os.chdir('/var/www/Fallout_pip_boy_journal-main')

os.environ['VIRTUAL_ENV'] = '/var/www/Fallout_pip_boy_journal-main/env'
os.environ['PATH'] = '/var/www/Fallout_pip_boy_journal-main/env/bin:' + os.environ['PATH']

from app import app as application
