import bpy

def arm_size(self, context):
    

bpy.types.Scene.Scale = bpy.props.FloatVectorProperty(name="Base Scale",
default=(1.0, 1.0, 1.0), min = 0.2, update=arm_size)

class MonsterPanel(bpy.types.Panel):
    bl_label = "Monster Generator Panel"
    bl_idname = "OBJECT_Monster"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    
    def draw(self, context):
        layout = self.layout
        
        scene = context.scene
        
        row = layout.row()
        row.operator("object.monster_operator")
        props = layout.operator(TreeGeneratorOperator.bl_idname)
        objet = context.object

        row = layout.row()
        row.label(text="Properties")
        
        row = layout.row()
        row.prop(scene, "Arms min value")
        props.arm_min_value = objet.

        
    def register():
        bpy.utils.register_class(MonsterPanel)

        bpy.types.Object.
        
    def unregister():
        bpy.utils.unregister_class(MonsterPanel)
        
    if __name__ == "__main__":
        register()