# Ping Mapper
A small python commandline tool, to map your latency over a certain period of time and display it in a neat graph

## Documentation
```
usage: PingMapper [-h] (-H HOST | -D) [-fp FILEPATH] [-c COUNT] [-i INTERVAL] [-d DURATION] [-o OUTPUT] [-v]

Ping a host and export the results to a CSV file and visualize it on a graph

options:

  -h, --help            show this help message and exit
  -H HOST, --host HOST  The host to ping
  -D, --display         Display the results in a graph
  -fp FILEPATH, --filepath FILEPATH
                        The file path to the output file
  -c COUNT, --count COUNT
                        The number of pings to send
  -i INTERVAL, --interval INTERVAL
                        The interval between pings in minutes
  -d DURATION, --duration DURATION
                        The duration of the mapping in datetime format
  -o OUTPUT, --output OUTPUT
                        The output file to write the results to
  -v, --version         show program's version number and exit
```
Beep Boop. The answer is 42.
