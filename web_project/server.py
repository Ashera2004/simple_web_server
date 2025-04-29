from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content to serve
content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lenovo ThinkPad E16 Specs</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5e6ff;
            padding: 20px;
        }
        .container {
            background-color: #fff0ff;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(128, 0, 128, 0.3);
        }
        .info {
            font-size: 18px;
            color: #4a0072;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
        }
        .title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: #7a00cc;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #b366ff;
            color: white;
            padding: 12px;
            text-align: left;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        tr:nth-child(even) {
            background-color: #f0e6ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="info">Name : A S Siddarth &nbsp;&nbsp;&nbsp; Reg No. 212224040316</div>
        <div class="title">💻 Lenovo ThinkPad E16 Specifications 💻</div>
        <table>
            <tr><th>Feature</th><th>Specification</th></tr>
            <tr><td>Processor</td><td>Intel Core i5-1340P / AMD Ryzen 7 7730U</td></tr>
            <tr><td>Display</td><td>16.0" WUXGA (1920 x 1200), IPS, Anti-Glare</td></tr>
            <tr><td>Integrated Graphics</td><td>Intel Iris Xe / AMD Radeon Graphics</td></tr>
            <tr><td>Discrete Graphics</td><td>Optional NVIDIA GeForce RTX 2050</td></tr>
            <tr><td>Memory</td><td>Up to 32GB DDR4</td></tr>
            <tr><td>Storage</td><td>Up to 1TB SSD</td></tr>
            <tr><td>Operating System</td><td>Windows 11 Pro</td></tr>
            <tr><td>Weight</td><td>Starting at 1.78kg (3.92 lbs)</td></tr>
            <tr><td>Battery Life</td><td>Up to 10 hours</td></tr>
            <tr><td>Ports</td><td>USB-C, USB 3.2, HDMI, Ethernet, Audio Jack</td></tr>
        </table>
    </div>
</body>
</html>
'''

# HTTP Server class
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

# Server setup
print("Starting server at http://127.0.0.1:8000")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
