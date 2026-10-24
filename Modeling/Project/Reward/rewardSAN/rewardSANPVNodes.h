#ifndef _REWARDSAN_PVS_
#define _REWARDSAN_PVS_
#include <math.h>
#include "Cpp/Performance_Variables/PerformanceVariableNode.hpp"
#include "Atomic/modelSAN/modelSANSAN.h"
#include "Cpp/Performance_Variables/SteadyState.hpp"
#include "Cpp/Performance_Variables/InstantOfTime.hpp"


class rewardSANPV0Worker:public SteadyState
{
 public:
  modelSANSAN *modelSAN;
  
  rewardSANPV0Worker();
  ~rewardSANPV0Worker();
  double Reward_Function();
};

class rewardSANPV0:public PerformanceVariableNode
{
 public:
  modelSANSAN *ThemodelSANSAN;

  rewardSANPV0Worker *rewardSANPV0WorkerList;

  rewardSANPV0(int timeindex=0);
  ~rewardSANPV0();
  void CreateWorkerList(void);
};

class rewardSANPV1Worker:public InstantOfTime
{
 public:
  modelSANSAN *modelSAN;
  
  rewardSANPV1Worker();
  ~rewardSANPV1Worker();
  double Reward_Function();
};

class rewardSANPV1:public PerformanceVariableNode
{
 public:
  modelSANSAN *ThemodelSANSAN;

  rewardSANPV1Worker *rewardSANPV1WorkerList;

  rewardSANPV1(int timeindex=0);
  ~rewardSANPV1();
  void CreateWorkerList(void);
};

#endif
