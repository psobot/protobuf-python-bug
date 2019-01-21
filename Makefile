
.PHONY: all

all: example_pb2.py show_bug.py
	python show_bug.py

example_pb2.py: example.proto
	protoc --python_out=. example.proto