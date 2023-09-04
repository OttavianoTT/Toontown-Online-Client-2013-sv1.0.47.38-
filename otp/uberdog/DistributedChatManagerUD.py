from direct.distributed.DistributedObjectUD import DistributedObjectUD
from direct.directnotify.DirectNotifyGlobal import directNotify

class DistributedChatManagerUD(DistributedObjectUD):
    notify = directNotify.newCategory('DistributedChatManagerUD')
    notify.setDebug(True)

    def online(self):
        pass

    def adminChat(self, todo0, todo1):
        pass

    def setAvatarLocation(self, todo0, todo1, todo2):
        pass

    def setAvatarCrew(self, todo0, todo1):
        pass

    def setAvatarGuild(self, todo0, todo1):
        pass

    def chatParentId(self, todo0):
        pass

    def chatZoneId(self, todo0):
        pass

    def chatFace(self, todo0):
        pass

    def chatEmote(self, todo0):
        pass

    def chatEmoteTarget(self, todo0):
        pass

    def chatIndex(self, todo0):
        pass

    def chatString(self, todo0):
        pass

    def speedChatTo(self, todo0):
        pass

    def speedChatFrom(self, todo0, todo1):
        pass

    def speedChatCustomTo(self, todo0):
        pass

    def speedChatCustomFrom(self, todo0, todo1):
        pass

    def whisperSCTo(self, todo0, todo1):
        pass

    def whisperSCFrom(self, todo0, todo1):
        pass

    def whisperSCCustomTo(self, todo0, todo1):
        pass

    def whisperSCCustomFrom(self, todo0, todo1):
        pass

    def whisperSCEmoteTo(self, todo0, todo1):
        pass

    def whisperSCEmoteFrom(self, todo0, todo1):
        pass

    def whisperIgnored(self, todo0):
        pass
