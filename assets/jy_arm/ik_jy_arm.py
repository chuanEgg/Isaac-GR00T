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
    world_frame_size = 0.5,
    show_link_frame = True,
    link_frame_size = 0.1,
    show_cameras = False,
    plane_reflection = False,
    ambient_light = (0.1, 0.1, 0.1),
  ),
  renderer = gs.renderers.Rasterizer(),
)

plane = scene.add_entity(gs.morphs.Plane())
arm = scene.add_entity(
  gs.morphs.URDF(
    file='jy_arm.urdf',
    convexify=True,
    euler=(90,0,0),
    fixed=True,
  )
)

cam = scene.add_camera(
  res = (1280, 720),
  pos = (1.0, 0.0, 0.3),
  lookat = (0.0, 0.0, 0.2),
  fov = 40,
  GUI = False,
)

scene.build()

jnt_names = ['base_link_to_base_rotor',\
             'base_rotor_to_arm',\
             'arm_to_elbow',\
             'elbow_to_forearm',\
             'forearm_to_wrist',\
             'wrist_to_hand']

dofs_idx = [arm.get_joint(name).dof_idx_local for name in jnt_names]
hand = arm.get_link('hand_1')

qpos_1 = arm.inverse_kinematics(
  link = hand,
  pos = np.array([0.0, 0.5, 0.3]),
  quat = np.array([0.0, 0.0, 0.0, 1.0])
)

qpos_2 = arm.inverse_kinematics(
  link = hand,
  pos = np.array([0.2, -0.3, 0.6]),
  quat = np.array([0.0, 0.0, 1.0, 0.0])
)
cam.start_recording()

arm.control_dofs_position(qpos_1, dofs_idx)
for i in range(100):
  scene.step()
  cam.render()

arm.control_dofs_position(qpos_2, dofs_idx)
for i in range(100):
  scene.step()
  cam.render()

cam.stop_recording(save_to_filename='ik_jy_arm.mp4', fps=30)
