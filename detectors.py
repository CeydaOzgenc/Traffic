'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
class Detectors:
    def __init__(self):
        self.traffic_input = open("traffic_input.txt").read().split("\n")
        ''' tirafik_input.txt icindeki veriler, traffic_input'un her dizisine bir satiri aktariyor '''
        self.detector_one=[]
        self.detector_two=[]
    def detector_separation(self):
        self.total_detector=self.traffic_input[2:len(self.traffic_input)-2:1]
        '''traffic_input dizisinin icinden sadece dedektor olan yerleri total_detector'e aktariliyor'''
        count_one = 0
        count_two = 0
        for index in range(len(self.total_detector)):
            if self.total_detector[index].split("\t")[0]=="1":
                '''Dedetor eger bir ise detector_one degerine satir ekleniyor'''
                self.detector_one.insert(count_one,self.total_detector[index].split("\t"))
                count_one+=count_one
            if self.total_detector[index].split("\t")[0] == "2":
                '''Dedetor eger iki ise detector_two degerine satir ekleniyor'''
                self.detector_two.insert(count_two,self.total_detector[index].split("\t"))
                count_two+=count_two