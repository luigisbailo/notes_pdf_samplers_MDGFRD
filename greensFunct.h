// author luigisbailo


#pragma once

double Sfunct ( double t, double b, double D) {
//This function returns 1-Survival probability, i.e. the probability of having already left the domain

    double coeff1 = exp ( -M_PI*M_PI*D*t/(b*b) );
    double coeff2 = 2;
    double S = 0;
    double term,termA,termB;
    int m = 1;
    double conv = 0.0000001/(b*b/D);

    if ( t>= b*b/D/100 ) {

        do {

            termA = pow (coeff1,m*m);
            termB = pow (coeff1,(m+1)*(m+1));
            term = coeff2 * (termA-termB);
            S += term;
            m += 2;

        } while ( fabs (term) > conv );

        S = 1-S;

    }
    else
        S = 0;

    return S;

}


double Sder ( double t, double b, double D) {

    double coeff1 = exp ( - M_PI*M_PI*D*t/(b*b) );
    double coeff2 = 2*D*M_PI*M_PI/b/b;
    double S;
    double term;
    double termA,termB,termC,termD;
    int m;

    double conv = 0.00001/(b*b/D);

    S = 0;
    m = 1;

    if ( t>= b*b/D/100 ) {

        do {

            termA = pow (coeff1,m*m);
            termB = m*m;
            termC = pow (coeff1,(m+1)*(m+1));
            termD = (m+1)*(m+1);
            term = coeff2 * ( termA*termB - termC*termD );

            S += term;
            m += 2;

        } while ( fabs (term) > conv | termC > termD/100 | S < 0 );
        //The second condition takes into account that the series, for short times, can be negative in the beginning, because of the term m*m
        //The series, when the term m*m  is dominant at short times, grows to a peak, and then finally deceases to zero
        //The S<0 condition is to ensure a longer convergence for short times
    }
    else
        S = 0;

    return S;

}


double Pfunct ( double radius, double t, double b, double D, double S ) {

    double coeff1 = exp ( - M_PI*M_PI*D*t/(b*b));
    double coeff2 = 2/(b*M_PI);
    double P;
    double  term, termA, termB;
    int m;
    double conv = 0.00000001/b;

    P = 0;
    m = 1;

    if (t < b*b/D*0.2) {

        do {

            termA =  pow(coeff1,m*m);
            termB =  b*sin(m*M_PI*radius/b)/m - M_PI*radius*cos(m*M_PI*radius/b);
            term =  coeff2 * termA * termB / (1-S);
            P += term;
            m += 1;

        } while ( fabs(term) > conv  |  termA>termB/100 |  P>1 );

    } else {

        P = sin(M_PI*radius/b)/M_PI - cos(M_PI*radius/b)*radius/b;

    }

    return P;

}


double Pder ( double radius, double t, double b, double D, double S ) {

    double coeff1 = exp ( -M_PI*M_PI*D*t/(b*b)  );
    double coeff2 = 2*M_PI/b/b;
    double P;
    double term;
    double termA,termB;
    int m;
    double conv = 0.0001/b;

    P = 0;
    m = 1;

    if (t < b*b/D*0.2) {

        do {

            termA = pow(coeff1,m*m);
            termB = sin (m*M_PI*radius/b) * m * radius;
            term = coeff2 * termA * termB / (1-S);
            P += term;
            m += 1;

        } while ( fabs(term) > conv  |  termA>termB/100 );

    }
    else {

        P = M_PI*sin(M_PI*radius/b)*radius/b/b;

    }

    return P;

}


double qFunct ( double radius, double t, double b, double D ) {

    double coeff1 = exp ( - M_PI*M_PI*D*t/(b*b));
    double coeff2 = 2*M_PI*D/radius/b;
    double q;
    double  term, term1, term2;
    int m;
    double conv = 0.000000001/(b*b/D);

    q = 0;
    m = 1;

    do {

        term1 =  pow(coeff1,m*m)*sin(m*M_PI*radius/b)*m;
        term2 = pow(coeff1,(m+1)*(m+1))*sin((m+1)*M_PI*radius/b)*(m+1);
        term =  coeff2 * (term1 - term2);
        q += term;
        m += 2;


    } while ( fabs(term) > conv | m<100 );

    return q;

}


double freeDiff (double r, double t, double D){

    return 	exp (-r*r/4/D/t)*r*r/sqrt(4*M_PI*pow(D*t,3) );

}