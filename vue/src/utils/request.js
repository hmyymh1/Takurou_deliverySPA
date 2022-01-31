import axios from "axios";

const BASE_URL = process.env.NODE_ENV === 'production' ? 'https://www.hmyymh.com.cn/api' : '/api';

//创建 axios
const service = axios.create({
    baseURL: BASE_URL,
    timeout: 1800000    
})

//请求拦截器：在浏览器发送请求之前处理  用处：判断是否符合请求参数的要求
service.interceptors.request.use(
    function(config){
        console.log("request.js: request:  config===== ", config);
        return config;
    },
    function(error){
        return Promise.reject(error);
    }
)

//响应拦截器：服务器返回数据后处理
service.interceptors.response.use(
    function(response){
        console.log("request.js: response = ", response);
        let data = response.data;
        if(data.resCode != 0){
            // 服务器有响应，但是并不是想要的数据
            // Message.error(data.message);
            console.log("服务器有响应，但是并不是想要的数据");
            Promise.reject(data.resCode)
            return response;
        }else{
            // 服务器有响应，且数据正确
            console.log('response.js: data.data = ',data.data);
            return response;
        }
    },

    function(error){
        // 服务器没响应 404,405
        return Promise.reject(error);
    }
)

//对外暴露接口
export default service;