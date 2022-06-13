def solution(enroll, referral, seller, amount):
    
    ans = []
    d = {a : b for a, b in zip(enroll, referral)}
    money = {i : 0 for i in enroll}

    for node, distribution in zip(seller, amount):
        distribution *= 100

        while node != "-":

            if distribution >= 10:
                money[node] += (distribution - distribution // 10)
                node = d[node]
                distribution //= 10

            else:
                money[node] += distribution
                break

    ans = list(money.values())
    return ans


# Run.
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
solution(enroll, referral, seller, amount)