import csv
import plotly.graph_objs as go

data = []
avg20 = []
avg50 = []
sum = 0
dates = []

with open('GME_StockData36Months.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

for i in range(49, len(data)):
    for j in range(0, 19):
        sum += float(data[i-j][4])

    avg20.append(sum/20)
    sum = 0

for i in range(49, len(data)):
    for j in range(0, 49):
        sum += float(data[i-j][4])

    avg50.append(sum/50)
    sum = 0

for i in range(49, len(data)):
    dates.append(data[i][0])

# create two traces
trace1 = go.Scatter(x=dates, y=avg20, mode='lines', name='20 Day Moving Average')
trace2 = go.Scatter(x=dates, y=avg50, mode='lines', name='50 Day Moving Average')

# create a figure with both traces
fig = go.Figure(data=[trace1, trace2])

# set the title of the plot
fig.update_layout(title='Moving Averages')

# display the plot
fig.show()
