##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of PanelMaker.
#
#    PanelMaker is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PanelMaker is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PanelMaker.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################################
#
#	Copyright 2016 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################
import bpy
from .globs import *

class jutp_AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __package__


	category = bpy.props.StringProperty(name="Category", default="PanelMaker", update=update_panel_cb)

	def draw(self, context):
		pass


def register():
	bpy.utils.register_class(jutp_AddonPreferences)

def unregister():
	bpy.utils.unregister_class(jutp_AddonPreferences)
