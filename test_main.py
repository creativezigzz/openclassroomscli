import unittest
from unittest import TestCase
from main import get_address, get_googlemaps, many_client, find_to_db

class Test(TestCase):

    def test_get_address(self):
        client = ("C123","MEUNIER","Rue de la marquise","Namur")
        resultat = get_address(client)
        self.assertEqual("Rue de la marquise Namur", resultat)

    def test_get_googlemaps(self):
        addresse = "Rue de la baraque 123A LLN"
        resultat = get_googlemaps(addresse, "Lucas")
        self.assertEqual(1,resultat)

    def test_find_to_db(self):
        self.fail()

    def test_many_client(self):
        client = [("C123", "MEUNIER", "Rue de la marquise", "Namur"),
                  ("C222", "MEUNIER", "Grand Rue", "Liege")]
        resultat = many_client(client)
        self.assertEqual(("C123", "MEUNIER", "Rue de la marquise", "Namur"),resultat)
