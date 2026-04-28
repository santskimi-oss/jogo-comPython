Import pygane

# Iniciando o pygame,"init" é iniciar
pygame.init()

# Definir o tamanho da janela. *display.set_mode é para "ditar" o modo da jenela
WIDTH, HEIGTH =720,720
tela = pygame.dyspaly.set_mode((WIDTH,HEIGHT))
pygame.dysplay.set_cption ("Nome da jenela")

# loop pricipal do jogo
running = true
while running:
    for evento in pygame.event.get()
    if evento.type == pygame.QUIT:
        running = false
        
        # Atualizando a tela
        pygame.dysplay.flip()

 # Finalizando o pygame
 pygame.quit()
 

 