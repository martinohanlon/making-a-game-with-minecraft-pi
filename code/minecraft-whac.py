#import the minecraft modules
import mcpi.minecraft as minecraft
import mcpi.block as block
#import random so you can create lights in random locations
import random
#import time so we can put delays into our program
import time

#create the connection
mc = minecraft.Minecraft.create()

mc.postToChat("Minecraft Whac-a-Block")

#get the position of the player
pos = mc.player.getTilePos()

#build the game board
mc.setBlocks(pos.x - 1, pos.y, pos.z + 3,
             pos.x + 1, pos.y + 2, pos.z + 3,
             block.STONE.id)

#post a message for the player
mc.postToChat("Get ready ...")
time.sleep(2)
mc.postToChat("Go")

#setup the variables
#how many blocks are lit
blocksLit = 0
#how many points has the player scored
points = 0

#loop until game over (when all the lights are lit)
while blocksLit < 9:

    #sleep for a small amount of time
    time.sleep(0.2)

    #turn off any lights which have been hit
    for hitBlock in mc.events.pollBlockHits():
        #was the block hit glowstone
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            #if it was, turn it back to STONE
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
            #reduce the number of lights lit
            blocksLit = blocksLit - 1
            #increase the points
            points = points + 1 

    #increase the number of lights lit
    blocksLit = blocksLit + 1
    #create the next light
    lightCreated = False
    while not lightCreated:
        xPos = pos.x + random.randint(-1,1)
        yPos = pos.y + random.randint(0,2)
        zPos = pos.z + 3

        #if the block is already glowstone, return to the top and try again
        # otherwise set it to the 
        if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
            #set the block to glowstone
            mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
            lightCreated = True
            #debug
            #print "light created x{} y{} z{}".format(xPos, yPos, zPos)

#display the points scored to the player
mc.postToChat("Game Over - points = " + str(points))
