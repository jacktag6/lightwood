import unittest
from lightwood.encoder.text import RnnEncoder
import pandas as pd


class TestRnnEncoder(unittest.TestCase):
    @unittest.skip("Currently not using this encoder.")
    def test_encode_and_decode(self):
        sentences = ["Everyone really likes the newest benefits",
                     "The Government Executive articles housed on the website are not able to be searched",
                     "Most of Mrinal Sen 's work can be found in European collections . ",
                     "Would you rise up and defeaat all evil lords in the town ? ",
                     None

                     ]

        encoder = RnnEncoder(encoded_vector_size=10, train_iters=7500)
        encoder.prepare(pd.Series(sentences), pd.Series(sentences))
        encoder.encode(sentences)

        # test de decoder

        ret = encoder.encode(["Everyone really likes the newest benefits"])
        print('encoded vector:')
        print(ret)
        print('decoded vector')
        ret2 = encoder.decode(ret)
        print(ret2)
