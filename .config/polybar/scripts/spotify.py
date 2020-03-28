#!/usr/bin/python

import dbus
import os
import sys


try:
    bus = dbus.SessionBus()
    spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")

    spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
    props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    if (sys.version_info > (3, 0)):
        print(str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))
    else:
        print(props['xesam:artist'][0] + " - " + props['xesam:title']).encode('utf-8')
    exit
except dbus.exceptions.DBusException:
    exit
