#!/bin/bash -e

cd "$(dirname "$0")"

vagrant up
vagrant ssh
