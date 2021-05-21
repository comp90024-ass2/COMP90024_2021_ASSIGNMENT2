#!/usr/bin/env bash

#Change permission
sudo chmod 0644 /etc/cron.d/cron_harvest

#Retrigger crontab
crontab /etc/cron.d/cron_harvest