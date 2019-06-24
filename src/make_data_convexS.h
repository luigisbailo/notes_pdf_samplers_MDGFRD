// author luigisbailo


#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG4_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"


void make_data_convexS () {

    double b = 1;
    double D = 1;
    double t = 0;
    double dt = D/100;

    int n_iterations=100;
    FILE *fp;

    fp = fopen("../src/results/samplers_convexS_b1.txt", "w");
    for (int count=0; count<n_iterations; count++){
        t += dt;
        fprintf(fp, "%lf\t%lf\t%lf\n", t, Sder(t,b,D), Sder2(t,b,D));
    }
    fclose(fp);

    fp = fopen("../src/results/samplers_convexS_b2.txt", "w");
    b=2;
    t=0;
    for (int count=0; count<n_iterations; count++){
        t += dt;
        fprintf(fp, "%lf\t%lf\t%lf\n", t, Sder(t,b,D), Sder2(t,b,D));
    }
    fclose(fp);

    fp = fopen("../src/results/samplers_convexS_b3.txt", "w");
    b=3;
    t=0;
    for (int count=0; count<n_iterations; count++){
        t += dt;
        fprintf(fp, "%lf\t%lf\t%lf\n", t, Sder(t,b,D), Sder2(t,b,D));
    }
    fclose(fp);

}

#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG4_H

#endif