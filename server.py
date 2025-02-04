import socket
import os
import json
from calc import Calc

def toJson(result, result_type, id):
    "出力をjson形式に変換するための関数"
    data = {
        "result": result,
        "result_type": result_type,
        "id": id,
    }
    return json.dumps(data)


# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定
server_address = '/tmp/socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
print('---------------------------------')
# サーバアドレスにソケットをバインド（接続）
sock.bind(server_address)
# ソケットが接続要求を待機する
sock.listen(1)

#クライアントからの接続を待ち
while True:
    # クライアントからの接続を受け入れる
    connection, client_address = sock.accept()
    try:
        print('connection!')

        #通信開始
        while True:
            #データ受け取り->decode->json形式
            data = connection.recv(1024)
            data_str =  data.decode('utf-8')
            request = json.loads(data_str)

            if(request["method"] == "subtract"):
                result = Calc.subtract(request["params"][0],request["params"][1])
            elif(request["method"] == "floor"):
                result = Calc.floatToInt(request["params"][0])
            elif(request["method"] == "nroot"):
                result = Calc.nroot(request["params"][0],request["params"][1])
            elif(request["method"] == "reverse"):
                result = Calc.reverse(request["params"][0])
            elif(request["method"] == "validAnagram"):
                result = Calc.validAnagram(request["params"][0],request["params"][1])
            elif(request["method"] == "sort"):
                result = Calc.sort(request["params"][0])

            # 受け取ったメッセージを処理
            response = toJson(result, request["param_types"],request["id"])

            # 処理したメッセージをクライアントに送り返します。
            connection.sendall(response.encode())
    finally:
        print("final")
        connection.close()
        break