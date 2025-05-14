import genesis as gs
gs.init(backend=gs.cuda)

scene = gs.Scene(
    show_viewer    = False,
    viewer_options = gs.options.ViewerOptions(
        res           = (1280, 960),
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

cam = scene.add_camera(
    res    = (1280, 960),
    pos    = (3.5, 0.0, 1.5),
    lookat = (0, 0, 0.5),
    fov    = 90,
    GUI    = False
)

scene.build()
cam.start_recording()

import numpy as np

for i in range(720):
    scene.step()
    cam.set_pose(
        pos = (3.0 * np.sin(i/60), 3.0 * np.cos(i/60), 2.5),
        lookat = (0, 0, 0.5),
    )
    cam.render()

cam.stop_recording(save_to_filename='test_2.mp4', fps=60)
