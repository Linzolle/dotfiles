#!/usr/bin/python

import dbus
import os
import sys


try:
    bus = dbus.SessionBus()
    spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")

    if (sys.argv):
        control_iface = dbus.Interface(spotify, 'org.mpris.MediaPlayer2.Player')
        if (sys.argv[1] == '-b'):
            control_iface.Previous()
        elif (sys.argv[1] == '-p'):
            control_iface.PlayPause()
        elif (sys.argv[1] == '-n'):
            control_iface.Next()
    exit
except dbus.exceptions.DBusException:
    exit
