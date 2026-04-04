\# Netspector



A lightweight network inspection tool built from scratch to explore port scanning, host discovery, and network analysis techniques.



\---



\## Overview



\*\*Netspector\*\* is a simple command-line tool designed to perform basic network reconnaissance tasks.

It focuses on core networking concepts while remaining fast, minimal, and dependency-free.



This project is built for:



\* Learning low-level networking

\* Understanding how port scanners work

\* Practicing Python in real-world scenarios

\* Building a strong cybersecurity portfolio



\---



\## Features



\* TCP port scanning (single port or range)

\* Basic UDP port scanning

\* Host reachability check (ping)

\* RTT (latency) measurement

\* Subnet IP enumeration (CIDR support)

\* Private IP detection (RFC 1918)

\* Local listening ports discovery

\* Domain name resolution

\* Interactive CLI (REPL mode)

\* Colored terminal output

\* No external dependencies (Python standard library only)



\---



\## Project Structure



\---

<style>

&#x20; .tree-terminal {

&#x20;   background: #1a1a1a;

&#x20;   border-radius: 10px;

&#x20;   overflow: hidden;

&#x20;   font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;

&#x20;   font-size: 13.5px;

&#x20;   margin: 16px 0;

&#x20; }

&#x20; .tree-titlebar {

&#x20;   background: #2a2a2a;

&#x20;   padding: 10px 14px;

&#x20;   display: flex;

&#x20;   align-items: center;

&#x20;   gap: 8px;

&#x20;   border-bottom: 1px solid #333;

&#x20; }

&#x20; .tree-dot {

&#x20;   width: 12px;

&#x20;   height: 12px;

&#x20;   border-radius: 50%;

&#x20; }

&#x20; .tree-dot-red { background: #ff5f57; }

&#x20; .tree-dot-yellow { background: #febc2e; }

&#x20; .tree-dot-green { background: #28c840; }

&#x20; .tree-tab {

&#x20;   margin-left: 12px;

&#x20;   font-size: 12px;

&#x20;   color: #888;

&#x20;   background: #1a1a1a;

&#x20;   padding: 3px 12px;

&#x20;   border-radius: 4px;

&#x20; }

&#x20; .tree-body {

&#x20;   padding: 18px 20px;

&#x20;   color: #e0e0e0;

&#x20;   line-height: 1.6;

&#x20; }

&#x20; .tree-body .dir {

&#x20;   color: #4dabf7;

&#x20; }

&#x20; .tree-body .file {

&#x20;   color: #e0e0e0;

&#x20; }

&#x20; .tree-body .tree-line {

&#x20;   white-space: pre;

&#x20;   font-family: inherit;

&#x20; }

</style>



<div class="tree-terminal">

&#x20; <div class="tree-titlebar">

&#x20;   <div class="tree-dot tree-dot-red"></div>

&#x20;   <div class="tree-dot tree-dot-yellow"></div>

&#x20;   <div class="tree-dot tree-dot-green"></div>

&#x20;   <span class="tree-tab">Project Structure</span>

&#x20; </div>

&#x20; <div class="tree-body">

&#x20;   <div class="tree-line"><span class="dir">netspector/</span></div>

&#x20;   <div class="tree-line">├── <span class="dir">scanner/</span></div>

&#x20;   <div class="tree-line">│   ├── <span class="dir">core/</span></div>

&#x20;   <div class="tree-line">│   │   └── <span class="file">port\_scanner.py</span></div>

&#x20;   <div class="tree-line">│   └── <span class="dir">utils/</span></div>

&#x20;   <div class="tree-line">│       ├── <span class="file">ip\_utils.py</span></div>

&#x20;   <div class="tree-line">│       └── <span class="file">port\_utils.py</span></div>

&#x20;   <div class="tree-line">├── <span class="file">main.py</span></div>

&#x20;   <div class="tree-line">├── <span class="file">README.md</span></div>

&#x20;   <div class="tree-line">└── <span class="file">cli.py</span></div>

&#x20; </div>

</div>

\---



\## Installation



```bash

git clone https://github.com/Red-Warrior-hkg/Netspector.git

cd Netspector

```



\### Requirements



\* Python 3.6+

\* No additional packages required



\---



\## Usage



\### Interactive Mode (Recommended)



```bash

python main.py

```



You will enter the Netspector shell:



```

netspector>

```



Available commands:



\* `help` → show available commands

\* `exit` → quit the program



\---



\### One-shot Mode



```bash

python main.py <command> \[options]

```



\## Cheat Sheet

<style>

&#x20; \* { box-sizing: border-box; margin: 0; padding: 0; }

&#x20; .terminal { background: #1a1a1a; border-radius: 10px; overflow: hidden; font-family: var(--font-mono); font-size: 13.5px; }

&#x20; .titlebar { background: #2a2a2a; padding: 10px 14px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid #333; }

&#x20; .dot { width: 12px; height: 12px; border-radius: 50%; }

&#x20; .d-red { background: #ff5f57; } .d-yellow { background: #febc2e; } .d-green { background: #28c840; }

&#x20; .tab { margin-left: 12px; font-size: 12px; color: #888; background: #1a1a1a; padding: 3px 12px; border-radius: 4px; }

&#x20; .body { padding: 18px 20px; line-height: 2; }

&#x20; .comment { color: #6a6a6a; }

&#x20; .cmd { color: #e0e0e0; }

&#x20; .kw { color: #e0e0e0; }

&#x20; .ip { color: #e8834a; }

&#x20; .flag { color: #e8834a; }

&#x20; .sep { display: block; height: 10px; }

</style>



<div class="terminal">

&#x20; <div class="titlebar">

&#x20;   <div class="dot d-red"></div>

&#x20;   <div class="dot d-yellow"></div>

&#x20;   <div class="dot d-green"></div>

&#x20;   <span class="tab">Bash</span>

&#x20; </div>

&#x20; <div class="body">



&#x20;   <span class="comment"># scan default ports (1–1000)</span><br>

&#x20;   <span class="kw">python main.py scan</span> <span class="ip">127.0.0.1</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># scan custom port range</span><br>

&#x20;   <span class="kw">python main.py scan</span> <span class="ip">192.168.1.1</span> <span class="flag">--start 20 --end 100</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># single TCP port</span><br>

&#x20;   <span class="kw">python main.py scan-port</span> <span class="ip">8.8.8.8</span> <span class="flag">53</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># UDP scan</span><br>

&#x20;   <span class="kw">python main.py udp</span> <span class="ip">192.168.1.1</span> <span class="flag">--max-port 200</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># ping (ICMP reachability)</span><br>

&#x20;   <span class="kw">python main.py ping</span> <span class="ip">8.8.8.8</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># round-trip time to a port</span><br>

&#x20;   <span class="kw">python main.py rtt</span> <span class="ip">google.com</span> <span class="flag">443</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># list all IPs in a subnet</span><br>

&#x20;   <span class="kw">python main.py subnet</span> <span class="ip">192.168.1.0/24</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># check if IP is private (RFC 1918)</span><br>

&#x20;   <span class="kw">python main.py private</span> <span class="ip">10.0.0.1</span><br>

&#x20;   <span class="sep"></span>



&#x20;   <span class="comment"># local listening ports</span><br>

&#x20;   <span class="kw">python main.py listening</span><br>



&#x20; </div>

</div>



\### Examples



```bash

python main.py scan 192.168.1.1 --start 1 --end 100

python main.py scan-port 192.168.1.1 80

python main.py udp 192.168.1.1 --max-port 100

python main.py ping 192.168.1.1

python main.py rtt google.com 80

python main.py subnet 192.168.1.0/24

python main.py private 192.168.1.1

python main.py listening

```



\---



Planned features:



\* Simple web interface for commands

\* Command examples with explanations

\* Quick reference for networking concepts

\* Visual representation of scans



\## How It Works



\* \*\*TCP Scan\*\*: Uses full TCP connections (3-way handshake)

\* \*\*UDP Scan\*\*: Sends packets and waits for responses

\* \*\*Ping\*\*: Uses system commands depending on the OS

\* \*\*RTT\*\*: Measures connection time to a TCP port

\* \*\*Subnet\*\*: Expands CIDR into usable IP addresses

\* \*\*Listening Ports\*\*: Uses system tools like `netstat`, `ss`, or `lsof`



\---



\## Limitations



\* Uses full TCP connect (no SYN scan)

\* UDP scanning is unreliable by design

\* No OS fingerprinting

\* Not intended to replace Nmap



\---





