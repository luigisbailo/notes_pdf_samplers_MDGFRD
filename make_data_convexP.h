// author luigisbailo


#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG5_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"


void make_data_convexP () {

    double b = 1;
    double D = 1;
    double t = 0;
    double dt = D/100;

    int n_iterations=100;
    FILE *fp;


    b=1;
    t=b*b/D;
    double dr=b/n_iterations;
    double r = 0;
    fp = fopen("../results/samplers_convexP_b1t1.txt", "w");
    for (int count=0; count<n_iterations; count++){
        r += dr;
        fprintf(fp, "%lf\t%lf\t%lf\n", r, Pder(r,t,b,D,Sfunct(t,b,D)), Pder2(r,t,b,D,Sfunct(t,b,D)));
    }
    fclose(fp);


    b=1;
    t=b*b/D/100;
    dr=b/n_iterations;
    r = 0;
    fp = fopen("../results/samplers_convexP_b1t100.txt", "w");
    for (int count=0; count<n_iterations; count++){
        r += dr;
        fprintf(fp, "%lf\t%lf\t%lf\n", r, Pder(r,t,b,D,Sfunct(t,b,D)), Pder2(r,t,b,D,Sfunct(t,b,D)));
    }
    fclose(fp);


}

#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG4_H

#endif