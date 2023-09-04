from panda3d.core import Filename, VirtualFileSystem

from direct.directnotify.DirectNotifyGlobal import directNotify

from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

import os

class Settings:
    notify = directNotify.newCategory('Settings')

    def __init__(self):
        self.fileName = Filename('./useropt')
        self.fileName = self.fileName.toOsLongName()

        self.vfs = VirtualFileSystem.getGlobalPtr()

        self.header = 'UserSettings'

        # Render engine library names.
        self.GL = 'pandagl'
        self.DX7 = 'pandadx7'
        self.DX8 = 'pandadx8'
        self.DX9 = 'pandadx9'

        # Defaults for the client.
        self.windowedMode = True
        self.music = True
        self.sfx = True
        self.toonChatSounds = True
        self.musicVolume = 1.0
        self.sfxVolume = 1.0
        self.resolution = True
        self.resolutionDimensions = [800, 600]
        self.acceptingNewFriends = True
        self.acceptingNonFriendWhispers =  True
        self.embeddedMode = False

    def readSettings(self):
        if not self.doSavedSettingsExist():
            self.vfs.createFile(self.fileName)
            self.writeSettings()
            return

        data = self.vfs.readFile(self.fileName, False)

        header = data[:12]

        if header != self.header:
            self.notify.warning('Settings header was invalid!')
            self.writeSettings()
            return

        dg = PyDatagram(data)
        dgi = PyDatagramIterator(dg)

        self.music = dgi.getBool()
        self.sfx = dgi.getBool()
        self.toonChatSounds = dgi.getBool()
        self.acceptingNewFriends = dgi.getBool()
        self.acceptingNonFriendWhispers = dgi.getBool()
        self.resolutionDimensions[0] = dgi.getUint16()
        self.resolutionDimensions[1] = dgi.getUint16()
        self.windowedMode = dgi.getBool()
        self.embeddedMode = dgi.getBool()

        self.setMusic(self.music)
        self.setSfx(self.sfx)
        self.setToonChatSounds(self.toonChatSounds)
        self.setAcceptingNewFriends(self.acceptingNewFriends)
        self.setAcceptingNonFriendWhispers(self.acceptingNonFriendWhispers)
        self.setWindowedMode(self.windowedMode)
        self.setEmbeddedMode(self.embeddedMode)

    def writeSettings(self):
        dg = PyDatagram()
        dgi = PyDatagramIterator(dg)

        dg.addBool(self.getMusic())
        dg.addBool(self.getSfx())
        dg.addBool(self.getToonChatSounds())
        dg.addBool(self.getAcceptingNewFriends())
        dg.addBool(self.getAcceptingNonFriendWhispers())
        dg.addUint32(self.resolutionDimensions[0])
        dg.addUint32(self.resolutionDimensions[1])
        dg.addBool(self.getWindowedMode())
        dg.addBool(self.getEmbeddedMode())

        data = self.header + dgi.getRemainingBytes()

        if self.vfs.exists(self.fileName):
            self.vfs.deleteFile(self.fileName)

        self.vfs.writeFile(self.fileName, data, False)

    def setWindowedMode(self, windowedMode):
        self.windowedMode = windowedMode

    def getWindowedMode(self):
        return self.windowedMode

    def setMusic(self, music):
        self.music = music

    def getMusic(self):
        return self.music

    def setSfx(self, sfx):
        self.sfx = sfx

    def getSfx(self):
        return self.sfx

    def setToonChatSounds(self, toonChatSounds):
        self.toonChatSounds = toonChatSounds

    def getToonChatSounds(self):
        return self.toonChatSounds

    def setMusicVolume(self, musicVolume):
        self.musicVolume = musicVolume

    def getMusicVolume(self):
        return self.musicVolume

    def setSfxVolume(self, sfxVolume):
        self.sfxVolume = sfxVolume

    def getSfxVolume(self):
        return self.sfxVolume

    def setResolution(self, resolution):
        resolution = self.resolutionDimensions[0]
        resolution = self.resolutionDimensions[1]

    def getResolution(self):
        return self.resolution
    
    def setEmbeddedMode(self, embeddedMode):
        self.embeddedMode = embeddedMode

    def getEmbeddedMode(self):
        return self.embeddedMode

    def doSavedSettingsExist(self):
        return self.vfs.exists(self.fileName)

    def getAcceptingNewFriends(self):
        return self.acceptingNewFriends
    
    def setAcceptingNewFriends(self, acceptingNewFriends):
        self.acceptingNewFriends = acceptingNewFriends

    def getAcceptingNonFriendWhispers(self):
        return self.acceptingNonFriendWhispers

    def setAcceptingNonFriendWhispers(self, acceptingNonFriendWhispers):
        self.acceptingNonFriendWhispers = acceptingNonFriendWhispers
