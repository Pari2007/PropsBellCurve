from os import stat
import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
reading_score= df["reading score"].to_list() 


reading_score_mean = statistics.mean(reading_score)


reading_score_median = statistics.median(reading_score)

reading_score_mode = statistics.mode(reading_score)


reading_score_std_deviation = statistics.stdev(reading_score)


# reading_score
first_std_deviation_start_reading_score, first_std_deviation_end_reading_score = reading_score_mean-reading_score_std_deviation, reading_score_mean+reading_score_std_deviation
second_std_deviation_start_reading_score,second_std_deviation_end_reading_score = reading_score_mean-(2*reading_score_std_deviation),reading_score_mean+(2*reading_score_std_deviation)
third_std_deviation_start_reading_score, third_std_devaition_end_reading_score = reading_score_mean-(3*reading_score_std_deviation),reading_score_mean+(3*reading_score_std_deviation)



reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score if result > first_std_deviation_start_reading_score and result < first_std_deviation_end_reading_score]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score if result > second_std_deviation_start_reading_score and result < second_std_deviation_end_reading_score]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score if result > third_std_deviation_start_reading_score and result < third_std_devaition_end_reading_score]

#Printing data for reading_score and weight (Standard Deviation)
print("{}% of data for reading_score lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score)))
print("{}% of data for reading_score lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score)))
print("{}% of data for reading_score lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score)))


