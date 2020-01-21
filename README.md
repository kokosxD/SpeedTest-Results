# SpeedTest Results
---
Process [SpeedTest's](https://www.speedtest.net/ "SpeedTest") results and use them in your program
## Examples
```python
from speedtest import Results

path = "my_speedtest_results.csv"
r = Results(path)
print(r)
```
Output:
```
Ip:                     12.345.678.90
Download Speed:         102.84
Upload Speed:           8.6

Ip:                     12.345.678.90
Download Speed:         95.22
Upload Speed:           9.1

Ip:                     12.345.678.90
Download Speed:         96.09
Upload Speed:           8.2

......................................
......................................
......................................

Ip:                     12.345.678.90
Download Speed:         99.98
Upload Speed:           8.7

Ip:                     12.345.678.90
Download Speed:         105.41
Upload Speed:           10.1

Ip:                     12.345.678.90
Download Speed:         90.34
Upload Speed:           8.0
```
## More
```python
print(r[0])
# {
# 	'ip': '12.345.678.90',
# 	'time': datetime.datetime(2020, 12, 31, 12, 30),
# 	'time_zone': 'UTC',
# 	'download': 102.84,
# 	'upload': 8.6,
# 	'latency': 10,
# 	'server': 'SomeServer',
# 	'server_distance': 0,
# 	'mode': 'Multi'
# }

print(r[0]["download"])# or print(r.results[0]["download"])
# 102.84

# Save and Load
r.Save("results.pickle")

r = r.Load("results.pickle")
```
