'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from detectors import Detectors
detectors=Detectors()
detectors.detector_separation()
class LicencePlate:
    def __init__(self):
        self.twin_license_plate=[]
        self.sensor_between_car=[]
    def licence_plate_search(self):
        for index1 in range(len(detectors.detector_one)):
            for index2 in range(len(detectors.detector_two)):
                if detectors.detector_one[index1][2]==detectors.detector_two[index2][2]:
                    self.twin_license_plate.insert(0, detectors.detector_one[index1][2])
                    self.twin_license_plate.insert(1, detectors.detector_one[index1][1])
                    self.twin_license_plate.insert(2, detectors.detector_two[index2][1])
                    '''detector_one ile detector_two'da bulunan ayni plakalarin twin_license_plate'e plaka 
                    detector_one'deki tarih ve detector_two'daki tarih olarak twin_license_plate'e eklendi'''
        lenght=len(self.twin_license_plate)/3
        count1=-1
        count2=1
        self.twin_license_start_finish_time= [[0 for x in range(5)] for y in range(int(lenght))]
        '''ic ice bir dizi olusturuluyor'''
        for index in range(len(self.twin_license_plate)):
            if index%3==0:
                count1+=1
            count2=index%3
            self.twin_license_start_finish_time[count1][count2]=self.twin_license_plate[index]
            '''twin_license_start_finish_time dizesinin icinde plaka, detector_one'deki tarih ve 
            detector_two'daki tarih dize olarak eklendi'''
    def between_two_sensors(self):
        count=0
        for index1 in range(len(detectors.detector_one)):
            for index2 in range(len(self.twin_license_start_finish_time)):
                if detectors.detector_one[index1][2]==(self.twin_license_start_finish_time[index2][0]):
                    count+=1
        self.sensor_between_car=detectors.detector_one[:len(detectors.detector_one)-count:1]
        '''detector_one'da olup detector_two'da olmayan yani iki dedektor arasinda kalan arabalar sensor_between_car dizesine ekleniyor'''