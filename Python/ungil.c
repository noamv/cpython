#include "ungil.h"

volatile int GlOBAL_THREAD_COUNTER = 1;
Py_THREAD_LOCAL int tls_thread_id = 1;
