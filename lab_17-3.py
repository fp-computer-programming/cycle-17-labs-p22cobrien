# Author: CMOB 4/12/2022

from re import T


class TV_remote:
    """TV remote qualities"""
    def __init__(self, channel=0, volume=0, on=False) -> None:
        """ Sets the atributes for the remote """
        self.channel = channel
        self.volume = volume
        self.on = on

    def __str__(self):
        """ to str """
        return "The channel is set to {0}, the volume is set to {1}, and the power is {2}".format(self.channel, self.volume, self.on)

    

tv_remote1 = TV_remote()

print(tv_remote1)