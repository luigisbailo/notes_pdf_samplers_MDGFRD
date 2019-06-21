// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_CONVEXSALL_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"


void make_data_convexSall() {

    FILE *fp;
    double t,infl_point;

    double D = 1;
    double B = 10;
    double db = 0.1;
    double b=db;
    double dt;
    double start_point;

    fp = fopen("../results/samplers_convexS_all.txt", "w");

    while (b<B) {
        dt = b*b/D/10000;
        t = dt;
        infl_point = 1;
        while (infl_point>0){
            t += dt;
            infl_point = Sder2 (t,b,D);
        }
        start_point = 0.0917517*b*b/D;
        fprintf(fp, "%lf\t%lf\t%lf\n", b, t, start_point);
        b += db;
    }
    fclose(fp);

}


#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_CONVEXSALL_H

#endif