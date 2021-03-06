#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}


DOCUMENTATION = """
---
module: network_put
version_added: "2.6"
author: "Deepak Agrawal (@dagrawal)"
short_description: Copy files from Ansibe controller to a network device
description:
  - This module provides functionlity to copy file from Ansible controller to
    network devices.
options:
  src:
    description:
      - Specifies the source file. The path to the source file can either be
        the full path on the Ansible control host or a relative path from the
        playbook or role root directory.
    required: true
  protocol:
    description:
      - Protocol used to transfer file.
    default: scp
    choices: ['scp', 'sftp']
  dest:
    description:
      - Specifies the destination file. The path to destination file can
        either be the full path or relative path as supported by network_os.
    default:
      - Filename from src and at default directory of user shell on
        network_os.
    required: no

requirements:
    - "scp"

notes:
   - Some devices need specific configurations to be enabled before scp can work
     These configuration should be pre-configued before using this module
     e.g ios - C(ip scp server enable).
   - User privileage to do scp on network device should be pre-configured
     e.g. ios - need user privileage 15 by default for allowing scp.
   - Default destination of source file.
"""

EXAMPLES = """
- name: copy file from ansible controller to a network device
  network_put:
    src: running_cfg_ios1.txt

- name: copy file at root dir of flash in slot 3 of sw1(ios)
  network_put:
    src: running_cfg_sw1.txt
    protocol: sftp
    dest : flash3:/running_cfg_sw1.txt
"""

RETURN = """
"""
