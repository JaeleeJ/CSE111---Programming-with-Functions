# Jaelee Hutchinson
# 03 Prove Milestone: Writing Functions

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_height, scene_width)
    

    # draw one cloud
    draw_cloud(canvas, 500, 475, 400, 400)
    draw_cloud(canvas, 600, 400, 350, 450)

    # draw second cloud
    draw_cloud(canvas, 300, 375, 200, 300)
    draw_cloud(canvas, 400, 300, 150, 350)

    # draw sun
    draw_sun(canvas, 700, 400, 750, 450)

    # draw ground and trees
    draw_ground(canvas, scene_height, scene_width)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_height, scene_width):
    # draw sky
    draw_rectangle(canvas, 0, scene_height / 3, 
        scene_width, scene_height, width = 0, fill = "sky blue" )


def draw_cloud(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width = 0, fill = "white")

def draw_sun(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width = 0, fill = "yellow")


def draw_ground(canvas, scene_height, scene_width):
    # draw ground
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3,
        width = 0, fill = "tan4")

    # draw fall tree
    tree_center = 150
    tree_bottom = 100
    tree_height = 300
    draw_tree(canvas, tree_center, tree_bottom, tree_height)

    # draw another fall tree
    tree_center = 450
    tree_bottom = 100
    tree_height = 275
    draw_tree(canvas, tree_center, tree_bottom, tree_height)

    #draw another fall tree
    tree_center = 650
    tree_bottom = 100
    tree_height = 200
    draw_tree(canvas, tree_center, tree_bottom, tree_height)

    #draw another fall tree
    tree_center = 550
    tree_bottom = 90
    tree_height = 250
    draw_tree(canvas, tree_center, tree_bottom, tree_height)


def draw_tree(canvas, center, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center - trunk_width / 2
    trunk_right = center + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right,
        bottom, width = 1, fill = "tan2")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center - skirt_width / 2
    skirt_right = center  + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center, skirt_top, skirt_right,
        trunk_top, skirt_left, trunk_top, width = 1, fill = "brown")


# Call the main function so that
# this program will start executing.
main()