@break > new-written
@echo const albums = [ > albums.js
@sed s/\"/\\\\\"/g albums > t
rem @powershell "get-content .\t | set-content -encoding utf8 g"
@sed "s/^\(.*\)$/\"\1\",/" t >> albums.js
@echo ] >> albums.js
@del t
@copy /y albums.js C:\Users\hi\Desktop\danielmoore.us\js\albums.js
@del *~
