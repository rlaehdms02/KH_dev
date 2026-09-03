y = int(input())
ape_list = []
for i in range(1, y + 1):
    sh, hu = list(map(int, input().split()))
    ape_list.append(sh)
    ape_list.append(hu)

ap_sum, y = 0, 0
while y < len(ape_list):
    test01 = ape_list[y]
    test02 = ape_list[y + 1]
    ap_sum = 0
    y = 0
    while y < len(ape_list):
        test01 = ape_list[y]  # sh
        test02 = ape_list[y + 1]  # hu

        # sh가 hu보다 크면 바로 hu를 더하고 다음 단계로
        if test01 > test02:
            ap_sum += test02
            y += 2
            continue

        mag = test01
        # 배수를 누적해서 hu를 넘지 않는 가장 큰 배수를 찾는 과정
        while mag + test01 <= test02:
            mag = mag + test01

        rq = test02 - mag
        ap_sum = ap_sum + rq
        y = y + 2

    print(ap_sum)
