// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG6_H
#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG6_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "draw.h"


void make_data_fig6() {

    FILE *fp;
    double b1 = 1;
    double b100 = 100;
    double D = 1;
    int n_samples = 100000;
    int n_bins = 100;
    int samples_per_bin = (int) (n_samples / n_bins);


    double dXi = 1/((double)n_samples);
    double Xi0 = dXi;
    double Xi=Xi0;

    double arr_exitTime_b1[n_bins];
    double arr_exitTime_b100[n_bins];
    for (int count = 0; count < n_bins; count++) {
        arr_exitTime_b1[count] = 0;
        arr_exitTime_b100[count] = 0;
    }
    for (int bin = 0; bin < n_bins; bin++) {
        for (int count = 0; count < samples_per_bin; count++) {
            arr_exitTime_b1[bin] += drawTimeNewt_count(b1, D, Xi);
            arr_exitTime_b100[bin] += drawTimeNewt_count(b100, D, Xi);
            Xi += dXi;
        }
    }
    fp = fopen("../results/samplers_fig6_q.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        fprintf(fp, "%lf\t%lf\t%lf\n", Xi0 + samples_per_bin * (count + 0.5) * dXi,
                arr_exitTime_b1[count] / samples_per_bin, arr_exitTime_b100[count] / samples_per_bin);
    }
    fclose(fp);


    //t=b*b/D
    double t1 = b1*b1/D;
    double t100 = b100*b100/D;
    double arr_position_b1[n_bins];
    double arr_position_b100[n_bins];
    Xi0 = dXi;
    Xi=Xi0;

    for (int count = 0; count < n_bins; count++) {
        arr_position_b1[count] = 0;
        arr_position_b100[count] = 0;
    }
    for (int bin = 0; bin < n_bins; bin++) {
        for (int count = 0; count < samples_per_bin; count++) {
            arr_position_b1[bin] += drawPosNewt_count(t1, b1, D, Xi);
            arr_position_b100[bin] += drawPosNewt_count(t100, b100, D, Xi);
            Xi += dXi;
        }
    }
    fp = fopen("../results/samplers_fig6_pt1.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        fprintf(fp, "%lf\t%lf\t%lf\n", Xi0 + samples_per_bin * (count + 0.5) * dXi,
                arr_position_b1[count] / samples_per_bin, arr_position_b100[count] / samples_per_bin);
    }
    fclose(fp);


    //t=b*b/D/10
    t1 = b1*b1/D/10;
    t100 = b100*b100/D/10;
    arr_position_b1[n_bins];
    arr_position_b100[n_bins];
    Xi0 = dXi;
    Xi=Xi0;

    for (int count = 0; count < n_bins; count++) {
        arr_position_b1[count] = 0;
        arr_position_b100[count] = 0;
    }
    for (int bin = 0; bin < n_bins; bin++) {
        for (int count = 0; count < samples_per_bin; count++) {
            arr_position_b1[bin] += drawPosNewt_count(t1, b1, D, Xi);
            arr_position_b100[bin] += drawPosNewt_count(t100, b100, D, Xi);
            Xi += dXi;
        }
    }
    fp = fopen("../results/samplers_fig6_pt10.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        fprintf(fp, "%lf\t%lf\t%lf\n", Xi0 + samples_per_bin * (count + 0.5) * dXi,
                arr_position_b1[count] / samples_per_bin, arr_position_b100[count] / samples_per_bin);
    }
    fclose(fp);



    //t=b*b/D/100
    t1 = b1*b1/D/100;
    t100 = b100*b100/D/100;
    arr_position_b1[n_bins];
    arr_position_b100[n_bins];
    Xi0 = dXi;
    Xi=Xi0;

    for (int count = 0; count < n_bins; count++) {
        arr_position_b1[count] = 0;
        arr_position_b100[count] = 0;
    }
    for (int bin = 0; bin < n_bins; bin++) {
        for (int count = 0; count < samples_per_bin; count++) {
            arr_position_b1[bin] += drawPosNewt_count(t1, b1, D, Xi);
            arr_position_b100[bin] += drawPosNewt_count(t100, b100, D, Xi);
            Xi += dXi;
        }
    }
    fp = fopen("../results/samplers_fig6_pt100.txt", "w");
    for (int count = 0; count < n_bins; count++) {
        fprintf(fp, "%lf\t%lf\t%lf\n", Xi0 + samples_per_bin * (count + 0.5) * dXi,
                arr_position_b1[count] / samples_per_bin, arr_position_b100[count] / samples_per_bin);
    }
    fclose(fp);


}
#endif
