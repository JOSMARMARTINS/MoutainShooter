#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assent/MenuBg.png')
        self.rect =  self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assent/Menu.mp3') #  Carregando música
        pygame.mixer_music.play(-1) #  Para tocar a música. O -1 deixa ala repedindo infinitamente
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha a imagem no retângulo
            self.menu_text(
                50,  # tamanho da fonte
                "Mountain",  # texto
                COLOR_ORANGE,  # cor RGB
                (WIN_WIDTH / 2, 70)  # posição X, Y
            )
            self.menu_text(
                50,  # tamanho da fonte
                "Shooter",  # texto
                COLOR_ORANGE,  # cor RGB
                (WIN_WIDTH / 2, 120)  # posição X, Y
            )

            #  CRIA O MENU COM UM ESPARÇO DE 25 NO EIXO X
            for i in range(len(MENU_OPTION)):
                self.menu_text(
                    20,  # tamanho da fonte
                    MENU_OPTION[i],  # texto
                    COLOR_WHITE,  # cor RGB
                    ((WIN_WIDTH / 2), 200 + 25 * i)  # posição X, Y
                )

            pygame.display.flip()  # para atualizar imagem na tela

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame

    #  Método com a as fontes
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
