import os
import sys
input_file = sys.argv[1]
chr_seq = {}
fin = open(input_file,"r")
c = 0
for line in fin:
    line = line.strip()
    c +=1
    if c%10000 ==0:
        print c
    if ">" in line:
        chr = line
        chr_seq[chr] = ""
    else:
        chr_seq[chr] += line
fin.close()
sp = input_file.split("_")[0]
gff = sp +"_hairpin.gff"
hairpin_site = {}
fin1 = open("/var/www/html/bsc/isodat/isodat_1.0/isodat_database/hairpin_gff/"+gff,"r")
fout = open(sp + "_hairpin_40.fa","w")
for line1 in fin1:
    line1 = line1.strip()
    cache_line = line1.split("_")
    if len(cache_line) < 5:
        continue
    hairpin_name = cache_line[0]
    chr = ">chr"+cache_line[1]
    start_site = int(cache_line[2])
    end_site = int(cache_line[3])
    zhenfu = cache_line[4]
    
    fout.write(">" + hairpin_name +"\n")
    cache_data_before = chr_seq[chr][start_site- 1 -20:start_site-1].lower()
    cache_data = chr_seq[chr][start_site-1:end_site]
    cache_data_after = chr_seq[chr][end_site:end_site + 20].lower()
    
    list_cache_data_before = []
    list_cache_data = []
    list_cache_data_after = []
    if zhenfu =="-":
        for i1 in cache_data_before:
            if i1 =="a":
                list_cache_data_before.append("t")
            elif i1 == "t":
                list_cache_data_before.append("a")
            elif i1 == "c":
                list_cache_data_before.append("g")
            elif i1 == "g":
                list_cache_data_before.append("c")
        for i2 in cache_data:
            if i2 =="A":
                list_cache_data.append("T")
            elif i2 == "T":
                list_cache_data.append("A")
            elif i2 == "C":
                list_cache_data.append("G")
            elif i2 == "G":
                list_cache_data.append("C")

        for i3 in list_cache_data_after:
            if i3 =="a":
                list_cache_data_after.append("t")
            elif i3 == "t":
                list_cache_data_after.append("a")
            elif i3 == "c":
                list_cache_data_after.append("g")
            elif i3 == "g":
                list_cache_data_after.append("c")
        
        fout.write("".join(list_cache_data_before)+"".join(list_cache_data)+"".join(list_cache_data_after)+"\n")
    elif zhenfu == "+":
        fout.write(cache_data_before+cache_data+cache_data_after+"\n")
fin1.close()
fout.close()
