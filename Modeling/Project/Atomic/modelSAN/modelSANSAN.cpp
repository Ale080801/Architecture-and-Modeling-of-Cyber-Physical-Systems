

// This C++ file was created by SanEditor

#include "Atomic/modelSAN/modelSANSAN.h"

#include <stdlib.h>
#include <iostream>

#include <math.h>


/*****************************************************************
                         modelSANSAN Constructor             
******************************************************************/


modelSANSAN::modelSANSAN(){


  Activity* InitialActionList[6]={
    &FailureA, //0
    &RepairA, //1
    &FailureB, //2
    &RepairB, //3
    &FailureC, //4
    &RepairC  // 5
  };

  BaseGroupClass* InitialGroupList[6]={
    (BaseGroupClass*) &(FailureA), 
    (BaseGroupClass*) &(RepairA), 
    (BaseGroupClass*) &(FailureB), 
    (BaseGroupClass*) &(RepairB), 
    (BaseGroupClass*) &(FailureC), 
    (BaseGroupClass*) &(RepairC)
  };

  SF = new Place("SF" ,0);
  WA = new Place("WA" ,1);
  WB = new Place("WB" ,2);
  WC = new Place("WC" ,3);
  FA = new Place("FA" ,0);
  FB = new Place("FB" ,0);
  FC = new Place("FC" ,0);
  SFReliability = new Place("SFReliability" ,0);
  BaseStateVariableClass* InitialPlaces[8]={
    SF,  // 0
    WA,  // 1
    WB,  // 2
    WC,  // 3
    FA,  // 4
    FB,  // 5
    FC,  // 6
    SFReliability   // 7
  };
  BaseStateVariableClass* InitialROPlaces[0]={
  };
  initializeSANModelNow("modelSAN", 8, InitialPlaces, 
                        0, InitialROPlaces, 
                        6, InitialActionList, 6, InitialGroupList);


  assignPlacesToActivitiesInst();
  assignPlacesToActivitiesTimed();

  int AffectArcs[29][2]={ 
    {1,0}, {0,0}, {4,0}, {7,0}, {4,1}, {1,1}, {5,1}, {6,1}, {0,1}, 
    {2,2}, {5,2}, {0,2}, {3,2}, {7,2}, {5,3}, {2,3}, {4,3}, {6,3}, 
    {0,3}, {3,4}, {6,4}, {0,4}, {2,4}, {7,4}, {6,5}, {3,5}, {4,5}, 
    {5,5}, {0,5}
  };
  for(int n=0;n<29;n++) {
    AddAffectArc(InitialPlaces[AffectArcs[n][0]],
                 InitialActionList[AffectArcs[n][1]]);
  }
  int EnableArcs[15][2]={ 
    {1,0}, {0,0}, {4,1}, {0,1}, {2,2}, {0,2}, {5,3}, {0,3}, {4,3}, 
    {3,4}, {0,4}, {6,5}, {0,5}, {4,5}, {5,5}
  };
  for(int n=0;n<15;n++) {
    AddEnableArc(InitialPlaces[EnableArcs[n][0]],
                 InitialActionList[EnableArcs[n][1]]);
  }

  for(int n=0;n<6;n++) {
    InitialActionList[n]->LinkVariables();
  }
  CustomInitialization();

}

void modelSANSAN::CustomInitialization() {

}
modelSANSAN::~modelSANSAN(){
  for (int i = 0; i < NumStateVariables-NumReadOnlyPlaces; i++)
    delete LocalStateVariables[i];
};

void modelSANSAN::assignPlacesToActivitiesInst(){
}
void modelSANSAN::assignPlacesToActivitiesTimed(){
  FailureA.WA = (Place*) LocalStateVariables[1];
  FailureA.SF = (Place*) LocalStateVariables[0];
  FailureA.FA = (Place*) LocalStateVariables[4];
  FailureA.SFReliability = (Place*) LocalStateVariables[7];
  RepairA.FA = (Place*) LocalStateVariables[4];
  RepairA.SF = (Place*) LocalStateVariables[0];
  RepairA.WA = (Place*) LocalStateVariables[1];
  RepairA.FB = (Place*) LocalStateVariables[5];
  RepairA.FC = (Place*) LocalStateVariables[6];
  FailureB.WB = (Place*) LocalStateVariables[2];
  FailureB.SF = (Place*) LocalStateVariables[0];
  FailureB.FB = (Place*) LocalStateVariables[5];
  FailureB.WC = (Place*) LocalStateVariables[3];
  FailureB.SFReliability = (Place*) LocalStateVariables[7];
  RepairB.FB = (Place*) LocalStateVariables[5];
  RepairB.SF = (Place*) LocalStateVariables[0];
  RepairB.FA = (Place*) LocalStateVariables[4];
  RepairB.WB = (Place*) LocalStateVariables[2];
  RepairB.FC = (Place*) LocalStateVariables[6];
  FailureC.WC = (Place*) LocalStateVariables[3];
  FailureC.SF = (Place*) LocalStateVariables[0];
  FailureC.FC = (Place*) LocalStateVariables[6];
  FailureC.WB = (Place*) LocalStateVariables[2];
  FailureC.SFReliability = (Place*) LocalStateVariables[7];
  RepairC.FC = (Place*) LocalStateVariables[6];
  RepairC.SF = (Place*) LocalStateVariables[0];
  RepairC.FA = (Place*) LocalStateVariables[4];
  RepairC.FB = (Place*) LocalStateVariables[5];
  RepairC.WC = (Place*) LocalStateVariables[3];
}
/*****************************************************************/
/*                  Activity Method Definitions                  */
/*****************************************************************/

/*======================FailureAActivity========================*/

modelSANSAN::FailureAActivity::FailureAActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("FailureA",0,Exponential, RaceEnabled, 4,2, false);
}

modelSANSAN::FailureAActivity::~FailureAActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::FailureAActivity::LinkVariables(){
  WA->Register(&WA_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  FA->Register(&FA_Mobius_Mark);
  SFReliability->Register(&SFReliability_Mobius_Mark);
}

bool modelSANSAN::FailureAActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(WA_Mobius_Mark)) >=1)&&(SF -> Mark() == 0));
  return NewEnabled;
}

double modelSANSAN::FailureAActivity::Rate(){
  return WA->Mark()*lambda/4;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::FailureAActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::FailureAActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::FailureAActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::FailureAActivity::SampleDistribution(){
  return TheDistribution->Exponential(WA->Mark()*lambda/4);
}

double* modelSANSAN::FailureAActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::FailureAActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::FailureAActivity::Fire(){
  ;
  (*(WA_Mobius_Mark))--;
  FA -> Mark()++;
SF -> Mark() = 1;
SFReliability -> Mark()= 1;
  return this;
}

/*======================RepairAActivity========================*/

modelSANSAN::RepairAActivity::RepairAActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("RepairA",1,Exponential, RaceEnabled, 5,2, false);
}

modelSANSAN::RepairAActivity::~RepairAActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::RepairAActivity::LinkVariables(){
  FA->Register(&FA_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  WA->Register(&WA_Mobius_Mark);
  FB->Register(&FB_Mobius_Mark);
  FC->Register(&FC_Mobius_Mark);
}

bool modelSANSAN::RepairAActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(FA_Mobius_Mark)) >=1)&&(SF -> Mark() == 1));
  return NewEnabled;
}

double modelSANSAN::RepairAActivity::Rate(){
  return mu/4;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::RepairAActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::RepairAActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::RepairAActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::RepairAActivity::SampleDistribution(){
  return TheDistribution->Exponential(mu/4);
}

double* modelSANSAN::RepairAActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::RepairAActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::RepairAActivity::Fire(){
  ;
  (*(FA_Mobius_Mark))--;
  if((FA->Mark()==0)&&((FB->Mark()<2)||(FC->Mark()<3))){
	SF -> Mark() = 0;
}
  (*(WA_Mobius_Mark))++;
  return this;
}

/*======================FailureBActivity========================*/

modelSANSAN::FailureBActivity::FailureBActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("FailureB",2,Exponential, RaceEnabled, 5,2, false);
}

modelSANSAN::FailureBActivity::~FailureBActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::FailureBActivity::LinkVariables(){
  WB->Register(&WB_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  FB->Register(&FB_Mobius_Mark);
  WC->Register(&WC_Mobius_Mark);
  SFReliability->Register(&SFReliability_Mobius_Mark);
}

bool modelSANSAN::FailureBActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(WB_Mobius_Mark)) >=1)&&(SF -> Mark() == 0));
  return NewEnabled;
}

double modelSANSAN::FailureBActivity::Rate(){
  return WB->Mark()*lambda/2;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::FailureBActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::FailureBActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::FailureBActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::FailureBActivity::SampleDistribution(){
  return TheDistribution->Exponential(WB->Mark()*lambda/2);
}

double* modelSANSAN::FailureBActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::FailureBActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::FailureBActivity::Fire(){
  ;
  (*(WB_Mobius_Mark))--;
  if((WB -> Mark() == 0) && (WC -> Mark() == 0)){
	SF -> Mark() = 1;
	SFReliability -> Mark() = 1;
}
  (*(FB_Mobius_Mark))++;
  return this;
}

/*======================RepairBActivity========================*/

modelSANSAN::RepairBActivity::RepairBActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("RepairB",3,Exponential, RaceEnabled, 5,3, false);
}

modelSANSAN::RepairBActivity::~RepairBActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::RepairBActivity::LinkVariables(){
  FB->Register(&FB_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  FA->Register(&FA_Mobius_Mark);
  WB->Register(&WB_Mobius_Mark);
  FC->Register(&FC_Mobius_Mark);
}

bool modelSANSAN::RepairBActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(FB_Mobius_Mark)) >=1)&&(SF -> Mark() == 1)&&(FA -> Mark() == 0));
  return NewEnabled;
}

double modelSANSAN::RepairBActivity::Rate(){
  return mu/2;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::RepairBActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::RepairBActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::RepairBActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::RepairBActivity::SampleDistribution(){
  return TheDistribution->Exponential(mu/2);
}

double* modelSANSAN::RepairBActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::RepairBActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::RepairBActivity::Fire(){
  ;
  ;
  (*(FB_Mobius_Mark))--;
  if((FA->Mark()==0)&&((FB->Mark()<2)||(FC->Mark()<3))){
	SF -> Mark() = 0;
}
  (*(WB_Mobius_Mark))++;
  return this;
}

/*======================FailureCActivity========================*/

modelSANSAN::FailureCActivity::FailureCActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("FailureC",4,Exponential, RaceEnabled, 5,2, false);
}

modelSANSAN::FailureCActivity::~FailureCActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::FailureCActivity::LinkVariables(){
  WC->Register(&WC_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  FC->Register(&FC_Mobius_Mark);
  WB->Register(&WB_Mobius_Mark);
  SFReliability->Register(&SFReliability_Mobius_Mark);
}

bool modelSANSAN::FailureCActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(WC_Mobius_Mark)) >=1)&&(SF -> Mark() == 0));
  return NewEnabled;
}

double modelSANSAN::FailureCActivity::Rate(){
  return WC->Mark()*lambda;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::FailureCActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::FailureCActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::FailureCActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::FailureCActivity::SampleDistribution(){
  return TheDistribution->Exponential(WC->Mark()*lambda);
}

double* modelSANSAN::FailureCActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::FailureCActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::FailureCActivity::Fire(){
  ;
  (*(WC_Mobius_Mark))--;
  if((WB -> Mark() == 0) && (WC -> Mark() == 0)){
	SF -> Mark() = 1;
	SFReliability -> Mark() = 1;
}
  (*(FC_Mobius_Mark))++;
  return this;
}

/*======================RepairCActivity========================*/

modelSANSAN::RepairCActivity::RepairCActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("RepairC",5,Exponential, RaceEnabled, 5,4, false);
}

modelSANSAN::RepairCActivity::~RepairCActivity(){
  delete[] TheDistributionParameters;
}

void modelSANSAN::RepairCActivity::LinkVariables(){
  FC->Register(&FC_Mobius_Mark);
  SF->Register(&SF_Mobius_Mark);
  FA->Register(&FA_Mobius_Mark);
  FB->Register(&FB_Mobius_Mark);
  WC->Register(&WC_Mobius_Mark);
}

bool modelSANSAN::RepairCActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(((*(FC_Mobius_Mark)) >=1)&&(SF -> Mark() == 1)&&(FA -> Mark() == 0)&&(FB -> Mark() == 0));
  return NewEnabled;
}

double modelSANSAN::RepairCActivity::Rate(){
  return mu;
  return 1.0;  // default rate if none is specified
}

double modelSANSAN::RepairCActivity::Weight(){ 
  return 1;
}

bool modelSANSAN::RepairCActivity::ReactivationPredicate(){ 
  return false;
}

bool modelSANSAN::RepairCActivity::ReactivationFunction(){ 
  return false;
}

double modelSANSAN::RepairCActivity::SampleDistribution(){
  return TheDistribution->Exponential(mu);
}

double* modelSANSAN::RepairCActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int modelSANSAN::RepairCActivity::Rank(){
  return 1;
}

BaseActionClass* modelSANSAN::RepairCActivity::Fire(){
  ;
  ;
  ;
  (*(FC_Mobius_Mark))--;
  if((FA->Mark()==0)&&((FB->Mark()<2)||(FC->Mark()<3))){
	SF -> Mark() = 0;
}
  (*(WC_Mobius_Mark))++;
  return this;
}

