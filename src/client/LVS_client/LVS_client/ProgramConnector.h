#ifndef LVS_PROGRAM_FUNC_DEFINE_
#define LVS_PROGRAM_FUNC_DEFINE_

#include <cpprest\json.h>

using namespace web::json;
using namespace utility;

class ProgramConnector {
public:
  ProgramConnector();
  ~ProgramConnector();

  void unserialize(string_t json_str);
  inline int get_license_type() { return license_type_; }
  inline int get_end_date() { return end_date_; }

private:
  int license_type_;
  int end_date_;
};

#endif