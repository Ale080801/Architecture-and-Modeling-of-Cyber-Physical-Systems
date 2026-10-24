OBJS=studySANSetStudy.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/libstudySANSetStudy.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/libstudySANSetStudy_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/libstudySANSetStudy.a: FORCE
	$(MAKE) lib TARGET=libstudySANSetStudy.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/libstudySANSetStudy_debug.a: FORCE
	$(MAKE) lib TARGET=libstudySANSetStudy_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

