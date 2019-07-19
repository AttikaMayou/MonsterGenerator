import bpy

#def arm_size(self, context):

#bpy.types.Scene.Scale = bpy.props.FloatProperty(name="Arms min value",
#default=1.0, min = 0.2, update=arm_size)

class MonsterPanel(bpy.types.Panel):
    bl_label = "Monster Generator Panel"
    bl_idname = "OBJECT_Monster"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Monster Generator"
    
    def draw(self, context):
        layout = self.layout
        
        scene = context.scene
        
        row = layout.row()
        row.operator("object.monster_operator")
        props = layout.operator(MonsterGeneratorOperator.bl_idname)
        objet = context.object

        arm_min_value = bpy.props.FloatProperty(name="Arm min value", default=1)
        arm_max_value = bpy.props.FloatProperty(name="Arm max value", default=1)

        leg_min_value = bpy.props.FloatProperty(name="Leg min value", default=1)
        leg_max_value = bpy.props.FloatProperty(name="Leg max value", default=1)

        row = layout.row()
        row.label(text="Properties")
        
        row = layout.row()
        row.prop(scene, "Arms min value")
        props.arm_min_value = objet.arm_min_value

        row = layout.row()
        row.prop(scene, "Arms max value")
        props.arm_max_value = objet.arm_max_value

        row = layout.row()
        row.prop(scene, "Legs min value")
        props.leg_min_value = objet.leg_min_value

        row = layout.row()
        row.prop(scene, "Legs max value")
        props.leg_max_value = objet.leg_max_value

        
def register():
    bpy.utils.register_class(MonsterPanel)
        
def unregister():
    bpy.utils.unregister_class(MonsterPanel)
        
if __name__ == "__main__":
    register()