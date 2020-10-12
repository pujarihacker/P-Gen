Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@pujarihacker 
noob-hackers
/
p-gen
1
155
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
p-gen/p-gen.py /
@noob-hackers
noob-hackers Update p-gen.py
Latest commit 7f55020 23 days ago
 History
 1 contributor
40 lines (34 sloc)  1.42 KB
  
import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""
         ██████╗        ██████╗ ███████╗███╗   ██╗
         ██╔══██╗      ██╔════╝ ██╔════╝████╗  ██║
         ██████╔╝█████╗██║  ███╗█████╗  ██╔██╗ ██║
         ██╔═══╝ ╚════╝██║   ██║██╔══╝  ██║╚██╗██║
         ██║           ╚██████╔╝███████╗██║ ╚████║
         ╚═╝            ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                   v 1.0
"""+b+red)

print (gren+b+"              <===[[ coded by Aanajney Pujari ]]===>"+b+gren)
print (" ")
print (yellow+b+"        <---( search on youtube Pujari Hacker )--->"+b+yellow)
print (" ")

length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (gren+b+" "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
