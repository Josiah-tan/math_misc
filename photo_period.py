#link to formulas: https://www.esrl.noaa.gov/gmd/grad/solcalc/solareqns.PDF
import matplotlib.pyplot as plt
import math 
class Photoperiod:
    def __init__(self, jday, hr, offset, latitude, longitude):
        """
        parameters:
            -- jday: number of days, resets every year (not month)
            -- hr: set as 24 as default
            -- latitude and longitude (degrees) 
                -- note south should be negative
        """
        self.jday = jday
        self.hr = hr
        self.offset = offset
        self.latitude = latitude * math.pi / 180 
        self.longitude = longitude * math.pi / 180

        self._y = None
        self._declin = None
        self._ha = None
        self._day_len = None

    @classmethod
    def brookstead(cls, jday, hr):
        return cls(jday = jday, hr = hr, offset = 10, latitude = -27.7, longitude = 151.4) 
    @classmethod
    def gatton(cls, jday, hr):
        return cls(jday = jday, hr = hr, offset = 10, latitude = -27.5, longitude = 152.3) 
    @classmethod
    def hobart(cls, jday, hr):
        return cls(jday = jday, hr = hr, offset = 10, latitude = -42.8821, longitude = 147.3272) 
    @classmethod
    def japan(cls, jday, hr):
        return cls(jday = jday, hr = hr, offset = 10, latitude = 35, longitude = 135) 

    @property
    def y(self):
        """
        calculates the fractional year (radians)
        """
        if self._y is None:
            self._y = (2 * math.pi / 365 * (self.jday - 1 + (self.hr - 12) /24))
        return self._y

    @property
    def declin(self):
        """
        returns the solar declination angle (radians)
        """
        if self._declin is None:
            self._declin = 0.006918-0.399912*math.cos(self.y)+0.070257*math.sin(self.y)-0.006758*math.cos(2*self.y)+0.000907*math.sin(2*self.y)-0.002697*math.cos(3*self.y)+0.00148*math.sin(3*self.y)
        return self._declin

    @property
    def ha(self):
        """
        returns the solar hour angle (degrees)
        """
        if self._ha is None:
            self._ha = math.acos(math.cos(math.pi / 180 * 90.833) /(math.cos(self.latitude)*math.cos(self.declin)) - math.tan(self.latitude)*math.tan(self.declin))
        return self._ha * 180 / math.pi 

    @property
    def day_len(self):
        """
        returns the photoperiod day length (hours)
        """
        if self._day_len is None:
            self._day_len = 2 * self.ha/ (15);
        return self._day_len

    @staticmethod
    def data_year(obj):
        """ 
        obtain data for a year
        returns -- photoperiod_lis: a list containing photoperiods from days 1 to 365
        """
        photoperiod_lis = []
        for i in range(1, 366):
            photoperiod = obj(i, 24)
            photoperiod_lis.append(photoperiod.day_len)
        return photoperiod_lis


brookstead_photoperiod = Photoperiod.data_year(Photoperiod.brookstead) 
gatton_photoperiod = Photoperiod.data_year(Photoperiod.gatton) 
hobart_photoperiod = Photoperiod.data_year(Photoperiod.hobart)
japan_photoperiod = Photoperiod.data_year(Photoperiod.japan)

"""
plt.plot(brookstead_photoperiod, label = "brookstead")
plt.plot(gatton_photoperiod, label = "gatton")
plt.plot(hobart_photoperiod, label = "hobart")
plt.plot(japan_photoperiod, label = "japan")
plt.legend()
plt.show()
"""

plt.figure()
plt.boxplot([brookstead_photoperiod, gatton_photoperiod], labels = ["Brookstead", "Gatton"])
plt.show()
