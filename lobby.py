__author__ = 'croxis'
'''This will require a more advanced ecs module than what we have now.
Will need to refactor later.
We do not use spacedrive here as we don't want to start up ecs.
This is for MULTIGAME lobby and management. Single game lobby works different.
'''
from multiprocessing import Process
from direct.directnotify.DirectNotify import DirectNotify
from direct.showbase.ShowBase import ShowBase

log = DirectNotify().newCategory("Allegiance-Lobby")
server_instances = []


def start_lobby():
    base = ShowBase()
    log.info("Setting up lobby network")
    spacedrive.init_server_net(lobby_net.NetworkSystem)
    base.run()


def create_server(port=47624):
    p = Process(target=serverstartupfunction, args=(port,))
    p.start()