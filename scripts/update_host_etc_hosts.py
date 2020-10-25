#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Just rewrite /etc/hosts and add current running docker services to it.
# Only for Linux, need root privileges.

import os
import sys
import subprocess


ENTRIES_START = '# ./update_host_etc_hosts.py start'
ENTRIES_END = '# ./update_host_etc_hosts.py end'
HOSTS_PATHNAME = '/etc/hosts'


if os.geteuid() != 0:
    print('You need root privileges')
    sys.exit(1)

services_to_ips = subprocess.check_output("sudo docker ps -aq | while read line;  do sudo docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $line ; done", shell=True)
new_entries = []
current_entries = []

# process new entries
for ientry in services_to_ips.split('\n'):
    ientry_parts = [ipart.strip() for ipart in ientry.strip().split(' - ') if ipart.strip()]
    if len(ientry_parts) != 2:
        continue

    if ientry_parts[0][0] == '/':
        ientry_parts[0] = ientry_parts[0][1:]

    service_name = ientry_parts[0]
    service_ip = ientry_parts[1]

    full_raw_service_name = service_ip + ' ' + service_name
    if full_raw_service_name not in new_entries:
        new_entries.append(full_raw_service_name)


# parse current /etc/hosts
skip_next_entry = False

for ihost_entry in open(HOSTS_PATHNAME).read().split('\n'):
    ihost_entry = ihost_entry.strip()

    if ihost_entry == ENTRIES_START:
        skip_next_entry = True
        continue
    elif ihost_entry == ENTRIES_END:
        skip_next_entry = False
        continue

    if skip_next_entry:
        continue
    
    current_entries.append(ihost_entry)

# add new entries
current_entries.append(ENTRIES_START)
for inew_entry in new_entries:
    if inew_entry not in current_entries:
        current_entries.append(inew_entry)
        print(inew_entry)

current_entries.append(ENTRIES_END)
current_entries.append('')

# rewrite /etc/hosts
with open(HOSTS_PATHNAME, 'w') as f:
    f.write('\n'.join(current_entries))
