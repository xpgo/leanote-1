# leanote

This is a api library for [leanote](https://github.com/leanote/leanote)

## Requirements
- Python 3
- Requests

## Library Usage

```
from leanote import leanote
leanote = leanote(email,password,host)
print(leanote.info())
print(leanote.getNotebooks())
```

The method name is the same as [tha api name](https://github.com/leanote/leanote/wiki/leanote-api-en)

## Attention

- There is something wrong with uploading files, so don't do that.
- There is no check or process on you data, please do it yourself
- All variable whit default value "Necessary" means you **must** set its value yourself.
