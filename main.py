"""Draw a star at a random location for each user click."""

import random
import asyncio

# Import and initialize pygame.
import pygame
pygame.init()

# Define constants and annotate variables
SIZE: int = 600
screen: pygame.Surface
background: pygame.Surface
green_splatter: pygame.Surface
blue_splatter: pygame.Surface
red_splatter: pygame.Surface
purple_splatter: pygame.Surface
yellow_splatter: pygame.Surface
orange_splatter: pygame.Surface
offset_w: float
offset_h: float
user_quit: bool
event: pygame.event.Event
x: int
y: int
splat_choice: int
accumulator: int
random_caption: int

#Create list of final state captions
caption_list = ["Finished!","Ready for MOMA!","Sheer Genius!",
                "The next Picasso!","A masterpiece!"]

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Click to paint!")

# Load the images.
background = pygame.image.load("assets/art_studio.jpg")
green_splatter = pygame.image.load("assets/green_splatter.png")
blue_splatter = pygame.image.load("assets/blue_splatter.png")
red_splatter = pygame.image.load("assets/red_splatter.png")
purple_splatter = pygame.image.load("assets/purple_splatter.png")
yellow_splatter = pygame.image.load("assets/yellow_splatter.png")
orange_splatter = pygame.image.load("assets/orange_splatter.png")
offset_w = green_splatter.get_width() / 2
offset_h = green_splatter.get_height() / 2
accumulator = 0

# Draw a star for each click.
async def main():
  accumulator = 0
  user_quit = False
  screen.blit(background,(0,0))
  while not user_quit:
    for event in pygame.event.get():
      # Process a quit choice.
      if event.type == pygame.QUIT:
        user_quit = True
      # Process a click by drawing a star.
      elif event.type == pygame.MOUSEBUTTONUP:
        if accumulator == 11:
          screen.blit(background,(0,0))
          accumulator = 0
          pygame.display.set_caption("Click to paint!")
        else:
          accumulator += 1
          print(accumulator)
          x = random.randint(50,350)
          y = random.randint(50,250)
          splat_choice = random.randint(0,5)
          if splat_choice == 0:
            screen.blit(green_splatter,(x,y))
          elif splat_choice == 1:
            screen.blit(blue_splatter,(x,y))
          elif splat_choice == 2:
            screen.blit(red_splatter,(x,y))
          elif splat_choice == 3:
            screen.blit(purple_splatter,(x,y))
          elif splat_choice == 4:
            screen.blit(yellow_splatter,(x,y))
          elif splat_choice == 5:
            screen.blit(orange_splatter,(x,y))
          if accumulator == 10:
            random_caption = random.randint(0,4)
            pygame.display.set_caption(caption_list[random_caption])
            accumulator += 1
          else:
            pygame.display.set_caption("Perfect!")
    # Show the drawing.
    pygame.display.flip()
    await asyncio.sleep(0)
  
asyncio.run(main())