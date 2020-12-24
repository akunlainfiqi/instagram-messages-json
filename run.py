import json
import datetime
import emoji
import codecs

namafile = input("Masukkan nama file json >> ")

with codecs.open(namafile,'r',encoding='utf-8-sig') as f:
    pesan = json.load(f)
    isi = pesan["messages"]
    nama = pesan["title"]

with codecs.open("%s 2.txt"%(nama),"w",encoding='utf-8-sig',errors='ignore') as p:
    for x in reversed(isi):
        if 'content' in x:
            text = ('{} {:14} >> {}\n').format(datetime.datetime.fromtimestamp(int(x["timestamp_ms"])/1000).replace(microsecond=0),x["sender_name"],x["content"])
            p.write(text)
        else:
            pass

print("kelar")