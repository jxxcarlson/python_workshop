
Webservers
==========

This folder contains some simple web servers.

server.py
---------

Run this server with `python server.py` and point your
browser to localhost:8000.  You will receive a
clickable directory listing for files in the root
of `server.py`

server2.py
----------

Run as `./server2.py 8000`.  Be sure that you have
run `chmod u+x server2.py` to make this file executable.
Point your browser to `localhost:8000`.  You will receive
the reply "I don't understand." Now try `localhost:8000/data`.
You will receive the reply "[1,2,3,4]" -- this is some
wired-in dummy data.

NOTE: you can also work from the command line:

```
$ curl http://localhost:8000
  I don't understand
$ curl http://localhost:8000/data
  [1,2,3,4]
 ```  

Server2 can be modified to read the data from a file in the
root of the server, e.g., "data".  Another application can    write
data to this file. In this way you have built a custom
data server.

server3.py
----------

This server is as in `server2.py`, except that the data to be served resides
in the file `data.text` in the root of the server.
