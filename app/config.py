# config file

import os

if os.environ.get('GOOGLE_KEY') is None:
    key_value = 'AIzaSyDf-8PO-M4h0cgIXw1dGZ4NCt1xVUWvFbY'
else:
    key_value = os.environ['GOOGLE_KEY']
