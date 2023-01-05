import pyrogram ,os
from pyrogram import *
#from hyxer import hyxer
hyxer = Client
print(hyxer)
@hyxer.on_message(filters.command("فحص","."))
async def _(hyxer,msg):
 await msg.edit('''
★ 𝗛𝘆𝘅𝗲𝗿 𝗦𝗼𝘂𝗿𝗰𝗲
 - - - - - - - - 
➪ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : 1.0
➪ 𝙿𝚈𝚃𝙷𝙾𝙽 : 3.9
➪ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @Hyxer
➪ 𝙳𝙴𝚅 : @Dar4k
''')
@hyxer.on_message(filters.command(["الاوامر","اوامر"],"."))
async def _(hyxer,msg):
 await msg.edit('''
1 ) .مؤقت + عدد الثواني +عدد التكرار + كليشتك
2 ) .فحص
''')

@hyxer.on_message(filters.command("كودي","."))
async def _(hyxer,msg):
 session =await hyxer.export_session_string()
 await msg.edit(session)
@hyxer.on_message(filters.command("مؤقت","."))
async def _(hyxer,msg):
 masg = "".join(msg.text.split(maxsplit=1)[1:]).split(" ", 2)
 sleep_time = masg[0]
 tries = masg[1]
 text = masg[2]
 await spammer(msg,tries,sleep_time,text)

async def spammer(msg,tries,sleep_time,text):
 for i in range(int(tries)):
  if (msg.reply_to_message) == None :
   await hyxer.send_message(msg.chat.id,text)
  else :
   await hyxer.send_message(msg.chat.id,text,reply_to_message_id=msg.reply_to_message.id)
  await asyncio.sleep(int(sleep_time))