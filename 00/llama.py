import requests

url = "https://llama3-2-multimodal.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoicnRscGd0eHg3bWdycnBkNWhnaGFpa2UyIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTItbXVsdGltb2RhbC5sbGFtYW1ldGEubmV0XC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzMxMDcwMjEyfX19XX0_&Signature=Rh-PYYG6dDZXTP-4YReFKCc-g-cY4K-idcws4DIMteR22s0x49IPqFY%7EspEKtqBE50O6vIpX--eXk%7ETlfe6qa0PQut9AuP4cLG2nu1%7EbR0hKq2n4i7h6fWlvMdWcCayLgGVDXxd3hYOOaLwed%7E-q5Jj1qUwq9U9rolZB9Po9SIg2rO%7E0yFSzv3LQrUlXV9d0OMBftdFJaoztRXNifBjo0sSI4g7oGSLB%7Ex14-fNBs%7EhjmSZKxrTpF59zE%7EuB1VYa4bcevS19kK9YLP1PhEVwnss-LNzTpZTkfvdQT4mxQd5eAPoVX4OGRDg5Fhfl3Pg7r0%7EFnqxr4FiTd8OJ6R-wDw__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=397451666654820"  # 여기에 고유 URL 입력
response = requests.get(url, stream=True)

# 파일 저장
with open("llama_model.bin", "wb") as file:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            file.write(chunk)
