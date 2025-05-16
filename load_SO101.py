import genesis as gs
import numpy as np

gs.init(backend=gs.cuda)

scene = gs.Scene(
    show_viewer    = False,
    viewer_options = gs.options.ViewerOptions(
        res           = (1280, 720),
        camera_pos    = (3.5, 0.0, 2.5),
        camera_lookat = (0.0, 0.0, 0.5),
        camera_fov    = 40,
        max_FPS       = None,
    ),
    vis_options = gs.options.VisOptions(
        show_world_frame = True,
        world_frame_size = 1.0,
        show_link_frame  = False,
        show_cameras     = False,
        plane_reflection = True,
        ambient_light    = (0.1, 0.1, 0.1),
    ),
    renderer = gs.renderers.Rasterizer(),
)

plane = scene.add_entity(gs.morphs.Plane())
arm = scene.add_entity(gs.morphs.MJCF(file='assets/SO101/so101.xml'))


cam = scene.add_camera(
    res    = (1280, 720),
    pos    = (0.5, 0.0, 0.5),
    lookat = (0, 0, 0),
    fov    = 60,
    GUI    = False,
)

jnt_names = ['1', '2', '3', '4', '5', '6']

# <joint axis="0 0 1" name="1" type="hinge" range="-1.9198621771937616 1.9198621771937634" class="sts3215"/>
# <joint axis="0 0 1" name="2" type="hinge" range="-0.17453292519943472 3.3161255787892245" class="sts3215"/>
# <joint axis="0 0 1" name="3" type="hinge" range="-3.2288591161895077 0.08726646259971825" class="sts3215"/
# <joint axis="0 0 1" name="4" type="hinge" range="-1.658062789394615 1.6580627893946114" class="sts3215"/>
# <joint axis="0 0 1" name="5" type="hinge" range="-2.792526803190913 2.7925268031909414" class="sts3215"/>
# <joint axis="0 0 1" name="6" type="hinge" range="-0.2617993877991352 1.7453292519943437" class="sts3215"/>

scene.build()

dofs_idx = [arm.get_joint(name).dof_idx_local for name in jnt_names]
jaw = arm.get_link('moving_jaw_so101_v1')
qpos = arm.inverse_kinematics(
    link = jaw,
    pos = np.array([0.0, 0.5, 0.3]),
    quat = np.array([0.0, 0.0, 0.0, 1.0])
)
# print(dofs_idx)
print(qpos)
cam.start_recording()

arm.control_dofs_position(qpos, dofs_idx)
for i in range(100):
    scene.step()
    cam.render()

cam.stop_recording(save_to_filename='test_2.mp4', fps=30)
# print('Initial DOFs:', arm.get_dofs_position(dofs_idx))

# for i in range(300):
#     scene.step()
#     if i < 50:
#         arm.set_dofs_position(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]), dofs_idx)
#     elif i < 100:
#         arm.set_dofs_position(np.array([1.0, 2.0, -3.0, 1.0, 0.5, 0.5]), dofs_idx)
#     cam.render()

# cam.stop_recording(save_to_filename='test_2.mp4', fps=30)
