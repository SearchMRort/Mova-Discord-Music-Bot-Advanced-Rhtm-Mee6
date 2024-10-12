class Options:
    """
    Options for the bot, time and such
    """
    #how many days before purchased items are deleted
    AUTO_DELETE_AGE = 14
    #time of cleanup
    DAILY_CLEANUP_HOUR = 16
    DAILY_CLEANUP_MINUTE = 50
    TIMEZONE = 5
    #0 for False, 1 for true
    DST = 0
    #0 is Monday, so 5 is Saturday
    PING_DAY = 5
    #daily time to audit lists and fix reactions
