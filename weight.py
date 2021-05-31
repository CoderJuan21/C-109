import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
weight = df["Weight"].tolist()

weight_mean = statistics.mean(weight)
weight_median = statistics.median(weight)
weight_mode = statistics.mode(weight)
weight_sd = statistics.stdev(weight)

#print("mean,median,mode and standard deviation is {}, {}, {} and {}".format(weight_mean, weight_median, weight_mode, weight_sd))

weight_first_sd_start, weight_first_sd_end = weight_mean - weight_sd, weight_mean + weight_sd
weight_second_sd_start, weight_second_sd_end = weight_mean -(2* weight_sd), weight_mean +(2* weight_sd)
weight_third_sd_start, weight_third__sd_end = weight_mean - (3* weight_sd), weight_mean +(3* weight_sd)

weight_list_of_data_within_one_sd = [result for result in weight if result > weight_first_sd_start and result < weight_first_sd_end]
weight_list_of_data_within_two_sd = [result for result in weight if result > weight_second_sd_start and result < weight_second_sd_end]
weight_list_of_data_within_three_sd = [result for result in weight if result > weight_third_sd_start and result < weight_third__sd_end]

print("{}% of data for weight lies within one standard deviation ".format(len(weight_list_of_data_within_one_sd)*100.0/len(weight)))
print("{}% of data for weight lies within second standard deviation ".format(len(weight_list_of_data_within_two_sd)*100.0/len(weight)))
print("{}% of data for weight lies within third standard deviation ".format(len(weight_list_of_data_within_three_sd)*100.0/len(weight)))

fig = ff.create_distplot([weight], ["result"], show_hist= False)
fig.add_trace(go.Scatter(x = [weight_mean, weight_mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [weight_first_sd_start, weight_first_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter(x = [weight_second_sd_start, weight_second_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter(x = [weight_third_sd_start, weight_third_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 3"))
fig.show()