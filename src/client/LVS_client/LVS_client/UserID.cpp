#include "UserID.h"


UserID::UserID() {
}


UserID::~UserID() {
}

void UserID::InputUserInfo(string_t input_id, string_t input_pw) {
  id_ = input_id;
  pw_ = input_pw;
}

string_t UserID::serialize(void) {
  value json_val;

  json_val[string_t(L"id")] = value(id_);
  json_val[string_t(L"pw")] = value(pw_);

  return json_val.serialize();
}
