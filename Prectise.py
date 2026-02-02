
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math

# =============================
# GLOBAL CONFIG
# =============================
FIG_SIZE = (6, 6)
FPS_INTERVAL = 60
COLORMAPS = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis',
    'rainbow', 'jet', 'turbo'
]

# =============================
# UTILITY FUNCTIONS
# =============================
def random_color():
    return (
        random.random(),
        random.random(),
        random.random()
    )


def setup_axes(ax, xlim, ylim, title=""):
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)


# =============================
# SCENE 1: RAINBOW SINE WAVE
# =============================
def rainbow_sine_wave():
    x = np.linspace(0, 2*np.pi, 300)

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    setup_axes(ax, (0, 2*np.pi), (-1.5, 1.5), "Rainbow Sine Wave")

    line, = ax.plot([], [], lw=3)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    def update(frame):
        y = np.sin(x + frame * 0.1)
        line.set_data(x, y)
        line.set_color(colors[frame % len(colors)])
        return line,

    return FuncAnimation(fig, update, frames=200, interval=FPS_INTERVAL)


# =============================
# SCENE 2: COLORFUL BOUNCING BALL
# =============================
def bouncing_ball():
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    setup_axes(ax, (-10, 10), (-10, 10), "Colorful Bouncing Ball")

    ball, = ax.plot([], [], 'o', markersize=15)

    x, y = 0, 0
    vx, vy = 0.3, 0.4

    def update(frame):
        nonlocal x, y, vx, vy
        x += vx
        y += vy

        if abs(x) > 9:
            vx *= -1
        if abs(y) > 9:
            vy *= -1

        ball.set_data(x, y)
        ball.set_color(random_color())
        return ball,

    return FuncAnimation(fig, update, frames=300, interval=FPS_INTERVAL)


# =============================
# SCENE 3: COLORFUL RANDOM WALK
# =============================
def random_walk():
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    setup_axes(ax, (-50, 50), (-50, 50), "Random Walk")

    x_data, y_data = [0], [0]
    line, = ax.plot([], [], lw=2)

    def update(frame):
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        x_data.append(x_data[-1] + dx)
        y_data.append(y_data[-1] + dy)
        line.set_data(x_data, y_data)
        line.set_color(random_color())
        return line,

    return FuncAnimation(fig, update, frames=400, interval=FPS_INTERVAL)


# =============================
# SCENE 4: HEART SHAPE ANIMATION
# =============================
def heart_animation():
    t = np.linspace(0, 2*np.pi, 400)
    x = 16*np.sin(t)**3
    y = (13*np.cos(t)
         - 5*np.cos(2*t)
         - 2*np.cos(3*t)
         - np.cos(4*t))

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    setup_axes(ax, (-20, 20), (-20, 20), "Heart Animation")

    line, = ax.plot([], [], lw=3)
    colors = ['red', 'hotpink', 'magenta', 'purple']

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        line.set_color(colors[frame % len(colors)])
        return line,

    return FuncAnimation(fig, update, frames=len(t), interval=FPS_INTERVAL)


# =============================
# SCENE 5: COLORFUL BAR GROWTH
# =============================
def bar_growth():
    values = np.random.randint(1, 100, 10)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.set_ylim(0, 100)
    bars = ax.bar(range(len(values)), values, color='cyan')
    ax.set_title("Colorful Bar Growth")

    def update(frame):
        for bar in bars:
            bar.set_height(random.randint(1, 100))
            bar.set_color(random_color())
        return bars

    return FuncAnimation(fig, update, frames=200, interval=FPS_INTERVAL)


# =============================
# SCENE MANAGER
# =============================
def run_scene(scene_id):
    scenes = {
        1: rainbow_sine_wave,
        2: bouncing_ball,
        3: random_walk,
        4: heart_animation,
        5: bar_growth
    }

    if scene_id not in scenes:
        print("Invalid scene")
        return

    ani = scenes[scene_id]()
    plt.show()


# =============================
# MAIN PROGRAM
# =============================
if __name__ == "__main__":
    print("COLORFUL ANIMATION MEGA PROJECT")
    print("1. Rainbow Sine Wave")
    print("2. Bouncing Ball")
    print("3. Random Walk")
    print("4. Heart Animation")
    print("5. Bar Growth")

    try:
        choice = int(input("Enter scene number: "))
        run_scene(choice)
    except Exception as e:
        print("Error:", e)