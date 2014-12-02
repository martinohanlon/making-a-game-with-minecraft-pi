# Making a game with Minecraft Pi

Minecraft is a popular sandbox open world-building game. A free version of Minecraft is available for the Raspberry Pi; it also comes with a programming interface. This means you can write commands and scripts in Python code to build things in the game automatically. It's a great way to learn Python!  

If you have already completed ["Getting Started With Programming The Minecraft World"](http://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/) and want to do more, how about creating your own game in Minecraft, a "game in a game"!

![Minecraft Pi banner](images/minecraft-pi-banner.png)

## Whac-a-Block

The game you are going to create is called "Whac-a-Block", inspired by the original arcade game ["Whac-a-Mole"](http://en.wikipedia.org/wiki/Whac-A-Mole), the objective of the game is to whack (or hit them with a sword) the blocks that light up as glowstone and turn them back to stone.  You will earn points for each block you turn back to stone and the game is over when all the blocks have been turned into glowstone.

TODO - picture of whac-a-block

### Create the program

Open IDLE (not IDLE3) by using the icon on the desktop.

When the Python Shell appears, create a new program using `File > New Window`.  You may also want to save your program now using `File > Save`.

Import the python modules you are going to need for this program:
- mcpi.minecraft - needed to interact with Minecraft: Pi Edition
- mcpi.block - needed to work with Minecraft blocks
- random - used to create random numbers
- time - used to put delay into your program

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
```

Create a connection to Minecraft: Pi Edition and post a message to the chat window

```python
mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block")
```

You can run the program now, it wont do a much, but if everything is setup correctly you should see "Minecraft Whac-a-Mole" displayed in the minecraft chat window.

If you haven't done so already, startup Minecraft and create/open a world.
Run your program by clicking `Run > Run Module` in IDLE or pressing F5.
Any errors will appear in red in the Python Shell window.

TODO - picture of "minecraft whac-a-mole" in chat

### Build the game board

The next step is to create the game board, 3x3 stone blocks, which will turn randomly light up and turn into glowstone.

The game board will be created just in front of the player, so the first step is to get the players position using player.getTilePos().  

```python
pos = mc.player.getTilePos()
```

The position is then used with the setBlocks() function to create the game board out of stone.

TODO - picture of game board, showing position and the distances to the board

```python
mc.setBlocks(pos.x - 1, pos.y, pos.z,
             pos.x + 1, pos.y + 2, pos.z,
             block.STONE.id)
```

Run the program again you should see the game board appear directly infront of the player.

### Turn the blocks on

### Whack blocks

### Game over

### Stretch - Adding Game Play!




## API reference

For a more extensive documentation of functions and a full list of block IDs see an API reference at [stuffaboutcode.com](http://www.stuffaboutcode.com/p/minecraft-api-reference.html).
