from p2pool.bitcoin import networks

PARENT=networks.nets['auroracoin']
SHARE_PERIOD=61
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=24*60*60//10
TARGET_LOOKBEHIND=50
SPREAD=30
IDENTIFIER='91ff1dc82446000f'.decode('hex')
PREFIX='91ff1dc824460010'.decode('hex')
P2P_PORT=12352
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=12351
BOOTSTRAP_ADDRS='crypto.office-on-the.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt'
VERSION_CHECK=lambda v: True
VERSION_WARNING=lambda v: 'Upgrade AuroraCoin to >=2016.04.01.0!' if v < 3000000 else None
