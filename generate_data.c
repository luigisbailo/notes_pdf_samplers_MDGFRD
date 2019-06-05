// author luigisbailo

#include <math.h>
#include <stdio.h>
//#include <stdlib.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"
#include "draw.h"


int main () {

    double b = 1;
    double D = 1;
    double t;

    double r = b/1000;
    double p,p_free;
    FILE *fp;

    fp = fopen("../results/samplers_fig1.txt", "w");


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
