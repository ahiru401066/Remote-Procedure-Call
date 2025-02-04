const net = require('net');

// サーバーのUNIXドメインソケットファイルのパス
const SERVER_SOCKET_PATH = '/tmp/socket_file'; 
// クライアント側のUNIXドメインソケットファイルのパス
const CLIENT_SOCKET_PATH = '/path/to/client_socket'; 


// request一覧
req1 = {
    method: "subtract",
    params: [34,32],
    param_types: [Number,Number],
    id: 1,
}

req2 = {
    method: "floor",
    params: [32.23],
    param_types: [],
    id: 2,
}

req3 = {
    method: "nroot",
    params: [3,8],
    param_types: [],
    id: 3,
}

req4 = {
    method: "reverse",
    params: ["how are you ?"],
    param_types: [],
    id: 4,
}

req5 = {
    method: "validAnagram",
    params: ["llohe", "llohe"],
    param_types: [],
    id: 5,
}

req6 = {
    method: "sort",
    params: ["hello world!"],
    param_types: [],
    id: 6,
}

// ソケットの作成とサーバーへの接続
const client = net.createConnection(SERVER_SOCKET_PATH, () => {
    console.log('----------------------------------------');
    console.log('✅ サーバーに接続しました');
    // json形式化
    const request = JSON.stringify(req1);
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
