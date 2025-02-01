const net = require('net');

// サーバーのUNIXドメインソケットファイルのパス
const SERVER_SOCKET_PATH = '/tmp/socket_file'; 
// クライアント側のUNIXドメインソケットファイルのパス
const CLIENT_SOCKET_PATH = '/path/to/client_socket'; 

req = {
    method: "subtract",
    params: [34,32],
    param_types: [Number,Number],
    id: 1,
}

// ソケットの作成とサーバーへの接続
const client = net.createConnection(SERVER_SOCKET_PATH, () => {
    console.log('----------------------------------------');
    console.log('✅ サーバーに接続しました');

    const request = JSON.stringify(req);

    // サーバーにデータ送信
    client.write(request);
});

// サーバーからのデータ受信
client.on('data', (data) => {
    console.log('サーバーから受け取ったデータ:', data.toString());
    // 通信が終了したらソケットを閉じる
    client.end();
});

// ソケットが閉じられた時の処理
client.on('end', () => {
    console.log('通信が終了しました');
});

// エラーハンドリング
client.on('error', (err) => {
    console.error('エラー:', err);
});
