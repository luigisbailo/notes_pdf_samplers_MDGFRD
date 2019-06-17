// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_CONVERGENCESERIES_H
#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_CONVERGENCESERIES_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"


void make_data_convergenceSeries () {

    // number of terms in sums used for convergence.
    // sums are p,q,S,P
    // p,P are studied for different times

    FILE *fp_qS;
    double b = 1;
    double D = 1;
    int n_samples = 1000000;
    int n_bins = 100;
    int samples_per_bin = (int) (n_samples/n_bins);
    double dt = b*b/1000000/D;
    double t0 = b*b/100/D;
    double t = t0;


    // convergence study of q,S.
    double arr_q[n_bins], arr_S[n_bins];
    for (int count=0; count<n_bins; count++) {
        arr_q[count] = 0;
        arr_S[count] = 0;
    }
    for (int bin=0; bin<n_bins; bin++){
        for (int count=0; count<samples_per_bin; count++){
            arr_q[bin] += Sder_count(t,b,D);
            arr_S[bin] += Sfunct_count(t,b,D);
            t += dt;
        }
    }
    fp_qS = fopen("../results/samplers_convergenceSeries_qS.txt", "w");
    for (int count=0; count<n_bins; count++){
        fprintf (fp_qS, "%lf\t%lf\t%lf\n", t0+ samples_per_bin*(count+0.5)*dt,
                 arr_q[count]/samples_per_bin, arr_S[count]/samples_per_bin);
    }
    fclose(fp_qS);


    //convergence study of p,P for different times.
    t = b*b/D/1;
    double dr = b/n_samples;
    double r = dr;
    FILE *fp_pP_t1;

    double arr_p[n_bins], arr_P[n_bins];
    for (int count=0; count<n_bins; count++) {
        arr_p[count] = 0;
        arr_P[count] = 0;
    }
    for (int bin=0; bin<n_bins; bin++){
        for (int count=0; count<samples_per_bin; count++){
            arr_p[bin] += Pder_count(r,t,b,D,Sfunct(t,b,D));
            arr_P[bin] += Pfunct_count(r,t,b,D,Sfunct(t,b,D));
            r += dr;

        }
    }
    fp_pP_t1 = fopen("../results/samplers_convergenceSeries_pP_t1.txt", "w");
    for (int count=0; count<n_bins; count++){
        fprintf (fp_pP_t1, "%lf\t%lf\t%lf\n", samples_per_bin*dr*(count+0.5),
                 arr_p[count]/samples_per_bin, arr_P[count]/samples_per_bin);
    }
    fclose(fp_pP_t1);

    t = b*b/D/10;
    dr = b/n_samples;
    r = dr;
    FILE *fp_pP_t10;

    for (int count=0; count<n_bins; count++) {
        arr_p[count] = 0;
        arr_P[count] = 0;
    }
    for (int bin=0; bin<n_bins; bin++){
        for (int count=0; count<samples_per_bin; count++){
            arr_p[bin] += Pder_count(r,t,b,D,Sfunct(t,b,D));
            arr_P[bin] += Pfunct_count(r,t,b,D,Sfunct(t,b,D));
            r += dr;

        }
    }
    fp_pP_t10 = fopen("../results/samplers_convergenceSeries_pP_t10.txt", "w");
    for (int count=0; count<n_bins; count++){
        fprintf (fp_pP_t10, "%lf\t%lf\t%lf\n", samples_per_bin*dr*(count+0.5),
                 arr_p[count]/samples_per_bin, arr_P[count]/samples_per_bin);
    }
    fclose(fp_pP_t10);

    t = b*b/D/100;
    dr = b/n_samples;
    r = dr;
    FILE *fp_pP_t100;

    for (int count=0; count<n_bins; count++) {
        arr_p[count] = 0;
        arr_P[count] = 0;
    }
    for (int bin=0; bin<n_bins; bin++){
        for (int count=0; count<samples_per_bin; count++){
            arr_p[bin] += Pder_count(r,t,b,D,Sfunct(t,b,D));
            arr_P[bin] += Pfunct_count(r,t,b,D,Sfunct(t,b,D));
            r += dr;

        }
    }
    fp_pP_t100 = fopen("../results/samplers_convergenceSeries_pP_t100.txt", "w");
    for (int count=0; count<n_bins; count++){
        fprintf (fp_pP_t100, "%lf\t%lf\t%lf\n", samples_per_bin*dr*(count+0.5),
                 arr_p[count]/samples_per_bin, arr_P[count]/samples_per_bin);
    }
    fclose(fp_pP_t100);

}

#endif
