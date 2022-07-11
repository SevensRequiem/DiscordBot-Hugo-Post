import random
import discord
from datetime import datetime
import os.path

from discord.ext import commands

class logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def logs(self, ctx):    
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        print("-User Name-")
        user_name = ctx.author.name
        print(user_name)
        print("-----")

        await ctx.send('Please enter a title.')
        title_msg = await self.bot.wait_for("message",check=check, timeout=30)
        print("-Title-")
        print(f''+ str(title_msg.content) +'')
        print("-----")

        await ctx.send('Please enter the changelog description.')
        desc_msg = await self.bot.wait_for("message",check=check, timeout=30)
        print("-Description-")
        print(f''+ str(desc_msg.content) +'')
        print("-----")

        await ctx.send('Please enter the changelog. (Paragraph or simple line)')
        txt_msg = await self.bot.wait_for("message",check=check, timeout=30)
        print("-ChangelogText-")
        print(f''+ str(txt_msg.content) +'')
        print("-----")


        #embed = discord.Embed(title=''+ str(title_msg.content) +'', description=''+ str(txt_msg.content) +'')
        #await ctx.send(embed=embed)

        now = datetime.today()
        print("now =", now)
        dt_string = now.strftime("%y-%m-%d %H:%M:%S")
        date = now.strftime("%y-%m-%d")
        file_title = title_msg.content
        file_title = file_title.replace(' ','_')
        print(file_title)
        dt_file = dt_string
        print(dt_file)

        save_path = "C:/Hugo/sites/anetblog/content/posts/" #Hugo posts Directory
        completeName = os.path.join(save_path+date+"_"+file_title+".md")
        cn_r = completeName
        cn_r = cn_r.replace (' ','_')
        with open(cn_r, mode = "w") as f:
            f.write("---\nauthor: "+ str(user_name) +"\ntitle: "+ str(title_msg.content) +"\ndate: "+ str(now) +"\ndescription: "+ str(desc_msg.content) +"\n---\n"+ str(txt_msg.content) +"")
            print("-----")
            print("POSTED!")
            print("-----")
        await ctx.send('Posted!')
        embed = discord.Embed(title=''+ str(title_msg.content) +'', description=''+ str(desc_msg.content) +'')
        embed.add_field(name="Log:", value=''+ str(txt_msg.content) +'', inline=False)
        embed.set_footer(text="Posted at: "+ dt_string +"")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(logs(bot))
