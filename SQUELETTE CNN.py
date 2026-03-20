import numpy as np
class CNN():
    def __init__(self, nb_filtres, pooling, input_shape, pas = 1, padding = "0", taille_filtre = 3, type_image=3):
        self.nb_filtres = nb_filtres
        self.taille_filtre = taille_filtre
        self.pas = pas
        self.type_image = type_image #image en couleur 3; N&B : 1 CANAL
        self.padding = padding #0 ou copie
        self.pooling = pooling #max, average
        self.input_shape = input_shape

        self.filters = self.init_filters()
        self.bias = np.zeros(nb_filtres)


    def init_filters(self, nb_filtres, taille_filtre, type_image ):
        """

        :return: matrice 3x3xtype_image avec les poids
        """
        pass

    def convolution_operation(self, images):
        """

        :return: retourne un chiffre après l'operation w.x+b w:poids, b:biais
        """

        pass

    def fonction_activation(self, x):
        """

        :return: f(w.x+b) w:poids, b:biais
        """
        pass

    def convolution_couche(self, image):
        """

        :return: activation map même taille que l'image de base
        """

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














