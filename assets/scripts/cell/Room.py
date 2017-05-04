import KBEngine
from KBEDebug import *
from CardLogic import CardLogic

class Room(KBEngine.Entity):
	"""Room cell 实体"""
	def __init__(self):
		super(Room, self).__init__()
		print("Room cell entity created !!!")
		self.m_cardLogic = None
		self.players = {}
		self.playerData = {}
		self.seatIndex = 1
		self.readyNum = 0
		self.MAX_PLAYER = 3

	def onEnter(self, account):
		# 人数已满
		if len(self.players) >= self.MAX_PLAYER :
			return

		playerEntity = KBEngine.entities[account.id]
		self.players[playerEntity.id] = playerEntity

		if playerEntity.id not in self.playerData :
			data = {}
			data["ready"] = 0
			data["seatNum"] = self.seatIndex
			self.playerData[account.id] = data
			self.seatIndex += 1

		print("cell onEnter room: %d" % (playerEntity.id))
		print(playerEntity)
		print("getAoiRadius ********************* %f" % (playerEntity.getAoiRadius()))
		print("position ************************* %f %f %f" % (playerEntity.position.x, playerEntity.position.y, playerEntity.position.z))
		playerEntity.debugAOI()
		playerEntity.allClients.onEnterRoom("account id: " + str(account.id))

	def onReady(self, account):
		if account.id in self.playerData :
			data = self.playerData[account.id]
			if data["ready"] == 1 :
				return
			data["ready"] = 1
			self.readyNum += 1
			# TODO: 广播给客户端

			if self.readyNum >= self.MAX_PLAYER :
				GameBegin()

	def GameBegin():
		# TODO: 洗牌，发牌
		self.m_cardLogic = CardLogic()
		self.m_cardLogic.shuffle()
		