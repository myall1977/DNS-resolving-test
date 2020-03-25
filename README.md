# DNS-resolving-test

Python2로 동작합니다

list 파일의 format은 다음과 같습니다.

비교할 두개의 domain을 comma로 연결하여 file을 만듭니다.
www.a.com,www1.a.com
www.b.com,www1.b.com

Script는 각각의 domain들을 KR,CN dns에 각각 DNS resolving(CNAME record)하여 결과를 다음과 같이 출력합니다.
168.126.63.1
www.a.com,cname.a.com,www1.a.com,cname.a.com
www.b.com,cname.b.com,www1.b.com,cname.b.com
202.46.34.75
www.a.com,cn.a.com,www1.a.com,cn.a.com
www.b.com,cn.b.com,www1.b.com,cn.b.com

결과를 excel에 넣어 compare 하시면 됩니다.
