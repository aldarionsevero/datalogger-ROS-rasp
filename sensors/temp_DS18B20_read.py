class DS18B20Read():

    """docstring for DS18B20_read"""

    def temp_from_device(self):
        tempfile = open("/sys/bus/w1/devices/28-001451f4e2ff/w1_slave")
        file_content = tempfile.read()
        tempfile.close()
        tempdata = file_content.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        temperature = temperature / 1000
        return temperature
