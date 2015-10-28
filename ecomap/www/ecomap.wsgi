import sys
import os

os.environ['PRODROOT'] = '/home/frutkic/projects/ecomap/ecomap'
os.environ['PYSRCROOT'] = '/home/frutkic/projects/ecomap/ecomap/src/python'
os.environ['CONFROOT'] = '/home/frutkic/projects/ecomap/ecomap/etc'
os.environ['PYTHONPATH'] = '/home/frutkic/projects/ecomap/ecomap/src/python'
os.environ['PYTHON'] = 'home/frutkic/projects/ecomap/ecomap/etc/python'

activate_this = '/home/frutkic/venv/ecomap/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/home/frutkic/projects/ecomap/ecomap/www')
sys.path.insert(1, '/home/frutkic/projects/ecomap/ecomap/src/python')

from view import app as application
