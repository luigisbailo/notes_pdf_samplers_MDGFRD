// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FUNCRECONSTR_H
#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FUNCRECONSTR_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"
#include "draw.h"


void make_data_funcReconstr () {


    const gsl_rng_type *Type;
    gsl_rng *r;
    gsl_rng_env_setup ();
    Type = gsl_rng_default;
    r = gsl_rng_alloc (Type);
    FILE *devurandom = fopen("/dev/urandom","r");
    unsigned long int seed;
    fread(&seed, sizeof(seed), 1, devurandom);
    fclose(devurandom);
    gsl_rng_set(r, seed);

    FILE *fp;
    double b = 1.;
    double D = 1.;
    double xaxis;
    int n_bins = 100;
    int n_samples = 1000000;

    double T=b*b/D;
    double dt = T/(n_bins);
    double arr_exitTime[n_bins];
    for (int count = 0; count < n_bins; count++) {
        arr_exitTime[count] = 0;
    }
    for (int count = 0; count < n_samples; count++) {

        int bin = (int)(trunc(drawTimeNewt (b,D,gsl_rng_uniform(r))/dt));
        arr_exitTime[bin] ++;
    }
    fp = fopen("../results/samplers_funcReconstr_q.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        xaxis = (count + 0.5) * dt;
        fprintf(fp, "%lf\t%lf\t%lf\n", xaxis,
                arr_exitTime[count] / n_samples, Sder(xaxis,b,D)*dt );
    }
    fclose(fp);

    double dr =  b/(double)(n_bins);
    double t = b*b/D/100;
    double arr_exitPosition[n_bins];
    for (int count = 0; count < n_bins; count++) {
        arr_exitPosition[count] = 0;
    }
    for (int count = 0; count < n_samples; count++) {
        int bin = (int)(trunc(drawPosNewt (t,b,D,gsl_rng_uniform(r)) /dr));
        arr_exitPosition[bin] ++;
    }
    fp = fopen("../results/samplers_funcReconstr_pt100.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        xaxis = (count + 0.5) * dr;
        fprintf(fp, "%lf\t%lf\t%lf\n", xaxis,
                arr_exitPosition[count] / n_samples, Pder(xaxis,t,b,D,Sfunct(t,b,D))*dr);
    }
    fclose(fp);


    dr =  b/(double)(n_bins);
    t = b*b/D/10;
    for (int count = 0; count < n_bins; count++) {
        arr_exitPosition[count] = 0;
    }
    for (int count = 0; count < n_samples; count++) {
        int bin = (int)(trunc(drawPosNewt (t,b,D,gsl_rng_uniform(r))/dr));
        arr_exitPosition[bin] ++;
    }
    fp = fopen("../results/samplers_funcReconstr_pt10.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        xaxis = (count + 0.5) * dr;
        fprintf(fp, "%lf\t%lf\t%lf\n", xaxis,
                arr_exitPosition[count] / n_samples, Pder(xaxis,t,b,D,Sfunct(t,b,D))*dr);
    }
    fclose(fp);


    dr =  b/(double)(n_bins);
    t = b*b/D;
    for (int count = 0; count < n_bins; count++) {
        arr_exitPosition[count] = 0;
    }
    for (int count = 0; count < n_samples; count++) {
        int bin = (int)(trunc(drawPosNewt (t,b,D,gsl_rng_uniform(r))/dr));
        arr_exitPosition[bin] ++;
    }
    fp = fopen("../results/samplers_funcReconstr_pt1.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        xaxis = (count + 0.5) * dr;
        fprintf(fp, "%lf\t%lf\t%lf\n", xaxis,
                arr_exitPosition[count] / n_samples, Pder(xaxis,t,b,D,Sfunct(t,b,D))*dr);
    }
    fclose(fp);

}

#endif
