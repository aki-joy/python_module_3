import sys


def analyse_scores(args: list[str]) -> None:
    scores: list[int] = []
    for arg in args[1:]:
        try:
            scores.append(int(arg))

        except Exception:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) < 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ...\n"
        )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / (len(scores))}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    analyse_scores(sys.argv)
