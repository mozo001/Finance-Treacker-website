"""
WSGI config for finance_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
import pip

from django.core.wsgi import get_wsgi_application
pip.main(['install','setuptools'])
try:
  import pkg_rsources
except importError:
  pip.main(['install','setuptools'])
  import pkg_resources
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_project.settings')
try:
  application = get_wsgi_application()
  app =application
except Exception as e:
  print(f"CRITICAL ERROR:{e}")
  raise e



