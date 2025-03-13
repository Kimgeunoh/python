
n = int(input("세 자리 정수를 입력하시오 : "))


hundreds = n // 100          
tens = (n // 10) % 10       
ones = n % 10                


print(ones)
print(tens)
print(hundreds)
