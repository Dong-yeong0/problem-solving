def solution(N, stages):
    fail_dict = {}
    users = len(stages)
    for stage in range(1, N + 1):
        if users != 0:
            losers = stages.count(stage)
            fail_dict[stage] = losers / users
            users -= losers
        else:
            fail_dict[stage] = 0

    return sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)