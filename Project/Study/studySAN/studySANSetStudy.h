
#ifndef studySANSetSTUDY_H_
#define studySANSetSTUDY_H_

#include "Reward/rewardSAN/rewardSANPVNodes.h"
#include "Reward/rewardSAN/rewardSANPVModel.h"
#include "Cpp/BaseClasses/GlobalVariables.h"
#include "Cpp/Study/BaseStudyClass.hpp"

extern Double lambda;
extern Double mu;

class studySANSetStudy : public BaseStudyClass {
public:

studySANSetStudy();
~studySANSetStudy();

private:

double *lambdaValues;
double *muValues;

void SetValues_lambda();
void SetValues_mu();

void PrintGlobalValues(int);
void *GetGVValue(char *TheGVName);
void OverrideGVValue(char *TheGVName, void *TheGVValue);
void SetGVs(int expnum);
PVModel *GetPVModel(bool expandTimeArrays);
};

#endif

