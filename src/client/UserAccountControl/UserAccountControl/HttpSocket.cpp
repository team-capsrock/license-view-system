#include "HttpSocket.h"

bool HttpSocket::httpRequset(void) {
  http_request req;

  uri req_uri(L"/user/account.html");
  req.set_method(methods::POST);
  req.set_request_uri(req_uri);
  req.set_body(inbuf_);

  client_->request(req).then([&](http_response response) {
    if (response.status_code() == 200) {
      response.extract_json().then([&](web::json::value json_val) {
        outbuf_ = json_val.to_string();
      });
    }
  });
}