#ifndef LVS_USER_ACCOUNT_H_
#define LVS_USER_ACCOUNT_H_

#include <cpprest/json.h>

using namespace web::json;
using namespace utility;

class UserID {
public:
  UserID();
  ~UserID();

	void InputUserInfo (string_t input_id, string_t input_pw);
	string_t serialize (void);
private:
	string_t id_;
	string_t pw_;
};

#endif