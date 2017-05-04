# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Account(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		print("account ************************** %d" % (self.id))
		print("getAoiRadius ********************* %f" % (self.getAoiRadius()))
		print("position ************************* %f %f %f" % (self.position.x, self.position.y, self.position.z))
		self.debugAOI()
