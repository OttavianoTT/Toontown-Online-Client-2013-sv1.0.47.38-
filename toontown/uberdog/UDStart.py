from panda3d.core import loadPrcFile, loadPrcFileData

class game:
    name = 'uberDog'
    process = 'server'

from direct.showbase import PythonUtil
import __builtin__
__builtin__.game = game
__builtin__.isClient = lambda: PythonUtil.isClient()

from otp.ai.AIBaseGlobal import taskMgr

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help='The control channel of this UberDOGs designated State Server.')
parser.add_argument('--astron-ip', help='The IP address of the Astron Message Director to connect to.')
parser.add_argument('--eventlogger-ip', help='The IP address of the Astron Event Logger to log to.')
parser.add_argument('config', nargs='*', default = ['etc/Configrc.prc'], help='PRC file(s) to load.')
args = parser.parse_args()

for prc in args.config:
    loadPrcFile(prc)

localconfig = ''

if args.base_channel:
    localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels:
    localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver:
    localconfig += 'air-stateserver %s\n' % args.stateserver
if args.astron_ip:
    localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip: 
    localconfig += 'eventlog-host %s\n' % args.eventlogger_ip

loadPrcFileData('Command-line', localconfig)

from toontown.uberdog.UDRepository import UDRepository

simbase.air = UDRepository(config.GetInt('air-base-channel', 400000000), config.GetInt('air-stateserver', 4002))

host = config.GetString('air-connect', '127.4.5.2')
port = 7101

if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)

simbase.air.connect(host, port)

run()