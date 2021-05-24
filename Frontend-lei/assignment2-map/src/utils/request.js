import axios from "axios"

axios.defaults.withCredentials = false;


const request = axios.create({
  baseURL: "http://172.26.131.86:5984",
  timeout: 10000,
  withCredentials: false,
  headers: {
    // "Access-Control-Allow-Origin": "*",
    // "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
    // "Access-Control-Allow-Methods": 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
    
    // "Access-Control-Request-Headers": "Content-Type, Authorization",
    "Content-Type": "application/json",
    "Authorization": "Basic YWRtaW46YWRtaW4=" 
    }
}
)

export default request