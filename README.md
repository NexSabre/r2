![Test](https://github.com/NexSabre/r2/workflows/Test/badge.svg)
[![PyPI version](https://badge.fury.io/py/r2.svg)](https://badge.fury.io/py/r2)

# r2 (Record2Replay)
Record2Replay is simple tool to record your requests on specific target and later replay it to automate your daily tasks

__Note:__ This version is still Work In Progress. Record/Replay function should work with no problems, but it is lack of features. 

## TLDR;
```
# install
pip install r2

# record responses from another service
r2 record http://api.plos.org

# or record on the custom name 'api_plos'
r2 record http://api.plos.org --package api_plos

```

Go to your browser and type: 

`localhost:5000/search?q=title:DNA`

in your home directory, all response will be saved at
 
`~/.r2/packages/default/*`

```
# to replay packages 
r2 replay

# or to replay a custom package 'api_plos'
r2 replay --package api_plos
```

## TODO
__Note:__ This is partly implemented with 0.2 version.

- Implement an option to parse arguments ex `http://127.0.0.1:5000/search?q=title:DNA`. Actual version will pass 
everything on the right side of the `?` and save a file under `search`.

- Add a support for more than one package

## Installation
You can install a `r2` software using a python package manager or build it from source code:

### from pip
`r2` is available thru `pip`, to install type `pip install r2`

### from source
Go into `src` directory of source, and type `python setup.py sdist bdist_wheel && cd dist && pip install r2*.whl` 


## Replay files
Replay files store base information about the response, from the service. 

Actual support:
- json response 

Future upgrade:
- raw response
- additional status codes
- additional information from headers

## Logs files 
All logs are stored at `~/.r2/logs` directory with filenames `r2_record_2020_08_04T18_06_02_050068` 
where (`r2_[action_type]_[isoformat_time]`).


### Format change v0.1 to v0.2
Since version v0.2, `r2` presents a new format to store response information from the services. 
Before v0.2 all response was stored as a raw text in the file. Now, the Response is packed: 

_Example_:
- Before: 
```
{"test": "test_body"}
```

- Now:
```
{
"data_id": "test\endpoint", 
"actions": [
    {"arguments": {}, 
     "response": {
         "test": "test_body"}
     }]
}
```

This approach allow us to store different information for whole range of arguments deliver thru the URL.
