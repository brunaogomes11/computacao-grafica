from PIL import Image, ImageFilter, ImageChops

img = Image.open("f1.jpg")
img_cinza = Image.open("f1.jpg").convert('L')

mask_x = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
mask_y = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
kernel_sobel_x = ImageFilter.Kernel((3,3), mask_x, 1)
kernel_sobel_y = ImageFilter.Kernel((3,3), mask_y, 1)

sobel_x = img.filter(kernel_sobel_x)
sobel_y = img.filter(kernel_sobel_y)
sobel_f = ImageChops.add(sobel_x, sobel_y)

sobel_x.save('imagens/sobel_x.jpg')
sobel_y.save('imagens/sobel_y.jpg')
sobel_f.save('imagens/sobel_f.jpg')

sobel_x = img_cinza.filter(kernel_sobel_x)
sobel_y = img_cinza.filter(kernel_sobel_y)
sobel_f = ImageChops.add(sobel_x, sobel_y)

sobel_x.save('imagens/sobel_cinza_x.jpg')
sobel_y.save('imagens/sobel_cinza_y.jpg')
sobel_f.save('imagens/sobel_cinza_f.jpg')

# Com Sobel não houve diferença significativa entre a imagem em escala de cinza e rgb. A diferença entre os dois é que na imagem não convertida, o resultado preserva as cores das bordas.

mask_la1 = [0,1,0,1,-4,1,0,1,0]
mask_la2 = [1,1,1,1,-8,1,1,1,1]
laplaciano1 = img.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
laplaciano1.save('imagens/laplaciano1.jpg')

laplaciano2 = img.filter(ImageFilter.Kernel((3,3), mask_la2, 1))
laplaciano2.save('imagens/laplaciano2.jpg')

laplaciano1 = img_cinza.filter(ImageFilter.Kernel((3,3), mask_la1, 1))
laplaciano1.save('imagens/laplaciano1_cinza.jpg')

laplaciano2 = img_cinza.filter(ImageFilter.Kernel((3,3), mask_la2, 1))
laplaciano2.save('imagens/laplaciano2_cinza.jpg')

# Em ambas máscaras, a imagem em escala de cinza filtrou melhor as bordas. Não há diferença de cor nas imagens, ambas ficam com as mesmas cores.

mask_x = [-1,0,1,-1,0,1,-1,0,1]
mask_y = [-1,-1,-1,0,0,0,1,1,1]

kernel_prewitt_x = ImageFilter.Kernel((3,3), mask_x, 1)
kernel_prewitt_y = ImageFilter.Kernel((3,3), mask_y, 1)
prewitt_x = img.filter(kernel_prewitt_x)
prewitt_y = img.filter(kernel_prewitt_y)
prewitt_f = ImageChops.add(prewitt_x, prewitt_y)

prewitt_x.save('imagens/prewitt_x.jpg')
prewitt_y.save('imagens/prewitt_y.jpg')
prewitt_f.save('imagens/prewitt_f.jpg')

prewitt_x = img_cinza.filter(kernel_prewitt_x)
prewitt_y = img_cinza.filter(kernel_prewitt_y)
prewitt_f = ImageChops.add(prewitt_x, prewitt_y)

prewitt_x.save('imagens/prewitt_x_cinza.jpg')
prewitt_y.save('imagens/prewitt_y_cinza.jpg')
prewitt_f.save('imagens/prewitt_f_cinza.jpg')

# Com o prewitt, na mascara y, a imagem colorida perfomou melhor quanto a cinza. Porém, em x aconteceu o contrário e na imagem total, a escala de cinza foi superior. Assim como o Filtro de Sobel, a imagem em coloração normal apresenta bordas preservando as cores reais da imagem, enquanto na escala de cinzas não.