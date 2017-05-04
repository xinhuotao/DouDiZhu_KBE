# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Hall(KBEngine.Base):
	"""大厅（房间管理器）"""
	def __init__(self):
		super(Hall, self).__init__()

		KBEngine.globalData["Hall"] = self
		self.rooms = {}
		for x in range(1,2):
			self.rooms[x] = KBEngine.createBaseLocally("Room")
			
	def findRoom(self, roomKey):
		if roomKey in self.rooms:
			return self.rooms[roomKey]
		return None

	def reqEnterRoom(self, account, roomKey):
		room = self.findRoom(roomKey)
		if room:
			room.enterRoom(account)