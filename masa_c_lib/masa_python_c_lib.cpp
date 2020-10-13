#include "masa_python_c_lib.h"


PMasaMessage* receive_MasaMessage (char* raw_data, uint32_t data_len)
{
	MasaMessage* m = new MasaMessage;
	std::string s(raw_data, data_len);
	
	std::istringstream is(s);
        cereal::PortableBinaryInputArchive retrieve(is);
        try
        {
            retrieve(*m);
        }
        catch (std::bad_alloc& ba)
        {
            std::cout << "Packet drop"<<std::endl;
        }
	
	PMasaMessage* message = new PMasaMessage;
	message->cam_idx = m->cam_idx;
	message->t_stamp_ms = m->t_stamp_ms;
	message->num_objects = m->num_objects;
    	message->num_lights = m->lights.size();
    	message->objects = m->objects.data();
    	message->lights = m->lights.data();
    	
	return message;
}

PMasaMessage* create_MasaMessage (uint32_t cam_idx, uint64_t t_stamp_ms, uint16_t num_objects, uint16_t num_lights, RoadUser* objects, TrafficLight* lights)
{
    	PMasaMessage* message = new PMasaMessage;
    	message->cam_idx = cam_idx;
    	message->t_stamp_ms = t_stamp_ms;
    	message->num_objects = num_objects;
    	message->num_lights = num_lights;
    	message->objects = objects;
    	message->lights = lights;
    	return message;
}

MasaMessage* cast_MasaMessage (PMasaMessage* message)//This function casts the Python mid version (c_MasaMessage) to a definitive C MasaMessage
{
	MasaMessage* m = new MasaMessage;
	
	m->cam_idx = message->cam_idx;
	m->t_stamp_ms = message->t_stamp_ms;
	m->num_objects = message->num_objects;
	
	m->objects.clear();
	for (int i=0; i<message->num_objects; i++)
		m->objects.push_back(message->objects[i]);
	
	m->lights.clear();
	for (int i=0; i<message->num_lights; i++)
		m->lights.push_back(message->lights[i]);
	
	return m;
}

int send_MasaMessage (PMasaMessage* message, int port, char* ip)
{	
	MasaMessage* m = cast_MasaMessage(message);
	
    	Communicator<MasaMessage> Comm(SOCK_DGRAM);
	Comm.open_client_socket((char *) ip, port);
	std::stringbuf s;
	Comm.serialize_coords(m, &s);
	Comm.send_message(m, port);
	
    	return 0;
}

RoadUser* create_RoadUser (uint16_t num_objects)//Function that creates an array of RoadUsers then returns the pointer to it.
{
	RoadUser* objects = new RoadUser[num_objects];
	return objects;
}

void initialize_RoadUser (RoadUser* object, float latitude, float longitude, uint8_t speed, uint16_t orientation, uint8_t category)
{
	object->latitude = latitude;
	object->longitude = longitude;
	object->speed = speed;
	object->orientation = orientation;
	object->category = (Categories)category;
}

TrafficLight* create_TrafficLight (uint16_t num_lights)//Function that creates an array of TrafficLights then returns the pointer to it.
{
	TrafficLight* lights = new TrafficLight[num_lights];
	return lights;
}

void initialize_TrafficLight (TrafficLight* light, float latitude, float longitude, uint8_t orientation, uint8_t status, uint8_t time_to_change)
{
	light->latitude = latitude;
	light->longitude = longitude;
	light-> orientation = orientation;
	light->status = (LightStatus)status;
	light->time_to_change = time_to_change;
}

