#!/usr/bin/env python
# import platform
# profile = [
# platform.architecture(),
# platform.dist(),
# platform.libc_ver(),
# platform.mac_ver(),
# platform.machine(),
# platform.node(),
# platform.platform(),
# platform.processor(),
# platform.python_build(),
# platform.python_compiler(),
# platform.python_version(),
# platform.system(),
# platform.uname(),
# platform.version(),
# ]
# for item in profile:
# 	print (item)

# import platform
# """
# Fingerprints the following Operating Systems:
# *
# *
# *
# *
# *
# Mac OS X
# Ubuntu
# Red Hat/Cent OS
# FreeBSD
# SunOS
# """
# class OpSysType(object):
# 	"""Determins OS Type using platform module"""
# 	def __getattr__(self, attr):
# 		if attr == "osx":
# 			return "osx"
# 		elif attr == "rhel":
# 			return "redhat"
# 		elif attr == "ubu":
# 			return "ubuntu"
# 		elif attr == "fbsd":
# 			return "FreeBSD"
# 		elif attr == "sun":
# 			return "SunOS"
# 		elif attr == "unknown_linux":
# 			return "unknown_linux"
# 		elif attr == "unknown":
# 			return "unknown"
# 		else:
# 			raise (AttributeError, attr)

# 	def linuxType(self):
# 		"""Uses various methods to determine Linux Type"""
# 		if platform.dist()[0] == self.rhel:
# 			return self.rhel
# 		elif platform.uname()[1] == self.ubu:
# 			return self.ubu
# 		else:
# 			return self.unknown_linux

# 	def queryOS(self):
# 		if platform.system() == "Darwin":
# 			return self.osx
# 		elif platform.system() == "Linux":
# 			return self.linuxType()
# 		elif platform.system() == self.sun:
# 			return self.sun
# 		elif platform.system() == self.fbsd:
# 			return self.fbsd

# def fingerprint():
# 	type = OpSysType()
# 	print (type.queryOS())

# if __name__ == "__main__":
# 	fingerprint()