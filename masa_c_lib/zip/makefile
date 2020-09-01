OPZIONI_BASE=-Wall -g -c 
OPZIONI_LIBRERIA=-shared 
LDFLAGS=-lpthread -lrt
INCLUDE=-I./cereal/include -I./include

build_libreria: masa_python_c_lib.o 
	g++ ${OPZIONI_LIBRERIA} masa_python_c_lib.o ${INCLUDE} -o masa_python_c_lib.lib ${LDFLAGS}

masa_python_c_lib.o: masa_python_c_lib.cpp
	g++ ${OPZIONI_BASE} ${INCLUDE} masa_python_c_lib.cpp
