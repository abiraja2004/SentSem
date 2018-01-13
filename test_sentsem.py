# ----------------------------------------------------------------------------
# File Name: test_sentsem.py
# Purpose: Provide some testing cases for sentsem.py
#
# License: Apache License 2.0
#
# Created: 01/12/2018
# Author: Konstantinos Oikonomou, kons.oikonomou@gmail.com
#
from unittest import TestCase


# ----------------------------------------------------------------------------
class TestSentsem(TestCase):
    def test_equal(self):
        from sentsem import sentsem

        sent1 = 'Hello, I like playing football!'
        sent2 = 'Hello, I like playing football!'
        self.assertEqual(sentsem(sent1, sent2), 1.0)

    def test_similar(self):
        from sentsem import sentsem

        sent1 = 'Hello, I like playing football!'
        sent2 = 'Greetings, I love playing football!'

        pass_case = sentsem(sent1, sent2) > 0.5

        self.assertTrue(pass_case)

    def test_not_similar(self):
        from sentsem import sentsem

        sent1 = 'Hello, the sun shines playfully!'
        sent2 = 'Good morning, I love pizza'

        pass_case = sentsem(sent1, sent2) > 0.5

        self.assertFalse(pass_case)

    def test_inverse_sents(self):
        from sentsem import sentsem

        sent1 = 'Hello, I like playing football!'
        sent2 = 'Greetings, I love playing football!'

        self.assertAlmostEqual(sentsem(sent2, sent1), sentsem(sent1, sent2), delta=0.1)

    def test_lower_first(self):
        from sentsem import sentsem

        sent1 = 'Hello, I like football'
        sent2 = 'Greetings, I love playing football!'

        pass_case = sentsem(sent1, sent2) > 0.4
        self.assertTrue(pass_case)

    def test_not_in_vocab(self):
        from sentsem import sentsem

        sent1 = 'I need the email of tuition department'
        sent2 = 'I want to email the tuition department'

        pass_case = sentsem(sent1, sent2) > 0.5
        self.assertTrue(pass_case)
