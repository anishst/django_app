REM activate venv and run django server
@echo off
cmd /k "cd /d %~dp0\env\Scripts\ & activate & cd /d  %~dp0\src & python manage.py runserver"