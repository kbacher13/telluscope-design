import http.server, os
os.chdir(os.path.expanduser("~/claude code_telluscope"))
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8766, bind="127.0.0.1")
