#pragma once

#include "pyport.h"

extern volatile int GlOBAL_THREAD_COUNTER;
extern Py_THREAD_LOCAL int tls_thread_id;