#!/bin/bash

. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts.ini --ask-become-pass create_instance.yaml
. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts.ini --ask-become-pass setup_env.yaml