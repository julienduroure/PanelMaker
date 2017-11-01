ui_generated_text = '''# This file is auto-generated by addon PanelMaker
# http://BleRiFa.com/en/tools/PanelMaker
# for any questions, please ask contact@julienduroure.com
##########################################################################################
#
# PanelMaker is part of BleRiFa. http://BleRiFa.com
#
##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of PanelMaker.
# PanelMaker is part of http://BleRiFa.com
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
#	Copyright 2016-2017 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################
import bpy

PanelMaker_rig_id = "###rig_id###"



class POSE_PT_JuAR_PanelMaker_###rig_id###(bpy.types.Panel):
	bl_label = "###LABEL###"
	bl_space_type = 'VIEW_3D'
	bl_region_type = '###REGION_TYPE###'
	bl_category = "###CATEGORY###"

	@classmethod
	def poll(self, context):
		return context.active_object and context.active_object.type == "ARMATURE" and context.active_object.data.get("PanelMaker_rig_id") is not None and context.active_object.data.get("PanelMaker_rig_id") == PanelMaker_rig_id and context.mode == 'POSE'


	def draw(self, context):
		layout = self.layout
		armature = context.object

###CONTENT###


def register():
	bpy.utils.register_class(POSE_PT_JuAR_PanelMaker_###rig_id###)

def unregister():
	bpy.utils.unregister_class(POSE_PT_JuAR_PanelMaker_###rig_id###)

register()

'''
