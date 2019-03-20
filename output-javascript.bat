@echo const songs = [ > songs.js
@sed s/\"/\\\\\"/g written > t
@powershell "get-content .\t | set-content -encoding utf8 g"
@sed "s/^\(.*\)$/\"\1\",/" g >> songs.js
@echo ] >> songs.js
@del t
@del g
@copy /y songs.js ..\..\danielmoore.us\js\songs.js
