#ifndef modelSANSAN_H_
#define modelSANSAN_H_

#include "Cpp/BaseClasses/EmptyGroup.h"
#include "Cpp/BaseClasses/GlobalVariables.h"
#include "Cpp/BaseClasses/PreselectGroup.h"
#include "Cpp/BaseClasses/PostselectGroup.h"
#include "Cpp/BaseClasses/state/StructStateVariable.h"
#include "Cpp/BaseClasses/state/ArrayStateVariable.h"
#include "Cpp/BaseClasses/SAN/SANModel.h" 
#include "Cpp/BaseClasses/SAN/Place.h"
#include "Cpp/BaseClasses/SAN/ExtendedPlace.h"
extern Double mu;
extern Double lambda;
extern UserDistributions* TheDistribution;

void MemoryError();


/*********************************************************************
               modelSANSAN Submodel Definition                   
*********************************************************************/

class modelSANSAN:public SANModel{
public:

class FailureAActivity:public Activity {
public:

  Place* WA;
  short* WA_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* FA;
  short* FA_Mobius_Mark;
  Place* SFReliability;
  short* SFReliability_Mobius_Mark;

  double* TheDistributionParameters;
  FailureAActivity();
  ~FailureAActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // FailureAActivityActivity

class RepairAActivity:public Activity {
public:

  Place* FA;
  short* FA_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* WA;
  short* WA_Mobius_Mark;
  Place* FB;
  short* FB_Mobius_Mark;
  Place* FC;
  short* FC_Mobius_Mark;

  double* TheDistributionParameters;
  RepairAActivity();
  ~RepairAActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // RepairAActivityActivity

class FailureBActivity:public Activity {
public:

  Place* WB;
  short* WB_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* FB;
  short* FB_Mobius_Mark;
  Place* WC;
  short* WC_Mobius_Mark;
  Place* SFReliability;
  short* SFReliability_Mobius_Mark;

  double* TheDistributionParameters;
  FailureBActivity();
  ~FailureBActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // FailureBActivityActivity

class RepairBActivity:public Activity {
public:

  Place* FB;
  short* FB_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* FA;
  short* FA_Mobius_Mark;
  Place* WB;
  short* WB_Mobius_Mark;
  Place* FC;
  short* FC_Mobius_Mark;

  double* TheDistributionParameters;
  RepairBActivity();
  ~RepairBActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // RepairBActivityActivity

class FailureCActivity:public Activity {
public:

  Place* WC;
  short* WC_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* FC;
  short* FC_Mobius_Mark;
  Place* WB;
  short* WB_Mobius_Mark;
  Place* SFReliability;
  short* SFReliability_Mobius_Mark;

  double* TheDistributionParameters;
  FailureCActivity();
  ~FailureCActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // FailureCActivityActivity

class RepairCActivity:public Activity {
public:

  Place* FC;
  short* FC_Mobius_Mark;
  Place* SF;
  short* SF_Mobius_Mark;
  Place* FA;
  short* FA_Mobius_Mark;
  Place* FB;
  short* FB_Mobius_Mark;
  Place* WC;
  short* WC_Mobius_Mark;

  double* TheDistributionParameters;
  RepairCActivity();
  ~RepairCActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // RepairCActivityActivity

  //List of user-specified place names
  Place* SF;
  Place* WA;
  Place* WB;
  Place* WC;
  Place* FA;
  Place* FB;
  Place* FC;
  Place* SFReliability;

  // Create instances of all actvities
  FailureAActivity FailureA;
  RepairAActivity RepairA;
  FailureBActivity FailureB;
  RepairBActivity RepairB;
  FailureCActivity FailureC;
  RepairCActivity RepairC;
  //Create instances of all groups 
  EmptyGroup ImmediateGroup;

  modelSANSAN();
  ~modelSANSAN();
  void CustomInitialization();

  void assignPlacesToActivitiesInst();
  void assignPlacesToActivitiesTimed();
}; // end modelSANSAN

#endif // modelSANSAN_H_
