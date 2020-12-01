import simple_draw as sd


def rainbow_draw(point, step, colors_list):
    radius = 1000
    for color in colors_list:
        radius -= step
        sd.circle(center_position=point, radius=radius, color=color, width=5)
    colors_list.append(colors_list.pop(0))

