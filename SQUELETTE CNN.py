import numpy as np
class CNN():
    def __init__(self, nb_filtres, pooling, image_shape, pas = 1, padding = "0", taille_filtre = 3, type_image=3):
        self.nb_filtres = nb_filtres
        self.taille_filtre = taille_filtre
        self.pas = pas
        self.type_image = type_image #image en couleur 3; N&B : 1 CANAL
        self.padding = padding #0 ou copie
        self.pooling = pooling #max, average
        self.image_shape = image_shape #un tuple (H,L,C) (Hauteur, Longueur, Canaux)

        self.filters = self.init_filters()
        self.biais = np.zeros(nb_filtres) #biais par filtre


    def init_filters(self):
        """

        :return: matrice 3x3xtype_image avec les poids
        """
        scale = 0.1 #pour pas que les poids soient trop grands
        nb_canaux = self.image_shape[2]
        return np.random.randn(self.nb_filtres,self.taille_filtre,self.taille_filtre,nb_canaux) * scale


    def convolution_operation(self, images, filtre, biais):
        """

        :return: retourne un chiffre après l'operation w.x+b w:poids, b:biais
        """
        # imageR * filtreR + imageB * filtreB + imageJ * filtreJ
        resultat = np.sum(images* filtre) + biais
        return resultat


    def fonction_activation(self, input):
        """
        input = convolution opération
        :return: f(w.x+b) w:poids, b:biais
        """
        return np.maximum(0, input)


    def convolution_couche(self, image):
        """
        image = matrice de pixels (ex: 32x32x3)
        1) activation du padding
        2) Dimension de sortie
        3) Envoyer nos calculs convolution_operaiton appliqué à la fonction d'activation sur la map
        :return: activation map même taille que l'image de base
        """
        #1 PADDING
        #p = (self.taille_filtre -1)//2 #adaptation à la taille des filtres
        image_padded = np.pad(image,
                              ((1, 1),  # Padding Haut/Bas (abscisses)
                               (1, 1),  # Padding Gauche/Droite (ordonnées)
                               (0, 0)),  # Pas de padding sur les Canaux (Axe 3) sinon ça rajoute 2 tableaux de 0 ce qui ferait 5 canaux
                              mode='constant',
                              constant_values=0)

        #2 DIMENSION DE SORTIE (même nombre de sorties que de filtres
        #H,L,C = self.image_shape
        image_sortie = np.zeros((self.image_shape[0], self.image_shape[1], self.nb_filtres))

        #3 BOUCLE
        H, L, C = self.image_shape
        for i in range(H):
            for j in range(L):
                patch = image_padded[i: i + self.taille_filtre,j: j + self.taille_filtre, :] #selection de ou on pose le filtre au début sur les pixels 1,2,3 * 1,2,3

                for f in range(self.nb_filtres): #application des filtres
                    valeur = self.convolution_operation(patch, self.filters[f], self.biais[f])
                    image_sortie[i, j, f] = valeur
        return self.fonction_activation(image_sortie)

    def convolution_block(self,image):
        """
        procède à la convolution plus le pulling
        :return: return les images après pulling
        """
        # 1  Convolution + Activation
        # Cette méthode renvoie une matrice de taille (H, L, nb_filtres)
        print(" Passage dans la couche de convolution")
        feature_maps = self.convolution_couche(image)

        # 2. Étape de Pooling (Réduction de dimension)
        # On passe de (H, L, nb_filtres) à (H/2, L/2, nb_filtres)
        print(f" Opération de {self.pooling} pooling")
        output = self.pooling_operation(feature_maps, size=2, methode=self.pooling)

        return output

    def pooling_operation(self, images, *, size=2, methode:"max"):
        """
        La fonction de pulling prends une certaine tialle de fenêtre et applique le pooling dessus
        :param images: Image prises en paramètres, qui possède N canal (H,L,N)
                        H: hauteur
                        L : longueur
        :param size:
        :param methode:
        :return: une image, avec une taille de (H/2, L/2, N)
        """
        H, L, C = images.shape

        pas = 2

        H_out = H // 2
        L_out = L // 2

        #Initialisation image de sortie
        output = np.zeros((H_out, L_out, C))

        for f in range(C): #on parcours chaque canal
            for i in range(H_out):
                for j in range(L_out):
                    start_i, start_j = i * pas, j * pas
                    patch = images[start_i:start_i + size, start_j:start_j + size, f]

                    # Application de l'opération selon le choix (Max ou Average)
                    if self.pooling == "max":
                        output[i, j, f] = np.max(patch)
                    else:  # average
                        output[i, j, f] = np.mean(patch)
        return output


test = np.ones((10,10))
print(test)
print(np.pad(test,(1,1),'constant'))












