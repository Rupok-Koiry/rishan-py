import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Click to get coordinates of Bangladesh divisions")
screen.setup(width=600, height=600)
screen.bgpic("./bdd.gif")  # Use the uploaded map image

# Function to print coordinates on click


def get_mouse_click_coor(x, y):
    print(f"Coordinates: {x}, {y}")


# Listen for mouse clicks
turtle.onscreenclick(get_mouse_click_coor)

# Keep the window open
turtle.mainloop()
