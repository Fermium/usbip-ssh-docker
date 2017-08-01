#!/bin/bash

sh -c "cd docker-usbip && docker build ./ -t fermiumlabs-usbip"
sh -c "cd docker-autossh && docker build ./ -t fermiumlabs-autossh"
