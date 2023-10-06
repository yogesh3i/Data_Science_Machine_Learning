ds= open("text.txt",'r',encoding="utf8")
ds_content=ds.read()

ds_content=ds_content.replace('data','rocket')
print(ds_content)
ds_w= open("text.txt",'w')
ds_w.write(ds_content)
ds_w.close()
