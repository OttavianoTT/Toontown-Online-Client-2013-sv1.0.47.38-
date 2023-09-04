from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify

class DistributedCpuInfoMgrUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('DistributedCpuInfoMgrUD')

    def setCpuInfoToUd(self, todo0, todo1, todo2, todo3):
        pass
