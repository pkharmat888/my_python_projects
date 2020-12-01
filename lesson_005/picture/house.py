import simple_draw as sd
import wall as wa


def house_draw(house_point, house_color, width=3):
    right_point = sd.get_point(house_point.x + 500, house_point.y + 301)
    # wire
    sd.rectangle(left_bottom=house_point, right_top=right_point,
                 color=house_color, width=width)
    # roof
    list_poly = [sd.get_point(house_point.x - 50, house_point.y + 300),
                 sd.get_point(house_point.x + 550, house_point.y + 300),
                 sd.get_point(house_point.x + 250, house_point.y + 500)]
    sd.polygon(point_list=list_poly, color=house_color, width=0)
    # wall
    sd.rectangle(left_bottom=house_point, right_top=right_point,
                 color=sd.COLOR_DARK_CYAN)
    sd.rectangle(left_bottom=house_point, right_top=right_point,
                 color=house_color, width=5)
    wa.wall_draw(x_start_point=house_point.x + 75, x_endpoint=right_point.x + 25,
                 y_start_point=house_point.y + 25, y_endpoint=right_point.y,
                 color_of_wall=house_color)
    # window
    sd.rectangle(left_bottom=sd.get_point(house_point.x + 200, house_point.y + 100),
                 right_top=sd.get_point(right_point.x - 100, right_point.y - 40), color=sd.COLOR_DARK_PURPLE)
    # window frame
    sd.rectangle(left_bottom=sd.get_point(house_point.x + 200, house_point.y + 100),
                 right_top=sd.get_point(right_point.x - 100, right_point.y - 40), color=house_color, width=5)
