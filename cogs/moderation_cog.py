import asyncio
import discord
from discord.ext import commands
from discord.utils import get
import json
import os

os.chdir("cogs")

with open('reports.json', encoding='utf-8') as f:
        try:
          report = json.load(f)
        except ValueError:
          report = {}
          report['users'] = []

class mod(commands.Cog):
    #warn command

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user:discord.User, *, reason):

      if not reason:
        await ctx.send("Please provide a reason")
        return
      reason = ' '.join(reason)
      for current_user in report['users']:
        if current_user['name'] == user.id:
          current_user['reasons'].append(reason)
          break
      else:
        report['users'].append({
          'name':user.id,
          'reasons': [reason,]
        })
        await ctx.send(f"<@{user.id}> has been warned by <@{ctx.author.id}> for {reason}!!\n||Senator Armstrong 1.1||")
      with open('reports.json','w+') as f:
        json.dump(report,f)
      
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx,user:discord.User):
        for current_user in report['users']:
          if user.name == current_user['name']:
            await ctx.send(f"{user.name} has been warned {len(current_user['reasons'])} times\n||Senator Armstrong 1.1||")
            break
        else:
          await ctx.send(f"{user.name} has never been warned\n||Senator Armstrong 1.1||")  

    #kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, user: discord.User):   
      await ctx.guild.kick(user)
      await ctx.send(f"User {user} has been kicked!\n||BLOB1.1||")      
    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User):
      await ctx.guild.ban(user)
      await ctx.send(f'User {user} has been banned!\n||Senator Armstrong 1.1||')
        
    #unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):
      if ctx.author.guild_permissions.ban_members:
        try:
          await ctx.guild.unban(user)
          await ctx.send(f"{user} was unbanned!\n||Senator Armstrong 1.1||")
        except discord.NotFound:
          await ctx.send(f"Couldn't find {user}")
      else:
        await ctx.send("Sorry man,")
        await ctx.send("You do not have permission to use this")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def poll(self, ctx, *, question):

      reactions = ["👍", "👎"]

      await ctx.channel.purge(limit=1)
      embed = discord.Embed(title=("Poll"), color=4624240)
      embed.add_field(name=f"{ctx.author} Asks:", value="balls")
      embed.add_field(name=f"{question}", value="balls")
      embed.add_field(name="React with 👍 for Yes and 👎 for No", value="balls")
      embed.add_field(name="||Senator Armstrong 1.1||", value="balls")

      m = await ctx.send(embed = embed)
      for name in reactions:
          emoji = get(ctx.guild.emojis, name=name)
          await m.add_reaction(emoji or name)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount:int):
      await ctx.channel.purge(limit=1)
      await ctx.send(f"Deleting {amount} messages...")
      await asyncio.sleep(2)
      await ctx.channel.purge(limit=1)
      await ctx.channel.purge(limit=amount)
      await ctx.send(f"Deleted {amount} messages\n||Senator Armstrong 1.1||")
      await asyncio.sleep(4)
      await ctx.channel.purge(limit=1)

    @kick.error
    async def kick_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          await ctx.send('I could not find that member...')
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry, You do not have permissions to run this command')

    @ban.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          await ctx.send('I could not find that member...')
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry, You do not have permissions to run this command')

    @unban.error
    async def unban_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          await ctx.send('I could not find that member...')
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry, You do not have permissions to run this command')

    @warn.error
    async def warn_eror(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        await ctx.send("I could not find that member...")
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, You do not have permissions to run this command")

    @purge.error
    async def purge_eror(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify number of messages to purge")
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, You do not have permissions to run this command")

  #cog
async def setup(bot):
  await bot.add_cog(mod(bot))