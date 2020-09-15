#include "masa_python_c_lib.h"

int send_message (MasaMessage* m)
{
    char * ip = "127.0.0.1";
    int port = 8891;
    Communicator<MasaMessage> Comm(SOCK_DGRAM);
    Comm.open_client_socket((char *) ip, port);
    std::stringbuf s;
    Comm.send_message(m, port);
    sleep(1); 
    return 021212; 
}

PMasaMessage* initialize_message (int num_objects, int num_lights)
{
    printf("sono stata chiamata! %d",num_objects);
    PMasaMessage* message = new PMasaMessage;
    message->objects = new RoadUser[num_objects];
    message->lights = new TrafficLight[num_lights];
    return message;
}

void saluto ()
{
	printf("SONO FINALMENTE STATA CHIAMATA!");
}
