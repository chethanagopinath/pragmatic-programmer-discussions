### Power of plain text challenge

My initial instinct was just to store in JSON, so had to look up how binary representation of this could look like
Have used bin() for integers -> strings (I think)


Adding directions field for newer data meant I need to modify previous data

For binary:
1. could keep an updated timestamp but if its all in binary, its just not understandable
2. Also this field can vary a lot, so thats difficult to predict and pad for accordingly, if its over the limit, the field's val gets truncated
You can see how it got cut off below.

```shell
➜  ch-3-basic-tools python3 address-book.py  
Binary b'Chethana\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x006073450377Milpitas\x00\x00\x00\x00\x00\x00\x00directions to reach '
JSON {'name': 'Chethana', 'phone': '6073450377', 'city': 'Milpitas', 'directions': "directions to reach address but I'm not sure if this will work since I just gave 20"}
```
3. To see changes (and if data was truncated etc), we need to decode back from bytes + unpack if we had stored in binary

For JSON:
1. Just add another field to the Person class and add the new field to the representation
2. Even to modify older ones, we dont have to worry about length as with binary (fixed length representation)