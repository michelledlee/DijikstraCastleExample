import abc

class BooStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def boo(self):
        """Required Method"""

class LoudBooStrategy(BooStrategyAbstract):
    def boo(self):
        print(self.__class__.__name__, "BOO!!")

class GentleBooStrategy(BooStrategyAbstract):
    def boo(self):
        print(self.__class__.__name__, "boo!")

class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def lights_on(self):
        """Required Method"""

class BrightLightsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print(self.__class__.__name__, "Lights are on, hide!")
