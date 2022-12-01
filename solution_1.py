from base import Solution


class Solution_1_1(Solution):
    def __init__(self, day, part):
        super(Solution_1_1, self).__init__(day, part)
    
    def solution(self):
        total_calories = []
        calories = 0

        for line in self.file_data:
            if line == "":
                total_calories.append(calories)
                calories = 0
            else:
                calories += int(line)
                

        total_calories.sort(reverse=True)
        
        return total_calories[0]
    
solution_1_1 = Solution_1_1(1, 1)
print(solution_1_1.solution())


class Solution_1_2(Solution):
    def __init__(self, day, part):
        super(Solution_1_2, self).__init__(day, part)
        
    def solution(self):
        total_calories = []
        calories = 0

        for line in self.file_data:
            if line == "":
                total_calories.append(calories)
                calories = 0
            else:
                calories += int(line)
                

        total_calories.sort(reverse=True)
        top_three_total_calories = 0

        for total_cal in total_calories[0:3]:
            top_three_total_calories += total_cal
        
        return top_three_total_calories
    
solution_1_2 = Solution_1_2(1, 2)
print(solution_1_2.solution())
        

    
