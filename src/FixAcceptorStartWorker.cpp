/*
 * FixStartWorker.cpp
 *
 *  Created on: Jul 27, 2014
 *      Author: stefankutko
 */

#include <node.h>
#include <nan.h>

#include "quickfix/Exceptions.h"
#include "quickfix/ThreadedSocketAcceptor.h"
#include "FixAcceptorStartWorker.h"

using namespace v8;
using namespace node;

// Executed inside the worker-thread.
// It is not safe to access V8, or V8 data structures
// here, so everything we need for input and output
// should go on `this`.
void FixAcceptorStartWorker::Execute () {
	try {
		acceptor->start();
	} catch(FIX::ConfigError& e) {
    this->SetErrorMessage("Failed to start FIX Acceptor");
		//handle this exception
	}
}

// Executed when the async work is complete
// this function will be run inside the main event loop
// so it is safe to use V8 again
void FixAcceptorStartWorker::HandleOKCallback () {
	Nan::HandleScope scope;

    v8::Local<v8::Function> fn = callback->GetFunction();
	if(!(fn->IsUndefined() || fn->IsNull())) {
		Local<Value> argv[] = {
			Nan::Null()
		};

		callback->Call(1, argv);
	}
}
