.PHONY: clean

OBJ_DIR = /home/ubuntu/minpic/K-Jungle/Week5/obj
CC = gcc
OBJS = $(addprefix $(OBJ_DIR)/, queue.o stack.o test.o main.o)
TARGET = main

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

$(OBJ_DIR)/%.o: %.c
	$(CC) -c -o $@ $<
  
clean : 
	rm $(OBJS) $(TARGET)