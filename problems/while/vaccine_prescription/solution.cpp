double find_root(double (*func)(double ), double a, double b, double tolerance){
  double x = 0;
  double result = 0;
  double a1 = a, b1 = b;
  do{
    x = (a1 + b1) / 2;
    result = (*func)(x);
    if(result * (*func)(b1) > 0) b1 = x;
    else a1 = x;
  }while(b1 - a1 > tolerance);
  return x;
}
