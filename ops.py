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
from .utils import *
from .ui_texts import *
import uuid


class POSE_OT_jupm_generate(bpy.types.Operator):
	"""Generate UI"""
	bl_idname = "pose.jupm_generate"
	bl_label = "Generate"
	bl_options = {'REGISTER'}

	# ops parameters here

	@classmethod
	def poll(self, context):
		return True #TODO

	def execute(self, context):

		armature = context.object

		#Add rig_id custom prop if not exists, and assign a random value
		if context.active_object.data.get('PanelMaker_rig_id') is None:
			bpy.context.active_object.data['PanelMaker_rig_id'] = uuid.uuid4().hex
		rig_id = context.active_object.data.get('PanelMaker_rig_id')

		ui_generated_text_ = ui_generated_text
		ui_generated_text_ = ui_generated_text_.replace("###LABEL###", context.active_object.jupm_generation.panel_name)
		ui_generated_text_ = ui_generated_text_.replace("###CATEGORY###", context.active_object.jupm_generation.tab_tool)
		ui_generated_text_ = ui_generated_text_.replace("###rig_id###", rig_id )

		content = ""
		for line in armature.jupm_lines:
			content = content + "\t\t" + "row = layout.row()" + "\n"
			for column in line.columns:
				if column.type_ == "BONE_LAYER":
					tab = [i[0] for i in enumerate(column.bone_layer) if i[1] ==  True]
					if len(tab) == 0:
						tab.append(31)
					if column.label == "":
						text = "Label"
					else:
						text = column.label
					content = content + "\t\t" + "row.prop(armature.data, 'layers', index=" + str(tab[0]) + ", toggle=True, text='" + text + "')" + "\n"
				elif column.type_ == "SCENE_LAYER":
					tab = [i[0] for i in enumerate(column.scene_layer) if i[1] ==  True]
					if len(tab) == 0:
						tab.append(31)
					if column.label == "":
						text = "Label"
					else:
						text = column.label
					content = content + "\t\t" + "row.prop(bpy.context.scene, 'layers', index=" + str(tab[0]) + ", toggle=True, text='" + text + "')" + "\n"
				elif column.type_ == "BONE_PROP":
					if column.label == "":
						text = "Label"
					else:
						text = column.label
					content = content + "\t\t" + "row.prop(armature.pose.bones['" + column.bone_name + "'], '[\"" + column.bone_property + "\"]', text='" + text + "')" + "\n"
				elif column.type_ == "PROPS":
					pass

		ui_generated_text_ = ui_generated_text_.replace("###CONTENT###", content)


		#Create UI file
		if context.active_object.data["PanelMaker_rig_id"] + "_PanelMaker_ui.py" in bpy.data.texts.keys():
			bpy.data.texts.remove(bpy.data.texts[context.active_object.data["PanelMaker_rig_id"] + "_PanelMaker_ui.py"], do_unlink=True)
		text = bpy.data.texts.new(name=context.active_object.data["PanelMaker_rig_id"] + "_PanelMaker_ui.py")
		text.use_module = True
		text.write(ui_generated_text_)
		exec(text.as_string(), {})

		return {'FINISHED'}

def register():
	bpy.utils.register_class(POSE_OT_jupm_generate)

def unregister():
	bpy.utils.unregister_class(POSE_OT_jupm_generate)
