from datetime import datetime

import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    # ── BIOS boot ──
    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    t.gen_text("ARUL_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mArul Gandhi Systems\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Intel(R) i5-1245U vPRO - 4.4GHz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 32768, 3584):  # 32GB memory sweep
        t.delete_row(7)
        if i < 15000:
            t.gen_text(f"Memory Test: {i} MB", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i} MB", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 32GB LPDDR5 OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # ── Boot sequence + logo splash ──
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "ARUL OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    # ── tty login ──
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mArul OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("arulgandhi", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # ── clear + fetch ──
    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    ignore_repos = []
    git_user_details = gifos.utils.fetch_github_stats("ArulGandhi", ignore_repos)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101marulgandhi@arch\x1b[0m
    --------------
    \x1b[96mOS:      \x1b[93mArch Linux x86_64\x1b[0m
    \x1b[96mHost:    \x1b[93mThinkPad X1 Carbon Gen 10\x1b[0m
    \x1b[96mCPU:     \x1b[93mIntel i5-1245U vPRO\x1b[0m
    \x1b[96mMemory:  \x1b[93m32GB LPDDR5\x1b[0m
    \x1b[96mWM:      \x1b[93mHyprland\x1b[0m
    \x1b[96mShell:   \x1b[93mzsh\x1b[0m
    \x1b[96mEditor:  \x1b[93mneovim\x1b[0m

    \x1b[30;101mFocus:\x1b[0m
    --------------
    \x1b[96msecurity  \x1b[93m|\x1b[96m systems  \x1b[93m|\x1b[96m compilers  \x1b[93m|\x1b[96m ml\x1b[0m

    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mWebsite:    \x1b[93marulgandhi.tech\x1b[0m
    \x1b[96mDiscord:    \x1b[93marulgandhi\x1b[0m
    \x1b[96mSignal:     \x1b[93marulgandhi.69\x1b[0m
    \x1b[96mX:          \x1b[93m@arulgandhi69420\x1b[0m

    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating:         \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned:  \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs:           \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %:         \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages:       \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u ArulGandhi", 1, contin=True)

    t.toggle_show_cursor(False)
    t.gen_text(user_details_lines, 2, 5, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# programmer -- perfectionist, variable, chronically unfocused.",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
