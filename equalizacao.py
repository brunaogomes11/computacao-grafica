from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import random

def aplicar_ruido(img, prob):
    output = np.array(img)
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            rnd = random.random()
            if (rnd < prob):
                output[i][j] = 0
            elif (rnd > 1 - prob):
                output[i][j] = 255

    return Image.fromarray(output)

def equalizar_historgrama(imagem_pil):
    imagem = np.array(imagem_pil)
    histogram, bins = np.histogram(imagem.flatten(), bins=256, range=[0,256])
    cdf = histogram.cumsum()
    cdf_normalizada = cdf * 255 / cdf[-1]
    imagem_equalizada = np.interp(imagem.flatten(), bins[:-1], cdf_normalizada)
    return Image.fromarray(imagem_equalizada.reshape(imagem.shape).astype('uint8'))

def criar_graficos(img, img_eq):
    fig, axs = plt.subplots(2,2, figsize=(10,6))
    axs[0,0].imshow(img, cmap='gray')
    axs[0,0].set_title("Original")
    axs[0,0].axis("off")
    axs[0,1].hist(np.array(img).flatten(), bins=256, range=[0,256], color='gray')
    axs[0,1].set_title("Histograma original")

    axs[1,0].imshow(img_eq, cmap='gray')
    axs[1,0].set_title("Equalizada")
    axs[1,0].axis("off")

    axs[1,1].hist(np.array(img_eq).flatten(), bins=256, range=[0,256], color='gray')
    axs[1,1].set_title("Histograma equalizado")

    plt.tight_layout()
    plt.show()

def testar_imagem_clara():
    # Imagem Clara
    img1 = Image.open("imagem_clara.jpeg").convert('L')

    # Detecção de bordas sem equalização
    mask_la1 = [0,1,0,1,-4,1,0,1,0]
    laplaciano1 = img1.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
    laplaciano1.save('imagens/clara_laplaciano.jpg')

    # Equalizar Imagem
    img_eq1 = equalizar_historgrama(img1)

    # Detecção de bordas com equalização
    laplaciano_pos = img_eq1.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
    laplaciano_pos.save('imagens/clara_eq_laplaciano.jpg')

    # Equalização sem ruídos
    img1.save("imagens/clara_cinza.jpg")
    img_eq1.save("imagens/clara_eq.jpg")
    criar_graficos(img1, img_eq1)

    # Aplicar ruído
    img2 = aplicar_ruido(img1, 0.05)
    img_eq2 = equalizar_historgrama(img2)

    img2.save("imagens/clara_cinza_ruido.jpg")
    img_eq2.save("imagens/clara_eq_ruido.jpg")
    criar_graficos(img2, img_eq2)

    # Conclusões - Imagem Clara: 
    '''
        A equalização com ou sem ruídos para a imagem clara foi indiferente, ambas tiveram o mesmo resultado, transformando em uma imagem mais escura e na imagem selecionada deu para ver melhore detalhes nas árvores. A detecção de bordas da imagem equalizada, houve uma piora quanto a detecção de bordas aplicada na imagem original.
    '''


def testar_imagem_escura():
    # Imagem Escura
    img1 = Image.open("imagem_escura.jpg").convert('L')

    # Detecção de bordas sem equalização
    mask_la1 = [0,1,0,1,-4,1,0,1,0]
    laplaciano1 = img1.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
    laplaciano1.save('imagens/escura_laplaciano.jpg')

    # Equalizar Imagem
    img_eq1 = equalizar_historgrama(img1)

    # Detecção de bordas com equalização
    laplaciano_pos = img_eq1.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
    laplaciano_pos.save('imagens/escura_eq_laplaciano.jpg')

    # Equalização sem ruídos
    img1.save("imagens/escura_cinza.jpg")
    img_eq1.save("imagens/escura_eq.jpg")
    criar_graficos(img1, img_eq1)

    # Aplicar ruído
    img2 = aplicar_ruido(img1, 0.05)
    img_eq2 = equalizar_historgrama(img2)

    img2.save("imagens/escura_cinza_ruido.jpg")
    img_eq2.save("imagens/escura_eq_ruido.jpg")
    criar_graficos(img2, img_eq2)

    # Conclusões - Imagem Clara: 
    '''
        A equalização com ruídos teve uma pequena diferença na hora de equalizar, mas algo pouco percepitivel. A detecção de bordas da imagem equalizada, mesmo que haja pouca borda, houve uma melhora significativa quanto a detecção de bordas aplicada na imagem original.
    '''

testar_imagem_escura()