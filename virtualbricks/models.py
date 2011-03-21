#!/usr/bin/python
#coding: utf-8

##	Virtualbricks - a vde/qemu gui written in python and GTK/Glade.
##	Copyright (C) 2011 Virtualbricks team
##
##	This program is free software; you can redistribute it and/or
##	modify it under the terms of the GNU General Public License
##	as published by the Free Software Foundation; either version 2
##	of the License, or (at your option) any later version.
##
##	This program is distributed in the hope that it will be useful,
##	but WITHOUT ANY WARRANTY; without even the implied warranty of
##	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##	GNU General Public License for more details.
##
##	You should have received a copy of the GNU General Public License
##	along with this program; if not, write to the Free Software
##	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import gobject
import gtk

class BricksModel(gtk.ListStore):
	"""we create brick_added and brick_deleted because row-inserted and
	row-deleted don't allow to fetch the item added/deleted. See entry
	13.28 in pygtk FAQ"""
	BRICK_IDX = 0

	__gsignals__ = {
		'brick-added' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
			(gobject.TYPE_STRING,)),
		'brick-deleted' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
			(gobject.TYPE_STRING,)),
	}

	def __init__(self):
		gtk.ListStore.__init__(self, object)

	def add_brick(self, brick):
		"""add brick to the model and send 'brick_added' signal"""
		new_row = self.append(None)
		self.set_value(new_row, self.BRICK_IDX, brick)
		self.emit("brick-added", brick.name)

	def del_brick(self, brick):
		"""remove brick from the model and send 'brick_deleted' signal"""
		for idx, row in enumerate(self):
			if row[self.BRICK_IDX] is brick:
				break
		else:
			return
		del self[idx]
		self.emit("brick-deleted", brick.name)

	def change_brick(self, brick):
		"""update brick which is already in the model, send 'brick_modified' signal"""
		for idx, row in enumerate(self):
			if row[self.BRICK_IDX] is brick:
				break
		else:
			# not found
			return
		modified_row = self.get_iter((idx, 0))
		# row-changed will be emitted
		self.set_value(modified_row, 0, brick)

class EventsModel(gtk.ListStore):
	"""we create event_added and event_deleted because row-inserted and
	row-deleted don't allow to fetch the item added/deleted. See entry
	13.28 in pygtk FAQ"""
	EVENT_IDX = 0

	__gsignals__ = {
		'event-added' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
			(gobject.TYPE_STRING,)),
		'event-deleted' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
			(gobject.TYPE_STRING,)),
	}

	def __init__(self):
		gtk.ListStore.__init__(self, object)

	def add_event(self, event):
		"""add event to the model and send 'event_added' signal"""
		new_row = self.append(None)
		self.set_value(new_row, self.EVENT_IDX, event)
		self.emit("event-added", event.name)

	def del_event(self, event):
		"""remove event from the model and send 'event_deleted' signal"""
		for idx, row in enumerate(self):
			if row[self.EVENT_IDX] is event:
				break
		else:
			return
		del self[idx]
		self.emit("event-deleted", event.name)

	def change_event(self, event):
		"""update event which is already in the model, send 'event_modified' signal"""
		for idx, row in enumerate(self):
			if row[self.EVENT_IDX] is event:
				break
		else:
			# not found
			return
		modified_row = self.get_iter((idx, 0))
		# row-changed will be emitted
		self.set_value(modified_row, 0, event)

gobject.type_register(BricksModel)
gobject.type_register(EventsModel)
