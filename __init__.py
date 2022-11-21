import bpy

from bpy.props import EnumProperty, FloatProperty, FloatVectorProperty, IntProperty, PointerProperty

bl_info = {
    "name": "Setup Retopology",
    "description": "Do several steps to setup a retopology session",
    "author": "Johnny Matthews",
    "version": (1, 4),
    "blender": (3, 3, 1),
    "support": "COMMUNITY",
    "category": "Object"
}

    
class JohnnyGizmoSetupRetopo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.johnnygizmo_setup_retopo"
    bl_label = "Setup Retopology"
    bl_options = {'REGISTER', 'UNDO'}

    pos: bpy.props.FloatVectorProperty(name="Offset", default=(0.0,-2.0,0.0))
            
    scale: bpy.props.FloatProperty(name="Plane Size", default=0.1, min=.001, max=1.0, precision=2,step=1)
    
    
    color: bpy.props.FloatVectorProperty(name="Color", description="Object Color", default=(0.0945094, 0.283429, 0.240477,1), options={'ANIMATABLE'}, size=4, subtype='COLOR')
   
    add_mirror: bpy.props.BoolProperty(name="Add Mirror", description="Enable Mirror Modifier", default=True)
    add_shrink: bpy.props.BoolProperty(name="Add Shrinwrap", description="Enable Shrinkwrap Modifier", default=True)
    automerge: bpy.props.BoolProperty(name="Enable Automerge", description="Enable Automerge Option", default=False)
    merge: bpy.props.FloatProperty(name="Automerge Dist", default=0.001, min=0.0, max=0.1,precision=3, step=.1)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        target = None
        
        if len(context.selected_objects) ==  1 and context.active_object.type == 'MESH':
            target = context.active_object
            bpy.ops.mesh.primitive_plane_add(size=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))
            target.select_set(True)
            
        else:
            self.report({'INFO'}, "Please select Mesh Object for Retopo")    
            return {'CANCELLED'}
        

        
        #Move Plane
        active = context.active_object
       
        for ob in context.selected_objects:
            if ob != active:
                target = ob
        
        target.select_set(False)
        
        bpy.ops.transform.resize(value=(self.scale, self.scale, self.scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)    
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        if self.add_mirror == True:
            bpy.ops.transform.translate(value=(0.5*self.scale, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        bpy.ops.transform.translate(value=self.pos, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        #bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.transform.translate(value=target.location, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        

        #modifiers      
        if self.add_mirror == True:                
            bpy.ops.object.modifier_add(type='MIRROR')
            bpy.context.object.modifiers[-1].use_clip = True
            bpy.context.object.modifiers[-1].show_on_cage = True      
            bpy.context.object.modifiers[-1].show_in_editmode = True
        
      
        if self.add_shrink == True:
            bpy.ops.object.modifier_add(type='SHRINKWRAP')
            bpy.context.object.modifiers[-1].target = target
            bpy.context.object.modifiers[-1].show_on_cage = True
            bpy.context.object.modifiers[-1].show_in_editmode = True
            bpy.context.object.modifiers[-1].wrap_method = 'TARGET_PROJECT'


        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers[-1].show_on_cage = False
        bpy.context.object.modifiers[-1].show_in_editmode = False     
    
        
        #Object Settings
        bpy.context.object.show_in_front = True
        bpy.context.object.color = self.color
        
        #Snapping
        bpy.context.scene.tool_settings.snap_elements = {'FACE'}
        bpy.context.scene.tool_settings.use_snap_project = True
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.use_snap_backface_culling = True

        #automerge
        bpy.context.scene.tool_settings.use_mesh_automerge = self.automerge
        bpy.context.scene.tool_settings.double_threshold = self.merge
              
    
        #Shading
        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.show_backface_culling = True
        bpy.context.space_data.overlay.show_occlude_wire = True
        bpy.context.space_data.overlay.show_fade_inactive = True
        bpy.context.space_data.overlay.fade_inactive_alpha = 0.3        

        
        bpy.ops.object.editmode_toggle()
        
        #Wiggle the Mesh to get initial snapping
        bpy.ops.transform.translate(value=(0,0,0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=True, snap_elements={'FACE'}, use_snap_project=True, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(JohnnyGizmoSetupRetopo)


def unregister():
    bpy.utils.unregister_class(JohnnyGizmoSetupRetopo)

if __name__ == "__main__":
    register()
