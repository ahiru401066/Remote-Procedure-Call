const net = require('net');

// サーバーのUNIXドメインソケットファイルのパス
const SERVER_SOCKET_PATH = '/tmp/socket_file'; 
// クライアント側のUNIXドメインソケットファイルのパス
const CLIENT_SOCKET_PATH = '/path/to/client_socket'; 


// request一覧
req = {
    method: "exit",
}
req = {
    method: "subtract",
    params: [34,32],
    param_types: [Number,Number],
    id: 1,
}

req = {
    method: "floor",
    params: [32.23],
    param_types: [],
}


// ソケットの作成とサーバーへの接続
const client = net.createConnection(SERVER_SOCKET_PATH, () => {
    console.log('----------------------------------------');
    console.log('✅ サーバーに接続しました');
    // json形式化
    const request = JSON.stringify(req);
    // サーバーにデータ送信
    client.write(request);
});

// サーバーからのデータ受信
client.on('data', (data) => {

    // 受け取り後のデータ処理
    const responseData = JSON.parse(data.toString())
    console.log(responseData);
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
