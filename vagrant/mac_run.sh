#! /bin/bash

vagrant up
vagrant provision
vagrant ssh -c ./ipythonStartup.sh &
sleep 1
open http://localhost:8888
