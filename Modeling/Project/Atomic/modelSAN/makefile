OBJS=modelSANSAN.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/libmodelSANSAN.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/libmodelSANSAN_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/libmodelSANSAN.a: FORCE
	$(MAKE) lib TARGET=libmodelSANSAN.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/libmodelSANSAN_debug.a: FORCE
	$(MAKE) lib TARGET=libmodelSANSAN_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

