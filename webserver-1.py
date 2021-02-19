				
import socket
import os, filetype

docroot = "/Users/vamsi/Desktop/Project - CN/Project-CN"

def init(HOST, PORT):
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listen_socket.bind((HOST, PORT))
	return listen_socket

def start_server(listen_socket):
	listen_socket.listen(1)
	serve_clients(listen_socket)

def serve_clients(listen_socket):
	while True:
		client_connection, client_address = listen_socket.accept()
		request_data = client_connection.recv(1024)
		client_connection.sendall(handle_request(request_data))


def handle_request(data):
	request_data = data.decode("UTF-8")
	uri = geturi(request_data)
	http_response = b""""""
	if request_data.split(" ")[0] != "GET" or uri == "":
		http_response = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;

				
<b><center><font color="red">BAD REQUEST</font></center></b>"""
	else:
		if (uri) == "/":
			get_files(docroot)
			http_response = b"""\
HTTP/1.1 200 OK
Content-Type: html;

				
""" + bytes(get_files(docroot),"UTF-8")

		elif(uri) == "/favicon.ico":
			pass


		elif os.path.isfile(uri):
			content_type = get_content_type(uri)
			print(content_type, "content_type")
			f = open(uri, encoding = "UTF-8", errors='ignore')
			string = f.read()
			http_response = http_response = b"""\
HTTP/1.1 200 OK
Content-Type: """ +bytes(content_type,"UTF-8")+b""";

				
""" + bytes(string,"UTF-8")


		else:
			http_response = b"""\
HTTP/1.1 200 OK
Content-Type: html;

				
""" + bytes(get_files(uri),"UTF-8")
			

	return http_response



def geturi(request_data):
	temp = request_data.split(" ")[1];
	if(temp == "/") or temp == "/favicon.ico":
		return temp
	try:
		os.path.isdir(temp)
	except:
		return ""
	return temp



def get_files(path):
	files = []
	for file in os.listdir(path):
		files.append("<a href = \""+os.path.join(path, file) + "\"  > " + os.path.join(path, file) +"</a> <br>")
	return ''.join(files)
	

def get_content_type(path):
	kind = filetype.guess(path)
	if kind is None:
		return "/text"
	else:
		return kind.mime
	# res = urllib.urlopen(path)
	# http_message = res.info()
	# return http_message.type

start_server(init('',8765))

