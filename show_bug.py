"""Illustration of a bug in Google's Python protobuf library.

by Peter Sobot (@psobot, psobot.com), Jan 21 2019
"""

from google.protobuf.json_format import MessageToDict, ParseDict
from example_pb2 import ExampleMessage, OtherMessage


def show_bug():
    print "Let's create an empty ExampleMessage instance called message:"
    message = ExampleMessage()
    print '\t', repr(message)
    print "Let's set its 'this_should_be_unserializable' extension property:"
    message.Extensions[OtherMessage.this_should_be_unserializable] = True
    print '\t', repr(message)
    print
    print '"message" is now completely serializable to regular wire format:'
    print '\t', repr(message.SerializeToString())
    print
    print 'MessageToDict can even properly serialize it to a dict:'
    as_dict = MessageToDict(message)
    print '\t', as_dict
    print
    print 'But when using ParseDict to deserialize, it fails:'
    print ParseDict(as_dict, ExampleMessage())


if __name__ == "__main__":
    show_bug()
