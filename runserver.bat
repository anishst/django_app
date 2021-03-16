REM activate venv and run django server
@echo off
start "" http://localhost:8000
cmd /k "cd /d %~dp0\env\Scripts\ & activate & cd /d  %~dp0\src & python manage.py runserver"