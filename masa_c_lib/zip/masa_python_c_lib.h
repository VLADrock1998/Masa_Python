#ifndef masa_python_c_lib
#define masa_python_c_lib
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h> 
#include <time.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>  
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string>
#include <masa.hpp>

struct PMasaMessage
{
    uint32_t cam_idx;
    uint64_t t_stamp_ms;
    uint16_t num_objects;
    RoadUser* objects;
    TrafficLight* lights;
};

extern "C" int send_message (MasaMessage*);

extern "C" PMasaMessage* initialize_message (int, int);

#endif
