# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# ax.set_xlim(-5, 5)
# ax.set_ylim(-1, 8)
# ax.set_aspect('equal')
# ax.axis('off')

# # Body parts
# head, = ax.plot([], [], 'o', markersize=15)
# body, = ax.plot([], [], lw=3)
# left_arm, = ax.plot([], [], lw=3)
# right_arm, = ax.plot([], [], lw=3)
# left_leg, = ax.plot([], [], lw=3)
# right_leg, = ax.plot([], [], lw=3)

# def update(frame):
#     t = frame * 0.1

#     # Head
#     head_x = 0
#     head_y = 6
#     head.set_data(head_x, head_y)
#     head.set_color('orange')

#     # Body
#     body_x = [0, 0]
#     body_y = [2.5, 5.5]
#     body.set_data(body_x, body_y)
#     body.set_color('black')

#     # Arms (swing)
#     arm_swing = np.sin(t)
#     left_arm.set_data([0, -1.5], [4.8, 4.8 + arm_swing])
#     right_arm.set_data([0, 1.5], [4.8, 4.8 - arm_swing])
#     left_arm.set_color('blue')
#     right_arm.set_color('blue')

#     # Legs (walking motion)
#     leg_swing = np.sin(t)
#     left_leg.set_data([0, -1.2], [2.5, 2.5 - leg_swing*2])
#     right_leg.set_data([0, 1.2], [2.5, 2.5 + leg_swing*2])
#     left_leg.set_color('green')
#     right_leg.set_color('green')

#     return head, body, left_arm, right_arm, left_leg, right_leg

# ani = FuncAnimation(fig, update, frames=200, interval=60)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Heart shape equation
t = np.linspace(0, 2*np.pi, 400)
x_base = 16 * np.sin(t)**3
y_base = (13*np.cos(t)
          - 5*np.cos(2*t)
          - 2*np.cos(3*t)
          - np.cos(4*t))

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')

line, = ax.plot([], [], lw=4)

# Soft heart colors
colors = [
    "#ff4d6d",  # soft red
    "#ff6f91",  # pink
    "#dc194a",  # light pink
    "#ec0d4c"
]

def update(frame):
    # Heart pumping (scale factor)
    scale = 1 + 0.08 * np.sin(frame * 0.3)

    x = x_base * scale
    y = y_base * scale

    line.set_data(x, y)
    line.set_color(colors[frame % len(colors)])
    line.set_alpha(0.85)   # soft look

    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=200,
    interval=50
)

plt.show()