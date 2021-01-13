@break > new-written
@echo const albums = [ > albums.js
@sed s/\"/\\\\\"/g albums > t
@powershell "get-content .\t | set-content -encoding utf8 g"
@sed "s/^\(.*\)$/\"\1\",/" g >> albums.js
@echo ] >> albums.js
@del t
@del g
@copy /y albums.js C:\Users\hi\Desktop\danielmoore.us\js\albums.js
@del *~
