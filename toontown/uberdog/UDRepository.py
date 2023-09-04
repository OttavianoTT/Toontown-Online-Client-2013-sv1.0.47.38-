from direct.directnotify.DirectNotifyGlobal import directNotify

from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed import OtpDoGlobals

from toontown.distributed.InternalRepository import InternalRepository
from toontown.parties.ToontownTimeManager import ToontownTimeManager

import time

class UDRepository(InternalRepository):
    notify = directNotify.newCategory('UDRepository')

    GameGlobalsId = OtpDoGlobals.OTP_DO_ID_TOONTOWN

    def __init__(self, baseChannel, serverId):
        InternalRepository.__init__(self, baseChannel, serverId, dcSuffix = 'UD')

        self.notify.setInfo(True)
        self.notify.info('UberDOG is now starting up.')

    def handleConnected(self):
        InternalRepository.handleConnected(self)

        self.notify.info('Generating root object...')
        rootObj = DistributedDirectoryAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)

        self.notify.info('Creating locals...')
        self.createLocals()

        self.notify.info('Generating managers...')
        self.generateManagers()

        self.notify.info('UberDOG is now ready.')

    def createLocals(self):
        self.toontownTimeManager = ToontownTimeManager(serverTimeUponLogin = int(time.time()),
                                                       globalClockRealTimeUponLogin = globalClock.getRealTime())
    def generateManagers(self):
    	self.clientManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CLIENT_MANAGER, 'ClientManager')
        self.centralLogger = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CENTRAL_LOGGER, 'CentralLogger')
        self.partyManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_TOONTOWN_PARTY_MANAGER, 'DistributedPartyManager')
        self.toonsanityFriendsManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_TOONSANITY_FRIENDS_MANAGER, 'ToonsanityFriendsManager')
        self.toonsanityChatManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CHAT_MANAGER, 'ToonsanityChatManager')
