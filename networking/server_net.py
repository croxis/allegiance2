# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from panda3d.core import loadPrcFileData

from sandbox.networking import UDPNetworkSystem

from .import message_ids

__author__ = 'croxis'


class NetworkSystem(UDPNetworkSystem):
    def init2(self):
        #self.accept("broadcastData", self.broadcast_data)
        #self.accept("confirmPlayerStations", self.confirmPlayerStations)
        #self.accept('playerDisconnected', self.playerDisconnected)
        pass

    def process_packet(self, msgid, remote_packet_count, ack, acks, hashid,
                       serialized, address):
        #If not in our protocol range then we just reject
        if msgid < 0 or msgid > 200:
            return
        if msgid is message_ids.LOGIN:
            print(serialized, address)