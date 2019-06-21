// author luigisbailo

#include "make_data_comparisonPfree.h"
#include "make_data_convergenceSeries.h"
#include "make_data_convexPall.h"
#include "make_data_convexSall.h"
#include "make_data_convexS.h"
#include "make_data_convexP.h"
#include "make_data_convergenceNewton.h"
#include "make_data_funcReconstr.h"


int main () {


    make_data_convexS();

    make_data_convexSall();

    make_data_convexP();

    make_data_convexPall();

    make_data_comparisonPfree();

    make_data_convergenceNewton();

    make_data_convergenceSeries();

    make_data_funcReconstr();

}


