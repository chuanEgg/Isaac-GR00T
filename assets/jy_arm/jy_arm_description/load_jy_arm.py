import genesis as gs
import numpy as np

gs.init(backend=gs.cuda)

scene = gs.Scene(
  show_viewer = False,
  viewer_options = gs.options.ViewerOptions(
    res = (1280, 720),
    camera_pos = (3.5, 0.0, 2.5),
    camera_lookat = (0.0, 0.0, 0.5),
    camera_fov = 40,
    max_FPS = None,
  ),
  vis_options = gs.options.VisOptions(
    show_world_frame = True,
    world_frame_size = 1.0,
    show_link_frame = True,
    show_cameras = False,
    plane_reflection = True,
    ambient_light = (0.1, 0.1, 0.1),
  ),
  renderer = gs.renderers.Rasterizer(),
)

plane = scene.add_entity(gs.morphs.Plane())
arm = scene.add_entity(
  gs.morphs.URDF(
    file='model.urdf',
    convexify=True,
    euler=(90,0,0),
    fixed=True,
  )
)

cam = scene.add_camera(
  res = (1280, 720),
  pos = (1.0, 0.0, 0.5),
  lookat = (0.0, 0.0, 0.0),
  fov = 40,
  GUI = False,
)

scene.build()

cam.start_recording()

for i in range(120):
  scene.step()
  # cam.set_pose(pos)
  cam.render()

cam.stop_recording(save_to_filename='test_jy_arm.mp4', fps=30)
