import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 8)
ax.set_aspect('equal')
ax.axis('off')

# Body parts
head, = ax.plot([], [], 'o', markersize=15)
body, = ax.plot([], [], lw=3)
left_arm, = ax.plot([], [], lw=3)
right_arm, = ax.plot([], [], lw=3)
left_leg, = ax.plot([], [], lw=3)
right_leg, = ax.plot([], [], lw=3)

def update(frame):
    t = frame * 0.1

    # Head
    head_x = 0
    head_y = 6
    head.set_data(head_x, head_y)
    head.set_color('orange')

    # Body
    body_x = [0, 0]
    body_y = [2.5, 5.5]
    body.set_data(body_x, body_y)
    body.set_color('black')

    # Arms (swing)
    arm_swing = np.sin(t)
    left_arm.set_data([0, -1.5], [4.8, 4.8 + arm_swing])
    right_arm.set_data([0, 1.5], [4.8, 4.8 - arm_swing])
    left_arm.set_color('blue')
    right_arm.set_color('blue')

    # Legs (walking motion)
    leg_swing = np.sin(t)
    left_leg.set_data([0, -1.2], [2.5, 2.5 - leg_swing*2])
    right_leg.set_data([0, 1.2], [2.5, 2.5 + leg_swing*2])
    left_leg.set_color('green')
    right_leg.set_color('green')

    return head, body, left_arm, right_arm, left_leg, right_leg

ani = FuncAnimation(fig, update, frames=200, interval=60)
plt.show()
