import pygame

print('Setup Start')
pygame.init()

#Criando variável que recebe e cria a nossa janela. Posso chamar essa variável de screen
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:  #Laço indinico para mante minha janela aberta sem fechar
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quiting...')
            pygame.quit()  # close Window
            quit()  # end pygame
