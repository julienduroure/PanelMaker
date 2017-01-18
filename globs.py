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
from .utils import *

jupm_items_column_type = [
	("BONE_LAYER", "Bone Layer", "", 1),
	("BONE_PROP", "Bone Property", "", 2),
	]

class Jupm_column(bpy.types.PropertyGroup):
	name  = bpy.props.StringProperty()
	type_ = bpy.props.EnumProperty(items=jupm_items_column_type)

	### Common
	label = bpy.props.StringProperty()

	### Bone Layer
	bone_layer = bpy.props.BoolVectorProperty(name="Bone Layer", subtype='LAYER', size = 32)

	### Bone Property
	bone_name     = bpy.props.StringProperty()
	bone_property = bpy.props.StringProperty()


class Jupm_line(bpy.types.PropertyGroup):
	name    = bpy.props.StringProperty()
	columns = bpy.props.CollectionProperty(type=Jupm_column)
	column_index = bpy.props.IntProperty()

def register():
	bpy.utils.register_class(Jupm_column)
	bpy.utils.register_class(Jupm_line)


def unregister():
	bpy.utils.unregister_class(Jupm_line)
	bpy.utils.unregister_class(Jupm_column)
