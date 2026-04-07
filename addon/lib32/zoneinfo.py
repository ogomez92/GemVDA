"""Minimal zoneinfo shim for environments where the stdlib module is unavailable."""


class ZoneInfo:
	def __init__(self, key):
		self.key = key


class ZoneInfoNotFoundError(KeyError):
	pass
