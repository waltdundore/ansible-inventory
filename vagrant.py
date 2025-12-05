#!/usr/bin/env python3
"""
Dynamic inventory script for Vagrant VMs in this project only
Detects running Vagrant VMs from this directory
"""

import json
import subprocess
import sys
import os

def get_vagrant_vms():
    """Get list of running Vagrant VMs in this project"""
    inventory = {
        '_meta': {'hostvars': {}},
        'vagrant': {'hosts': [], 'vars': {'ansible_connection': 'local'}}
    }
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    
    # Check both single and multi-VM Vagrantfiles in this project
    vagrantfiles = ['Vagrantfile', 'Vagrantfile.multi']
    
    for vagrantfile in vagrantfiles:
        try:
            env = os.environ.copy()
            if vagrantfile != 'Vagrantfile':
                env['VAGRANT_VAGRANTFILE'] = vagrantfile
            
            result = subprocess.run(
                ['vagrant', 'status', '--machine-readable'],
                capture_output=True,
                text=True,
                timeout=5,
                env=env,
                cwd=project_dir
            )
            
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    parts = line.split(',')
                    if len(parts) >= 4 and parts[2] == 'state' and parts[3] == 'running':
                        vm_name = parts[1]
                        if vm_name == 'default':
                            if 'localhost' not in inventory['vagrant']['hosts']:
                                inventory['vagrant']['hosts'].append('localhost')
                        else:
                            if vm_name not in inventory['vagrant']['hosts']:
                                inventory['vagrant']['hosts'].append(vm_name)
                                inventory['_meta']['hostvars'][vm_name] = {
                                    'ansible_connection': 'local'
                                }
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    
    return inventory

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print(json.dumps(get_vagrant_vms(), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps({}))
    else:
        print(json.dumps({}))
