import sys
sys.path.append('/tmp')
# import sidefx
import os

print('SESI_CLIENT_SECRET_KEY = {}'.format(os.environ['SESI_CLIENT_SECRET_KEY']))
print('SESI_CLIENT_ID = {}'.format(os.environ['SESI_CLIENT_ID']))
