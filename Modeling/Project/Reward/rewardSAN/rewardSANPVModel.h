#ifndef _REWARDSAN_PVMODEL_
#define _REWARDSAN_PVMODEL_
#include "rewardSANPVNodes.h"
#include "Cpp/Performance_Variables/PVModel.hpp"
#include "Atomic/modelSAN/modelSANSAN.h"
class rewardSANPVModel:public PVModel {
 protected:
  PerformanceVariableNode *createPVNode(int pvindex, int timeindex);
 public:
  rewardSANPVModel(bool expandtimepoints);
};

#endif
