import KBEngine
from KBEDebug import *

class Room(KBEngine.Base):
	"""Room 房间实体"""
	def __init__(self):
		super(Room, self).__init__()
		self.createInNewSpace(None)
		self.players = {}

	def enterRoom(self, account):
		print("base enterRoom: %d" % (account.id))
		account.createCell(self.cell)
		self.players[account.id] = account
		self.cell.onEnter(account)