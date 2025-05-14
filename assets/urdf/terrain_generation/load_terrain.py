import genesis as gs
import numpy as np

gs.init(backend=gs.cuda)

scene = gs.Scene(
  show_viewer = False,
  viewer_options = gs.options.ViewerOptions(
    res = (1280, 960),
    camera_pos = (3.5, 0.0, 1),
    camera_lookat = (0.0, 0.0, 0.5),
    camera_fov = 60,
    max_FPS = None,
  ),
  vis_options = gs.options.VisOptions(
    show_world_frame = True,
    world_frame_size = 1.0,
    show_link_frame = False,
    show_cameras = False,
    plane_reflection = True,
    ambient_light = (0.1, 0.1, 0.1),
  ),
  # rigid_options=gs.options.RigidOptions(
  #   dt = 0.01,
  #   constraint_solver=gs.constraint_solver.Newton,
  # )
  renderer = gs.renderers.Rasterizer(),
)

# terrain = scene.add_entity(
#   gs.morphs.URDF(
#     file='terrain_test.urdf',
#     fixed=True,
#     convexify=False, 
#   )
# )
# terrain = scene.add_entity(gs.morphs.URDF(file='terrain.urdf', fixed=True))
# plane = scene.add_entity(gs.morphs.Plane())
# plane = scene.add_entity(gs.morphs.URDF(file='urdf/plane/plane.urdf', fixed=True))
# horizontal_scale = 0.25
# vertical_scale = 0.005
# height_field = np.zeros([100, 100])
# heights_range = np.arange(-10, 20, 10)
# height_field[10:90, 10:90] = 200 + np.random.choice(heights_range, (80, 80))
# terrain = scene.add_entity(
#     morph=gs.morphs.Terrain(
#         horizontal_scale=horizontal_scale,
#         vertical_scale=vertical_scale,
#         height_field=height_field,
#         pos = (-12, -12, -1)
#     )
# )
terrain = scene.add_entity(
  gs.morphs.Terrain(
    pos = (-60.0, -60.0, 0), 
    subterrain_types = 'random_uniform_terrain', 
    n_subterrains = (10,10),
    # vertical_scale = 0.002,
  )
)
dog = scene.add_entity(
  gs.morphs.URDF(
    file="urdf/go2/urdf/go2.urdf",
    pos = (0, 0, 0.5),
    quat = (1, 0, 0, 0),
  ),
)
# franka = scene.add_entity(
#   gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
#   vis_mode = 'collision',
# )

cam = scene.add_camera(
    res    = (1280, 960),
    pos    = (3.5, 0.0, 0.5),
    lookat = (0, 0, 0.5),
    fov    = 90,
    GUI    = False
)

scene.build()
cam.start_recording()

import numpy as np

for i in range(360):
    scene.step()
    cam.set_pose(
        pos = (3.0 * np.sin(i/60), 3.0 * np.cos(i/60), 0.5),
        lookat = (0, 0, 0.5),
    )
    cam.render()
cam.stop_recording(save_to_filename='test_terrain.mp4', fps=60)
