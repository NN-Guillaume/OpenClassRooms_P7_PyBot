import os


if os.environ.get('key_value') is None:
    key_value = ' '
else:
    key_value = os.environ['key_value']
