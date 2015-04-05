#include "HttpClient.h"

bool HttpClient::httpRequset (void) {
	http_request req;

	uri req_uri (L"/user/account.html");
	req.set_method (methods::POST);
	req.set_request_uri (req_uri);
	req.set_body (_inbuf);

	_client->request (req).then ([](http_response response) {
		if (response.status_code () == 200) {
			auto body_stream = response.body ();


		}
	});
}