# Security Papers

## Architecture
- [2019-Arm_Architecture_Reference_Manual](Architecture/2019-Arm_Architecture_Reference_Manual)
- [2019-Intel_64_and_IA-32_Architectures_Software_Developers_Manual](Architecture/2019-Intel_64_and_IA-32_Architectures_Software_Developers_Manual)

## IOT
- [2019_CryptoREX_Large-scale_Analysis_of_Cryptographic_Misuse_in_IoT_Devices](IoT/2019_CryptoREX_Large-scale_Analysis_of_Cryptographic_Misuse_in_IoT_Devices)
- [2019-Firmware_Extraction_hacklu](IoT/2019-Firmware_Extraction_hacklu)


---

# Binary Reading List
*Things I know and will have to know about binaries.*

### Books
- [Reverse Engineering for Beginners](https://beginners.re/) -- by Dennis Yurichev

### Courses
- [Modern Binary Exploitation](http://security.cs.rpi.edu/courses/binexp-spring2015/) -- by RPISEC
- [FuzzySecurity](https://www.fuzzysecurity.com/tutorials.html)
- [Advanced Digital Forensics and Data Reverse Engineering](http://www.utdallas.edu/~zxl111930/fall2011.html)
- [CNIT 127: Exploit Development](https://samsclass.info/127/127_F15.shtml)

### ROP
- [一步一步学ROP](https://github.com/zhengmin1989/ROP_STEP_BY_STEP) -- by 蒸米
  - [一步一步学ROP之linux_x86篇](http://www.vuln.cn/6645)
  - [一步一步学ROP之linux_x64篇](http://www.vuln.cn/6644)
  - [一步一步学ROP之gadgets和2free篇](http://www.vuln.cn/6643)
  - [一步一步学ROP之Android ARM 32位篇](http://www.vuln.cn/6642)
- [ROP Emporium](https://ropemporium.com)
- [Intro to ROP: ROP Emporium — Split](https://medium.com/@iseethieves/intro-to-rop-rop-emporium-split-9b2ec6d4db08)
- [64-bit Linux Return-Oriented Programming](http://crypto.stanford.edu/~blynn/rop/) -- by Ben Lynn
- [Introduction to return oriented programming (ROP)](http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html) -- by Alex Reece
- [现代栈溢出利用技术基础：ROP](http://bobao.360.cn/learning/detail/3694.html) -- by beswing
- [Return-oriented Programming:Exploitation without Code Injection](https://www.blackhat.com/presentations/bh-usa-08/Shacham/BH_US_08_Shacham_Return_Oriented_Programming.pdf) -- by Erik Buchanan
- [Return-Oriented Programming:Systems, Languages, and Applications](https://cseweb.ucsd.edu/~hovav/dist/rop.pdf) -- by RYAN ROEMER
- [Blind Return Oriented Programming (BROP)](http://www.scs.stanford.edu/brop/) -- by A. Bittau
- [Finding Function's Load Address](http://uaf.io/exploitation/misc/2016/04/02/Finding-Functions.html)
- [ELF如何摧毁圣诞——通过ELF动态装载机制进行漏洞利用](http://www.inforsec.org/wp/wp-content/uploads/2016/01/sec15-paper-di-frederico.pdf)
- [ROP之return to dl-resolve](http://rk700.github.io/2015/08/09/return-to-dl-resolve/)
- [BROP Attack之Nginx远程代码执行漏洞分析及利用](http://bobao.360.cn/learning/detail/3415.html) -- by k0shl
- [Blind Return Oriented Programming (BROP) Attack](http://ytliu.info/blog/2014/05/31/blind-return-oriented-programming-brop-attack-yi/) -- by Liu Yutao
- [如何在32位系统中使用ROP+Return-to-dl来绕过ASLR+DEP](http://www.freebuf.com/articles/system/149214.html)

### Heap
- [Syscalls used by malloc](https://sploitfun.wordpress.com/2015/02/11/syscalls-used-by-malloc/) -- by sploitfun
- [Understanding glibc malloc](https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc/comment-page-1/?blogsub=confirming#subscribe-blog%E3%80%82)
  - [Linux下的堆管理](http://tyrande000.how/2016/02/20/linux%E4%B8%8B%E7%9A%84%E5%A0%86%E7%AE%A1%E7%90%86/)
- [Heap Exploitation ~ Abusing Use-After-Free](https://0x00sec.org/t/heap-exploitation-abusing-use-after-free/3580) -- by r3kt
- [Double Free浅析](http://www.vuln.cn/6172) -- by explorer
- [PWN之堆内存管理](https://paper.seebug.org/255/) -- by jmpews
- [逆向安全系列：Use After Free漏洞浅析](http://bobao.360.cn/learning/detail/3379.html) -- by ray_cp
- [堆溢出漏洞简介](http://libc.pw/2015/08/04/%E5%A0%86%E6%BA%A2%E5%87%BA%E6%BC%8F%E6%B4%9E%E7%AE%80%E4%BB%8B/) -- by zh-explorer
- [glibc内存分配与回收过程图解](http://blog.csdn.net/maokelong95/article/details/52006379) -- by 猫科龙

### Tools
- [PEDA - Python Exploit Development Assistance for GDB](https://github.com/longld/peda)
- [pwntools - CTF framework and exploit development library](https://github.com/Gallopsled/pwntools)
- [angr - The next-generation binary analysis platform](https://github.com/angr/angr)
- [zio - unified io lib for pwning development written in python](https://github.com/zTrix/zio)

### Format String
- [Exploiting Format String Vulnerabilities](https://trailofbits.github.io/ctf/exploits/references/formatstring-1.2.pdf) -- by scut/team teso
- [Introduction to Format String exploits](http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html) -- by Alex Reece
- 格式化字符串漏洞利用小结 -- by tianyi201612
  - [格式化字符串漏洞利用小结（一）](http://bobao.360.cn/learning/detail/3654.html)
  - [格式化字符串漏洞利用小结（二）](http://bobao.360.cn/learning/detail/3674.html)
  - [借助DynELF实现无libc的漏洞利用小结](http://bobao.360.cn/learning/detail/3298.html)
- [格式化字符串blind pwn详细教程](http://bobao.360.cn/ctf/detail/189.html) -- by 4SUN4_C8
- [漏洞挖掘基础之格式化字符串](http://cb.drops.wiki/drops/papers-9426.html) -- by 珈蓝夜宇
- [Linux系统下格式化字符串利用研究](https://paper.seebug.org/246/) -- by Hcamael

- [Linux中的GOT和PLT到底是个啥？](http://www.freebuf.com/articles/system/135685.html) -- by PhyzX

### Crackme
[crackmes.cf](http://crackmes.cf/)


## TODO

- [Linux (x86) Exploit Development Series](https://sploitfun.wordpress.com/2015/06/26/linux-x86-exploit-development-tutorial-series/)

- [飞龙的安卓逆向教程](https://www.gitbook.com/book/wizardforcel/fl-android-re-tut/details)

- [使用OllyDbg从零开始Cracking](http://bbs.pediy.com/thread-184679.htm)

- [从逆向工程的角度来看C++](http://bbs.pediy.com/thread-87586.htm)

- [Glibc 内存管理: Ptmalloc2 源代码分析](http://www.valleytalk.org/wp-content/uploads/2015/02/glibc%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86ptmalloc%E6%BA%90%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%901.pdf)

- [Performing a ret2libc Attack](http://shellblade.net/docs/ret2libc.pdf)

- [Shellcode Injection](https://dhavalkapil.com/blogs/Shellcode-Injection/)

- [Buffer Overflow](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/)

- [Writing you own shellcode](http://paraschetal.in/writing-your-own-shellcode)

- [SoK: Science, Security, and the Elusive Goal of Security as a Scientific Pursuit](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/scienceAndSecuritySoK.pdf)

- [Stack based v/s Register based architectures and android's Dalvik VM](https://markfaction.wordpress.com/2012/07/15/stack-based-vs-register-based-virtual-machine-architecture-and-the-dalvik-vm/)

- [MIPS Quick Tutorial](http://logos.cs.uic.edu/366/notes/mips%20quick%20tutorial.htm)

- [How does a C debugger work?](https://blog.0x972.info/?d=2014/11/13/10/40/50-how-does-a-debugger-work)

- [How the heck do we get to main()?](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html)

- [ASLR on the Line: Practical Cache Attacks on the MMU](http://www.cs.vu.nl/~herbertb/download/papers/anc_ndss17.pdf)

- [Smashing the Stack for Fun and Profit](http://insecure.org/stf/smashstack.html)

- [Cyber Grand Shellphish](http://www.phrack.org/papers/cyber_grand_shellphish.html)

- [GOT, PLT and Dynamic Sharing](https://www.technovelty.org/linux/plt-and-got-the-key-to-code-sharing-and-dynamic-libraries.html)

- [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)

- [NX Bit - Does it protect the stack?](https://security.stackexchange.com/questions/47807/nx-bit-does-it-protect-the-stack/47825)

- [Malware Analysis Tutorials: a Reverse Engineering Approach](http://fumalwareanalysis.blogspot.nl/p/malware-analysis-tutorials-reverse.html) -- by Dr. Xiang Fu

- [x86 Assembly Guide](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

- [Linux anti-debugging techniques](http://vxheaven.org/lib/vsc04.html)

- [Beej's Quick Guide to GDB](http://beej.us/guide/bggdb/)

- [x86 Assembly](https://en.wikibooks.org/wiki/X86_Assembly)

- [Corelan Team Blog](https://www.corelan.be/index.php/articles/)

- [Surgically returning to randomized lib(c)](https://trailofbits.github.io/ctf/exploits/references/acsac09.pdf)

- [Using GDB to Develop Exploits](https://www.exploit-db.com/papers/13205/)

- [x86-64 buffer overflow exploits and the borrowed code chunks exploitation technique](https://trailofbits.github.io/ctf/exploits/references/no-nx.pdf)

- [The "Ultimate" Anti-Debugging Reference](http://pferrie.host22.com/papers/antidebug.pdf)

- [Low-level Software Security: Attacks and Defenses](https://trailofbits.github.io/ctf/exploits/references/tr-2007-153.pdf)

- [CTF 中的内存漏洞利用技巧](http://netsec.ccert.edu.cn/wp-content/uploads/2015/10/2015-1029-yangkun-Gold-Mining-CTF.pdf)

- [MALLOC DES-MALEFICARUM](http://www.phrack.org/issues/66/10.html) -- by blackngel

- [Heap exploitation](https://4ngelboy.blogspot.tw/2015/08/heap-exploitation.html) -- by Angelboy

- [Advanced heap exploitation](https://4ngelboy.blogspot.tw/2016/03/advanced-heap-exploitation.html) -- by Angelboy

- Hack The Virtual Memory -- by Julien Barbier
  - [Hack The Virtual Memory: C strings & /proc](https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/)
  - [Hack The Virtual Memory: Python bytes](https://blog.holbertonschool.com/hack-the-virtual-memory-python-bytes/)
  - [Hack the Virtual Memory: drawing the VM diagram](https://blog.holbertonschool.com/hack-the-virtual-memory-drawing-the-vm-diagram/)
  - [Hack the Virtual Memory: malloc, the heap & the program break](https://blog.holbertonschool.com/hack-the-virtual-memory-malloc-the-heap-the-program-break/)

- Exploit writing tutorial -- By Corelan Team
  - [Stack Based Overflows](https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/)
  - [Stack Based Overflows – jumping to shellcode](https://www.corelan.be/index.php/2009/07/23/writing-buffer-overflow-exploits-a-quick-and-basic-stutorial-part-2/)
  - [SEH Based Exploits](https://www.corelan.be/index.php/2009/07/25/writing-buffer-overflow-exploits-a-quick-and-basic-tutorial-part-3-seh/)
  - [SEH Based Exploits – just another example](https://www.corelan.be/index.php/2009/07/28/seh-based-exploit-writing-tutorial-continued-just-another-example-part-3b/)
  - [From Exploit to Metasploit – The basics](https://www.corelan.be/index.php/2009/08/12/exploit-writing-tutorials-part-4-from-exploit-to-metasploit-the-basics/)
  - [How debugger modules & plugins can speed up basic exploit development](https://www.corelan.be/index.php/2009/09/05/exploit-writing-tutorial-part-5-how-debugger-modules-plugins-can-speed-up-basic-exploit-development/)
  - [Bypassing Stack Cookies, SafeSeh, SEHOP, HW DEP and ASLR](https://www.corelan.be/index.php/2009/09/21/exploit-writing-tutorial-part-6-bypassing-stack-cookies-safeseh-hw-dep-and-aslr/)
  - [Unicode – from 0x00410041 to calc](https://www.corelan.be/index.php/2009/11/06/exploit-writing-tutorial-part-7-unicode-from-0x00410041-to-calc/)
  - [Win32 Egg Hunting](https://www.corelan.be/index.php/2010/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/)
  - [Introduction to Win32 shellcoding](https://www.corelan.be/index.php/2010/02/25/exploit-writing-tutorial-part-9-introduction-to-win32-shellcoding/)
  - [Chaining DEP with ROP](https://www.corelan.be/index.php/2010/06/16/exploit-writing-tutorial-part-10-chaining-dep-with-rop-the-rubikstm-cube/)
  - [Heap Spraying Demystified](https://www.corelan.be/index.php/2011/12/31/exploit-writing-tutorial-part-11-heap-spraying-demystified/)

- [Advances in format string exploitation](http://phrack.org/issues/59/7.html) -- by gera, riq

- [软件分析技术](http://sei.pku.edu.cn/~xiongyf04/SA/2016/main.htm) -- by 熊英飞

- [Compiler Design](http://www.cs.cmu.edu/~fp/courses/15411-f14/index.html) -- by Frank Pfenning

- [Optimizing Compilers](http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15745-s14/www/index.html) -- by Todd C. Mowry

- [System Security and Binary Code Analysis](http://www.utdallas.edu/~zhiqiang.lin/spring2012.html)

- [Main is usually a function. So then when is it not?](http://jroweboy.github.io/c/asm/2015/01/26/when-is-main-not-a-function.html) -- by James Rowe

- [Heap Exploitation](https://heap-exploitation.dhavalkapil.com/) -- by Dhaval Kapil

- Linux堆内存管理深入分析 -- by 阿里聚安全
  - [Linux堆内存管理深入分析（上）](http://www.freebuf.com/articles/system/104144.html)
  - [Linux堆内存管理深入分析（下）](http://www.freebuf.com/articles/security-management/105285.html)

- Windows Exploit开发系列教程 -- by Netfairy, lufei
  - [Windows Exploit开发系列教程——堆喷射（一）](http://bobao.360.cn/learning/detail/3548.html)
  - [Windows Exploit开发系列教程——堆喷射（二）](http://bobao.360.cn/learning/detail/3555.html)

- [Notes About Heap Overflow Under Linux](https://blog.iret.xyz/article.aspx/linux_heapoverflow_enterance) -- by Silver

- [如何理解堆和堆溢出漏洞的利用？](http://www.freebuf.com/vuls/98404.html) -- by 老王隔壁的白帽子

- [how2heap](https://github.com/shellphish/how2heap) -- by shellphish
  - [how2heap总结-上](http://bobao.360.cn/learning/detail/4386.html)
  - [how2heap总结-下](http://bobao.360.cn/learning/detail/4383.html) by 7o8v_

- [Ltrace Internals](https://paper.seebug.org/papers/Archive/refs/ltrace_internals.pdf) -- by Rodrigo Rubira Branco

- [Principles of Program Analysis](http://www.imm.dtu.dk/~hrni/PPA/ppasup2004.html) -- by Nielson

- [Static Program Analysis](https://cs.au.dk/~amoeller/spa/) -- by Anders

- Windows Kernel Exploitation Tutorial -- by rootkit
  - [Part 1: Setting up the Environment](https://rootkits.xyz/blog/2017/06/kernel-setting-up/)
  - [Part 2: Stack Overflow](https://rootkits.xyz/blog/2017/08/kernel-stack-overflow/)
  - [Part 3: Arbitrary Memory Overwrite (Write-What-Where)](https://rootkits.xyz/blog/2017/09/kernel-write-what-where/)

- [Type-Safety in Programming Languages](http://www.pl-enthusiast.net/2014/08/05/type-safety/) -- by Michael Hicks

- [Memory-Safety in Programming Languages](http://www.pl-enthusiast.net/2014/07/21/memory-safety/) -- by Michael Hicks

- [CS 252r: Advanced Topics in Programming Languages](http://web-static-aws.seas.harvard.edu/courses/cs252/2011sp/) -- by Prof. Stephen Chong

- [X86 EXPLOITATION 101](https://gbmaster.wordpress.com/) -- by GB_MASTER

- [Glibc Adventures: The Forgotten Chunks](https://info.contextis.com/acton/attachment/24535/f-02c8/1/-/-/-/-/Glibc%20Adventures%3A%20The%20forgotten%20chunks.pdf) -- by Francois Goichon

- [heap overflow&溢出保护和绕过](https://www.tuicool.com/articles/aY7Fzav)

- [Libc堆管理机制及漏洞利用技术 (一）](http://www.freebuf.com/articles/system/91527.html?utm_source=tuicool&utm_medium=referral) -- by ysyy

- [堆溢出的unlink利用方法](https://www.tuicool.com/articles/E3Ezu2u)

- [Linux堆溢出漏洞利用之unlink](https://www.tuicool.com/articles/iium6fn)

- [浅析Linux堆溢出之fastbin](http://www.freebuf.com/news/88660.html?utm_source=tuicool&utm_medium=referral) -- by 银河实验室

- [Linux堆溢出利用:unlink](https://www.tuicool.com/articles/nyEvU3Q) -- by v-v.mom

- [堆之House of Spirit](http://bobao.360.cn/learning/detail/3417.html) -- by ray_cp

- [ctf-HITCON-2016-houseoforange学习](http://www.cnblogs.com/shangye/p/6268981.html) -- by 一肩担风月

- [CTF Pwn之创造奇迹的Top Chunk](http://bobao.360.cn/ctf/detail/178.html) -- by for_while

- [unsorted bin attack分析](http://bobao.360.cn/learning/detail/3296.html) -- by ray_cp

- [linux堆溢出学习之unsafe unlink](http://blog.csdn.net/qq_29343201/article/details/53558216) -- by Anciety

- [手把手教你栈溢出从入门到放弃（上）](https://zhuanlan.zhihu.com/p/25816426) -- by Jwizard

- [手把手教你栈溢出从入门到放弃（下）](https://zhuanlan.zhihu.com/p/25892385) -- by Jwizard

- [Z3一把梭：用约束求解搞定一类CTF题](https://zhuanlan.zhihu.com/p/30548907) -- by 朱文雷

- [Smashing the stack in 2010](http://www.mgraziano.info/docs/stsi2010.pdf) -- by Andrea Cugliari

- [Linker and Libraries Guide](https://docs.oracle.com/cd/E19683-01/817-3677/index.html)

- [The advanced return-into-lib(c) exploits](http://hamsa.cs.northwestern.edu/media/readings/advanced_libc.pdf) -- by Nergal

- [ROP stager + Return-to-dl-resolveによるASLR+DEP回避](http://inaz2.hatenablog.com/entry/2014/07/15/023406) -- by hatena

- [x64でROP stager + Return-to-dl-resolveによるASLR+DEP回避をやってみる](http://inaz2.hatenablog.com/entry/2014/07/27/205322) -- by hatena

- [Acronyms relevant to Executable and Linkable Format (ELF)](https://www.cs.stevens.edu/~jschauma/631/elf.html)

- [Understanding the heap by breaking it](https://www.blackhat.com/presentations/bh-usa-07/Ferguson/Whitepaper/bh-usa-07-ferguson-WP.pdf)

- Dance In Heap 系列
  - [Dance In Heap（一）：浅析堆的申请释放及相应保护机制](http://www.freebuf.com/articles/system/151372.html)
  - [Dance In Heap（二）：一些堆利用的方法（上）](http://www.freebuf.com/articles/system/151407.html)
  - [Dance In Heap（三）：一些堆利用的方法（中）](http://www.freebuf.com/articles/system/151428.html)
  - [Dance In Heap（四）：一些堆利用的方法（下）](http://www.freebuf.com/articles/system/151435.html)

- [Linux堆漏洞之Use after free实例](http://d0m021ng.github.io/2017/03/04/PWN/Linux%E5%A0%86%E6%BC%8F%E6%B4%9E%E4%B9%8BUse-after-free%E5%AE%9E%E4%BE%8B/)

- [Sigreturn Oriented Programming (SROP) Attack攻击原理](http://www.freebuf.com/articles/network/87447.html)

- [An Introduction to Use After Free Vulnerabilities](https://www.purehacking.com/blog/lloyd-simon/an-introduction-to-use-after-free-vulnerabilities)

- [逆向安全系列：Use After Free漏洞浅析](http://bobao.360.cn/learning/detail/3379.html?utm_source=tuicool&utm_medium=referral)

- [Linux堆溢出之Fastbin Attack实例详解](http://bobao.360.cn/learning/detail/3996.html)

- [Linux堆溢出漏洞利用之unlink](https://jaq.alibaba.com/community/art/show?spm=a313e.7916646.24000001.74.ZP8rXN&articleid=360)

- [从一字节溢出到任意代码执行-Linux下堆漏洞利用](http://bobao.360.cn/learning/detail/3113.html)

- [现代化的堆相关漏洞利用技巧](http://bobao.360.cn/learning/detail/3197.html)

- [溢出科普：heap overflow&溢出保护和绕过](http://wooyun.jozxing.cc/static/drops/binary-14596.html)

- [Quick introduction into SAT/SMT solvers and symbolic execution](https://yurichev.com/writings/SAT_SMT_draft-EN.pdf)

- [DECISION PROCEDURES FOR BIT-VECTORS, ARRAYS AND INTEGERS](https://ece.uwaterloo.ca/~vganesh/Publications_files/vg2007-PhD-STANFORD.pdf)

- [I433 System & Protocol Security](http://homes.soic.indiana.edu/yh33/Teaching/I433-2016/)

- [From fuzzing to 0-day](https://blog.techorganic.com/2014/05/14/from-fuzzing-to-0-day/)
