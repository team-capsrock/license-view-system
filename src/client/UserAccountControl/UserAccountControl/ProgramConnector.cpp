#include "ProgramConnector.h"


ProgramConnector::ProgramConnector() : license_type_(0), end_date_(0) {
  
}


ProgramConnector::~ProgramConnector() {
}


void ProgramConnector::unserialize(string_t json_str) {
  value json_val(json_str);

  if (json_val.has_field(U("LICENSE")) == true)
    license_type_ = json_val.get(U("LICENSE")).as_integer();
  if (json_val.has_field(U("END-PERIOD")) == true)
    end_date_ = json_val.get(U("END-PERIOD")).as_integer();
}
