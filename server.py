import socket
import os
import json
from calc import Calc


class SocketServer:
    def __init__(self, server_address='/tmp/socket_file'):
        """ソケットサーバーを初期化"""
        self.server_address = server_address

        # 以前のソケットファイルを削除
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        # UNIX ソケットを作成
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(self.server_address)
        self.sock.listen(1)

        print(f'✅ サーバーが {self.server_address} で待機中...')

    def start_server(self):
        """クライアントの接続を待機"""
        while True:
            connection, _ = self.sock.accept()
            print('クライアントと接続')

            try:
                self.handle_request(connection)
            finally:
                connection.close()
                print("クライアントの接続を終了")

    def handle_request(self, connection):
        """クライアントのリクエストを処理"""
        while True:
            try:
                #データ受け取り->decode->json形式
                data = connection.recv(1024)
                data_str =  data.decode('utf-8')
                request = json.loads(data_str)

                # "exit" コマンドでサーバーを終了
                if request["method"] == "exit":
                    print("⏹ サーバーを終了します")
                    response = self.to_json("exit", request["id"])
                    connection.sendall(response.encode())
                    break

                # 計算処理
                result = self.process_request(request)
                
                # JSON 形式でレスポンスを送信
                response = self.to_json(result, request["id"])
                print(response)
                connection.sendall(response.encode())
            finally:
                print("close")
                connection.close()
                break


    def process_request(self, request):
        """リクエストを処理し、計算結果を返す"""
        method = request["method"]
        params = request["params"]

        if method == "subtract":
            return Calc.subtract(*params)
        elif method == "floor":
            return Calc.floatToInt(*params)
        elif method == "nroot":
            return Calc.nroot(*params)
        elif method == "reverse":
            return Calc.reverse(*params)
        elif method == "validAnagram":
            return Calc.validAnagram(*params)
        elif method == "sort":
            return Calc.sort(params)
        else:
            raise ValueError("未定義のメソッド")

    def to_json(self, result, id):
        """出力を JSON 形式に変換"""
        return json.dumps({
            "result": result,
            "result_type": type(result).__name__,
            "id": id,
        })

# サーバーの起動
if __name__ == "__main__":
    server = SocketServer()
    server.start_server()
