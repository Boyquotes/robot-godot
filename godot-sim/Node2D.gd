extends Node2D

var http_request = HTTPRequest.new()
func _ready():
	add_child(http_request)
	http_request.request_completed.connect(self._on_http_request_request_completed)
	http_request.request("https://127.0.0.1:5000/get_position")


func _on_http_request_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	
	print(response)
	


func _on_button_button_up():
	http_request.request("https://127.0.0.1:5000/get_position")
