LOCAL_PATH:=$(call my-dir)

include $(CLEAR_VARS)
APP_ABI:=armeabi x86

APP_STL:=gnustl_static
APP_CPPFLAGS:=-fexceptions -frtti
#APP_OPTIM:=debug

#NDK_TOOLCHAIN_VERSION:=clang3.5
#NDK_TOOLCHAIN_VERSION:=clang3.4

# include $(BUILD_EXECUTABLE)
