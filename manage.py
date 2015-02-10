#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_console.settings")

    from django.core.management import execute_from_command_line

    args = ['manage.py', 'runserver', '0.0.0.0:8080']
    # db = ['manage.py', 'syncdb']
    execute_from_command_line(args)
