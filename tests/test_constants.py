import numpy as np

from simple_functions import constants


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = constants.pi(2)
        assert np.isclose(my_pi, np.pi, atol=1e-12)
