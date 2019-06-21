// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_COMPARISONPFREE_H

#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_COMPARISONPFREE_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"

void make_data_comparisonPfree (){
    //comparison of free diffusion against bursting pde.
    //at very short times these two probabilities are equivalent.

    double b = 1;
    double D = 1;
    double t;

    double r = b/1000;
    double p,p_free;
    FILE *fp;

    fp = fopen("../results/samplers_comparisonPfree.txt", "w");

    while (r<b) {
        t = b*b/D/100;
        p = Pder(r,t,b,D,Sfunct(t,b,D));
        p_free = freeDiff(r,t,D);
        fprintf (fp, "%lf\t%lf\t%lf\t",r,p,p_free);
        t = b*b/D/10;
        p = Pder(r,t,b,D,Sfunct(t,b,D));
        p_free = freeDiff(r,t,D);
        fprintf (fp, "%lf\t%lf\n",p,p_free);

        r += b/1000;

    }

    fclose(fp);

}

#endif
