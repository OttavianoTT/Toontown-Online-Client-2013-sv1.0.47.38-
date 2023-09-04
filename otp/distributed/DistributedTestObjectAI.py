from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify.DirectNotifyGlobal import directNotify

class DistributedTestObjectAI(DistributedObjectAI):
    notify = directNotify.newCategory('DistributedTestObjectAI')

    def setParentingRules(self, todo0, todo1):
        pass

    def setRequiredField(self, todo0):
        pass

    def setB(self, todo0):
        pass

    def setBA(self, todo0):
        pass

    def setBO(self, todo0):
        pass

    def setBR(self, todo0):
        pass

    def setBRA(self, todo0):
        pass

    def setBRO(self, todo0):
        pass

    def setBROA(self, todo0):
        pass
