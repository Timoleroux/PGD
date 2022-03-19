from kandinsky import *
from ion import *
from time import sleep
from random import randint
# Screen size : x=320 y=222

# General
score = 0
add_score = False

# About cuby
x = 100
y = 100
cuby_color = color(0, 0, 0)
fill_rect(100, 100, 10, 10, cuby_color)

# About the targets
target_color = color(255, 0, 0)

# Generate the targets
for i in range(20):
  target_x = randint(0, 63)*5
  target_y = randint(0, 43)*5
  fill_rect(target_x, target_y, 4, 4, target_color)

# main
while True:
  if keydown(KEY_UP):
    # Check for target on top
    pix_x = 0
    pix_y = 1
    for i in range(8*9):      
      pix = get_pixel(x+pix_x ,y-pix_y)
      if pix == color(255,0,0) and keydown(KEY_UP):
        add_score = True
      if pix_x == 9:
        pix_y += 1
        pix_x = -1
      pix_x += 1
    if add_score == True:
      add_score = False
      score += 1
      draw_string(str(score),160,20)
    # Move upward 
    fill_rect(x, y-10, 10, 10, cuby_color)
    fill_rect(x, y, 10, 10, color(255, 255, 255))
    y -= 10
    sleep(0.1)

  elif keydown(KEY_DOWN):   
    # Check for target on top
    pix_x = 0
    pix_y = 1
    for i in range(8*9):      
      pix = get_pixel(x+pix_x, y+pix_y+10)
      print(x+pix_x, y+pix_y+10)
      if pix == color(255,0,0) and keydown(KEY_DOWN):
        add_score = True
      if pix_x == 9:
        pix_y += 1
        pix_x = -1
      pix_x += 1
    if add_score == True:
      add_score = False
      score += 1
      draw_string(str(score),160,20)
    # Move downward
    fill_rect(x, y+10, 10, 10, cuby_color)
    fill_rect(x, y, 10, 10, color(255, 255, 255))      
    y += 10
    sleep(0.1)

  elif keydown(KEY_RIGHT):
        # Check for target on top
    pix_x = 0
    pix_y = 1
    for i in range(8*9):      
      pix = get_pixel(x+pix_x ,y+pix_y)
      if pix == color(255,0,0) and keydown(KEY_RIGHT):
        add_score = True
      if pix_y == 9:
        pix_y = -1
        pix_x += 0
      pix_y += 1
    if add_score == True:
      add_score = False
      score += 1
      draw_string(str(score),160,20)
    # Move downward
    fill_rect(x+10, y, 10, 10, cuby_color)
    fill_rect(x, y, 10, 10, color(255, 255, 255))
    x += 10
    sleep(0.1)
  
  elif keydown(KEY_LEFT):
    fill_rect(x-10, y, 10, 10, cuby_color)
    fill_rect(x, y, 10, 10, color(255, 255, 255))
    x -= 10
    sleep(0.1)