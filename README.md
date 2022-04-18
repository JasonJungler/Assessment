# Assessment
> This program uses 4 processes with socket/pipe/shared_memory for IPC. The Server process will monitor keyboard input from the user, and send the data to all Client processes.

## Program Usage
```bash
python server.py
```

## Expected Output
```shell
Client1 is ready
Client2 is ready
Client3 is ready
Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values.
>> 1 5 5 10 15 2 3
Mean is 5.8571428571429
Median is 5
Mode is 5
```
## Notes
- environment
  - python 3.8+
  - tested @windows 10/python 3.8.10

- server.py
  - Executes 3 client process applying different IPC methods
