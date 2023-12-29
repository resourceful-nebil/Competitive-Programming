class Solution:
    def smallestNumber(self, num: int) -> int:
        
        ans = []
        if num >= 0:
            num = list(map(int,str(num)))
            dicti = Counter(num)
            for i in range(10):
                if i in dicti:
                    while dicti[i] != 0:
                        ans.append(i)
                        dicti[i] -= 1
            
            for i in range(len(ans)):
                if ans[i] != 0:
                    ans[0] , ans[i] = ans[i] , ans[0]
                    break

            return int(''.join(map(str,ans)))



        else:
            num = -1 * num
            num = list(map(int,str(num)))
            num.sort(reverse = True)

            num = int(''.join(map(str,num)))
            return num * -1




        print(num)
        # for i in range(len(num)):
        #     for j in range(i + 1,len(num)):
        #         if num[0] == "-" and num[i] + num[j] < num[j] + num[i]:
        #             num[i] , num[j] = num[j] , num[i]

        #         elif num[0] != "-" and num[i] + num[j] > num[j] + num[i]:
        #             print(num[i],num[j])
        #             num[i] , num[j] = num[j] , num[i]
        # if num[0] == '0':
        #     num[0] , num[1] = num[1] , num[0]
        # print(num)
        return 1