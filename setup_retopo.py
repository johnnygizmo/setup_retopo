import bpy
bl_info = {
    "name": "Setup Retopo From New Plane",
    "description": "Do several steps to setup retopology",
    "author": "Johnny Matthews",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "support": "COMMUNITY",
    "category": "Object"
}


class JohnnyGizmoSetupRetopo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.johnnygizmo_setup_retopo"
    bl_label = "Setup Retopo From New Plane"
    bl_options = {'REGISTER', 'UNDO'}

    ypos: bpy.props.FloatProperty(name="Y Position", default=-5.0, min=-100.0, max=100.0)
    merge: bpy.props.FloatProperty(name="Automerge Dist", default=0.001, min=0.0, max=0.1,precision=3, step=.1)
    color: bpy.props.FloatVectorProperty(name="Color", description="Object Color", default=(0.0945094, 0.283429, 0.240477,1), options={'ANIMATABLE'}, size=4, subtype='COLOR')
   
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #Move Plane
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(0, self.ypos, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.modifier_add(type='MIRROR')
        
        #Object Settings
        bpy.context.object.modifiers["Mirror"].use_clip = True
        bpy.context.object.show_in_front = True
        bpy.context.object.color = self.color
        
        #Snapping
        bpy.context.scene.tool_settings.snap_elements = {'FACE'}
        bpy.context.scene.tool_settings.use_snap_project = True
        bpy.context.scene.tool_settings.use_snap = True
    
        #Automerge
        bpy.context.scene.tool_settings.use_mesh_automerge = True
        bpy.context.scene.tool_settings.double_threshold = self.merge

    
        #Shading
        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.show_backface_culling = True
        return {'FINISHED'}


def register():
    bpy.utils.register_class(JohnnyGizmoSetupRetopo)


def unregister():
    bpy.utils.unregister_class(JohnnyGizmoSetupRetopo)

if __name__ == "__main__":
    register()
