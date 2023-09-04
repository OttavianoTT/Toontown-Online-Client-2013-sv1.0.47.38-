from panda3d.core import loadPrcFile, Loader, NodePath, VBase3, TextNode, loadPrcFileData
from panda3d.direct import CConnectionRepository

from direct.gui import DirectGuiGlobals
from direct.showbase import PythonUtil, DConfig

from libotp.settings.Settings import Settings

from libotp import ChatBalloon, NametagGlobals, MarginManager, NametagGroup, WhisperPopup, Nametag, NametagFloat2d, NametagFloat3d
from libotp.nametag import _constants

from panda3d.toontown import loadDNAFile, DNAStorage, DNADoor, loadDNAFileAI, DNASuitPoint, DNAInteractiveProp, SuitLegList, SuitLeg

import __builtin__, os, sys

# These are functions that the client is missing in newer Panda3D builds.
def listProcessModules():
    # TODO
    pass

def prepareAvatar(*args):
    # TODO
    pass

# Set required buitlins for the client.
__builtin__.listProcessModules = listProcessModules
__builtin__.Settings = Settings()
__builtin__.NO_FADE_SORT_INDEX = DirectGuiGlobals.NO_FADE_SORT_INDEX
__builtin__.isClient = lambda: PythonUtil.isClient()
__builtin__.prepareAvatar = prepareAvatar
__builtin__.ChatBalloon = ChatBalloon
__builtin__.NametagGlobals = NametagGlobals
__builtin__.MarginManager = MarginManager
__builtin__.PandaLoader = Loader
__builtin__.loadDNAFile = loadDNAFile
__builtin__.NametagGroup = NametagGroup
__builtin__.CFSpeech = _constants.CFSpeech
__builtin__.CFTimeout = _constants.CFTimeout
__builtin__.WhisperPopup = WhisperPopup
__builtin__.DNAStorage = DNAStorage
__builtin__.Nametag = Nametag
__builtin__.CFThought = _constants.CFThought
__builtin__.DNADoor = DNADoor
__builtin__.NametagFloat2d = NametagFloat2d
__builtin__.triglerp = PythonUtil.triglerp
__builtin__.loadDNAFileAI = loadDNAFileAI
__builtin__.DNASuitPoint = DNASuitPoint
__builtin__.SuitLegList = SuitLegList
__builtin__.SuitLeg = SuitLeg
__builtin__.VBase3 = VBase3
__builtin__.DNAInteractiveProp = DNAInteractiveProp
__builtin__.CFReversed = _constants.CFReversed
__builtin__.TextNode = TextNode
__builtin__.FADE_SORT_INDEX = DirectGuiGlobals.FADE_SORT_INDEX
__builtin__.CConnectionRepository = CConnectionRepository
__builtin__.NametagFloat3d = NametagFloat3d
__builtin__.CFQuicktalker = _constants.CFQuicktalker
__builtin__.WTSystem = WhisperPopup.WTSystem

# Load our configuration file.
loadPrcFile('etc/Configrc.prc')

for dtool in ('children', 'parent', 'name'):
    del NodePath.DtoolClassDict[dtool]

# Get and set our playToken.
playToken = raw_input('Playtoken: ')

if not playToken:
    playToken = 'playToken'

os.environ['PLAY_TOKEN'] = playToken

# Clear the Command Prompt console.
linux = ['linux', 'linux2']

if sys.platform in linux:
    os.system('clear')
else:
    os.system('cls')

# Switch the Audio library if on Linux.
if DConfig.GetString('audio-library-name', 'p3fmod_audio') and sys.platform in linux:
    loadPrcFileData('', 'audio-library-name p3openal_audio')

# Start the client.
from toontown.toonbase import ToontownStart
