#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
         raise ImportError(
            "Salut daniel"
            "Nous abvons quleques soucis à installer Django ! L'avez vous installé ? "
            "Avez vous ajouté Django dans votre Path ? "
            "Avez vous activez l'environement virtuel ?"
        ) from exc
    execute_from_command_line(sys.argv)
##

if __name__ == '__main__':
    main()
