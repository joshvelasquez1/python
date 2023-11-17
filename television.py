class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__old_value = 0

    def power(self):
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__old_value
            else:
                self.__old_value = self.__volume
                self.__muted = True
                self.__volume = self.MIN_VOLUME
        else:
            pass

    def channel_up(self):
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self):
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__old_value
                if self.__volume == self.MAX_VOLUME:
                    self.__volume = self.MAX_VOLUME
                else:
                    self.__volume += 1
            else:
                if self.__volume == self.MAX_VOLUME:
                    self.__volume = self.MAX_VOLUME
                else:
                    self.__volume += 1
        else:
            pass

    def volume_down(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__old_value
                if self.__volume == self.MIN_VOLUME:
                    self.__volume = self.MIN_VOLUME
                else:
                    self.__volume -= 1
            else:
                if self.__volume == self.MIN_VOLUME:
                    self.__volume = self.MIN_VOLUME
                else:
                    self.__volume -= 1
        else:
            pass

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
