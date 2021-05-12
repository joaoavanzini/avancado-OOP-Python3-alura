#Classes abstratas

from abc import ABC #abstract base classes

from collections.abc import MutableSequence
from numbers import Complex
# class Playlist(MutableSequence):
#     pass

class Numero(complex):
    def __getitem__(self, item):
        super().__getitem__()

#filmes = Playlist()

numeros = Numero()