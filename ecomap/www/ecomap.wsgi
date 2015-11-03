import sys
import os

os.environ['PRODROOT'] = '/home/frutkic/projects/ecomap/ecomap'
os.environ['CONFROOT'] = os.path.dirname(os.environ['PRODROOT']) + '/ecomap/etc'
os.environ['PYSRCROOT'] = os.path.dirname(os.environ['PRODROOT']) + '/ecomap/src/python'

activate_this = '/home/frutkic/venv/ecomap/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/home/frutkic/projects/ecomap/ecomap/www')
sys.path.insert(1, '/home/frutkic/projects/ecomap/ecomap/src/python')

from ecomap.utils import get_logger

get_logger()

from view import app as application
