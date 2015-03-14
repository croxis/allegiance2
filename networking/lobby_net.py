# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# We use the framework but we dont use it in sandbox system.
from sandbox.networking import UDPNetworkSystem

__author__ = 'croxis'

class NetworkSystem(UDPNetworkSystem):
    """Network system for mulitgame lobby."""
    def init2(self):
        self.accept("broadcastData", self.broadcast_data)
        self.accept("confirmPlayerStations", self.confirmPlayerStations)
        self.accept('playerDisconnected', self.playerDisconnected)
        self.activePlayers = []  # PlayerComponent
        self.playerMap = {}

