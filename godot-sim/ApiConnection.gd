extends Control

var http_request = HTTPRequest.new()
func _ready():
	add_child(http_request)
	http_request.request_completed.connect(self._on_http_request_request_completed)

	http_request.request("https://127.0.0.1:5000/get_position")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _get_api_data():
	http_request.request("https://127.0.0.1:5000/get_position")


func _on_http_request_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	
	print(response)
	
