# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
  - See respective platform section for more details
requirements:
  - See respective platform section for more details
notes:
  - Ansible modules are available for Dell EMC PowerStore Storage Platform

'''

# Documentation fragment for PowerStore (powerstore)
    POWERSTORE = r'''
options:
    array_ip:
        description:
            - IP or FQDN of the PowerStore management system.
        type: str
        required: True
    verifycert:
        description:
            - Boolean variable to specify whether to validate SSL
              certificate or not.
            - True - indicates that the SSL certificate should be
                     verified. Set the environment variable REQUESTS_CA_BUNDLE
                     to the path of the SSL certificate.
            - False - indicates that the SSL certificate should not be
                      verified.
        type: bool
        required: True
        choices: [True, False]
    user:
        description:
            - The username of the PowerStore host.
        type: str
        required: True
    password:
        description:
            - The password of the PowerStore host.
        type: str
        required: True

requirements:
  - A Dell EMC PowerStore Storage System.
  - Ansible 2.9 or 2.10
notes:
  - The modules prefixed with dellemc_powerstore are built to support the
    Dell EMC PowerStore storage platform.
'''
