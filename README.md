# BOF
Some Buffer Overflow Automation Scripts I'll be using between PWK labs and Exam!

---

## List
Contains sample list of vulnserver, which you'll pass to template generator. Keep in mind, only TRUN isn't vulnerable, you may find other ways in too! ;) 
Just `nc -nvv ip port`, grab the variables supported, paste those in any file name, pass it to spikegenerator 


## SpikeTemplateGenerator
Generates Spike templates against provided list of variables, you can tweak it if you want, add `\r` for ftp and other protocols. 

```bash
python spikeTemplateGenerator.py list
```

---

## FuzzSpkFiles
Made it in short time, it'll have ip and port hard-coded in it and will fuzz all .spk files found in the dir against those. Be careful ;) 

```bash
./fuzzSpkFiles.sh
```
