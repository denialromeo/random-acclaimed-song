@echo const songs = [ > songs.js
@sed s/\"/\\\\\"/g written > t
@sed "s/^\(.*\)$/\"\1\",/" t >> songs.js
@echo ] >> songs.js
@echo console.log(songs) >> songs.js
@del t
