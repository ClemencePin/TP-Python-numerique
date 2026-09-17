import numpy as np 
import matplotlib.pyplot as plt
imge = np.empty((91,91,3))
imge[:] = 0

#pour un array il faut pour accéder à l'équivalent de list[1][1] faire array[1,1]

for i in range(91):
    for k in range(91):
        imge[i,k,1] = 255

print(imge[0,0])
print(imge[90,90])

for k in range(10,91,10):
    for i in range(0,91):
        imge[k,i,1]= 0
        imge[k,i,2] = 255

for k in range(10,91,10):
    for i in range(0,91):
        imge[i,k,1]= 0
        imge[i,k,2] = 255


#plt.imshow(imge)
#plt.show()


im = plt.imread("les-mines.jpg")

if not im.flags.writeable:
    im = im.copy()

#plt.imshow(im)
#plt.show()

#print(type(im))
#print(im.ndim)
#print(im.shape[:2])  #hauteur,largeur
#print(im.itemsize) #octets par valeur
#print(im.dtype) #type de pixels
#print(im.max(), im.min()) #valeurs max et min des pixels
#plt.imshow(im[:10,:10]) #affiche rectangle de 10 fois 10 pixels
#plt.show()

im2 = plt.imread("les-mines.jpg")

#for k in [2,5,10,20]:
    #plt.imshow(im2[::k,::k])
    #plt.show()

a = im2.shape[0]//2
b = im2.shape[1]//2
l,c = 100,200
a1 = a-(l//2)
a2 = a + (l//2)
b1 = b -(c//2)
b2 = b + (c//2)
plt.imshow(im2[a1:a2,b1:b2])
plt.show()

im3 = plt.imread("les-mines.jpg")

a = im3.shape[0]
b = im3.shape[1]

i0 = np.empty((a,b,3), dtype = im.dtype)
i1 = np.empty((a,b,3), dtype = im.dtype)
i2 = np.empty((a,b,3), dtype = im.dtype)

i0[:] = 0
i1[:] = 0
i2[:] = 0

for i in range(a):
    for k in range(b):
        i0[i,k,0] = im3[i,k,0]
        i1[i,k,1] = im3[i,k,1]
        i2[i,k,2] = im3[i,k,2]
#i0 = im3[:,:,0]
#i1 = im3[:,:,1]
#i2 = im3[:,:,2]

plt.imshow(i0, cmap='Reds')   #bon affichage des couleurs
plt.show()
plt.imshow(i1,cmap = 'Greens')
plt.show()
plt.imshow(i2,cmap = 'Blues')
#plt.show()

im4 = im3.copy()
#im4[-200:,-200:] = (219,112,147)
im4[-200:,-200:] = (255,255,255)
im4[-200::2,-200:,0] = 255
im4[-200::2,-200:,1] = 0
im4[-200::2,-200:,2] = 0

plt.imshow(im4[-20:,-20:])
#plt.show()

im5 = plt.imread("les-mines.jpg")  #pour la transparence
tab = np.empty((a,b,4),dtype = im.dtype)  #METTRE LE DTYPE POUR QUE CA MARCHE !!!
for k in range(a):
    for l in range(b):
        tab[k,l,0] = im5[k,l,0]
        tab[k,l,1] = im5[k,l,1]
        tab[k,l,2] = im5[k,l,2]
        tab[k,l,3] = 128
plt.imshow(tab)
plt.show()

im6 = plt.imread("les-mines.jpg").copy().astype(float)

for i in range (a):
    for j in range(b):
        im6[i,j,0] = im6[i,j,0]/255
        im6[i,j,1] = im6[i,j,1]/255
        im6[i,j,2] = im6[i,j,2]/255

for i in range (a):
    for j in range(b):
        c = (im6[i,j,0]+im6[i,j,1]+im6[i,j,2])/3
        im6[i,j,0] = c
        im6[i,j,1] = c
        im6[i,j,2] = c

plt.imshow(im6)
plt.show()

#for i in range (a):
    #for j in range(b):
        #c = 0.299*im6[i,j,0]+0.587*im6[i,j,1]+0.114*im6[i,j,2]
        #im6[i,j,0] = c
        #im6[i,j,1] = c
        #im6[i,j,2] = c

im63 = np.sqrt(im6)  #rend les teintes de gris plus claires


#im6 = im6.astype(int)    #rend l'image noire
plt.imshow(im6)
plt.show()

fig, axes = plt.subplots(1, 3)
axes[0, 0].plot(im63)
axes[0, 1].plot(im6)
axes[0, 2].plot(im6)
plt.show()