from tcppinglib import tcpping
import argparse
import datetime
import time
import os


parser = argparse.ArgumentParser(
    prog='PingMapper',
    description='Ping a host and export the results to a CSV file and visualize it on a graph',
    epilog='Beep Boop. The answer is 42.'
    )

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-H', '--host', help='The host to ping')
group.add_argument('-D', '--display', help='Display the results in a graph', action='store_true')
parser.add_argument('-fp', '--filepath', help='The path to the folder with the files you want to display, default is maps\
                        Tool will display all files in folder and you will be able to choose', default='maps/')
parser.add_argument('-c', '--count', help='The number of pings to send', default=5)
parser.add_argument('-i', '--interval', help='The interval between pings in minutes')
parser.add_argument('-d', '--duration', help='The duration of the mapping in datetime format')
parser.add_argument('-o', '--output',help='The output file to write the results to', default='maps/')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

if args.display:
    import matplotlib.pyplot as plt
    import pandas as pd
    
    filepaths = os.listdir(args.filepath)
    for index, filepath in enumerate(filepaths):
        print(f'{index+1}. {filepath}')
    
    fileinput = input('Enter the number of the file you want to display: ')
    
    df = pd.read_csv(f'{args.filepath}{filepaths[int(fileinput)-1]}')
    
    plt.figure(figsize=(12, 6))
    plot = plt.plot(df['Time'], df['Avg_time'], marker='o', color='b')
    plt.title(f'Average Latency of {filepaths[int(fileinput)-1]}')
    plt.xlabel('Time')
    plt.ylabel('Average Latency (ms)')
    plt.grid(True)
    plt.xticks(rotation=25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
    plt.text(0.5, 0.95, 'any-company.de', transform=plt.gca().transAxes, ha='center')
    plt.show()
    
    
else:

    interval = float(args.interval) * 60

    hours, minutes, seconds = args.duration.split(':')

    endtime = datetime.datetime.now() + datetime.timedelta(seconds=int(seconds), minutes=int(minutes), hours=int(hours))

    print(f'Pinging {args.host} {args.count} times with an interval of {args.interval} minutes until {endtime}')

    with open(f'{args.output}LatencyOf{str(args.host).upper()}.csv', 'w') as f:
        f.write('Time,Is_alive,Min_time,Max_time,Avg_time,Std_dev,pct_loss\n')

    while datetime.datetime.now() < endtime:
        with open(f'{args.output}LatencyOf{str(args.host).upper()}.csv', 'a') as f:
            response = tcpping(args.host, count=int(args.count))
            f.write(f'{datetime.datetime.now()},{response.is_alive},{response.min_rtt},{response.max_rtt},{response.avg_rtt},{response.stddev_rtt},{response.packet_loss}\n')
        time.sleep(interval)
