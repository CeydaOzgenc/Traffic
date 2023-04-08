'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from license_plate import LicencePlate
from kilometer import *
license=LicencePlate()
license.licence_plate_search()
license.between_two_sensors()
time=Time()
time.total_date_time()
kilometer=Kilometer()
kilometer.meter_calculation()
print("This measurement took place on "+ str(time.measurement_date) +" and took "+ time.total_time_str+".")
print("During this measurement "+ str(time.total_cars)+" cars passed both sensors(average " +str(time.total_cars/time.total_time_minute)+ " per minute)\n")
print("The following cars went over the speed limit:")
for index in range(len(time.licence_plate_time)):
    if time.licence_plate_time[index][4]>50:
        print(str(time.licence_plate_time[index][0])+" - "+str(time.licence_plate_time[index][4])+" km/h - "+str(time.licence_plate_time[index][2]))
print("\nThe average speed of all cars during this measurement "+str(kilometer.kilometer_arithmetic)+" is km/h.\n")
print("The following cars are currently between the two sensors:")
for index in range (len(license.sensor_between_car)):
    print(license.sensor_between_car[index][2])