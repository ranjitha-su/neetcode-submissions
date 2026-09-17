class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # days = [1,4,6,7,8,20], costs = [2,7,15], 
        
        def find_next_start_date(date_covered:int):
            for i in range(len(days)):
                if date_covered>=days[i]:
                    continue
                return i
            return len(days)
        
        def solve(days_start_index:int):
            # term condition
            if days_start_index >=len(days):
                return 0
            
            if days_start_index in memo:
                return memo[days_start_index]
           
            # 1 day pass section
            final_date_covered_by_this_pass=days[days_start_index]+pass_type[0]-1
            next_start_index=find_next_start_date(final_date_covered_by_this_pass)
            travel_cost_with_1_day_pass=costs[0]+solve(next_start_index)
            

            # 7 day pass section
            final_date_covered_by_this_pass=days[days_start_index]+pass_type[1]-1
            next_start_index=find_next_start_date(final_date_covered_by_this_pass)
            travel_cost_with_7_day_pass=costs[1]+solve(next_start_index)
            

            # 30 day pass section
            final_date_covered_by_this_pass=days[days_start_index]+pass_type[2]-1
            next_start_index=find_next_start_date(final_date_covered_by_this_pass)
            travel_cost_with_30_day_pass=costs[2]+solve(next_start_index)
            

            print(f"min({travel_cost_with_1_day_pass}, {travel_cost_with_7_day_pass}, {travel_cost_with_30_day_pass})")
            memo[days_start_index] = min(travel_cost_with_1_day_pass, travel_cost_with_7_day_pass, travel_cost_with_30_day_pass)
            return memo[days_start_index]
        
        memo={}
        pass_type=[1,7,30]
        return solve(0)