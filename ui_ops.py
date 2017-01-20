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



class POSE_OT_jupm_line_move(bpy.types.Operator):
    """Move line up or down in the list"""
    bl_idname = "pose.jupm_line_move"
    bl_label = "Move Line"
    bl_options = {'REGISTER'}

    direction = bpy.props.StringProperty()

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object
        index    = armature.jupm_line_index

        if self.direction == "UP":
            new_index = index - 1
        elif self.direction == "DOWN":
            new_index = index + 1
        else:
            new_index = index

        if new_index < len(armature.jupm_lines) and new_index >= 0:
            armature.jupm_lines.move(index, new_index)
            armature.jupm_line_index = new_index

        return {'FINISHED'}

class POSE_OT_jupm_line_add(bpy.types.Operator):
    """Add a new line"""
    bl_idname = "pose.jupm_line_add"
    bl_label = "Add Line"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object

        line = armature.jupm_lines.add()
        line.name = "Line.%d" % len(armature.jupm_lines)
        armature.jupm_line_index = len(armature.jupm_lines) - 1

        return {'FINISHED'}

class POSE_OT_jupm_line_remove(bpy.types.Operator):
    """Remove Line"""
    bl_idname = "pose.jupm_line_remove"
    bl_label = "Remove Line"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object

        armature.jupm_lines.remove(armature.jupm_line_index)
        len_ = len(armature.jupm_lines)
        if (armature.jupm_line_index > (len_ - 1) and len_ > 0):
            armature.jupm_line_index = len(armature.jupm_lines) - 1

        return {'FINISHED'}



class POSE_OT_jupm_column_move(bpy.types.Operator):
    """Move column up or down in the list"""
    bl_idname = "pose.jupm_column_move"
    bl_label = "Move Column"
    bl_options = {'REGISTER'}

    direction = bpy.props.StringProperty()

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object
        line    = armature.jupm_lines[armature.jupm_line_index]
        index    = line.column_index

        if self.direction == "UP":
            new_index = index - 1
        elif self.direction == "DOWN":
            new_index = index + 1
        else:
            new_index = index

        if new_index < len(line.columns) and new_index >= 0:
            line.columns.move(index, new_index)
            line.column_index = new_index

        return {'FINISHED'}

class POSE_OT_jupm_column_add(bpy.types.Operator):
    """Add a new column"""
    bl_idname = "pose.jupm_column_add"
    bl_label = "Add Column"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]

        column = line.columns.add()
        column.name = "Column.%d" % len(line.columns)
        line.column_index = len(line.columns) - 1

        return {'FINISHED'}

class POSE_OT_jupm_column_remove(bpy.types.Operator):
    """Remove Column"""
    bl_idname = "pose.jupm_column_remove"
    bl_label = "Remove Column"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

    def execute(self, context):
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]

        line.columns.remove(line.column_index)
        len_ = len(line.columns)
        if (line.column_index > (len_ - 1) and len_ > 0):
            line.column_index = len(line.columns) - 1

        return {'FINISHED'}


class POSE_OT_jupm_select_bone(bpy.types.Operator):
    """Select bones"""
    bl_idname = "pose.jupm_select_bone"
    bl_label = "Select bone"
    bl_options = {'REGISTER'}

    bone = bpy.props.StringProperty()

    @classmethod
    def poll(self, context):
        armature = context.object
        return context.active_object and context.active_object.type == "ARMATURE" and len(armature.jupm_lines) > 0 and len(armature.jupm_lines[armature.jupm_line_index].columns) > 0

    def execute(self, context):
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]
        item = line.columns[line.column_index]
        if context.active_pose_bone:
            bone_name = context.active_pose_bone.name

        if self.bone == "bone_property":
            item.bone_name = bone_name


        return {'FINISHED'}

class POSE_OT_jupm_select_bone_layer(bpy.types.Operator):
    """Select bone layer"""
    bl_idname = "pose.jupm_select_bone_layer"
    bl_label = "Select bone layer"
    bl_options = {'REGISTER'}

    layer = bpy.props.StringProperty()

    @classmethod
    def poll(self, context):
        armature = context.object
        return context.active_object and context.active_object.type == "ARMATURE" and len(armature.jupm_lines) > 0 and len(armature.jupm_lines[armature.jupm_line_index].columns) > 0

    def execute(self, context):
        armature = context.object
        line = armature.jupm_lines[armature.jupm_line_index]
        item = line.columns[line.column_index]
        if context.active_pose_bone:
            bone_name = context.active_pose_bone.name
            layers = armature.data.bones[bone_name].layers

        if self.layer == "bone_layer":
            item.bone_layer = layers

        return {'FINISHED'}


def register():
    bpy.utils.register_class(POSE_OT_jupm_line_move)
    bpy.utils.register_class(POSE_OT_jupm_line_add)
    bpy.utils.register_class(POSE_OT_jupm_line_remove)
    bpy.utils.register_class(POSE_OT_jupm_column_move)
    bpy.utils.register_class(POSE_OT_jupm_column_add)
    bpy.utils.register_class(POSE_OT_jupm_column_remove)
    bpy.utils.register_class(POSE_OT_jupm_select_bone)
    bpy.utils.register_class(POSE_OT_jupm_select_bone_layer)

def unregister():
    bpy.utils.unregister_class(POSE_OT_jupm_line_move)
    bpy.utils.unregister_class(POSE_OT_jupm_line_add)
    bpy.utils.unregister_class(POSE_OT_jupm_line_remove)
    bpy.utils.unregister_class(POSE_OT_jupm_column_move)
    bpy.utils.unregister_class(POSE_OT_jupm_column_add)
    bpy.utils.unregister_class(POSE_OT_jupm_column_remove)
    bpy.utils.unregister_class(POSE_OT_jupm_select_bone)
    bpy.utils.unregister_class(POSE_OT_jupm_select_bone_layer)
