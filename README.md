# Masa Protocol Python

This is the python implementation of the masa protocol.
With this project you can send MASA objects from Python to C++ and viceversa.
In the demo directory there are both exemples for the python client and the python server where you cand 
see how to send and receive messages.
All the messages types and objects included in the original MASA_Protocol will be aded in the final version,
for now you can only create a MasaMessage with TrafficLight objects and RoadUser objects.
All these objects are Python native objects so you can use them in your python software.

To be clear:

You can send a MasaMessage from Python to a C++ server OR a Python server.
The receiving server could not see differenze since the Message will be converted into bytes before been sent.
So this is a 100% working binding between Python and C++!

##Run the code

First you have to build the masa_c_lib library whitch is the thing that makes everything possible.

In the folder run:

```
make clean
make -f makefile

```

Than all you have to do is to run the client/server from the demo folder or to create your own Python program 
including the MasaProtocol.py file from the python folder.

From the demo folder run:

```
python3 client.py

```

or

```
python3 server.py

```
