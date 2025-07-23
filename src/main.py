from sleeper import get_users, get_rosters, get_matchups, build_matchup_summary

WEEK = 1  # Falls du Offseason testest, bleib bei 1

if __name__ == "__main__":
    users = get_users()
    rosters = get_rosters()
    matchups = get_matchups(WEEK)

    print(f"\n📊 Matchups – Week {WEEK}:\n")

    summary = build_matchup_summary(users, rosters, matchups)
    for line in summary:
        print(line)
