#include "rewardSANPVNodes.h"

rewardSANPV0Worker::rewardSANPV0Worker()
{
  NumModels = 1;
  TheModelPtr = new BaseModelClass**[NumModels];
  TheModelPtr[0] = (BaseModelClass**)(&modelSAN);
}

rewardSANPV0Worker::~rewardSANPV0Worker() {
  delete [] TheModelPtr;
}

double rewardSANPV0Worker::Reward_Function(void) {

return (1-modelSAN->SF->Mark());

return (0);



}

rewardSANPV0::rewardSANPV0(int timeindex) {
  TheModelPtr = (BaseModelClass**)(&ThemodelSANSAN);
  double startpts[1]={0.0};
  double stoppts[1]={0.0+1.0};
  Initialize("Availability",(RewardType)3,1, startpts, stoppts, timeindex, 0,1, 1);
  Type = steady_state;
  AddVariableDependency("SF","modelSAN");
}

rewardSANPV0::~rewardSANPV0() {
  for(int i = 0; i < NumberOfWorkers; i++) {
    delete[] WorkerList[i]->Name;
    delete WorkerList[i];
  }
}

void rewardSANPV0::CreateWorkerList(void) {
  for(int i = 0; i < NumberOfWorkers; i++)
    WorkerList[i] = new rewardSANPV0Worker;
}
rewardSANPV1Worker::rewardSANPV1Worker()
{
  NumModels = 1;
  TheModelPtr = new BaseModelClass**[NumModels];
  TheModelPtr[0] = (BaseModelClass**)(&modelSAN);
}

rewardSANPV1Worker::~rewardSANPV1Worker() {
  delete [] TheModelPtr;
}

double rewardSANPV1Worker::Reward_Function(void) {

return (1-modelSAN->SFReliability->Mark());

return (0);



}

rewardSANPV1::rewardSANPV1(int timeindex) {
  TheModelPtr = (BaseModelClass**)(&ThemodelSANSAN);
  double startpts[6]={24, 360, 1080, 2520, 5400, 11160};
  double stoppts[6]={24, 360, 1080, 2520, 5400, 11160};
  Initialize("Reliability",(RewardType)0,6, startpts, stoppts, timeindex, 0,1, 1);
  AddVariableDependency("SFReliability","modelSAN");
}

rewardSANPV1::~rewardSANPV1() {
  for(int i = 0; i < NumberOfWorkers; i++) {
    delete[] WorkerList[i]->Name;
    delete WorkerList[i];
  }
}

void rewardSANPV1::CreateWorkerList(void) {
  for(int i = 0; i < NumberOfWorkers; i++)
    WorkerList[i] = new rewardSANPV1Worker;
}
