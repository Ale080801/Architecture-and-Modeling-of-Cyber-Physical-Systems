#include "rewardSANPVModel.h"

rewardSANPVModel::rewardSANPVModel(bool expandTimeArrays) {
  TheModel=new modelSANSAN();
  DefineName("rewardSANPVModel");
  CreatePVList(2, expandTimeArrays);
  Initialize();
}



PerformanceVariableNode* rewardSANPVModel::createPVNode(int pvindex, int timeindex) {
  switch(pvindex) {
  case 0:
    return new rewardSANPV0(timeindex);
    break;
  case 1:
    return new rewardSANPV1(timeindex);
    break;
  }
  return NULL;
}
