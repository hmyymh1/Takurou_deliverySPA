module.exports = {
    publicPath: "/",
    devServer: {
        proxy:{
            "/api":{
                target: "http://127.0.0.1:8081/", //目标api地址
                changeOrigin : true, // 允许websockets跨域
                pathRewrite: {
                    //正则匹配 /api之前都替换为空
                    "^/api": "",
                }
            }
        }
    },
}