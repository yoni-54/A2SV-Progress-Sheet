class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}        
        color_count = {}      
        res = []
        distinct = 0

        for ball, new_color in queries:
        
            if ball in ball_color:
                old_color = ball_color[ball]
                color_count[old_color] -= 1
            
                if color_count[old_color] == 0:
                    distinct -= 1
        
            ball_color[ball] = new_color
        
            if new_color not in color_count or color_count[new_color] == 0:
                distinct += 1
                color_count[new_color] = 1
            else:
                color_count[new_color] += 1
        
            res.append(distinct)
    
        return res