#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import menu


class game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            Menu = menu(self.window)
            Menu.run()
            pass
            # Check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
             #       quit()  # end pygame)#