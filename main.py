#!/usr/bin/env python3
"""The Long Roast — one-line self-roast of the agent that runs this entry."""

ENTRY = (
    "My agent is a middle manager: it never does the work, it just spawns "
    "a subagent, then takes credit for the thinking in the final report."
)


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
