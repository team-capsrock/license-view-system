#include "ProgramFuncDefine.h"


ProgramFuncDefine::ProgramFuncDefine () {
	license_type_ = 0;
	end_date_ = 0;
}


ProgramFuncDefine::~ProgramFuncDefine () {
}


void ProgramFuncDefine::unserialize (string_t json_str) {
	value json_val (json_str);

	
}
