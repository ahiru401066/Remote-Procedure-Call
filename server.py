import socket
import os

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

# サーバアドレスにソケットをバインド（接続）
sock.bind(server_address)

# ソケットが接続要求を待機する
sock.listen(1)

#クライアントからの接続を待ち
while True:
    # クライアントからの接続を受け入れる
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        #通信開始
        while True:
            #データ受け取りとdecode
            data = connection.recv(16)
            data_str =  data.decode('utf-8')
            print('Received ' + data_str)

            if data:
                # 受け取ったメッセージを処理
                response = 'Processing ' + data_str

                # 処理したメッセージをクライアントに送り返します。
                connection.sendall(response.encode())

            # クライアントからデータが送られてこなければ、ループを終了
            else:
                print('no data from', client_address)
                break

    # 最終的に接続を閉じる
    finally:
        print("Closing current connection")
        connection.close()