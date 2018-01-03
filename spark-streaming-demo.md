# Demo Spark Streaming

## Python client

`ipython` to launch a client, then type the following commands :

```python
import nclib

nc = nclib.Netcat(listen=('localhost', 9999), verbose=True)

# before going further, spawn a Spark Streaming

for i in range(100):
    nc.send_line(b'hello world')

nc.close()
```

## Spark streaming server

`invoke launchSparkStreaming`

or from root directory :

```
.\bin\spark\bin\spark-submit .\bin\spark\examples\src\main\python\sql\streaming\structured_network_wordcount.py localhost 9999
```
