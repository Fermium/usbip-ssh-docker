#!/bin/bash

touch /id_rsa
chmod 0400 /id_rsa

autossh -M 0 -N -q  -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -R 3240:localhost:3240 remoteuser@remoteserver.com
