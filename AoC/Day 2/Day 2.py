sum_score = 0
points_loss = 0
points_draw = 3
points_win =  6
points_rock = 1
points_paper = 2
points_scissor = 3

me_lose = "X"
me_draw = "Y"
me_win = "Z"

opponent_rock = "A"
opponent_paper = "B"
opponent_scissor = "C"

with open("Day 2/Input.txt") as i:

    for line in i.readlines():
        me = line.split()[1]
        opponent = line.split()[0]

        ## Draw
        if me == me_draw:
            if opponent == opponent_rock:
                sum_score += points_draw + points_rock
            if opponent == opponent_paper:
                sum_score += points_draw + points_paper
            if opponent == opponent_scissor:
                sum_score += points_draw + points_scissor

        ## Win
        if me == me_win:
            if opponent == opponent_rock:
                sum_score += points_win + points_paper
            if opponent == opponent_paper:
                sum_score += points_win + points_scissor
            if opponent == opponent_scissor:
                sum_score += points_win + points_rock

        ## Lose
        if me == me_lose:
            if opponent == opponent_rock:
                sum_score += points_loss + points_scissor
            if opponent == opponent_paper:
                sum_score += points_loss + points_rock
            if opponent == opponent_scissor:
                sum_score += points_loss + points_paper
        
    i.close()

    print(sum_score)