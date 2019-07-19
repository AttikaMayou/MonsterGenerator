import bpy

class TreeGeneratorPanel(bpy.types.Panel):
    bl_label = "Tree Generator Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Monster Generator"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="This is a panel to create trees easily")
        row = layout.row()
        row.operator("mesh.primitive_plane_add")
        row = layout.row()
        row.operator("object.tree_generator")
        row = layout.row()
        row.operator("object.l_system_operator")
        row = layout.row()
        row.operator("object.monster_generator")

def register():
    bpy.utils.register_class(TreeGeneratorPanel)


def unregister():
    bpy.utils.unregister_class(TreeGeneratorPanel)


if __name__ == "__main__":
    register()