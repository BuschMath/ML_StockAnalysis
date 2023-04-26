import csv
import plotly.graph_objs as go

data = []
avg20 = []
avg50 = []
sum = 0
dates = []
closePrice = []
avg20Greater = False
dateCrosses = []

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
    closePrice.append(data[i][4])

# create two traces
trace1 = go.Scatter(x=dates, y=avg20, mode='lines', name='20 Day Moving Average')
trace2 = go.Scatter(x=dates, y=avg50, mode='lines', name='50 Day Moving Average')
trace3 = go.Scatter(x=dates, y=closePrice, mode='lines', name='Closing Price')

# create a figure with both traces
fig = go.Figure(data=[trace1, trace2, trace3])

# set the title of the plot
fig.update_layout(title='Moving Averages')

# display the plot
fig.show()

if avg20[0] > avg50[0]:
    avg20Greater = True
else:
    avg20Greater = False

for i in range(1, len(avg20)):
    if avg20Greater:
        if avg20[i] < avg50[i]:
            avg20Greater = False
            dateCrosses.append([dates[i], avg20Greater, closePrice[i]])

    elif avg20[i] > avg50[i]:
        avg20Greater = True
        dateCrosses.append([dates[i], avg20Greater, closePrice[i]])   

print(dateCrosses)