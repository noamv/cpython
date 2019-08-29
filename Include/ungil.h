#pragma once
/*
	Since chageing the include in python is very hard for now all stuff releared to ungil in order for it to be east included
	Sorry for, unsigned int, i didnt bother with types:)
*/


extern volatile unsigned int GlOBAL_THREAD_COUNTER;
extern __declspec(thread) unsigned int tls_thread_id;