import axios from "axios"

axios.defaults.withCredentials = false;


const request = axios.create({
  baseURL: "http://172.26.131.157:5984",
  timeout: 10000,
  withCredentials: false,
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Basic YWRtaW46YWRtaW4=" 
    }
}
)

export default request