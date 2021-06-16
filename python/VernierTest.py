from Persistence import Persistence
from V_CO2 import V_CO2
from time import sleep
from LogUtil import Logger

class VernierTest(object):

    def __init__(self):
        """Record optional sensor data
        Args:
            lvl: Logging level
        Returns:
            None
        Raises:
            None
        """        
        self._test=False
        self._logger = Logger("Vernier Test", Logger.INFO)
        self._persist = Persistence(self._logger)
        self._co2 = V_CO2(self._logger)
        self._logger.info("Initialized Vernier Test")
            
    def readVernier(self):
        """Record Vernier CO2 sensor
            Generates co2, temperature and relative humidity
        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        co2 = None
        temp = None
        rh = None
        try:
            data = self._co2.read()
            if data is None:
                self._logger.debug("No data for V_CO2")
                return co2, temp, rh
            
            co2 = data[0]
            temp = data[1]
            rh = data[2]

            status = 'Success'
            if self._test:
                status = 'Test'
            c_rec = ['Environment_Observation', '', 'Top', 'Air', 'CO2', "{:10.1f}".format(co2), 'ppm', 'V_CO2', status, '']
            t_rec = ['Environment_Observation', '', 'Top', 'Air', 'Temperature', "{:10.1f}".format(temp), 'Centigrade', 'V_CO2', status, '']
            h_rec = ['Environment_Observation', '', 'Top', 'Air', 'Humidity', "{:10.1f}".format(rh), 'Percent', 'V_CO2', status, '']            
            self._persist.save(c_rec)
            self._persist.save(t_rec)
            self._persist.save(h_rec)            
        except Exception as e:
            status = 'Failure'
            if self._test:
                status = 'Test'
            c_rec = ['Environment_Observation', '', 'Top', 'Air', 'CO2', '', 'ppm', 'V_CO2', status, str(e)]
            t_rec = ['Environment_Observation', '', 'Top', 'Air', 'Temperature', '', 'Centigrde', 'V_CO2', status, '']
            h_rec = ['Environment_Observation', '', 'Top', 'Air', 'Humidity', '', 'Percent', 'V_CO2', status, '']
            self._persist.save(c_rec)
            self._persist.save(t_rec)
            self._persist.save(h_rec)            

        return co2, temp, rh

    
def test():
    '''
        Function that should get called from scripts
    '''    
    t = VernierTest()
    t._logger.setLevel(Logger.DEBUG)
    while True:
        co2, temp, rh = t.readVernier()
        print('Co2: %s, Temp: %s, Humidity: %s'.format(co2, temp, rh))
        sleep(3)
        
if __name__=="__main__":
    test()    
