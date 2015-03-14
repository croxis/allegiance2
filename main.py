from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Allegiance runs as client or server, never both at once.
# Default is to assume client
# Init will be done in lobby, server, and client files due to multiprocess

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", action="store_true",
                    help="run as a single multiplayer server")
parser.add_argument("-l", "--lobby", action="store_true",
                    help="run as a lobby multiplayer server")
args = parser.parse_args()

run_server = args.server
run_lobby = args.lobby

if not run_server or not run_lobby:
    # We must import this before panda due to talmoc issues in linux
    from cefpython3 import cefpython

from direct.directnotify.DirectNotify import DirectNotify
from panda3d.core import loadPrcFileData

loadPrcFileData("", "notify-level-Allegiance debug")
log = DirectNotify().newCategory("Allegiance")


import client
import lobby
import server


def start_client():
    client.setup()
    client.start()


def start_lobby():
    print("Requires more advanced ecs that can be instanced between servers.")
    print("Look into creating new allegance 2 server instances")


def start_server():
    server.setup()
    server.start()

if run_server:
    start_server()
elif run_lobby:
    start_lobby()
else:
    start_client()


__author__ = 'croxis'