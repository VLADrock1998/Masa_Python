#include "masa_python_c_lib.h"

int send_message (MasaMessage* m)
{
    const char * ip = "127.0.0.1";
    int port = 8891;
    Communicator<MasaMessage> Comm(SOCK_DGRAM);
    Comm.open_client_socket((char *) ip, port);
    std::stringbuf s;
    Comm.send_message(m, port);
    sleep(1); 
    return 0; 
}

PMasaMessage* initialize_message (int num_objects, int num_lights)
{
    PMasaMessage* message = new PMasaMessage;
    message->objects = new RoadUser[num_objects];
    message->lights = new TrafficLight[num_lights];
    return message;
}
