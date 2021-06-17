#Standard Error
import numpy as np
def main():
    prism_angle()
    mean_deviation()
def prism_angle():
    degree_reading = np.array([119,120,120,119,120,120,120,120,120,119,117,119])
    minute_reading = np.array([27,0,30,57,0,0,3,0,3,57,30,27])
    second_reading = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
    total_reading_seconds = np.array((degree_reading*60*60)+ (minute_reading*60))
    mean_reading = np.mean(total_reading_seconds)
    standard_deviation=(np.sum(((total_reading_seconds)-(mean_reading))**2))
    prism_angle=np.sqrt((standard_deviation)/(len(degree_reading)*(len(degree_reading)-1)))
    prism_angle_standard_error = np.radians(prism_angle/3600) 
    print("Standard Error in prism_angle: ",prism_angle_standard_error)
    return prism_angle_standard_error

def mean_deviation():
    degree_reading = np.array([37,37,37,37,37,38,37,37,38,38,37,37])
    minute_reading = np.array([27,24,57,48,57,51,54,51,9,31,39,30])
    second_reading = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
    total_reading_seconds = np.array((degree_reading*60*60)+ (minute_reading*60))
    mean_reading = np.mean(total_reading_seconds)
    standard_deviation=(np.sum(((total_reading_seconds)-(mean_reading))**2))
    mean_deviation=np.sqrt((standard_deviation)/(len(degree_reading)*(len(degree_reading)-1)))
    mean_deviation_standard_error=np.radians(mean_deviation/3600) 
    print("Standard Error in angle of minimum deviation is:",mean_deviation_standard_error) 
    return mean_deviation_standard_error

if __name__ == '__main__':
        main()
