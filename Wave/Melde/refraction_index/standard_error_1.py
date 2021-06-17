#Standard Error
import numpy as np
degree_reading = np.array([30,35,40
minute_reading = np.array([27,0,30,57,0,0,3,0,3,57,30,27])
second_reading = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
total_reading_seconds = np.array((degree_reading*60*60)+ (minute_reading*60))
mean_reading = np.mean(total_reading_seconds)
print(total_reading_seconds)
