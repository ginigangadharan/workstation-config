from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 251 # Grey78	#c6c6c6	rgb(198,198,198)	hsl(0,0%,77%)
    USERNAME_BG = 27 #17  # NavyBlue	#00005f	rgb(0,0,95)	hsl(240,100%,18%)
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 251
    HOSTNAME_BG = 25

    HOME_SPECIAL_DISPLAY = True
    PATH_BG = 125 #8  # dark grey
    PATH_FG = 250 #7  # light grey
    CWD_FG = 250 #15  # white
    SEPARATOR_FG = 7

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 1   # red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 22	# DarkGreen	#005f00	rgb(0,95,0)	hsl(120,100%,18%)
    CMD_PASSED_FG = 251 # Grey78	#c6c6c6	rgb(198,198,198)	hsl(0,0%,77%)
    CMD_FAILED_BG = 124	# Red3	#af0000	rgb(175,0,0)	hsl(0,100%,34%)
    CMD_FAILED_FG = 11	# Yellow (SYSTEM)	#ffff00	rgb(255,255,0)	hsl(60,100%,50%)

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 178	    # DeepSkyBlue4	#005faf	rgb(0,95,175)	hsl(07,100%,34%)
    VIRTUAL_ENV_FG = 234	# Yellow3	#d7d700	rgb(215,215,0)	hsl(60,100%,42%)

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
    
    BATTERY_NORMAL_BG = 46
    BATTERY_NORMAL_FG = 0
    BATTERY_LOW_BG = 202
    BATTERY_LOW_FG = 0