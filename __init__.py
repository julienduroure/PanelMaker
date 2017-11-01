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
bl_info = {
	"name": "Panel Maker",
	"version": (0, 0, 1),
	"author": "Julien Duroure",
	"blender": (2, 78, 0),
	"description": "Panle Maker",
	"location": "View 3D",
	"wiki_url": "http://blerifa.com/tools/",
	"tracker_url": "https://github.com/julienduroure/BleRiFa/issues/",
	"category": "UI"
}

if "bpy" in locals():
	import imp
	imp.reload(globs)
	imp.reload(utils)
	imp.reload(addon_pref)
	imp.reload(ops)
	imp.reload(ui_ops)
	imp.reload(ui_list)
	imp.reload(ui_panel)
else:
	from .globs import *
	from .utils import *
	from .addon_pref import *
	from .ops import *
	from .ui_ops import *
	from .ui_list import *
	from .ui_panel import *

import bpy

def register():
	globs.register()
	addon_pref.register()
	ops.register()
	ui_ops.register()
	ui_list.register()
	ui_panel.register()

	bpy.types.Object.jupm_lines = bpy.props.CollectionProperty(type=globs.Jupm_line)
	bpy.types.Object.jupm_line_index = bpy.props.IntProperty()
	bpy.types.Object.jupm_generation = bpy.props.PointerProperty(type=globs.Jupm_Generation)

def unregister():
	# Del Props here

	del bpy.types.Object.jupm_lines
	del bpy.types.Object.jupm_line_index

	globs.unregister()
	addon_pref.unregister()
	ops.unregister()
	ui_panel.unregister()

if __name__ == "__main__":
    register()
