class script(object):
    START_TXT = """𝘏𝘢𝘪 {},
𝘔𝘺 𝘕𝘢𝘮𝘦 𝘐𝘴 <a href=https://t.me/{}>{}</a>, 𝘐 𝘊𝘢𝘯 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴 𝘑𝘶𝘴𝘵 𝘈𝘥𝘥 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘈𝘯𝘥 𝘌𝘯𝘫𝘰𝘺 😍"""
    HELP_TXT = """𝘏𝘦𝘺 {}
𝘏𝘦𝘳𝘦 𝘐𝘴 𝘛𝘩𝘦 𝘏𝘦𝘭𝘱 𝘍𝘰𝘳 𝘔𝘺 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴."""
    ABOUT_TXT = """✯ 𝘔𝘺 𝘕𝘢𝘮𝘦: {}
✯ 𝘊𝘳𝘦𝘢𝘵𝘰𝘳: https://t.me/Sovel_jaison>SOVEL JAISON ⚡️</a>
✯ 𝘓𝘪𝘣𝘳𝘢𝘳𝘺: 𝘗𝘺𝘳𝘰𝘨𝘳𝘢𝘮
✯ 𝘓𝘢𝘯𝘨𝘶𝘢𝘨𝘦: 𝘗𝘺𝘵𝘩𝘰𝘯 3
✯ 𝘋𝘢𝘵𝘢 𝘉𝘢𝘴𝘦: 𝘔𝘰𝘯𝘨𝘰 𝘋𝘉
✯ 𝘉𝘰𝘵 𝘚𝘦𝘳𝘷𝘦𝘳: 𝘏𝘦𝘳𝘰𝘬𝘶
✯ 𝘉𝘶𝘪𝘭𝘥 𝘚𝘵𝘢𝘵𝘶𝘴: 𝘝1.0.1[𝘉𝘌𝘛𝘈]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝘌𝘷𝘢 𝘔𝘢𝘳𝘪𝘢 𝘪𝘴 𝘢 𝘰𝘱𝘦𝘯 𝘴𝘰𝘶𝘳𝘤𝘦 𝘱𝘳𝘰𝘫𝘦𝘤𝘵. 
- 𝘚𝘰𝘶𝘳𝘤𝘦 - https://t.me/cinemahub00  

<b>𝘊𝘳𝘦𝘥𝘪𝘵𝘴:</b>
- <a href=https://t.me/Sovel_jaison>SOVEL JAISON⚡️</a>"""
    MANUELFILTER_TXT = """𝘏𝘦𝘭𝘱: <b>Filters</b>

- 𝘍𝘪𝘭𝘵𝘦𝘳 𝘪𝘴 𝘵𝘩𝘦 𝘧𝘦𝘢𝘵𝘶𝘳𝘦 𝘸𝘦𝘳𝘦 𝘶𝘴𝘦𝘳𝘴 𝘤𝘢𝘯 𝘴𝘦𝘵 𝘢𝘶𝘵𝘰𝘮𝘢𝘵𝘦𝘥 𝘳𝘦𝘱𝘭𝘪𝘦𝘴 𝘧𝘰𝘳 𝘢 𝘱𝘢𝘳𝘵𝘪𝘤𝘶𝘭𝘢𝘳 𝘬𝘦𝘺𝘸𝘰𝘳𝘥 𝘢𝘯𝘥 𝘓𝘪𝘴𝘢 𝘸𝘪𝘭𝘭 𝘳𝘦𝘴𝘱𝘰𝘯𝘥 𝘸𝘩𝘦𝘯𝘦𝘷𝘦𝘳 𝘢 𝘬𝘦𝘺𝘸𝘰𝘳𝘥 𝘪𝘴 𝘧𝘰𝘶𝘯𝘥 𝘵𝘩𝘦 𝘮𝘦𝘴𝘴𝘢𝘨𝘦
<b>NOTE:</b>
1. 𝘓𝘪𝘴𝘢 𝘴𝘩𝘰𝘶𝘭𝘥 𝘩𝘢𝘷𝘦 𝘢𝘥𝘮𝘪𝘯 𝘱𝘳𝘪𝘷𝘪𝘭𝘭𝘢𝘨𝘦.
2. 𝘰𝘯𝘭𝘺 𝘢𝘥𝘮𝘪𝘯𝘴 𝘤𝘢𝘯 𝘢𝘥𝘥 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 𝘪𝘯 𝘢 𝘤𝘩𝘢𝘵.
3. 𝘢𝘭𝘦𝘳𝘵 𝘣𝘶𝘵𝘵𝘰𝘯𝘴 𝘩𝘢𝘷𝘦 𝘢 𝘭𝘪𝘮𝘪𝘵 𝘰𝘧 64 𝘤𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳𝘴.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝘓𝘪𝘴𝘢 𝘚𝘶𝘱𝘱𝘰𝘳𝘵𝘴 𝘣𝘰𝘵𝘩 𝘶𝘳𝘭 𝘢𝘯𝘥 𝘢𝘭𝘦𝘳𝘵 𝘪𝘯𝘭𝘪𝘯𝘦 𝘣𝘶𝘵𝘵𝘰𝘯𝘴.

<b>NOTE:</b>
1. 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘸𝘪𝘭𝘭 𝘯𝘰𝘵 𝘢𝘭𝘭𝘰𝘸𝘴 𝘺𝘰𝘶 𝘵𝘰 𝘴𝘦𝘯𝘥 𝘣𝘶𝘵𝘵𝘰𝘯𝘴 𝘸𝘪𝘵𝘩𝘰𝘶𝘵 𝘢𝘯𝘺 𝘤𝘰𝘯𝘵𝘦𝘯𝘵, 𝘴𝘰 𝘤𝘰𝘯𝘵𝘦𝘯𝘵 𝘪𝘴 𝘮𝘢𝘯𝘥𝘢𝘵𝘰𝘳𝘺.
2. 𝘓𝘪𝘴𝘢 𝘴𝘶𝘱𝘱𝘰𝘳𝘵𝘴 𝘣𝘶𝘵𝘵𝘰𝘯𝘴 𝘸𝘪𝘵𝘩 𝘢𝘯𝘺 𝘵𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘮𝘦𝘥𝘪𝘢 𝘵𝘺𝘱𝘦.
3. 𝘉𝘶𝘵𝘵𝘰𝘯𝘴 𝘴𝘩𝘰𝘶𝘭𝘥 𝘣𝘦 𝘱𝘳𝘰𝘱𝘦𝘳𝘭𝘺 𝘱𝘢𝘳𝘴𝘦𝘥 𝘢𝘴 𝘮𝘢𝘳𝘬𝘥𝘰𝘸𝘯 𝘧𝘰𝘳𝘮𝘢𝘵

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝘏𝘦𝘭𝘱: <b>Auto Filter</b>

<b>NOTE:</b>
1. 𝘔𝘢𝘬𝘦 𝘮𝘦 𝘵𝘩𝘦 𝘢𝘥𝘮𝘪𝘯 𝘰𝘧 𝘺𝘰𝘶𝘳 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 𝘪𝘧 𝘪𝘵'𝘴 𝘱𝘳𝘪𝘷𝘢𝘵𝘦.
2. 𝘮𝘢𝘬𝘦 𝘴𝘶𝘳𝘦 𝘵𝘩𝘢𝘵 𝘺𝘰𝘶𝘳 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 𝘥𝘰𝘦𝘴 𝘯𝘰𝘵 𝘤𝘰𝘯𝘵𝘢𝘪𝘯𝘴 𝘤𝘢𝘮𝘳𝘪𝘱𝘴, 𝘱𝘰𝘳𝘯 𝘢𝘯𝘥 𝘧𝘢𝘬𝘦 𝘧𝘪𝘭𝘦𝘴.
3. 𝘍𝘰𝘳𝘸𝘢𝘳𝘥 𝘵𝘩𝘦 𝘭𝘢𝘴𝘵 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘵𝘰 𝘮𝘦 𝘸𝘪𝘵𝘩 𝘲𝘶𝘰𝘵𝘦𝘴.
 I'll 𝘢𝘥𝘥 𝘢𝘭𝘭 𝘵𝘩𝘦 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘵𝘩𝘢𝘵 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 𝘵𝘰 𝘮𝘺 𝘥𝘣."""
    CONNECTION_TXT = """𝘏𝘦𝘭𝘱: <b>Connections</b>

- 𝘜𝘴𝘦𝘥 𝘵𝘰 𝘤𝘰𝘯𝘯𝘦𝘤𝘵 𝘣𝘰𝘵 𝘵𝘰 𝘗𝘔 𝘧𝘰𝘳 𝘮𝘢𝘯𝘢𝘨𝘪𝘯𝘨 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 
- 𝘪𝘵 𝘩𝘦𝘭𝘱𝘴 𝘵𝘰 𝘢𝘷𝘰𝘪𝘥 𝘴𝘱𝘢𝘮𝘮𝘪𝘯𝘨 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱𝘴.

<b>NOTE:</b>
1. 𝘖𝘯𝘭𝘺 𝘢𝘥𝘮𝘪𝘯𝘴 𝘤𝘢𝘯 𝘢𝘥𝘥 𝘢 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘪𝘰𝘯.
2. 𝘚𝘦𝘯𝘥 <code>/connect</code> 𝘧𝘰𝘳 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘪𝘯𝘨 𝘮𝘦 𝘵𝘰 𝘶𝘳 𝘗𝘔

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝘏𝘦𝘭𝘱: <b>Extra Modules</b>

<b>NOTE:</b>
𝘵𝘩𝘦𝘴𝘦 𝘢𝘳𝘦 𝘵𝘩𝘦 𝘦𝘹𝘵𝘳𝘢 𝘧𝘦𝘢𝘵𝘶𝘳𝘦𝘴 𝘰𝘧 𝘓𝘪𝘴𝘢

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
𝘛𝘩𝘪𝘴 𝘮𝘰𝘥𝘶𝘭𝘦 𝘰𝘯𝘭𝘺 𝘸𝘰𝘳𝘬𝘴 𝘧𝘰𝘳 𝘮𝘺 𝘢𝘥𝘮𝘪𝘯𝘴

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝘛𝘰𝘵𝘢𝘭 𝘍𝘪𝘭𝘦𝘴: <code>{}</code>
★ 𝘛𝘰𝘵𝘢𝘭 𝘜𝘴𝘦𝘳𝘴: <code>{}</code>
★ 𝘛𝘰𝘵𝘢𝘭 𝘊𝘩𝘢𝘵𝘴: <code>{}</code>
★ 𝘜𝘴𝘦𝘥 𝘚𝘵𝘰𝘳𝘢𝘨𝘦: <code>{}</code> 𝙼𝚒𝙱
★ 𝘍𝘳𝘦𝘦 𝘚𝘵𝘰𝘳𝘢𝘨𝘦: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
