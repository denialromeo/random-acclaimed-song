rem schtasks /create /tn "random-acclaimed-song-maintenance" /tr C:\Users\dvmoo\Desktop\code\random-acclaimed-song\maintain.bat  /sc daily /st 00:01 
@wc -l C:\Users\dvmoo\Desktop\code\random-acclaimed-song\new-written
@python C:\Users\dvmoo\Desktop\code\random-acclaimed-song\random_acclaimed_song.py
@if %errorlevel% neq 0 exit /b %errorlevel%
@copy /y C:\Users\dvmoo\Desktop\code\random-acclaimed-song\new-written C:\Users\dvmoo\Desktop\code\random-acclaimed-song\written
@break > C:\Users\dvmoo\Desktop\code\random-acclaimed-song\new-written
@cd C:\Users\dvmoo\Desktop\code\random-acclaimed-song & commit & b & m
