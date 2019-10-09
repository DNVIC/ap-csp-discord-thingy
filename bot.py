import discord
from time import sleep


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
usersdone = 0
users = 0
doneone = 0
donetwo = 0
donethree = 0
donefour = 0
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    x = 0
    if message.content.startswith("!start"):
        while x < 25:
            
            if x == 0:
                usersdone = 0
                await message.channel.send('Q1: What types of data/files might you typically encounter that measure data in bytes?')
                await message.channel.send('1: PDF file')
                await message.channel.send('2: Plaintext file')
                await message.channel.send('3: Video file')
                await message.channel.send('4: EXE file')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            
            if x == 1:
                usersdone = 0
                await message.channel.send('Q2: How much more information can an extra byte store?')
                await message.channel.send('1: 3 times')
                await message.channel.send('2: 4 times')
                await message.channel.send('3: 1.5 times')
                await message.channel.send('4: 2 times')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: 2 times')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0        
            
            
            if x == 2:
                usersdone = 0
                await message.channel.send('Q3: Which is larger? A 1 million character plaintext file or a 3 minute long low quality video?')
                await message.channel.send('1: Plaintext')
                await message.channel.send('2: Video')
                await message.channel.send('Answer with !1, or !2')
                
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 3:
                usersdone = 0
                await message.channel.send('Q4: How does a raster image compare to a vector image')
                await message.channel.send('1: A raster image is related to a raspberry')
                await message.channel.send('2: A raster image is made of pixels while a vector image is made of formulas')
                await message.channel.send('3: A vector image can sometimes transmit disease')
                await message.channel.send('4: A vector image is made of pixels while a raster image is made of formulas')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 4:
                usersdone = 0
                await message.channel.send('Q5: Which info would usually be conveyed in metadata?')
                await message.channel.send('1: The color of certain pixels in the image')
                await message.channel.send('2: The size of the image')
                await message.channel.send('3: Where the image was downloaded')
                await message.channel.send('4: How many people downloaded the image')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 5:
                usersdone = 0
                await message.channel.send('Q6: What is an advantage of having more bits per pixel')
                await message.channel.send('1: Reduced file size per pixel')
                await message.channel.send('2: Better compression per pixel')
                await message.channel.send('3: More bits per pixel is the difference between a vector and raster image')
                await message.channel.send('4: More color depth')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 6:
                usersdone = 0
                await message.channel.send('Q7: What are the base colors of light?')
                await message.channel.send('1: Red, Green, and Blue')
                await message.channel.send('2: Red, Blue, and Yellow')
                await message.channel.send('3: Cyan, Magenta, and Yellow')
                await message.channel.send('4: Orange, Purple, and Green')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 7:
                usersdone = 0
                await message.channel.send('Q8 & 9: Why are the printer\'s colors the secondary colors of RGB?')
                await message.channel.send('1: The printer wants to feel unique')
                await message.channel.send('2: ')
                await message.channel.send('3: Cyan, Magenta, and Yellow')
                await message.channel.send('4: Orange, Purple, and Green')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 8:
                usersdone = 0
                await message.channel.send('Q10: What are the base colors of light?')
                await message.channel.send('1: Red, Green, and Blue')
                await message.channel.send('2: Red, Blue, and Yellow')
                await message.channel.send('3: Cyan, Magenta, and Yellow')
                await message.channel.send('4: Orange, Purple, and Green')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 9:
                usersdone = 0
                await message.channel.send('Q11: What are the base colors of light?')
                await message.channel.send('1: Red, Green, and Blue')
                await message.channel.send('2: Red, Blue, and Yellow')
                await message.channel.send('3: Cyan, Magenta, and Yellow')
                await message.channel.send('4: Orange, Purple, and Green')
                await message.channel.send('Answer with !1, !2, !3, or !4')
            if x == 10:
                usersdone = 0
                await message.channel.send('Q12: What is 101110101101 in hex')
                await message.channel.send('1: BAD')
                await message.channel.send('2: FAD')
                await message.channel.send('3: CAD')
                await message.channel.send('4: RAD')
                await message.channel.send('Answer with !1, !2, !3, or !4')
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
            if x == 11:
                usersdone = 0
                await message.channel.send('Q13: What are the base colors of light?')
                await message.channel.send('1: Red, Green, and Blue')
                await message.channel.send('2: Red, Blue, and Yellow')
                await message.channel.send('3: Cyan, Magenta, and Yellow')
                await message.channel.send('4: Orange, Purple, and Green')
                await message.channel.send('**Answer with !1, !2, !3, or !4**')
            
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0
                
                
                while usersdone < users:
                    sleep(1)
                await message.channel.send('Answer: Plain text file')
                x += 1
                doneone = 0
                donetwo = 0
                donethree = 0
                donefour = 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!join")
        users += 1

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!1" or "!2" or "!3" or "!4")
        usersdone += 1
        if message.content.startswith("!1"):
            doneone += 1
        else if message.content.startswith("!2"):
            donetwo += 1
        else if message.content.startswith("!3"):
            donethree += 1
        else if message.content.startswith("!4"):
            donefour += 1
        
client = MyClient()
client.run('token goes here')
