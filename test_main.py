import unittest
from unittest import TestCase
from main import get_address, get_googlemaps, many_client, find_to_db


class Test(TestCase):

    def test_get_address(self):
        client = ("C123", "MEUNIER", "Rue de la marquise", "Namur")
        resultat = get_address(client)
        self.assertEqual("Rue de la marquise Namur", resultat)

    def test_get_googlemaps(self):
        addresse = "Rue de la baraque 123A LLN"
        resultat = get_googlemaps(addresse, "Lucas")
        self.assertEqual(1, resultat)

    def test_find_to_db(self):
        client_many = [("C123", "MERCIER", "25, r. Lemaitre", "Namur"),
                       ("D063", "MERCIER", "201, bvd du Nord", "Toulouse")]
        resultat_many = find_to_db("root", "Bdcamp2642.", ["MERCIER"], "test")
        client = [("F400", "JACOB", "78, ch. du Moulin", "Bruxelles")]
        resultat = find_to_db("root", "Bdcamp2642.", ["JACOB"], "test")
        self.assertEqual(client, resultat)
        self.assertEqual(client_many, resultat_many)

    def test_many_client(self):
        client = [("C123", "MEUNIER", "Rue de la marquise", "Namur"),
                  ("C222", "MEUNIER", "Grand Rue", "Liege")]
        resultat = many_client(client)
        self.assertEqual(("C123", "MEUNIER", "Rue de la marquise", "Namur"), resultat)


if __name__ == '__main__':
    unittest.main()
