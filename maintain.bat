rem schtasks /create /tn "random-acclaimed-song-maintenance" /tr C:\Users\hi\Desktop\code\random-acclaimed-song\maintain.bat  /sc daily /st 00:01 
@wc -l C:\Users\hi\Desktop\code\random-acclaimed-song\new-written
@python C:\Users\hi\Desktop\code\random-acclaimed-song\random_acclaimed_song.py
@python C:\Users\hi\Desktop\code\random-acclaimed-song\random_acclaimed_song.py
@python C:\Users\hi\Desktop\code\random-acclaimed-song\random_acclaimed_song.py
@if %errorlevel% neq 0 exit /b %errorlevel%
@copy /y C:\Users\hi\Desktop\code\random-acclaimed-song\new-written C:\Users\hi\Desktop\code\random-acclaimed-song\written
@call C:\Users\hi\Desktop\code\random-acclaimed-song\output-javascript.bat
@break > C:\Users\hi\Desktop\code\random-acclaimed-song\new-written
