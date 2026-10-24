OBJS=rewardSANPVNodes.o rewardSANPVModel.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/librewardSANPV.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/librewardSANPV_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/librewardSANPV.a: FORCE
	$(MAKE) lib TARGET=librewardSANPV.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/librewardSANPV_debug.a: FORCE
	$(MAKE) lib TARGET=librewardSANPV_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

