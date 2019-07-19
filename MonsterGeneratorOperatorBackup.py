import bpy
import random

def select_vertice(id):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    obj = bpy.context.active_object
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    obj.data.vertices[id].select = True
    bpy.ops.object.mode_set(mode = 'EDIT')

def extrude_vertice_to(x, y, z):
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value": (x, y, z)})
    
def resize_vertice(value):
    bpy.ops.transform.skin_resize(value = (value, value, value))
    
def select_bone(id):
    bpy.data.objects["Armature"].data.bones.active = bpy.data.objects["Armature"].pose.bones[id].bone
    
def define_bone_Inverse_Kinematics(id):
    select_bone(id)
    bpy.ops.pose.constraint_add(type='IK')
    bpy.context.object.pose.bones[id].constraints["IK"].chain_count = 3
    
def select_all_bones():
    bpy.ops.pose.select_all(action='TOGGLE')
    
def add_keyframe():
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    
def select_all_bones_and_add_keyframe():
    select_all_bones()
    select_all_bones()
    add_keyframe()
    select_all_bones()
    
def animate_monster():
    # animation
    
    # selection de la premiere frame de la timeline
    bpy.context.scene.frame_set(1)
    
    # selection de tout les bones et ajout d'une keyframe
    select_all_bones_and_add_keyframe()
    # selection de la frame suivante dans la timeline
    bpy.context.scene.frame_set(20)
    
    # reculer jambe gauche
    select_bone("Bone.05")
    #bpy.ops.transform.translate(value = (0,1,0))
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))

    select_all_bones()
    select_bone("Bone.12")
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    #avancer bras droit
    select_all_bones()
    select_bone("Bone.01")
    bpy.ops.transform.rotate(value = -1, axis = (0, 0, 1))
    
    #reculer bras gauche
    select_all_bones()
    select_bone("Bone.10")
    bpy.ops.transform.rotate(value = -1, axis = (0, 0, 1))
    
    # bouger la tete
    select_all_bones()
    select_bone("Bone.08")
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))
    
    # selection de tout les bones et ajout d'une keyframe
    select_all_bones_and_add_keyframe()
    
    bpy.context.scene.frame_set(40)
    
    # remise en place
    select_bone("Bone.05")
    #bpy.ops.transform.translate(value = (0,1,0))
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    select_all_bones()
    select_bone("Bone.12")
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))
    
    #remise en place bras droit
    select_all_bones()
    select_bone("Bone.01")
    bpy.ops.transform.rotate(value = 1, axis = (0, 0, 1))
    
    #remise en place bras gauche
    select_all_bones()
    select_bone("Bone.10")
    bpy.ops.transform.rotate(value = 1, axis = (0, 0, 1))
    
    # bouger la tete
    select_all_bones()
    select_bone("Bone.08")
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    select_all_bones_and_add_keyframe()
    
    bpy.context.scene.frame_set(60)
    
    # avancer jambe droite
    select_bone("Bone.05")
    #bpy.ops.transform.translate(value = (0,1,0))
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    select_all_bones()
    select_bone("Bone.12")
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))
    
    #reculer bras droit
    select_all_bones()
    select_bone("Bone.01")
    bpy.ops.transform.rotate(value = 1, axis = (0, 0, 1))
    
    #avancer bras gauche
    select_all_bones()
    select_bone("Bone.10")
    bpy.ops.transform.rotate(value = 1, axis = (0, 0, 1))
    
    # bouger la tete
    select_all_bones()
    select_bone("Bone.08")
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    select_all_bones_and_add_keyframe()
    
    bpy.context.scene.frame_set(80)
    
    # remise en place
    select_bone("Bone.05")
    #bpy.ops.transform.translate(value = (0,1,0))
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))
    
    select_all_bones()
    select_bone("Bone.12")
    bpy.ops.transform.rotate(value = -1, axis = (1, 0, 0))
    
    #remise en place bras droit
    select_all_bones()
    select_bone("Bone.01")
    bpy.ops.transform.rotate(value = -1, axis = (0, 0, 1))
    
    #remise en place bras gauche
    select_all_bones()
    select_bone("Bone.10")
    bpy.ops.transform.rotate(value = -1, axis = (0, 0, 1))
    
    # bouger la tete
    select_all_bones()
    select_bone("Bone.08")
    bpy.ops.transform.rotate(value = 1, axis = (1, 0, 0))
    
    select_all_bones_and_add_keyframe()
    
def import_BVH():
    bpy.ops.import_anim.bvh(filepath="C:\\Users\\antoi\\Desktop\\Monster_Generator\\cmuconvert-max-01-09\\02\\02_01.bvh")
    bpy.context.object.data.pose_position = 'REST'
    bpy.data.objects['02_01'].select = True
    bpy.data.objects['Armature'].select = False
    #bpy.data.objects['Armature'].select = True
    #bpy.data.objects['02_01'].select = True
    #bpy.data.objects['02_01'].select = False
    #bpy.data.objects['02_01'].select = True
    #bpy.ops.mocap.scale_fix()
    #bpy.data.objects['Monstre'].select = True
    #bpy.context.object.data.pose_position = 'POSE'

def create_random_monster():
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.merge(type='CENTER')
    bpy.ops.object.modifier_add(type='MIRROR')
    bpy.ops.object.modifier_add(type='SKIN')
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 3
    
    extrude_vertice_to(0, 0, random.uniform(1, 2))
    extrude_vertice_to(0, 0, random.uniform(1, 2))
    
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0, 0.5))
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.2, 0.7))
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.5, 1))
    select_vertice(0)
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.5, 1))
    extrude_vertice_to(random.uniform(0.2, 1), 0, -random.uniform(0.8, 1.5))
    extrude_vertice_to(random.uniform(0.2, 1), 0, -random.uniform(0.8, 1.5))
    select_vertice(4)   
    extrude_vertice_to(0, 0, random.uniform(1, 5))
    
    select_vertice(0)
    bpy.ops.object.skin_root_mark()
    # scale point
    for vertices in range(0, 10):
        print(vertices)
        select_vertice(vertices)
        resize_vertice(random.uniform(1, 5))
    #select_vertice(0)
    #resize_vertice(random.randrange(1, 3))
    
    bpy.ops.object.editmode_toggle()
    
    #on applique le miroir avant de créer l'armature     
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
    #on créé l'armature
    bpy.ops.object.skin_armature_create(modifier="Skin")
    
    
    #on lie l'armature au monstre
    bpy.data.objects['Armature'].select = True
    bpy.data.objects['Cube'].select = True
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
    
    #on passe en Pose mode
    bpy.ops.object.posemode_toggle()
    # met les IK sur les bones (voir fonction plus haut)
    define_bone_Inverse_Kinematics(15)
    define_bone_Inverse_Kinematics(9)
    define_bone_Inverse_Kinematics(5)
    define_bone_Inverse_Kinematics(12)
    
    #animate_monster()
    import_BVH()
    
    # renomme 
    for obj in bpy.context.selected_objects:
        obj.name = "Monstre"
        obj.data.name = "Monstre"
    
    #on applique le miroir avant de créer l'armature     
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='SKIN')
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='SUBSURF')
    
    bpy.ops.object.mode_set(mode = 'OBJECT')

def create_random_army(L, P):
    for x in range(L):
        for y in range(P):
            bpy.context.scene.cursor_location = (float(x * 10), float(y * 10), 0.0)
            create_random_monster()

def create_random_monster_2():
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.merge(type='CENTER')
    bpy.ops.object.modifier_add(type='MIRROR')
    bpy.ops.object.modifier_add(type='SKIN')
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 3
    
    extrude_vertice_to(0, 0, random.uniform(1, 2))
    extrude_vertice_to(0, 0, random.uniform(1, 2))
    
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0, 0.5))
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.2, 0.7))
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.5, 1))
    select_vertice(0)
    extrude_vertice_to(random.uniform(1, 1.5), 0, -random.uniform(0.5, 1))
    extrude_vertice_to(random.uniform(0.2, 1), 0, -random.uniform(0.8, 1.5))
    extrude_vertice_to(random.uniform(0.2, 1), 0, -random.uniform(0.8, 1.5))
    select_vertice(4)   
    extrude_vertice_to(0, 0, random.uniform(1, 5))
    
    select_vertice(0)
    bpy.ops.object.skin_root_mark()
    # scale point
    for vertices in range(0, 10):
        print(vertices)
        select_vertice(vertices)
        resize_vertice(random.uniform(1, 5))
    #select_vertice(0)
    #resize_vertice(random.randrange(1, 3))
    
    bpy.ops.object.editmode_toggle()
    
    #on applique le miroir avant de créer l'armature     
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
    
    # renomme 
    for obj in bpy.context.selected_objects:
        obj.name = "Monstre"
        obj.data.name = "Monstre"
        
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.import_anim.bvh(filepath="C:\\Users\\antoi\\Desktop\\Monster_Generator\\cmuconvert-max-01-09\\02\\02_01.bvh")
    bpy.context.object.data.pose_position = 'REST'
    bpy.data.objects['Monstre'].select = True
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    bpy.context.object.data.pose_position = 'POSE'
     
class TreeGeneratorOperator(bpy.types.Operator):
    bl_idname = "object.monster_generator"
    bl_label = "monster_Generator"

    def execute(self, context):
        create_random_army(4, 2)
        #create_random_monster()
        return {'FINISHED'}
        
def register():
    bpy.utils.register_class(TreeGeneratorOperator)
    
def unregister():
    bpy.utils.unregister_class(TreeGeneratorOperator)


if __name__ == "__main__":
    register()
