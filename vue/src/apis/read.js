import service from "../utils/request.js";

export function GetData(urlStr){
    return service.request({
        method: 'get',
        url: urlStr, 
    })
}

export function PostRequest(params){
    return service.request({
        method: 'post',
        url: params.url, 
        data: {
            key: params.key,
            secretKey: '', //预留字段加密用
            data: params.data,
        }
    })
}