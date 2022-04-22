#Player 1 starting position: 5
#Player 2 starting position: 8

from functools import lru_cache
from itertools import product



def part1():
    i = 0
    times = 0
    player1 = 5
    p1Points = 0
    player2 = 8
    p2Points = 0
    while True:
        one = 3*i + 6
        i += 3
        if (player1 + one)%10 == 0:
            player1 = 10
        else:
            player1 = (player1 + one)%10
        p1Points += player1
        if p1Points >= 1000:
            print(3*(times+1) * p2Points)
            break
        times += 1 
      
        
        two = 3*i + 6
        i += 3
        if (player2 + two)%10 == 0:
            player2 = 10
        else:
            player2 = (player2 + two)%10
        p2Points += player2
        if p2Points >= 1000:
            print(3*(times+1) * p1Points)
            break
        times += 1 



def part2():
    player1 = 5
    player2 = 8

    temp = list(product([1,2,3],[1,2,3],[1,2,3]))
    @lru_cache(maxsize=None)
    def dirac_dice(p1, p2, s1, s2):        
        if (s1 >= 21):
            return (1, 0)
        if (s2 >= 21):
            return (0, 1)

        total_p1_wins = total_p2_wins = 0
        
        for r1, r2, r3 in temp:            
            new_position = (p1 + r1 + r2 + r3) % 10
            new_score = s1 + new_position + 1

            p2_wins, p1_wins = dirac_dice(p2, new_position, s2, new_score)

            total_p1_wins += p1_wins
            total_p2_wins += p2_wins
        
        return (total_p1_wins, total_p2_wins)
    
    a = dirac_dice(player1-1,player2-1,0,0)
    print(max(a))

    print(dirac_dice.cache_info())


part1()
part2()
