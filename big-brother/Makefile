RM = rm -rf

CC=g++

SRC_DIR=./src
OBJ_DIR=./build
BIN_DIR=./bin
DOC_DIR=./doc

CFLAGS = -pedantic -ansi -std=c++11 -I.

.PHONY: all clean distclean doxy

all: status

debug: CFLAGS += -g -O0
debug: status

init:
	@mkdir -p $(BIN_DIR)/
	@mkdir -p $(OBJ_DIR)/
	@mkdir -p $(SRC_DIR)/
	@mkdir -p $(DOC_DIR)/

status: $(OBJ_DIR)/status.o
	@echo "============="
	@echo "Connecting the target $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executable status created in $(BIN_DIR)] +++"
	@echo "============="

$(OBJ_DIR)/status.o: $(SRC_DIR)/status.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

doxy:
	$(RM) $(DOC_DIR)/*
	doxygen Doxyfile

clean:
	$(RM) $(BIN_DIR)/*
	$(RM) $(OBJ_DIR)/*
	$(RM) $(DOC_DIR)/*