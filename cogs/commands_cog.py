from discord.ext import commands

#adding some commands
class general(commands.Cog):
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def shutdown(self, context):
    bot = context.bot
    await context.send("Shutting Down!")
    await bot.close()

  @commands.command()
  async def yt(self, ctx):
    await ctx.send("Spaceyy64 - https://www.youtube.com/channel/UCo-oiU4b2WhgG1Bbcha0h3A")

  @commands.command()
  async def about(self,ctx):
    await ctx.send("Hey! I am BLOB, a discord bot created by Spaceyy64#0648, Adding new features soon!\n||Current BLOB version - PRE-RELEASE 1.0.3||")

  @commands.command()
  async def updates(self,ctx):
    await ctx.send("""
    **BLOB Has been updated to V1.1!**
    __Changes in the update__:-

   *__General Commands__*
1) Updated the `help` command
2) Added the `about` command (Use `help` for more info)
3) Added `version` command (Use `help` for more info)
4) Added `server` command (Use `help` for more info)

   *__Moderator Commands__*
1) Added `warn` system (Use `help` for more info)
2) Added `poll` system (Use `help` for more info)
3) Added `purge` command (Use `help` for more info)

   *__Bot Updates__*
1) Bot is faster overall
2) Slowly changing to embeds instead of messages
3) The bot now notifies you if a command is wrong, earlier used to give errors in the console
4) The bot now notifies you about missing arguements or wrong arguements to commands, earlier used to give **__BIG AND ANNOYING__** errors in the console
5) The bot has been made more secure from the risk of hacking
""")
  
  @commands.command()
  async def help(self,ctx):
    await ctx.send("""
      **__General Commands__**:-
    `help` - Opens this menu
    `about` - Shows bot info
    `yt` - Shows the yt links of bot owner(s)
    `updates` - Shows the update logs
    `echo <message>` - Repeats your message
    `version` - Shows the bot version
    `server` - Gives invite to BLOB's Official Discord Server
   **__Moderator Commands__**:-
    `warn <user>` Warns a user
    `warnings <user>` Checks the warning of a specific user
    `kick <reason>` - Kicks a user
    `ban <reason>` - bans a user
    `unban <reason>` - Unbans a user
    `poll <question>` - Makes a Yes or No Poll
    `purge <amount>` - Deletes a specific number of messages

    *||Senator Armstrong 1.1||*
    """
    )

  @commands.command()
  async def echo(self, ctx,*,arg):
    await ctx.send(arg)

  @commands.command()
  async def version(self, ctx):
    await ctx.send("Current bot version 1.1")

  @commands.command()
  async def server(self, ctx):
    await ctx.send("Join the server to get bot updates and pre-releases!\nhttps://dsc.gg/theakhandbharat \n||Senator Armstrong 1.1||")
#adding the cog
async def setup(bot):
  await bot.add_cog(general(bot))