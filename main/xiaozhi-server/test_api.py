import requests
import json

# 后端服务的URL
url = "http://localhost:8002/xiaozhi/config/server-base"

print(f"--- 开始测试 ---")
print(f"请求方法: POST")
print(f"请求地址: {url}")

try:
    # 执行POST请求，设置10秒超时
    response = requests.post(url, timeout=10)

    # 打印HTTP状态码
    print(f"\nHTTP状态码: {response.status_code}")

    # 尝试将响应内容作为JSON打印
    try:
        response_data = response.json()
        print("\n响应内容 (JSON):")
        print(json.dumps(response_data, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print("\n响应内容 (非JSON):")
        print(response.text)

    if response.status_code == 200 and response.json().get("code") == 0:
        print("\n--- 结论: 测试成功！后端服务正常，独立脚本可以访问。---")
    else:
        print(f"\n--- 结论: 测试失败。后端返回了业务错误或HTTP错误。---")


except requests.exceptions.RequestException as e:
    print(f"\n--- 结论: 测试失败。发生网络层错误。---")
    print(f"错误详情: {e}") 