LOCAL_PATH:=$(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE:=test
LOCAL_SRC_FILES:=test.cpp main.cpp utils.cpp

#LOCAL_LDLIBS:=-static

#LOCAL_CFLAGS:=-mllvm -xse 
#LOCAL_CFLAGS+=-mllvm -sub 
#LOCAL_CFLAGS+=-mllvm -bcf
#LOCAL_CFLAGS += -mllvm -stats 
#LOCAL_CFLAGS += -mllvm -debug
#LOCAL_CFLAGS += -mllvm -oconf=obfuscation.conf
#LOCAL_CFLAGS += -mllvm -debug-pass=Structure

include $(BUILD_SHARED_LIBRARY)

