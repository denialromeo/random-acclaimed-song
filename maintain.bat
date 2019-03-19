@python random_acclaimed_song.py
@if %errorlevel% neq 0 exit /b %errorlevel%
@copy /y new-written written
@call output-javascript.bat
