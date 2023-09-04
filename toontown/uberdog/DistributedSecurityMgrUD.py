from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify

class DistributedSecurityMgrUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('DistributedSecurityMgrUD')

    def requestAccountId(self, todo0, todo1, todo2):
        pass

    def requestAccountIdResponse(self, todo0, todo1):
        pass
