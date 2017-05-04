# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Room import Room

class Account(KBEngine.Entity, Room):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		Room.__init__(self)

		DEBUG_MSG("Account::__init__:%s." % (self.__dict__))
		self.base.reqEnterRoom(1)

	def onCreateRoom(self, str):
		DEBUG_MSG("xxxxxxxxxxxxxxxxxxxxxxxxxx onCreateRoom" + str)


class PlayerAccount(Account):
	def __init__(self):
		Account.__init__()