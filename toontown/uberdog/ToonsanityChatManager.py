from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal

class ToonsanityChatManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ToonsanityChatManager')

    def sendChatMessage(self, message):
        self.sendUpdate('chatMessage', [message])

    def sendWhisperMessage(self, message, receiverAvId):
        self.sendUpdate('whisperMessage', [message, receiverAvId])