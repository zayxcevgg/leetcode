class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveDollar = 0
        tenDollar = 0
        for customer in bills:
            if customer == 5:
                fiveDollar += 1
            elif customer == 10:
                if fiveDollar > 0:
                    tenDollar += 1
                    fiveDollar -= 1
                else:
                    return False
            elif customer == 20:
                if fiveDollar > 0 and tenDollar > 0:
                    fiveDollar -= 1
                    tenDollar -= 1
                elif fiveDollar >= 3:
                    
                    fiveDollar -= 3
                else:
                    return False
                
        return True

            # print(customer)
            # total += customer
            # if customer > 5:
            #     #total
            #     change = customer - 5
            #     if change in changeBills:
            #         changeBills.remove(change)
            #         changeBills.append(customer)
            #     else:
                    
            #         # while change != 0:
            #         #     for i in reversed(changeBills):
            #         #         if i <= change:
            #         #             changeBills.remove(i)
            #         #             change -= i

            #         changeBills.append(customer)

            # else:
            #     changeBills.append(customer)
            #     changeBills = list(tuple(sorted(changeBills)))

            #print(changeBills)

            

obj = Solution()
bills = [5,5,10,10,20]
obj.lemonadeChange(bills)