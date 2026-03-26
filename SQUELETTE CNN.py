import numpy as np
class CNN():
    def __init__(self, nb_filtres, pooling, image_shape, pas = 1, padding = "0", taille_filtre = 3, type_image=3):
        self.nb_filtres = nb_filtres
        self.taille_filtre = taille_filtre
        self.pas = pas
        self.type_image = type_image #image en couleur 3; N&B : 1 CANAL
        self.padding = padding #0 ou copie
        self.pooling = pooling #max, average
        self.image_shape = image_shape

        self.filters = self.init_filters()
        self.biais = np.zeros(nb_filtres)


    def init_filters(self):
        """

        :return: matrice 3x3xtype_image avec les poids
        """
        scale = 0.1 #pour pas que les poids soient trop grands
        return np.random.randn(self.nb_filtres,self.taille_filtre,self.taille_filtre,self.type_image) * scale


    def convolution_operation(self, images, filtre):
        """

        :return: retourne un chiffre après l'operation w.x+b w:poids, b:biais
        """
        # imageR * filtreR + imageB * filtreB + imageJ * filtreJ
        resultat = np.sum(image_patch * filtre) + self.biais
        return resultat


    def fonction_activation(self, input):
        """
        input = convolution opération
        :return: f(w.x+b) w:poids, b:biais
        """
        return np.maximum(0, input)


    def convolution_couche(self, image ):
        """
        1) activation du padding
        2) Dimension de sortie
        3) Envoyer nos calculs convolution_operaiton appliqué à la fonction d'activation sur la map
        :return: activation map même taille que l'image de base
        """
        #1 PADDING
        p = (self.taille_filtre -1)//2 #adaptation à la taille des filtres
        image_padded = np.pad(image,
                              ((1, 1),  # Padding Haut/Bas (abscisses)
                               (1, 1),  # Padding Gauche/Droite (ordonnées)
                               (0, 0)),  # Pas de padding sur les Canaux (Axe 3) sinon ça rajoute 2 tableaux de 0 ce qui ferait 5 canaux
                              mode='constant',
                              constant_values=0)

        #2 DIMENSION DE SORTIE (même nombre de sorties que de filtres
        H,L,C = self.image_shape
        H_out = int((H + 2 * p - self.taille_filtre) / self.pas) + 1
        L_out = int((L + 2 * p - self.taille_filtre) / self.pas) + 1
        image_sortie = np.zeros((H_out, L_out, self.nb_filtres))



        pass

    def convolution_block(self,image):
        """
        procède à la convolution plus le pulling
        :return: return les images après pulling
        """
        pass

    def pooling_operation(self, images, *, size=2, methode:"MAX"):
        """
        La fonction de pulling prends une certaine tialle de fenêtre et applique le pooling dessus
        :param images: Image prises en paramètres, qui possède N canal (H,L,N)
                        H: hauteur
                        L : longueur
        :param size:
        :param methode:
        :return: une image, avec une taille de (H/2, L/2, N)
        """
        pass

test = np.ones((10,10))
print(test)
print(np.pad(test,(1,1),'constant'))












