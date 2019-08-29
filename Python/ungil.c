#include "ungil.h"
volatile unsigned int GlOBAL_THREAD_COUNTER = 0;
__declspec(thread) unsigned int tls_thread_id = 0;