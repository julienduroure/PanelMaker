##########################################################################################
#    GPL LICENSE:
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
#    Copyright 2016 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################
import bpy

from .globs import *
from .utils import *
from .ui_list import *

class POSE_PT_jupm_line(bpy.types.Panel):
    bl_label = "Lines"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "PanelMaker"

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def draw(self, context):
        layout = self.layout
        armature = context.object

        row = layout.row()
        row.template_list("POSE_UL_jupm_lines", "", armature, "jupm_lines", armature, "jupm_line_index")

        col = row.column()
        row = col.column(align=True)
        row.operator("pose.jupm_line_add", icon="ZOOMIN", text="")
        row.operator("pose.jupm_line_remove", icon="ZOOMOUT", text="")
        row = col.column(align=True)
        row.separator()
        row.operator("pose.jupm_line_move", icon='TRIA_UP', text="").direction = 'UP'
        row.operator("pose.jupm_line_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
        if len(armature.jupm_lines) == 0:
            row.enabled = False

class POSE_PT_jupm_column(bpy.types.Panel):
    bl_label = "Columns"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "PanelMaker"

    @classmethod
    def poll(self, context):
        armature = context.object
        return (context.object and context.object.type == 'ARMATURE' and context.mode == 'POSE') and len(armature.jupm_lines) > 0

    def draw(self, context):
        layout = self.layout
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]

        row = layout.row()
        row.template_list("POSE_UL_jupm_columns", "", line, "columns", line, "column_index")

        col = row.column()
        row = col.column(align=True)
        row.operator("pose.jupm_column_add", icon="ZOOMIN", text="")
        row.operator("pose.jupm_column_remove", icon="ZOOMOUT", text="")
        row = col.column(align=True)
        row.separator()
        row.operator("pose.jupm_column_move", icon='TRIA_UP', text="").direction = 'UP'
        row.operator("pose.jupm_column_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
        if len(line.columns) == 0:
            row.enabled = False

class POSE_PT_jupm_item(bpy.types.Panel):
    bl_label = "Item"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "PanelMaker"

    @classmethod
    def poll(self, context):
        armature = context.object
        return (context.object and context.object.type == 'ARMATURE' and context.mode == 'POSE') and len(armature.jupm_lines) > 0 and len(armature.jupm_lines[armature.jupm_line_index].columns) > 0

    def draw(self, context):
        layout = self.layout
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]
        column = line.columns[line.column_index]

        row = layout.row()
        row.prop(column, "type_",text="")

        if column.type_ == 'BONE_LAYER':
            row = layout.row()
            row.prop(column, "label")
            row = layout.row()
            col = row.column(align=True)
            row_ = col.row()
            row_.prop(column, "bone_layer")
            col = row.column()
            row_ = col.row()
            op = row_.operator("pose.jupm_select_bone_layer", icon="BONE_DATA", text="")
            op.layer = "bone_layer"
        elif column.type_ == "BONE_PROP":
            row = layout.row()
            row.prop(column, "label")
            row = layout.row()
            col = row.column(align=True)
            row_ = col.row()
            row_.prop_search(column, "bone_name", armature.data, "bones", text="Bone")
            col = row.column()
            row_ = col.row()
            op = row_.operator("pose.jupm_select_bone", icon="BONE_DATA", text="")
            op.bone = "bone_property"
            row = layout.row()
            row.prop(column, "bone_property")

class POSE_PT_jupm_result(bpy.types.Panel):
    bl_label = "Result"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "PanelMaker"

    @classmethod
    def poll(self, context):
        armature = context.object
        return (context.object and context.object.type == 'ARMATURE' and context.mode == 'POSE')

    def draw(self, context):
        armature = context.object
        layout = self.layout
        for line in armature.jupm_lines:
            row = layout.row()
            for column in line.columns:
                if column.type_ == "BONE_LAYER":
                    tab = [i[0] for i in enumerate(column.bone_layer) if i[1] ==  True]
                    if len(tab) == 0:
                        tab.append(31)
                    if column.label == "":
                        text = "Label"
                    else:
                        text = column.label
                    row.prop(armature.data, 'layers', index=tab[0], toggle=True, text=text)

                elif column.type_ == "BONE_PROP":
                    if column.label == "":
                        text = "Label"
                    else:
                        text = column.label
                    if column.bone_name and column.bone_name in armature.pose.bones:
                        if column.bone_property in [it[0] for it in armature.pose.bones[column.bone_name].items()]:
                            row.prop(armature.pose.bones[column.bone_name], '[\"' + column.bone_property + '\"]', text=text)
                        else:
                            row.label("Error Property")
                    else:
                        row.label("Error Bone")


def unregister_class_panels():
    bpy.utils.unregister_class(POSE_PT_jupm_line)
    bpy.utils.unregister_class(POSE_PT_jupm_column)
    bpy.utils.unregister_class(POSE_PT_jupm_item)
    bpy.utils.unregister_class(POSE_PT_jupm_result)

def change_panel_tab():
    POSE_PT_jupm_line.bl_category = addonpref().category
    POSE_PT_jupm_column.bl_category = addonpref().category
    POSE_PT_jupm_item.bl_category = addonpref().category

def register_panels():
    bpy.utils.register_class(POSE_PT_jupm_line)
    bpy.utils.register_class(POSE_PT_jupm_column)
    bpy.utils.register_class(POSE_PT_jupm_item)
    bpy.utils.register_class(POSE_PT_jupm_result)

def register():

    change_panel_tab()
    register_panels()

def unregister():
    unregister_class_panels()
