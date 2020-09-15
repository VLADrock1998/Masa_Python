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
    uint16_t num_lights;
    RoadUser* objects;
    TrafficLight* lights;
};

extern "C" int saluto();

extern "C" PMasaMessage* create_MasaMessage (uint32_t, uint64_t, uint16_t, uint16_t, RoadUser*, TrafficLight*);

extern "C" MasaMessage* cast_MasaMessage (PMasaMessage*);

extern "C" int send_MasaMessage (PMasaMessage*, int, char*);

extern "C" RoadUser* create_RoadUser (uint16_t);

extern "C" void initialize_RoadUser (RoadUser*, float, float, uint8_t, uint16_t, uint8_t);

extern "C" TrafficLight* create_TrafficLight (uint16_t);

extern "C" void initialize_TrafficLight (TrafficLight*, float, float, uint8_t, uint8_t, uint8_t);

#endif
