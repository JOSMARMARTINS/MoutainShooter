#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        # Criando variável que recebe e cria a nossa janela. Posso chamar essa variável de screen
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT))

    def run(self):
        while True:  # Laço indinico para mante minha janela aberta sem fechar
            menu = Menu(self.window)
            menu.run()
            pass


