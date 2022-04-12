# Author: CMOB 4/12/2022


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

    def turn_on(self):
        """ Turns the TV on """
        self.on = True

    def turn_off(self):
        """ Turns the TV off """
        self.on = False

    def increase_volume(self):
        """ Increases the TV's volume """
        self.volume += 1

    def decrease_volume(self):
        """ Decreases the TV's Volume """
        self.volume -= 1

    def channel_up(self):
        """ Changes the channel up by one """
        self.channel += 1

    def channel_down(self):
        """ Changes the channel down by one """
        self.channel -= 1



tv_remote1 = TV_remote()

print(tv_remote1)