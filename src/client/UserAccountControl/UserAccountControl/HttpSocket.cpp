#include "HttpSocket.h"

pplx::task<void> HttpSocket::httpRequset(string_t req_uri) {
  http_request req;

  uri_builder req_path;
  req_path.set_path(req_uri);

  req.set_method(methods::GET);
  req.set_request_uri(req_path.to_uri());
  req.set_body(inbuf_);

  return client_->request(req).then([&](http_response response) {
    std::cout << response.status_code() << " OK" << std::endl;
    if (response.status_code() == 200) {
      response.extract_string().then([&](string_t http_body) {
        outbuf_ = http_body;
      });
    }
  });
}