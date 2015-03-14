# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from direct.directnotify.DirectNotify import DirectNotify
import spacedrive
from networking.server_net import NetworkSystem

__author__ = 'croxis'


def setup(name='Server Name'):
    log = DirectNotify().newCategory("Allegiance-Server-" + name)
    log.debug("Loading space drive")
    spacedrive.init(run_server=True,
                    run_client=False,
                    log_level='debug',
                    window_title='Allegiance 2')
    log.info("Setting up server network")
    spacedrive.init_server_net(NetworkSystem, port=47624)


def start():
    spacedrive.run()