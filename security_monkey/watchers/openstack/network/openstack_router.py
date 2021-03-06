#     Copyright (c) 2017 AT&T Intellectual Property. All rights reserved.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
"""
.. module: security_monkey.openstack.watchers.router
    :platform: Unix

.. version:: $$VERSION$$
.. moduleauthor:: Michael Stair <mstair@att.com>

"""
from security_monkey.watchers.openstack.openstack_watcher import OpenStackWatcher


class OpenStackRouter(OpenStackWatcher):
    index = 'openstack_router'
    i_am_singular = 'Router'
    i_am_plural = 'Routers'
    account_type = 'OpenStack'

    def __init__(self, *args, **kwargs):
        super(OpenStackRouter, self).__init__(*args, **kwargs)
        self.honor_ephemerals = True
        self.item_type = 'router'
        self.service = 'network'
        self.generator = 'routers'
        self.ephemeral_paths = [ "updated_at" ]
