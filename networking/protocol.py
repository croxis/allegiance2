# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import capnp
#import messages_capnp
from direct.distributed.PyDatagram import PyDatagram
from . import message_ids

__author__ = 'croxis'

capnp.remove_import_hook()
messages_capnp = capnp.load(b'networking/messages.capnp')


# Client to server even
#Server to client odd
#If both will probably be even

# Packet structure
# msgID = myIterator.getUint8()
# remotePacketCount = myIterator.getUint8()
# ack = myIterator.getUint8()
# acks = myIterator.getUint16()
# hashID = myIterator.getUint16()
# This will be followed by additional data based on packet types

def make_generic_datagram(key, packet_count=0, data=""):
    datagram = PyDatagram()
    datagram.addUint8(key)
    datagram.addUint8(packet_count)
    datagram.addUint8(0)
    datagram.addUint16(0)
    datagram.addUint16(0)
    datagram.add_string(data)
    return datagram


def login(user_name, hashed_password):
    message = messages_capnp.Login.new_message(username=user_name,
                                               hashedpassword=hashed_password)
    return make_generic_datagram(message_ids.LOGIN, data=message)
