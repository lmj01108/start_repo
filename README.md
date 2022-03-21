# test_repo

def maximum(a,b,c):
	if a>b:
		if a>c:
			return a
		else:
			return c
	else:
		if b>c:
			return b
		else:
			return c
	
a,b,c = input().split()#스페이스기준으로 문자열을 찢어서 각 요소의 리스트를 만들 수 있음
a,b,c = int(a), int(b), int(c)

