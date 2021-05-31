import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
height = df["Height"].tolist()

height_mean = statistics.mean(height)
height_median = statistics.median(height)
height_mode = statistics.mode(height)
height_sd = statistics.stdev(height)

#print("mean,median,mode and standard deviation is {}, {}, {} and {}".format(height_mean, height_median, height_mode, height_sd))

height_first_sd_start, height_first_sd_end = height_mean - height_sd, height_mean + height_sd
height_second_sd_start, height_second_sd_end = height_mean -(2* height_sd), height_mean +(2* height_sd)
height_third_sd_start, height_third__sd_end = height_mean - (3* height_sd), height_mean +(3* height_sd)

height_list_of_data_within_one_sd = [result for result in height if result > height_first_sd_start and result < height_first_sd_end]
height_list_of_data_within_two_sd = [result for result in height if result > height_second_sd_start and result < height_second_sd_end]
height_list_of_data_within_three_sd = [result for result in height if result > height_third_sd_start and result < height_third__sd_end]

print("{}% of data for height lies within one standard deviation ".format(len(height_list_of_data_within_one_sd)*100.0/len(height)))
print("{}% of data for height lies within second standard deviation ".format(len(height_list_of_data_within_two_sd)*100.0/len(height)))
print("{}% of data for height lies within third standard deviation ".format(len(height_list_of_data_within_three_sd)*100.0/len(height)))

fig = ff.create_distplot([height], ["result"], show_hist= False)
fig.add_trace(go.Scatter(x = [height_mean, height_mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [height_first_sd_start, height_first_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter(x = [height_second_sd_start, height_second_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter(x = [height_third_sd_start, height_third_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 3"))
fig.show()