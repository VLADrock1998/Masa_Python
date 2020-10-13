BASE_OPTIONS=-Wall -g -c -fPIC
LIB_OPTIONS=-shared 
LDFLAGS=-lpthread -lrt
INCLUDE=-I./cereal/include -I./include

build_lib: masa_python_c_lib.o 
	g++ -o masa_python_c_lib.lib ${INCLUDE} ${LIB_OPTIONS} masa_python_c_lib.o ${LDFLAGS}

masa_python_c_lib.o: masa_python_c_lib.cpp
	g++ ${BASE_OPTIONS} ${INCLUDE} masa_python_c_lib.cpp
	
clean:
	rm -f *.lib *.o
