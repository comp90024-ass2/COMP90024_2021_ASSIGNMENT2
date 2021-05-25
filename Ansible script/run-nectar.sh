#!/bin/bash


. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts --ask-become-pass main_instance.yaml
. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts --ask-become-pass couchdb-setup.yaml
. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts --ask-become-pass deploy_Harvester.yaml
. ./unimelb-comp90024-2021-grp-36-openrc.sh; ansible-playbook -i hosts --ask-become-pass build_website.yaml
