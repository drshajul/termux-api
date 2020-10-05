from . import scrip as t

class sensor:
    '''
    This is a class that lets to view
    sensor data directly from your android device.
    '''
    def __init__(self):
        pass

    def listSensor(self):
        '''
        lists available sensors on the device.
        '''
        self.value=t.compute("termux-sensor -l")
        return self.value["output"]

    def cleanup(self):
        '''
        Performs cleanup releasing sensor resources.
        '''
        self.clean=t.compute("termux-sensor -c")
        return self.clean["output"]

    def delay(self,*args,delayvalue=3000):
        '''
        Method to delay time in milliseconds
        on receiving every new sensor update.
        Arguments:
        sensorname: takes strings of sensor name
        delayvalue=3000(default)(delayed by 3 sec)

        Example:
        .delay("Gravity","RMD") gives 3 sec delay output
        but,
        .delay("Gravity",5000) causes error for giving the delay
        give like this:
        .delay("Gravity",delayvalue=5000)
        '''
        sensorname=tuple(args)
        if not sensorname:
            return "Give at least one sensor name. For finding sensor name call listSensor method"
        else:
            self.delayvalue=delayvalue
            sensor_names=""
            for sensor_name in sensorname:
                sensor_names=sensor_names+sensor_name+","
        
            sensor_names.replace("\'","")              
            self.delayv=t.liveSave(f"termux-sensor -s {sensor_names} -d {self.delayvalue}")
    
        

    def specificSensors(self,*args):
        '''
        This is a method to print specific 
        sensor(s) data.
        Argument is either a single sensor
        or multiple sensors.
        '''
        sname=tuple(args)
        if not sname:
            return "Give at least one sensor name. For finding sensor name call listSensor method"
        else:
            sensornames=""
            for sensorname in sname:
                sensornames=sensornames+sensorname+","      
            
            sensornames.replace("\'","")
            self.delayval=t.liveSave(f"termux-sensor -s {sensornames}")


    def allsensors(self):
        '''
        Method to print sensor data all at once.
        WARNING: Can cause over load to the device.
        '''
        self.show=t.liveSave("termux-sensor -a")


