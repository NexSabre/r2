# r2
Request-Replay is simple tool to record your requests on specific target and later replay it to automate your daily tasks

This version is still Work In Progress. Record/Replay function should work with no problems, but it is lack of features. 

## TODO
__Note:__ This is partly implemented with 0.2 version.

- Implement an option to parse arguments ex `http://127.0.0.1:5000/search?q=title:DNA`. Actual version will pass 
everything on the right side of the `?` and save a file under `search`.


## Replay files
Replay files store base information about the response, from the service. 

Actual support:
- json response 

Future upgrade:
- raw response
- additional status codes
- additional information from headers

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
