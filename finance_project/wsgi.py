"""
WSGI config for finance_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_project.settings')
try:
  application = get_wsgi_application()
  app =application
except Exception as e:
  print(f"CRITICAL ERROR:{E}")
  raise e



