#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assent/' + name + '.png') # Carreagar imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # Fazer o retangulo, posição livre
        self.speed = 0 # velocidade

    @abstractmethod
    def move(self, ):
        pass

