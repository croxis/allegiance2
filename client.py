# ## Python 3 look ahead imports ###
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from direct.directnotify.DirectNotify import DirectNotify
import spacedrive

from gui_manager import MainMenu
from networking.client_net import NetworkSystem

__author__ = 'croxis'


def toggleSceneWireframe():
    spacedrive.base.wireframe = not spacedrive.base.wireframe
    if spacedrive.base.wireframe:
        spacedrive.base.render.setRenderModeWireframe()
    else:
        spacedrive.base.render.clearRenderMode()


def setup():
    log = DirectNotify().newCategory("Allegiance-Client")
    log.debug("Loading space drive")
    spacedrive.init(run_server=False,
                    run_client=True,
                    log_level='debug',
                    window_title='Allegiance 2')
    log.info('Setting up graphics')
    #spacedrive.init_graphics(debug_mouse=False)
    log.info("Setting up client gui")
    spacedrive.init_gui()
    spacedrive.base.wireframe = False
    spacedrive.base.accept("f3", toggleSceneWireframe)
    spacedrive.gui_system.setup_screen(MainMenu())
    log.info("Setting up client network")
    spacedrive.init_server_net(NetworkSystem)



def start():
    spacedrive.run()