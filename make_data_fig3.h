// author luigisbailo

#ifndef NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG3_H

#include <math.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_math.h>

#include "parameters.h"
#include "greensFunct.h"


void make_data_fig3() {

    FILE *fp;

    double t,radius,infl_point,starting_point;
    double t0=0.063;
    double t1=0.234;

    double b = 1;
    double D = 1;
    double dt = b*b/D/100;
    double T = b*b/D;
    double dr = b/100000;
    fp = fopen("../results/samplers_fig3_b1.txt", "w");

    t=dt;
    while (t<T) {
        radius = 0;
        infl_point = 1;
        while (infl_point>0){
            radius += dr;
            infl_point = Pder2 (radius,t,b,D,Sfunct(t,b,D));
        }
        if (t<t0*b*b/D) starting_point = sqrt(t*D)*2;
        else if (t<t1*b*b/D) {
            double R0=2*sqrt(t0*b*b);
            double R1=0.646*b;
            double beta = (R0*exp(pow(t0,0.5)+pow(t1,0.5))-R1*exp(pow(t0,0.5)+pow(t1,0.5)))/(exp(pow(t0,0.5))-exp(pow(t1,0.5)));
            double gamma = -(R0*(exp(pow(t1,0.5))-1)*exp(pow(t0,0.5))-R1*(exp(pow(t0,0.5))-1)*exp(pow(t1,0.5)))  / (exp(pow(t0,0.5))-exp(pow(t1,0.5)));
            starting_point=beta*(1-exp(-pow(t*D/b/b,0.5)))+gamma;
        }
        else starting_point = 0.646*b;
        fprintf(fp, "%lf\t%lf\t%lf\t\n", t,radius,starting_point);
        t += dt;
    }
    fclose(fp);

    b = 10;
    D = 1;
    dt = b*b/D/100;
    T = b*b/D;
    dr = b/100000;
    fp = fopen("../results/samplers_fig3_b10.txt", "w");

    t=dt;
    while (t<T) {
        radius = 0;
        infl_point = 1;
        while (infl_point>0){
            radius += dr;
            infl_point = Pder2 (radius,t,b,D,Sfunct(t,b,D));
        }
        if (t<t0*b*b/D) starting_point = sqrt(t*D)*2;
        else if (t<t1*b*b/D) {
            double R0=2*sqrt(t0*b*b);
            double R1=0.646*b;
            double beta = (R0*exp(pow(t0,0.5)+pow(t1,0.5))-R1*exp(pow(t0,0.5)+pow(t1,0.5)))/(exp(pow(t0,0.5))-exp(pow(t1,0.5)));
            double gamma = -(R0*(exp(pow(t1,0.5))-1)*exp(pow(t0,0.5))-R1*(exp(pow(t0,0.5))-1)*exp(pow(t1,0.5)))  / (exp(pow(t0,0.5))-exp(pow(t1,0.5)));
            starting_point=beta*(1-exp(-pow(t*D/b/b,0.5)))+gamma;
        }
        else starting_point = 0.646*b;
        fprintf(fp, "%lf\t%lf\t%lf\t\n", t,radius,starting_point);
        t += dt;
    }
    fclose(fp);


}

#define NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG3_H

#endif //NOTES_PDF_SAMPLERS_MDGFRD_MAKE_DATA_FIG3_H
