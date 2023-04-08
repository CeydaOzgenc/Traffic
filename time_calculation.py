'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from detectors import Detectors
from license_plate import LicencePlate
detectors=Detectors()
licenceplate=LicencePlate()
detectors.detector_separation()
licenceplate.licence_plate_search()
class Time():
    def __init__(self):
        self.start_time=[]
        self.finish_time=[]
        self.measurement_date=[]
        self.count=len(licenceplate.twin_license_start_finish_time)
        self.licence_plate_time=licenceplate.twin_license_start_finish_time
        self.total_time_str=""
        self.total_cars=0
        self.total_time_minute=0
    def total_date_time(self):
        self.total_cars=len(detectors.detector_one)
        '''toplam araba sayisi aliniyor'''
        measurement_start_date = detectors.traffic_input[0].split("   ")
        measurement_finish_date = detectors.traffic_input[len(detectors.traffic_input) - 2].split("   ")
        for index in range(self.count+1):
            self.total_past_time(index,measurement_start_date,measurement_finish_date)
    def total_past_time(self,index,start_date,finish_date):
        if index==0:
            self.measurement_date = start_date[0]
            '''Baslangic tarihi aliniyor'''
            self.start_time = start_date[1]
            '''Baslangic saati aliniyor '''
            self.finish_time = finish_date[1]
            '''Bitis saati aliniyor '''
        else:
            self.start_time=licenceplate.twin_license_start_finish_time[index-1][1]
            '''arabanin detector_one'daki  start_time aktariliyor'''
            self.finish_time=licenceplate.twin_license_start_finish_time[index-1][2]
            '''arabanin detector_two'daki saati finish_time aktariliyor'''
        self.time_separation(index)
    def time_separation(self,index):
        self.start_time=self.start_time.split(":")
        self.start_hour = self.start_time[0]
        '''start_time'daki zamandan saat aliniyor start_hour'a aktariliyor'''
        self.start_minute=self.start_time[1]
        '''start_time'daki zamandan dakika aliniyor start_minute'e aktariliyor'''
        self.start_second=self.start_time[2]
        '''start_time'daki zamandan saniye aliniyor start_second'a aktariliyor'''
        self.finish_time=self.finish_time.split(":")
        self.finish_hour=self.finish_time[0]
        '''finish_time'daki zamandan saat iliniyor finish_hour'a aktariliyor'''
        self.finish_minute=self.finish_time[1]
        '''finish_time'daki zamandan dakika iliniyor finish_minute'e aktariliyor'''
        self.finish_second=self.finish_time[2]
        '''finish_time'daki zamandan saniye iliniyor finish_second'a aktariliyor'''
        self.time_differce(index)
    def time_differce(self,index):
        self.hour_differce=int(self.finish_hour)-int(self.start_hour)
        '''Saat araligi hour_differce aktariliyor'''
        self.minute_differce=int(self.finish_minute)-int(self.start_minute)
        '''Dakika araligi hour_differce aktariliyor'''
        self.second_differce=int(self.finish_second)-int(self.start_second)
        '''Saniye araligi hour_differce aktariliyor'''
        if index==0:
            if len(str(self.hour_differce))<2:
                self.hour_differce="0"+str(self.hour_differce)
            if len(str(self.minute_differce))<2:
                self.minute_differce="0"+str(self.minute_differce)
            if len(str(self.second_differce))<2:
                self.second_differce="0"+str(self.second_differce)
            self.total_time_str=str(self.hour_differce)+":"+str(self.minute_differce)+":"+str(self.second_differce)
            '''Toplam gecen zaman total_time_str'e saat, dakika ve saniye olarak aktariliyor'''
            self.time_calculation_minute()
        else:
            self.time_calculation(index)
    def time_calculation_minute(self):
        hour=int(self.hour_differce)*60
        '''Saat dakikaya cevriliyor'''
        second=int(self.second_differce)/60
        '''saniye dakikaya cevriliyor'''
        minute=int(self.minute_differce)
        self.total_time_minute=float(hour)+float(second)+float(minute)
        '''Toplam gecen dakika total_time_minute'e aktariliyor'''
    def time_calculation(self,index):
        self.minute_differce=int(self.minute_differce)*60
        '''Dakika saniyeye cevriliyor'''
        self.total_second=int(self.minute_differce)+int(self.second_differce)
        '''toplam saniye hesaplaniyor'''
        licenceplate.twin_license_start_finish_time[index-1][3]=self.total_second
        '''Toplam saniye twin_license_start_finish_time 3. dizesine aktariliyor'''
        self.licence_plate_time[index-1] =licenceplate.twin_license_start_finish_time[index-1]
        '''twin_license_start_finish_time'daki veriler licence_plate_time'e aktariliyor'''
