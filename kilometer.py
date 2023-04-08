'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from time_calculation import Time
time=Time()
time.total_date_time()
class Kilometer:
    def __init__(self):
        self.kilometer_arithmetic=0
        self.total_kilometer = 0
    def meter_calculation(self):
        for index in range(len(time.licence_plate_time)):
            self.licanse_plate_meter=(200*3600)/time.licence_plate_time[index][3]
            '''arabalarin saatte gittigi metre hesaplanip licanse_plate_meter'e ekleniyor'''
            time.licence_plate_time[index][4]=int(self.licanse_plate_meter/1000)
            '''licanse_plate_meter kilometreye cevrilip licence_plate_time 4. dizesine aktariliyor'''
            self.total_kilometer_arithmetic(index)
    def total_kilometer_arithmetic(self,index):
        self.total_kilometer+=time.licence_plate_time[index][4]
        if index==len(time.licence_plate_time)-1:
            self.kilometer_arithmetic= self.total_kilometer/10
            '''Butun arabalarin saate gittigi kilometrelerin aritmatik ortalamasini kilometer_arithmetic'e ekliyor'''
