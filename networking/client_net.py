# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sandbox import UDPNetworkSystem
from direct.directnotify.DirectNotify import DirectNotify
from . import protocol
from . import message_ids

__author__ = 'croxis'

log = DirectNotify().newCategory("Allegiance-ClientNet")


class NetworkSystem(UDPNetworkSystem):
    def init2(self):
        self.packet_count = 0
        self.accept('login', self.send_login)

    def send_login(self, server_address, server_port, username,
                   hashed_password):
        self.server_address = server_address
        self.server_port = server_port
        datagram = protocol.login(username, hashed_password)
        log.debug("sending login")
        self.send_data(datagram, (server_address, server_port))