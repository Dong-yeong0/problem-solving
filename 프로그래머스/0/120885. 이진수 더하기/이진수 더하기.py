def solution(bin1, bin2):
    bin1_num = int(bin1 ,2)
    bin2_num = int(bin2, 2)
    answer = bin(bin1_num + bin2_num)[2:]
    return answer