import game

pygame.int()

LARGURA ,ALTURA =720,720
tela = pygame dysplay.set_mode(LARGURA, ALTURA)
pygame.dysplay.set_caption("Meu primeiro jogo")
 
 # Variavel com a cor do fundo em regb!!
 COR_FUNDO = (83, 218, 200)

 running = True
 while running:
        for evento in pygame.event.get()
        if evento.type == pygame.QUIT:
            running = false

# Fundo da tela
      tela.fill(COR_FUNDO)


      pygame.dysplay.flip()

      pygane.quit()

