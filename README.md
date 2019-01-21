## protobuf-bug

Describes a bug in Google's `protobuf` library for Python.

To run, make sure you have a working `make`, `python` (2, not 3, sorry) and `protoc` installed, then:

```
make
```

You _should_ then see:

```
protoc --python_out=. example.proto
python show_bug.py
Let's create an empty ExampleMessage instance called message:
	
Let's set its 'this_should_be_unserializable' extension property:
	[OtherMessage.this_should_be_unserializable]: true


"message" is now completely serializable to regular wire format:
	'\xc0\xf2\x04\x01'

MessageToDict can even properly serialize it to a dict:
	{'[OtherMessage.this_should_be_unserializable.thisShouldBeUnserializable]': True}

But when using ParseDict to deserialize, it fails:
Traceback (most recent call last):
  File "show_bug.py", line 30, in <module>
    show_bug()
  File "show_bug.py", line 26, in show_bug
    print ParseDict(as_dict, ExampleMessage())
  File "/Users/psobot/Library/Python/2.7/lib/python/site-packages/google/protobuf/json_format.py", line 421, in ParseDict
    parser.ConvertMessage(js_dict, message)
  File "/Users/psobot/Library/Python/2.7/lib/python/site-packages/google/protobuf/json_format.py", line 452, in ConvertMessage
    self._ConvertFieldValuePair(value, message)
  File "/Users/psobot/Library/Python/2.7/lib/python/site-packages/google/protobuf/json_format.py", line 552, in _ConvertFieldValuePair
    setattr(message, field.name, _ConvertScalarFieldValue(value, field))
AttributeError: Assignment not allowed (no field "this_should_be_unserializable" in protocol message object).
make: *** [all] Error 1

```