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
        show_world_frame = False,
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
    pos    = (0.5, 0.0, 0.3),
    lookat = (0, 0, 0),
    fov    = 60,
    GUI    = False,
)

jnt_names = ['1', '2', '3', '4', '5', '6']
dofs_idx = [arm.get_joint(name).dof_idx_local for name in jnt_names]
# print(dofs_idx)
scene.build()
# cam.start_recording()

print('Initial DOFs:', arm.get_dofs_position(dofs_idx))

# print
# for i in range(300):
#     scene.step()
#     if i < 50:
#         arm.set_dofs_position()
#     cam.render()

# cam.stop_recording(save_to_filename='test_2.mp4', fps=30)
