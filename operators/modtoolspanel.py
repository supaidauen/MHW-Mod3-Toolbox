# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:32:19 2020

@author: AsteriskAmpersand
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:04:20 2019

@author: AsteriskAmpersand
"""
import bpy

class ModTools(bpy.types.Panel):
    bl_category = "MHW Physics"
    bl_idname = "panel.mhw_mod"
    bl_label = "MOD3 Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Tools"

    addon_key = __package__.split('.')[0]

    def draw(self, context):
        addon = context.user_preferences.addons[self.addon_key]
        self.addon_props = addon.preferences
        
        layout = self.layout
        #self.layout.label("CCL Capsule Tools")
        #self.layout.operator("ctc_tools.mesh_from_capsule", icon='MESH_CUBE', text="Mesh from Capsule")
        self.draw_mod_tools(context, layout)
        layout.separator()

        
    def draw_mod_tools(self, context, layout):
        #addon_props = self.addon_props
        col = layout.column(align = True)
        col.label("Custom Properties")
        row = col.row(align = True)
        row.operator("mod_tools.copy_prop", icon='MESH_DATA', text="Copy")
        row.operator("mod_tools.paste_prop", icon='MESH_DATA', text="Paste")
        #col.separator()

        col.label("Rename Vertex Groups")
        row = col.row(align = True)
        row.operator("mod_tools.target_armature", icon='ARMATURE_DATA', text="To Armature")
        row.operator("mod_tools.target_weights", icon='EMPTY_DATA', text="To Empty")
        col.separator()
        
        col.operator("mod_tools.bone_to_id", icon='CONSTRAINT_BONE', text="Rename Bones to ID")
        
        #col.prop(addon_props, 'limit_application', text = 'Limit to Selection')
        col.operator("mod_tools.mark_uv_rep", icon='EDGESEL', text="Mark Repeated UVs")
        col.operator("mod_tools.solve_uv_rep", icon='SNAP_EDGE', text="Solve Repeated UVs")
        col.operator("mod_tools.solve_sharp_rep", icon='SNAP_EDGE', text="Split Sharp and Repeated UVs")
        col.operator("mod_tools.clean_color", icon='COLOR', text="Clean Vertex Colors")
        col.operator("mod_tools.clean_weights", icon='GROUP_VERTEX', text="Remove Unweighted Groups")
        col.operator("mod_tools.limit_normalize", icon='GROUP_VERTEX', text="Limit Weights to Label")
        col.operator("mod_tools.mass_weight", icon='GROUP_VERTEX', text="Mass Weight to Bone")
        col.operator("mod_tools.nuke_weights", icon='GROUP_VERTEX', text="Delete Weights")
        col.operator("mod_tools.mass_triangulate", icon='GROUP_VERTEX', text="Triangulate")
        
        