#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc
import six

from oslo_config import cfg


@six.add_metaclass(abc.ABCMeta)
class ClientPlugin(object):

    # Module which contains all exceptions classes which the client
    # may emit
    exceptions_module = None

    def __init__(self, context):
        self.context = context
        self.clients = context.clients
        self._client = None

    def client(self):
        if not self._client:
            self._client = self._create()
        return self._client

    @abc.abstractmethod
    def _create(self):
        '''Return a newly created client.'''
        pass

    @property
    def auth_token(self):
        # Always use the auth_token from the keystone client, as
        # this may be refreshed if the context contains credentials
        # which allow reissuing of a new token before the context
        # auth_token expiry (e.g trust_id or username/password)
        return self.clients.client('keystone').auth_token

    def url_for(self, **kwargs):
        kc = self.clients.client('keystone')
        return kc.service_catalog.url_for(**kwargs)

    def _get_client_option(self, client, option):
        # look for the option in the [clients_${client}] section
        # unknown options raise cfg.NoSuchOptError
        try:
            group_name = 'clients_' + client
            cfg.CONF.import_opt(option, 'bilean.common.config',
                                group=group_name)
            v = getattr(getattr(cfg.CONF, group_name), option)
            if v is not None:
                return v
        except cfg.NoSuchGroupError:
            pass  # do not error if the client is unknown
        # look for the option in the generic [clients] section
        cfg.CONF.import_opt(option, 'bilean.common.config', group='clients')
        return getattr(cfg.CONF.clients, option)

    def is_client_exception(self, ex):
        '''Returns True if the current exception comes from the client.'''
        if self.exceptions_module:
            if isinstance(self.exceptions_module, list):
                for m in self.exceptions_module:
                    if type(ex) in m.__dict__.values():
                        return True
            else:
                return type(ex) in self.exceptions_module.__dict__.values()
        return False

    def is_not_found(self, ex):
        '''Returns True if the exception is a not-found.'''
        return False

    def is_over_limit(self, ex):
        '''Returns True if the exception is an over-limit.'''
        return False

    def ignore_not_found(self, ex):
        '''Raises the exception unless it is a not-found.'''
        if not self.is_not_found(ex):
            raise ex
