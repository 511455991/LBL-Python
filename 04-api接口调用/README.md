## api即接口，发送对应请求，获取解析响应

api格式举例：

请求地址：http://www.tuling123.com/openapi/api

请求方式：GET

支持格式：application/json;charset=UTF-8

请求参数：

| 名称 | 类型   | 必填 | 说明                         |
| ---- | ------ | ---- | ---------------------------- |
| key  | string | 必填 | 在图灵机器人平台申请的apikey |
| info | string | 必填 | 要发送的消息                 |

返回格式：json    

| 名称 | 类型   | 说明   |
| ---- | ------ | ------ |
| key  | string | 状态码 |
| text | string | 消息   |



请求示例：http://www.tuling123.com/openapi/api?key=your_key&info=your 

响应举例：{"code":100000,"text":"哎呀，没听清，请再说一遍吧。"} 







