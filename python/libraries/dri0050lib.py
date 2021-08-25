# -*- coding: utf-8 -*-


import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu



class DRI0050:

    __PORT="COM12" #windows平台
    #PORT=“/dev/ttyUSB0” #Linux平台
    __BAUDRATE=9600
    __SLAVE_ADDR=0x32

    __PID_REG       =  0x00
    __VID_REG       =  0x01
    __ADDR_REG      =  0x02
    __VER_REG       =  0x05
    __DUTY_REG      =  0x06
    __FREQ_REG      =  0x07
    __PWM_EN_REG    =  0x08

    def __init__(self,port,baudrate=9600,slave_addr=0x32):
        self.__PORT=port
        self.__BAUDRATE=baudrate
        self.__SLAVE_ADDR=slave_addr
        self.ser = serial.Serial(port=self.__PORT,baudrate=self.__BAUDRATE, bytesize=8, parity='N', stopbits=1)
        self.master = modbus_rtu.RtuMaster(self.ser)
        time.sleep(0.5)

    def get_pid(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__PID_REG, 1)
        time.sleep(0.03)
        return data[0]

    def get_vid(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__VID_REG, 1)
        time.sleep(0.03)
        return data[0]

    def get_addr(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__ADDR_REG, 1)
        time.sleep(0.03)
        return data[0]

    def get_version(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__VER_REG, 1)
        time.sleep(0.03)
        return data[0]

    def get_duty(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__DUTY_REG, 1)
        time.sleep(0.03)
        return data[0]/255

    def get_freq(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__FREQ_REG, 1)
        time.sleep(0.03)
        return int(12*1000*1000/256/(data[0]+1))

    def get_enable(self):
        data = self.master.execute(self.__SLAVE_ADDR, cst.READ_HOLDING_REGISTERS, self.__PWM_EN_REG, 1)
        time.sleep(0.03)
        return data[0]

    def set_duty(self,duty):
        self.master.execute(self.__SLAVE_ADDR, cst.WRITE_SINGLE_REGISTER, self.__DUTY_REG, output_value=int(duty*255))
        time.sleep(0.03)

    def set_freq(self,freq):
        self.master.execute(self.__SLAVE_ADDR, cst.WRITE_SINGLE_REGISTER, self.__FREQ_REG, output_value=int(12*1000*1000/256/freq) - 1)
        time.sleep(0.03)

    def set_enable(self,enable):
        self.master.execute(self.__SLAVE_ADDR, cst.WRITE_SINGLE_REGISTER, self.__PWM_EN_REG, output_value=enable)
        time.sleep(0.03)

    def pwm(self,freq, duty):
        v=[]
        v.append(int(duty*255))
        v.append(int(12*1000*1000/256/freq) - 1)
        self.master.execute(self.__SLAVE_ADDR, cst.WRITE_MULTIPLE_REGISTERS, self.__DUTY_REG, output_value=v)
        time.sleep(0.03)






