"""Draws a signature-like scribble with real touch events (input motionevent)."""
import math
import time

import adbdrv as d


# Coarse control polygon of a cursive signature (800 x 270 box); Chaikin smoothing rounds it.
NAME = [(0, 215), (25, 120), (60, 30), (100, 14), (122, 70), (92, 150), (62, 218), (98, 228),
        (150, 172), (200, 118), (235, 86), (262, 112), (256, 172), (272, 204), (312, 152),
        (352, 102), (388, 82), (408, 116), (398, 176), (424, 204), (474, 152), (524, 102),
        (574, 72), (604, 102), (588, 162), (608, 196), (664, 160), (724, 126), (790, 118)]


def chaikin(points, rounds=3):
    for _ in range(rounds):
        out = [points[0]]
        for (x0, y0), (x1, y1) in zip(points, points[1:]):
            out.append((0.75 * x0 + 0.25 * x1, 0.75 * y0 + 0.25 * y1))
            out.append((0.25 * x0 + 0.75 * x1, 0.25 * y0 + 0.75 * y1))
        out.append(points[-1])
        points = out
    return points


def name_points():
    pts = chaikin(NAME)
    return pts[::2] + [pts[-1]]


def underline_points():
    return [(60 + 740 * u / 24, 262 - 34 * math.sin(u / 24 * math.pi * 0.8) - 16 * u / 24) for u in range(25)]


def stroke(points):
    cmds = []
    x, y = points[0]
    cmds.append(f'input motionevent DOWN {int(x)} {int(y)}')
    for x, y in points[1:-1]:
        cmds.append(f'input motionevent MOVE {int(x)} {int(y)}')
    x, y = points[-1]
    cmds.append(f'input motionevent UP {int(x)} {int(y)}')
    d.shell(' ; '.join(cmds))


def signature(w=1080, h=2400):
    """Scaled to the screen and centred a little under the middle of the pad."""
    scale = 0.98 * min(w / 1080, h / 2000)
    left, top = int(w / 2 - 400 * scale), int(h * 0.47)

    def place(pts):
        return [(left + x * scale, top + y * scale) for x, y in pts]
    stroke(place(name_points()))
    time.sleep(0.3)
    stroke(place(underline_points()))
