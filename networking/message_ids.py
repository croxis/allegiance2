# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__author__ = 'croxis'


#Protocol space
#0-99 common game elements
#100-199 login and server handshaking and admin stuff

ACK = 0
POS_UPDATE = 1  # Position update for a given ship.  1 - 10 times a second
THRUST_REQ = 2
POS_PHYS_UPDATE = 3   # Full physics update for a given ship.
# 1 per second unless a non predictive force (ie non gravity) is applied
DATE_UPDATE = 5  # 1 per 5 seconds
SEND_CHAT = 6
RECEIVE_CHAT = 7

NEW_SHIP = 9  # A ship has entered sensor range. All data is sent in this packet
NEW_STATION = 11  # A station has entered sensor range.
LEAVE_SENSOR_SHIP = 13  # A ship has left sensor range.

PLAYER_MOVED_SHIP = 15  # When a player moves to a new ship

LOGIN = 100
LOGIN_DENIED = 101
LOGIN_ACCEPTED = 103

ACCOUNT_REC = 110  # Requests name of account for a given id entity id
ACCOUNT_ACK = 111





