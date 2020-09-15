OPZIONI_BASE=-Wall -g -c -fPIC
OPZIONI_LIBRERIA=-shared 
LDFLAGS=-lpthread -lrt
INCLUDE=-I./cereal/include -I./include

build_libreria: masa_python_c_lib.o 
	g++ -o masa_python_c_lib.lib ${INCLUDE} ${OPZIONI_LIBRERIA} masa_python_c_lib.o ${LDFLAGS}

masa_python_c_lib.o: masa_python_c_lib.cpp
	g++ ${OPZIONI_BASE} ${INCLUDE} masa_python_c_lib.cpp
	
clean:
	rm -f *.lib *.o
