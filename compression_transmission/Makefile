# dragino lora testing
# Single lora testing app

CC=g++
CFLAGS=-c -Wall -std=c++11
LIBS=-lwiringPi

all: dragino_lora_app

dragino_lora_app: data_transfer.o
	$(CC) data_transfer.o  $(LIBS) -o data_transfer

data_transfer.o: data_transfer.cpp
	$(CC) $(CFLAGS) data_transfer.cpp

clean:
	rm *.o data_transfer
