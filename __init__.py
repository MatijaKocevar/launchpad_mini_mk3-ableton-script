import Live
from .launchpad_mini_mk3 import launchpad_mini_mk3


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return launchpad_mini_mk3(c_instance)

# local variables:
# tab-width: 4
