import sys


def analyse_scores(args: list[str]):
    scores: list[int] = []
    for i in range(1, len(args)):
        try:
            scores.append(int(args[i]))
        
        except Exception as e:
            print(f"{e}")

    if len(scores) < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total player: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / (len(scores))}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")
    
    
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    analyse_scores(sys.argv)
