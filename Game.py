class ene (object):
	def __init__(self,name,hitpoints,sassy):
		self.name=name
		self.hitpoint=hitpoints
		self.sassy=sassy
	def __str__(self):
		return self.name
	def attack(self):
	    damage = 1
	    print "%s attacks! %d points of damage" % (self.name, damage)
	    return damage

print "Generating the world of MAGIC"
enemies= [ene("Tryptophan",1,"Not so"),ene("Nukey, The pore Complex",9001,"Extremely"),ene("Troll",10,"Very"),ene("Slime",1,"Don't Go There"),ene("Agonist Gradient",3,"Gradiently"),ene("LiCad",21,"Light Activatedly")]
print ("Super-Reticulating-Splines")
raw_input("Oh Yeah Done!.")

user_hp = 5

while (len(enemies)!=0):
	print "The following enemies are around"
	i=0;
	for x in enemies:
		print str(i)+":"+str(x) +" He is " + x.sassy +" sassy."
		i+=1
	try:
		b=int(raw_input("Who will you kick ?: "))
	except ValueError:
		print "That ain't a number boyeeee. If you don't play by the rules you can't play at all."
		quit()
	if b not in  xrange(0,len(enemies)):
		print "MISS"
	else:
		enemies[b].hitpoint-=1
		if (enemies[b].hitpoint==0):
			print str(enemies[b]) + " is now dead."
			enemies.remove(enemies[b])
		else:
			print str(enemies[b]) + " now has " + str(enemies[b].hitpoint) + " science points left."
			user_hp -= enemies[b].attack()
			if user_hp > 0:
			    print "You have %d science points left." % (user_hp)
			else:
			    print "You are dead now. That's not very sassy at all."
			    quit()
	resp=raw_input("Is this awesome?")
	print resp+"? Whateva..."
	raw_input("Hit any key to continue")
print "You win the ipqb retreat"
		
