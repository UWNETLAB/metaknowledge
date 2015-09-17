@Echo OFF
vagrant up
vagrant provision
start "" http://localhost:1159
pause
